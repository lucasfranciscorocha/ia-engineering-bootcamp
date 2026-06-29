

# Recapitulação Técnica: Resolução de Acesso IAM e Integração do AgentEngine com Vertex AI Search

Este documento serve como registro e manual técnico para a solução do erro de permissão ocorrido durante a integração do agente autônomo da esteira comercial (**LucasFrancoRocha.com.br**) com o banco de dados vetorial (**Vertex AI Search / Discovery Engine**) no projeto da Google Cloud Platform (GCP).

---

## 1. O Cenário Inicial e o Problema
Durante a execução do agente inteligente (`esteira_comercial_vertex_ai_search_agent`) via SDK da Google Cloud (`google.adk`), a ferramenta de busca vetorial disparava consistentemente o seguinte erro:

> `Error message: "Please grant discovery engine user role to your agent project's p4sa account in the data store project"`

### Diagnóstico Técnico:
A interface gráfica (Console GCP) indicava falsamente que as permissões estavam corretas ou impedia a adição de novos papéis devido a conflitos de interface. Na realidade, o ambiente de execução de código do agente (**AgentEngine / Reasoning Engine**) opera de forma regionalizada (ex: `us-central1`), enquanto o repositório de dados estruturados (**Data Store do Discovery Engine**) opera obrigatoriamente sob a localização `global`. 
Essa fronteira de escopo e federação de identidades gerava um bloqueio na camada do IAM (Identity and Access Management).

Durante os testes de execução do agente no painel de **Preview** do *Vertex AI Agent Builder*, a ferramenta de busca vetorial (`VertexAISearchAgent`) travava alternadamente em dois erros críticos: 
### Erro 1: Bloqueio de Federação de Identidades (IAM) >
```
Error message: "Please grant discovery engine user role to your agent project's p4sa account in the data store project"
``` 
* **Diagnóstico:** O agente (entidade de execução) não possuía permissões explícitas para interrogar o motor do *Discovery Engine* (onde residem os dados). A conta de serviço afetada era a **p4sa** (Project Service Agent), uma conta gerenciada diretamente pelo Google que opera nos bastidores e não aparece na listagem convencional de contas de serviço do IAM. 
* ### Erro 2: Falha Interna de Rotas (IDs Incorretos) > 
```
Error message: "Meet InternalError when sending message to the agent"
```
 * **Diagnóstico:** O agente tentava resolver o caminho do banco de dados utilizando parâmetros parciais ou invertidos na configuração da Tool, gerando um colapso interno (*crash*) por não localizar a coleção especificada.

---

## 2. Investigação via Terminal (Cloud Shell)

Para contornar as limitações da interface visual, utilizamos o Cloud Shell para interrogar o estado real das políticas do projeto `crewai-prospeccao-autonoma`.

### Passo 1: Verificação do Projeto Ativo
Confirmamos o ID do projeto para garantir que as alterações seriam feitas no escopo correto:
```bash
gcloud config get-value project
# Retorno confirmado: crewai-prospeccao-autonoma
```

### Passo 2: Extração da Política IAM Real
Utilizamos uma filtragem avançada para analisar as permissões existentes na conta de serviço nativa do Discovery Engine (`service-***********`):
```bash
gcloud projects get-iam-policy crewai-prospec-autonoma \
    --flatten="bindings[].members" \
    --format="table(bindings.role, bindings.members)" \
    --filter="bindings.members:service-************@gcp-sa-discoveryengine.iam.gserviceaccount.com"
```

Para solucionar o problema de forma definitiva e contornar as omissões da interface visual do console, transferimos a operação para o **Cloud Shell**. 

