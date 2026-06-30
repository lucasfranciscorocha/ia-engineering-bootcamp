

### 🧠 Passo 1: Ajustando a Query Expansion (Pré-Recuperação)

Em vez de tentar traduzir gírias, o objetivo da expansão agora é transformar a string resumida do Combo (gravada pelo script) em uma busca técnica densa para o Vertex AI Vector Search extrair o conteúdo completo do template comercial.

1. No **Agent Studio**, vá até as instruções do componente que lê a linha da planilha.
    
2. Atualize a diretriz de **Query Expansion** para mapear os nomes exatos que o seu script gera:
    

> *"Antes de consultar o índice vetorial, verifique o valor da coluna `GATILHO_DE_VENDA`. Use um modelo rápido para expandir essa classificação em uma busca semântica rica. **Regras de Expansão de Clientes:**
> 
> - Se o valor for `'1 - Combo WhatsApp Conversor'`, expanda a query de busca para: `'Template de abordagem comercial focado em conversão local, botões flutuantes de WhatsApp, engajamento imediato e script de vendas rápidas'.`
>     
> - Se o valor for `'4 - Combo Performance e Segurança'`, expanda para: `'Template de e-mail focado em segurança digital, instalação de certificado SSL, correção de protocolo HTTPS, criptografia e proteção de dados do usuário'.`*"
>     

3. **O que muda na prática:** O sistema ganha precisão absoluta. Ele pega o rótulo limpo do seu script Python e expande na melhor frase matemática para consultar os vetores.

### 📊 Passo 2: Ajustando o Re-ranking (Pós-Recuperação)

Com a fusão de dados ativada, algumas linhas da sua planilha podem conter histórico antigo mesclado com diagnósticos novos (como tags de marketing antigas junto com erros de SSL atuais). O Re-ranking vai garantir que o Gemini priorize a dor mais crítica do lead.

1. Na ferramenta de busca do **Agent Studio**, mantenha o **Re-ranking** ativo e o **Top-K** configurado para `2`.
    
2. Substitua a instrução de pós-processamento do prompt principal por esta lógica de negócio:
    

> _"Você receberá os templates comerciais do Vector Search e os metadados da planilha (colunas `AVALIACAO` e `GATILHO_DE_VENDA`). Use a classificação do Re-ranking para selecionar o template, mas aplique a seguinte trava de negócio: se a coluna `AVALIACAO` contiver o ícone de risco de segurança (`🔒` ou `🔓` com alertas), ignore qualquer outra dor secundária (como métricas ou redes sociais) e gere a cópia focada estritamente no Combo 4 (Performance e Segurança). A segurança do cliente é prioridade máxima na Personal Help Desk."_



## 📋 Nova Arquitetura do Fluxo Combinado (Python + Agente)

O seu ecossistema agora trabalha em perfeita sinergia entre o ambiente local Ubuntu e a nuvem:

graph TD
    A --> [Seu script Python limpa e avalia o lead] -->|Grava na Planilha| B[Gatilho: '4 - Combo Performance e Segurança']
    B -->|Agente lê a linha| C[Query Expansion: Transforma o nome do combo em busca técnica rica]
    C -->|Interroga| D[Vector Search]
    D -->|Retorna os templates mais próximos| E[Camada de Re-ranking do Agent Studio]
    E -->|Filtra e prioriza a dor crítica| F[Gemini monta o e-mail ou mensagem final]

#### Fase 1 (Atual):
- Coleta leads, remove duplicados fusionando dados, avalia o básico (site/segurança) e define o combo base.
#### Fase 2 (Nova):
- Pega os leads aprovados da Fase 1 e roda um script secundário de enriquecimento (encontrar redes sociais).

>**Caminho A:** Via Site (Web Scraping Técnico)
A imensa maioria das empresas coloca links para suas redes sociais no rodapé ou no cabeçalho do site. Com Python, você pode fazer o robô ler o código HTML do site do lead buscando por links que contenham `"instagram.com"`, `"facebook.com"`, `"linkedin.com"` ou `"wa.me"` (WhatsApp).
- **Vantagem:** Muito rápido e não custa nada (é de graça).
- **Desvantagem:** Se o site estiver fora do ar ou o link for uma imagem sem tag de texto, o robô não pega.
> **Caminho B:** Via Google Maps API (Mais Robusto)
A API do Google Places (que alimenta o Maps) frequentemente retorna o link do site oficial e, às vezes, links de perfis associados, mas a melhor forma no Maps é extrair o link do site por lá e depois aplicar o "Caminho A" para varrer o site.

