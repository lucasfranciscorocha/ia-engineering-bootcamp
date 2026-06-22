# 🗄️ Módulo 05 • Dia 34: Ingestion Pipelines: RAG vs. Fine-Tuning
## Guia de Engenharia Reversa e Arquitetura para Laboratórios (Google Cloud / Developers)

Este documento serve como um mapa de consulta rápida e auditoria técnica para tomada de decisões arquiteturais em nuvem, preparando o terreno para execuções práticas no Google Cloud Skills Boost e ambientes de produção.

---

## 🧭 1. O Dilema Arquitetural: Memória Paramétrica vs. Memória Externa

Ao desenhar a infraestrutura de dados para um LLM (como a família Gemini no Vertex AI), a primeira grande decisão técnica gira em torno de onde residirá a base de conhecimento do sistema.

```
                  ┌─────────────────────────────────────────┐
                  │          ENTRADA (REQUISIÇÃO)           │
                  └────────────────────┬────────────────────┘
                                       │
                     [¿O dado muda constantemente?]
                               /       \
                             SIM       NÃO
                             /           \
                            ▼             ▼
                 ┌───────────────────┐   ┌───────────────────┐
                 │   PIPELINE RAG    │   │    FINE-TUNING    │
                 │ (Memória Externa) │   │ (Memória Interna) │
                 └───────────────────┘   └───────────────────┘
```

### A. Fine-Tuning (Memória Paramétrica)
* **Conceito:** Modificação dos pesos sinápticos internos do modelo através de retropropagação (Backpropagation) utilizando um dataset estruturado (geralmente arquivos `.jsonl`).
* **Foco Real:** Ajuste de comportamento, assimilação de tom de voz (Persona), obediência cega a sintaxes rígidas de saída (como um padrão de código específico ou esquemas JSON complexos).
* **Analogia de Engenharia:** Alterar a fiação interna e a estrutura cognitiva do motor da IA.

### B. RAG - Retrieval-Augmented Generation (Memória Externa)
* **Conceito:** Otimização do prompt em tempo de execução (Runtime). O modelo original permanece intacto e congelado. Um sistema de busca (Vector DB ou API de busca) recupera fragmentos de dados externos relevantes e os injeta dinamicamente dentro da janela de contexto.
* **Foco Real:** Precisão factual, volatilidade extrema de dados (preços, estoque, notícias) e rastreabilidade total de fontes.
* **Analogia de Engenharia:** Fornecer um motor de busca de alta fidelidade e um manual de consulta na mesa do operador.

---

## ⚖️ 2. Matriz de Decisão para Engenheiros de Soluções

| Vetor de Avaliação | RAG (Retrieval-Augmented) | Fine-Tuning (Paramétrico) | Impacto no Google Cloud (Vertex AI) |
| :--- | :--- | :--- | :--- |
| **Volatilidade dos Dados** | **Dinâmico:** Atualização em milissegundos direto no banco de vetores. | **Estático:** Exige novo pipeline de treinamento (Pipeline Run no Vertex AI). | RAG economiza custos de processamento em dados que mudam diariamente. |
| **Risco de Alucinação** | **Mínimo:** É possível blindar o prompt para responder *apenas* com base nas fontes. | **Latente:** O modelo tenta "lembrar" estatisticamente, gerando falsos positivos. | RAG permite auditoria e conformidade (Citações de Ground Truth). |
| **Custo de Setup Inicial** | Baixo a Médio (Configuração de índices vetoriais ou chamadas de API). | Alto (Exige instâncias de computação dedicada e GPUs para treinamento). | Vertex AI cobra por hora de treinamento e nós de computação para tuning. |
| **Especialização de Escrita** | Limitada (Padrões passados apenas por contexto de janela/Few-Shot). | Excelente (O modelo assume a estrutura e formatação nativamente). | Fine-Tuning reduz o tamanho do prompt inicial (menor latência de token). |

---

## 🛡️ 3. Padrões Sensíveis para Laboratórios e Produção (GCP Vertex AI)

Ao executar laboratórios práticos na Google Cloud, atente-se aos seguintes direcionamentos técnicos:

### Diretriz para Dados Voláteis (O caso do E-commerce/ERP)
* **Arquitetura Correta:** RAG conectado via *Function Calling* ou *Vector Search*.
* **Por que?** Preços, estoques e inventários alterados diariamente necessitam de uma fonte única da verdade (Single Source of Truth). O Fine-Tuning falharia por obsolescência de dados em menos de 24 horas.

### Diretriz para Personas e Regras de Negócio de Marca (Tom de Voz)
* **Arquitetura Correta:** Abordagem Híbrida (Prompt de Sistema Robusto + RAG) ou Fine-Tuning leve (LoRA).
* **Por que?** Ensinar gírias locais e regras estritas de formatação de resposta através do RAG consome muitos tokens desnecessariamente a cada interação. O comportamento deve ser injetado nas instruções de sistema (System Instructions) ou gravado nos parâmetros do modelo.

### Governança e Rastreabilidade (FinOps e Compliance)
* **Auditoria de Decisões:** O RAG entrega os metadados de origem (`source_document`, `page_number`, `line_id`). Se a IA responder algo incorreto, o engenheiro pode identificar se o erro foi na recuperação do dado (RAG falhou) ou na interpretação do texto (LLM falhou). No Fine-Tuning, a resposta é uma caixa preta de probabilidades.

---

## 📝 4. Check-list de Validação Arquitetural

- [ ] Os dados mudam com frequência semanal ou diária? -> **Use RAG**
- [ ] Preciso saber exatamente qual documento gerou a resposta da IA? -> **Use RAG**
- [ ] O modelo precisa aprender uma linguagem de programação proprietária ou um dialeto específico? -> **Use Fine-Tuning**
- [ ] Meu objetivo principal é reduzir a latência de tokens de entrada eliminando prompts gigantes de contexto? -> **Use Fine-Tuning**
- [ ] Preciso garantir custo zero de treinamento de máquina para o MVP? -> **Use RAG**