> **Passo 1: Alinhamento de Escopo do Projeto** 
Garantimos que o terminal estava apontando para o ID textual correto do projeto, superando a restrição do `gcloud` que rejeita o Project Number em comandos de listagem IAM: ```bash gcloud config set project crewai-prospec-autonoma

* **Resultado:** Descobrimos que a conta de serviço padrão já possuía o papel `roles/discoveryengine.user`. Isso comprovou que o agente do AgentEngine utilizava uma **outra identidade corporativa/federada** nos bastidores para tentar ler os vetores.

>**Passo 2: Mapeamento de Contas Invisíveis**
Ao rodar `gcloud iam service-accounts list`, confirmamos que a conta `p4sa` do Discovery Engine era de fato oculta. O padrão técnico do Google para esse serviço em arquiteturas modernas segue o formato: `service-************@gcp-sa-discoveryengine.iam.gserviceaccount.com`

>**Passo 3: Aplicação da Role Exata (`discoveryengine.user`)**
Forçamos a injeção da permissão correta diretamente no barramento do IAM do projeto. Embora tivésse testado a role `viewer` inicialmente, o Agent Builder exige estritamente o papel de **User** para realizar buscas em produção:

```bash
gcloud projects add-iam-policy-binding crewai-prospeccao-autonoma \
    --member="principalSet://agents.global.proj-804230245480.system.id.goog/*" \
    --role="roles/discoveryengine.user"
```
A arquitetura moderna do Google Vertex AI Agent Builder utiliza um conceito chamado `principalSet` (federação de identidades de contêineres gerenciados) em vez de e-mails tradicionais de contas de serviço.
Para resolver o travamento de forma perene e cobrir qualquer variação de microsserviço que o SDK instancie sob a região global, aplicamos a permissão de usuário diretamente no conjunto de identidades do projeto:
###### O que este comando realizou:
* **Injeção de Curinga (`/*`):** Declarou para o IAM do projeto que *qualquer* contêiner de agente ou infraestrutura do Vertex AI vinda do projeto `804230245480` tem direito legítimo de leitura sobre o Data Store de templates comerciais.
---

## 3. Alinhamento Estrutural da "Tool"

Conforme validado através do `Screenshot_20260629_003824.png`, descobrimos que o ecossistema do Vertex AI Search exige mapeamentos de IDs extremamente rígidos na interface de ferramentas do Agente:

1. **Collection ID:** Deve ser preenchido invariavelmente como **`default_collection`** (o container padrão do sistema).
    
2. **Data Store ID:** Deve conter o ID técnico e exato gerado pelo console na criação, incluindo o sufixo numérico (timestamp). No nosso caso: **`base-templates-emails_***********`**.

| **Campo no Agent Builder** | **Valor Configurado**               | **Função**                               |
| -------------------------- | ----------------------------------- | ---------------------------------------- |
| **GCP Project ID**         | `crewai-prospec-autonoma`           | Aponta o escopo do faturamento/recursos. |
| **Location**               | `global`                            | Região de indexação da Data Store.       |
| **Collection ID**          | `default_collection`                | Agrupador lógico interno do Google.      |
| **Data Store ID**          | `base-templates-emails_***********` | O endereço físico e exato dos dados.     |

---

## 4. Resultado e Validação em Produção

Após um período de 7 minutos para a completa propagação das políticas de segurança na infraestrutura global do Google, a esteira comercial foi testada com sucesso absoluto.
### Fluxo Executado com Sucesso:

1. **Query Expansion (Pré-recuperação):** O input do operador contendo os gatilhos do lead (**Plus Language school**) foi expandido.
    
2. **Acesso ao RAG:** O agente cruzou com sucesso a barreira de segurança do IAM, consultou o Data Store e extraiu as regras dos combos.
    
3. **Lógica Condicional Aplicada:** O Gemini correlacionou as falhas detectadas (Site Inseguro `🔓`, Sem Botão de WhatsApp `❌`, Sem tags de conversão do Google Ads `🎯`).
    
4. **Output Comercial de Alta Conversão:** Gerou um e-mail ultra-personalizado sob a persona de Lucas Franco, combinando tom altamente técnico e abordagem amigável de agência local.