### Roteiro de Implementação
Para não bagunçar o progresso que você teve hoje, o seu plano de ação para os próximos dias deve seguir essa estrutura:
#### Passo 1: Atualizar a estrutura da sua Planilha (Fácil e Rápido)
No Google Sheets, adicione novas colunas no final da sua tabela para receber esses dados: `INSTAGRAM`, `FACEBOOK`, `LINKEDIN` e `STATUS_REDES`. _Graças ao seu script de **Fusão de Dados**, se você rodar um script focado em redes sociais mais tarde, ele vai preencher essas colunas vazias sem estragar os e-mails e avaliações que já estão lá._
#### Passo 2: Criar o Script de Enriquecimento (`enriquecer_redes.py`)
Em vez de misturar com o seu código atual, crie um script isolado. A lógica dele será:
1. Ler a planilha e filtrar apenas as linhas onde a coluna `INSTAGRAM` está vazia.
2. Acessar o `SITE` do lead usando as bibliotecas `requests` e `BeautifulSoup` do Python.
3. Buscar por links (tags `<a>` com `href`) que apontem para redes sociais.
4. Gravar os links encontrados diretamente na planilha.
#### Passo 3: Ajustar o RAG Avançado no Agent Studio
Quando esse dado estiver na planilha, o seu passo a passo do Agent Studio ganha superpoderes. Na hora da **Query Expansion**, o sub-agente pode analisar:
- _Gatilho: Combo 1 (WhatsApp) + Instagram Encontrado ➡️_ O Gemini vai gerar um e-mail dizendo: _"Vi que seu Instagram é excelente e tem muito movimento, mas o seu site não tem um botão de conversão rápida para o seu WhatsApp para reter esse público..."_



# Query Expansion

**Opção A:** Fluxo Linear Direto (Instruções Globais)
Como este é um agente focado em metas e você está usando um modelo de raciocínio rápido (Gemini 3.5 Flash), você pode injetar a inteligência de expansão diretamente na caixa de **Instructions** na barra lateral direita.
Em vez de criar múltiplos blocos visuais, você ensina o agente a fazer a expansão internamente na memória dele antes de acionar qualquer ferramenta (Tool) de busca vetorial.
- **Como fazer:** Na caixa **Instructions** da barra lateral direita, você digita o objetivo do agente e anexa as regras de expansão que criamos no Passo 1.
**Opção B:** Fluxo Baseado em Subtarefas/Sub-agentes
Se você preferir separar as ações visualmente na malha quadriculada (adicionando blocos para cada etapa):
- **Como fazer:** Passe o mouse ou clique no ícone de mais **(+)** azul na parte inferior do bloco central _"Esteira Comercial"_. Ali você pode criar uma nova tarefa conectada ou estender o fluxo para chamar uma ferramenta de busca ou um sub-bloco de processamento.