# 🗄️ Módulo 05 • Dia 35: Document Loading & High-Fidelity Parsing
## Tratamento de PDFs Complexos e Práticas de Design de Dados Nativos

Este guia técnico consolida as ferramentas de engenharia de dados para extração de PDFs estruturados no ecossistema Ubuntu Linux e estabelece o padrão de governança para a criação de documentos que dispensam pipelines de tratamento complexos.

---

## 🛠️ 1. Matriz de Ferramentas para Extração de PDFs (Tratadores de Dados)

Ao lidar com documentos legados ou relatórios multi-colunas no seu ambiente de desenvolvimento, a escolha do extrator determina a taxa de sucesso da busca semântica (RAG).

| Tecnologia | Tipo de Abordagem | Casos de Uso Recomendados | Vantagens no Ubuntu |
| :--- | :--- | :--- | :--- |
| **PyMuPDF (`fitz`)** | Baseado em Coordenadas | Manuais técnicos de TI, PDFs de duas colunas, documentos estruturados digitalmente. | Ultraveloz, permite ler blocos usando caixas delimitadoras ($x, y$) isolando as colunas. |
| **Marker (Deep Learning)** | Baseado em Modelos (AI) | Relatórios complexos com tabelas pesadas, artigos científicos e livros digitais. | Converte páginas densas diretamente para Markdown limpo com alta precisão. |
| **Unstructured.io** | Element-Based (Baseado em Elementos) | Pipeline de ingestão em lote (Batch Ingestion) integrado com LangChain/CrewAI. | Classifica os blocos textuais automaticamente em metadados (`Title`, `NarrativeText`, `Table`). |
| **PaddleOCR / Tesseract** | OCR Óptico (Visão computacional) | PDFs escaneados (imagens), notas fiscais digitalizadas, fotos de briefs físicos. | Executa a leitura de texto diretamente dos pixels quando não há camada vetorial de fonte. |

---

## 📐 2. Diretrizes Profissionais para Criação de Dados Nativos (Zero-Treatment)

A melhor forma de economizar tokens, custos de processamento (FinOps) e tempo com limpeza de dados é **gerar os dados diretamente em formatos nativos para IA**. Como Designer e Desenvolvedor, você pode padronizar a criação de briefings, wikis de projetos e relatórios usando a seguinte arquitetura estrutural:

### A. Priorização Estrita de Formatos
Abandone o fluxo tradicional de exportação para `.pdf` ou `.docx` para uso interno em agentes. Utilize:
1.  **Markdown (`.md`):** O formato soberano para LLMs. Mantém a hierarquia semântica pura através de tags leves (`#`, `##`, `-`, `*`).
2.  **JSON Estruturado (`.json`):** Ideal para dados relacionais, listagens de produtos, informações comerciais estruturadas por chaves e valores.
3.  **CSV Limpo (`.csv`):** Perfeito para dados tabulares sequenciais (como o mailing que você extrai para o Google Sheets).

### B. Regras de Ouro no Design de Layouts para IA
Se a exportação para PDF for estritamente obrigatória por exigência do cliente ou conformidade legal, configure o arquivo seguindo estas regras de engenharia:

* **Fluxo Linear Unicoluna:** Nunca crie layouts de documentação técnica em duas ou três colunas paralelas. O texto deve fluir verticalmente de cima para baixo.
* **Tabelas em Texto Puro ou Listas:** Evite mesclar células verticalmente em tabelas de PDFs. Sempre que possível, substitua tabelas visuais por estruturas de listas hierárquicas ou tópicos explicativos.
* **Camada de Texto Ativa:** Certifique-se de que o documento não foi gerado como uma "imagem chapada". O texto deve ser selecionável via cursor (vetorial).
* **Eliminação de Ruídos Gráficos:** Rodapés decorativos, números de página flutuantes no meio do layout, marcas d'água pesadas e elementos puramente estéticos devem ser removidos na matriz de geração do arquivo, pois poluem o algoritmo de fatiamento (*Chunking*).

---

## 💻 3. Snippet de Auditoria Local: Extração Unicoluna com PyMuPDF

Para testar no terminal do seu Ubuntu a leitura inteligente de blocos (evitando a mistura horizontal de duas colunas), utilize o padrão estrutural abaixo:

```python
import fitz  # PyMuPDF

def extrair_texto_por_blocos(pdf_path):
    doc = fitz.open(pdf_path)
    texto_consolidado = []
    
    for pagina in doc:
        # "blocks" extrai uma lista de tuplas: (x0, y0, x1, y1, "texto", block_no, block_type)
        blocos = pagina.get_text("blocks")
        
        # Ordena os blocos verticalmente (y0) e depois horizontalmente (x0)
        blocos.sort(key=lambda b: (b[1], b[0]))
        
        for b in blocos:
            texto_bloco = b[4].strip()
            if texto_bloco:
                texto_consolidado.append(texto_bloco)
                
    return "\n".join(texto_consolidado)
```

---

## 📝 4. Check-list de Governança de Dados para seu Portfólio

- [ ] Os documentos internos do projeto (Briefings, SOW) estão armazenados em formato `.md` ou `.json`?
- [ ] Os PDFs recebidos por terceiros possuem camada de texto ativa (vetorial) ou exigirão OCR?
- [ ] Removi cabeçalhos e rodapés repetitivos dos documentos de texto antes de gerar os embeddings?
- [ ] O layout dos manuais técnicos foi desenhado em coluna única para blindar a leitura linear?