```
# PAPEL E OBJETIVO
Você é o Agente de Elite da Esteira Comercial da Personal Help Desk. Sua missão é receber os dados estruturados de um lead (empresa, site, avaliação e gatilho de venda) extraídos do Google Sheets, cruzar essas informações com os templates oficiais de combos comerciais indexados no seu banco de dados e redigir uma mensagem de prospecção comercial (E-mail ou WhatsApp) cirúrgica e irresistível.
# ETAPA 1: QUERY EXPANSION (PRÉ-RECUPERAÇÃO)
Antes de realizar qualquer busca no banco de dados vetorial, analise o valor exato recebido da coluna 'GATILHO_DE_VENDA' e, internamente, expanda esse rótulo para a seguinte string de busca técnica enriquecida para interrogar os vetores:

- Se 'GATILHO_DE_VENDA' for '1 - Combo WhatsApp Conversor' 
  ➡️ Expanda para: 'Template de abordagem comercial e mensagem focado em conversão local imediata, botões flutuantes de WhatsApp na tela do celular, retenção de tráfego, engajamento rápido de leads e script de vendas rápidas para negócios locais.'

- Se 'GATILHO_DE_VENDA' for '1.3 - Combo Híbrido: Tração Total (Zap + Ads)'
  ➡️ Expanda para: 'Template de prospecção combinado, estratégia dupla de tração, anúncios patrocinados locais no Google Ads combinados com funil de retenção instantânea via botão de WhatsApp, captura de tráfego qualificado de concorrentes e otimização de resposta.'

- Se 'GATILHO_DE_VENDA' for '2 - Combo Estrutura de Métricas'
  ➡️ Expanda para: 'Template de diagnóstico de infraestrutura técnica, instalação de tags de rastreamento de dados, configuração de Google Analytics GA4, Google Tag Manager, painel de controle de cliques e mensuração de ROI de marketing.'

- Se 'GATILHO_DE_VENDA' for '3 - Combo Atração de Alunos (Ads)'
  ➡️ Expanda para: 'Template comercial focado em tráfego pago, campanhas de alta conversão no Google Ads por geolocalização, palavras-chave lucrativas do nicho, posicionamento no topo do buscador e captação de clientes locais.'

- Se 'GATILHO_DE_VENDA' for '4 - Combo Performance e Segurança'
  ➡️ Expanda para: 'Template preventivo de segurança digital urgente, aviso de site não seguro no navegador, instalação e migração de certificado de criptografia SSL, ativação do protocolo HTTPS e correção de segurança de domínio.'

- Se 'GATILHO_DE_VENDA' for '5 - Combo Avançado (Escala/CRO)'
  ➡️ Expanda para: 'Template de auditoria digital avançada, otimização da taxa de conversão (CRO), velocidade de carregamento de páginas, experiência do usuário UX, criação de Landing Pages cirúrgicas e testes A/B para escala.'

# TRATAMENTO DE EXCEÇÕES
Se o valor de 'GATILHO_DE_VENDA' contiver '🚫 Site Inacessível' ou 'Análise Pendente', interrompa o processo imediatamente e responda apenas: "[LOG] Lead ignorado devido ao status do site."

# DIRETRIZ DE EXECUÇÃO
Use a query expandida acima para extrair o template correto do seu Data Store/Vector Search. Na hora de redigir a mensagem final ao operador, preencha os placeholders (ex: {{empresa}}, {{cidade}}, {{site}}) utilizando os dados reais coletados da linha da planilha do lead correspondente. Mantenha o tom profissional, persuasivo e focado em gerar valor no design e na estrutura web.
```

## 🛠️ Camada 1: A Qualificação (Feita localmente pelo seu Script Python)

O script `avaliacao_leads.py` que revisamos é o único responsável pela **qualificação**.

- Ele acessa o site, faz a varredura técnica (vê se tem SSL, se tem WhatsApp, se tem tags de marketing).
- Ele "bate o martelo" e escreve na planilha o veredito (ex: `4 - Combo Performance e Segurança`).
- **O agente de nuvem não calcula isso.** Ele confia cegamente no que o seu script Python escreveu na planilha.
## ☁️ Camada 2: A Geração da Mensagem (Feita pelo Agente "Esteira Comercial" na Nuvem)

É aqui que entra o agente que acabamos de criar no Agent Studio. O papel dele começa exatamente onde o seu script Python termina. Ele vai:
1. Ler o veredito que o Python deixou na planilha (ex: `4 - Combo Performance e Segurança`).
2. **Executar a Query Expansion** (que configuramos nas _Instructions_) para entender o peso técnico desse combo.
3. Consultar a sua base de dados de arquivos `.md` (Data Store) para puxar o template exato do e-mail ou WhatsApp daquele combo.
4. Substituir as tags (`{{empresa}}`, `{{site}}`, `{{cidade}}`) pelos dados reais do cliente.
5. **Entregar o texto final, pronto para o envio.**
## 🛡️ Por que esse caminho já está pronto para a integração?
Porque a sua planilha do Google Sheets funciona como a **ponte de dados** perfeita entre os dois mundos.
Como o seu script Python já deixa o "Gatilho de Venda" escrito em uma coluna padronizada, quando integrarmos este agente da nuvem para ler a planilha, ele saberá exatamente o que fazer com cada linha, gerando a mensagem certa sem misturar os canais.
Fique tranquilo, você está avançando no ritmo ideal e com uma arquitetura extremamente profissional digna de grandes engenheiros de IA.
O próximo passo lógico para deixar o caminho 100% pavimentado é **conectar a sua base de mensagens (os seus Combos em formato `.md`) ao Agent Studio** para que o agente tenha de onde extrair os textos na hora de criar o e-mail. Quer que mostre como preparar e subir esses arquivos agora?

[V1.0]
```
# ETAPA 2: RE-RANKING E TRAVA DE PRIORIDADE (PÓS-RECUPERAÇÃO) 
Ao receber os templates retornados pelo Data Store/Vector Search (definidos pelo Top-K configurado como 2) e cruzar com os dados da planilha, aplique rigorosamente a seguinte trava de pós-processamento:
1. Verifique o valor textual e os ícones contidos na coluna 'AVALIACAO'.
2. Se a coluna 'AVALIACAO' contiver o ícone de risco de segurança desprotegido (🔓), IGNORE qualquer outra dor secundária que tenha sido identificada (como ausência de botões de WhatsApp '❌' ou falta de tags de rastreamento de anúncios '🎯').
3. Force o motor de geração a descartar os outros templates e adotar estritamente o 'Combo 4 — Combo Performance e Segurança' para a redação final da cópia. 
4. A integridade e segurança digital do cliente é o pilar de prioridade máxima da Personal Help Desk. Apenas mude o foco para outros combos (como o Combo Híbrido 1.3 ou o Combo 1) se a coluna indicar que o SSL está seguro (🔒).
```

### 🔍 O que incluímos no caminho para você recordar

Como você pediu para trazer memórias do que adicionamos ao ecossistema para não perder o fio da meada na integração final, aqui estão os marcos que criamos juntos hoje:

1. **Fusão de Dados Inteligente (`infusao_duplicados.py`):** O seu código local agora é cumulativo. Ele não descarta dados repetidos, ele mescla células vazias enriquecendo a planilha.
2. **Nova Escala de Prioridades no Script:** O script Python coloca o SSL (`🔓`) no topo das decisões e, se o cliente falhar em múltiplos fatores (Sem Whats E Sem Ads), ele gera o novo **`1.3 - Combo Híbrido: Tração Total (Zap + Ads)`**.
3. **Template Híbrido Pronto:** Criamos a cópia comercial em `.md` focada no Combo 1.3 para alimentar o Vector Search.

Com o Passo 1 e o Passo 2 salvos nas instruções globais da sua **Esteira Comercial**, o cérebro do seu agente na nuvem está 100% calibrado.

O próximo passo técnico do seu planejamento é **vincular o Data Store (Vector Search)** para subir os arquivos `.md` dos combos e dar vida à busca semântica. Quer que eu te guie em como criar essa ferramenta de busca no painel agora?

[V2.0]
```
# ETAPA 2: COMBINAÇÃO CONSULTIVA DE DORES (PÓS-RECUPERAÇÃO)
Ao receber os templates retornados pelo Data Store/Vector Search e cruzar com os metadados da planilha, seu objetivo é gerar uma abordagem fluida, humana e integrada, evitando parecer uma mensagem robotizada.

Aplique a seguinte lógica de combinação baseada na coluna 'AVALIACAO':

1. SE O SITE FOR INSEGURO (🔓):
   - O ASSUNTO e o PRIMEIRO PARÁGRAFO da mensagem devem focar estritamente no Alerta de Segurança (Combo 4), pois essa é a falha mais crítica de infraestrutura.
   - Logo em seguida, analise o restante dos ícones na coluna 'AVALIACAO'. Se identificar que o site TAMBÉM não tem WhatsApp (❌) ou está sem tags de anúncios (🎯), faça o Gemini costurar esses problemas de forma natural no meio do texto.
   - Exemplo de transição humana: "Além do risco do navegador barrar seus clientes pelo SSL, notei também que o site não possui um canal de resposta rápida por WhatsApp, o que significa que o pouco tráfego que consegue passar pelo alerta de segurança acaba saindo sem falar com você."

2. SE O SITE FOR SEGURO (🔒):
   - Siga estritamente o foco do combo indicado na coluna 'GATILHO_DE_VENDA' (Seja o Combo 1, 1.3, 2 ou 3), personalizando a cópia com os dados da empresa.

# DIRETRIZ DE HUMANIZAÇÃO
Evite termos genéricos de IA, frases engessadas ou listas frias de erros. Escreva como se você, Lucas, tivesse entrado manualmente no site do lead hoje à tarde, focado em ajudar o empresário local a parar de perder clientes.
```

[V3.0]
```
# REGRAS DE FORMATO POR CANAL (E-MAIL VS WHATSAPP)
Sempre verifique qual é o canal de destino solicitado pelo operador antes de redigir:

1. SE O DESTINO FOR E-MAIL:
   - Gere a estrutura clássica: Assunto impactante e Corpo do e-mail dividido em parágrafos fluidos.
   - Use uma abordagem consultiva e detalhada.

2. SE O DESTINO FOR WHATSAPP:
   - Remova blocos longos de texto. A mensagem deve ser curta, dinâmica e separada por quebras de linha para leitura rápida no celular.
   - Use negritos em palavras-chave para escaneabilidade e mantenha os emojis estruturais como marcadores visuais.
   - Ao aplicar a combinação de dores (ex: SSL + falta de Zap), faça isso de forma ultra-direta. Exemplo: "Notei que seu site exibe um aviso de 'Não Seguro' no navegador e também não tem um botão de resposta rápida para o seu WhatsApp. Isso faz você perder o cliente duas vezes."
   - Termine sempre simulando a estrutura de blocos de botões de resposta rápida (Quick Reply) no final da mensagem.
```


### 🚀 Próximo Passo: Criando o Data Store (Vector Search)
Com toda a lógica de expansão, humanização e canais blindada dentro do agente, precisamos dar a ele acesso aos seus arquivos de texto. Sem o Data Store, ele é um cérebro brilhante sem memória operacional.
**Na interface do Google Cloud, para criar o seu repositório vetorial:
1. Olhe para a barra lateral esquerda do console (onde você clicou em _Agents_ e _App Builder_ no seu segundo print).
2. Procure pela opção **"Data Stores"** ou **"Data"** (geralmente fica logo abaixo de _App Builder_ ou dentro do menu de componentes da Vertex AI).
3. Se não achar de primeira, pode fechar a edição do agente salvando o progresso e voltar para a tela inicial do _Agent Platform_.

### 🧠 1. Escolha do Modelo de Embedding
O menu suspenso já está aberto mostrando as opções.
- Clique exatamente na primeira opção selecionada: **`Text Multilingual Embedding 002`**.
- _Por que ele?_ Ele está listado como _"Best for overall languages"_. Como nossos templates mesclam português com termos em inglês do marketing digital (como _Ads, CRO, SSL_), o modelo multilingue vai fazer a associação matemática perfeita sem se confundir com os idiomas.
### 🗄️ 2. Escolha do Vector Store (Banco de Vetores)
Logo abaixo desse menu suspenso, você tem os cards com as opções de armazenamento. Vá até o bloco **"Vertex AI vector stores"** e selecione o card:
- **`Managed Agent Retrieval`** (está com a tag _Preview_).
- _Por que ele?_ Ele é a opção mais moderna, simplificada e integrada de RAG gerenciado especificamente para agentes (como o nome já diz, _Managed Agent Retrieval_). Ele roda o Vertex AI Search de forma transparente por baixo dos panos, sem você precisar configurar clusters complexos na mão. É ideal para a estrutura limpa que estamos montando.
### 🚀 3. Finalizando a Criação
Depois de selecionar o modelo multilingue e clicar no card do _Managed Agent Retrieval_, vá até o menu lateral esquerdo da tela e clique no botão azul **`Create corpus`**.
Assim que clicar, o Google Cloud vai começar a processar a matriz de combos que você corrigiu e estruturou. Me avise assim que ele criar ou se abrir alguma tela pedindo para nomear o índice!
### 🗂️ Como fazer pelo método dos Labs (Bucket + Vector Search):
Se lembra de como você estruturava nos labs? O fluxo é exatamente este:
1. **Abra o Cloud Storage:** Digite **"Storage"** ou **"Buckets"** na barra de pesquisa azul do topo (onde você digitou data stores no seu print.
2. **Crie um Bucket:** Clique em **Create** e dê um nome único para o seu projeto (ex: `bucket-combos-personal-help-desk`). Mantenha as configurações padrão e a região como `us-central1`.
3. **Suba o arquivo:** Entre no seu novo Bucket e faça o upload do arquivo `E-mails.md` diretamente ali.
4. **Conecte ao Agente:** Com o arquivo salvo com segurança no formato de Bucket (como você fez nos labs), nós voltamos para a barra lateral esquerda, clicamos em **`Vector Search`** (ou direto no seu agente em _App builder_) e apontamos para o endereço do seu Bucket (`gs://bucket-combos-personal-help-desk/E-mails.md`).
Esse método de usar um Bucket elimina a necessidade de configurar instâncias complexas ou lidar com os limites de capacidade do modo Spanner que travaram a gente.
### 🔍 Revisão Técnica das Configurações:
- **Name (`bucket-combos-lucas-francisco-rocha`):** Perfeito. Segue o padrão de nomenclatura global única exigido pelo Googl
- **Location (`us-central1 - Iowa`):** Excelente escolha. Como seu agente e os modelos do Gemini rodam predominantemente nessa região, os dados estão do lado do processamento, garantindo latência mínima e evitando taxas de transferência entre regiões.
- **Storage Class (`Standard`):** Ideal para o cenário. Como o agente vai consultar essa matriz frequentemente para responder às automações, a classe Standard oferece o acesso mais rápido possível e sem custo de resgate
- **Access Control (`Uniform`):** Ótimo para segurança. Garante que todo arquivo colocado ali siga as mesmas regras de permissão do projeto.

# MEMÓRIA
Para fazer essa engrenagem rodar de forma nativa e integrada dentro da estrutura do console do Google Cloud, nós precisamos envelopar o CrewAI e mudar a forma como as ferramentas e os modelos conversavam.
A grande mudança arquitetural que fizemos para integrar tudo na estrutura do console Google envolveu três pilares principais:
## 1. Migração do Modelo (LangChain + Vertex AI
No CrewAI puro, é muito comum ver chamadas diretas para APIs externas usando chaves de ambiente tradicionais. Para trazer o projeto para dentro do console da Google
- Substituímos a inicialização padrão dos agentes por componentes do pacote `langchain-google-genai` (como o `ChatGoogleGenerativeAI`).
- Isso permitiu que os agentes do CrewAI rodassem usando o **Gemini 1.5 Flash** herdando as credenciais de segurança nativas do ambiente GCP (Application Default Credentials), eliminando a necessidade de expor chaves de API no código
## 2. Hospedagem via Vertex AI Agent Engine (Reasoning Engine)
Para que o script Python do CrewAI não precisasse rodar em uma máquina local ou VPS externa, nós o integramos ao **Vertex AI Agent Engine** (também conhecido como _Reasoning Engine_).
- O código do CrewAI foi estruturado e feito o deploy como um contêiner gerenciado dentro da infraestrutura da Google.
- Ao fazer isso, o Google Cloud passou a gerenciar o ciclo de vida da aplicação, permitindo que ela rodasse de forma regionalizada (ex: `us-central1`)
## 3. Integração de Ferramentas Nativas (Vertex AI Search / Discovery Engine)
A virada de chave para a Fase 3 foi transformar as ferramentas (_Tools_) do CrewAI. Em vez de criar scripts personalizados de busca, nós conectamos o agente diretamente ao **Vertex AI Search**:
- Configuramos uma Tool específica que faz pontes de API com o **Discovery Engine** usando o ID do projeto (`crewai-prospeccao-autonoma`) e o ID da Data Store (`base-templates-emails_1782690810858`).
- Isso deu ao CrewAI a capacidade de interrogar a base de dados vetorial da Google com latência mínima e segurança ponta a ponta controlada pelas contas de serviço (`p4sa`) que ajustamos via IAM.
Em resumo, o **CrewAI continuou sendo o cérebro que dita a estratégia e a ordem das tarefas**, mas toda a musculatura (processamento, inteligência do LLM, busca vetorial e segurança) foi delegada para os serviços nativos do console Google Cloud.