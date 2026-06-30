
### 📖 Engenharia de IA & Arquitetura de Sistemas

Este ficheiro constitui o repositório central atemporal de jargões industriais, conceitos computacionais e mecânicas de baixo nível adotados na infraestrutura de **lucasfrancorocha.com.br** e nos seus estudos de IA.

#### 🅰️ A

- **Análise Estatística de I/O (Input/Output)**
    - _Mapeamento:_ 🇬🇧 _I/O Statistical Analysis_ | 🇪🇸 _Análise Estadístico de E/S_ | 🇫🇷 _Analyse Statistique d'E/S_
    - _Conceito:_ A medição, auditoria e rastreio de como o sistema operacional lê (_Input_) e escreve (_Output_) pacotes físicos de dados no disco rígido (SSD/NVMe).
    
- **Aquecimento do Cache (Cache Warming)**
    - _Mapeamento:_ 🇬🇧 _Cache Warming_ | 🇪🇸 _Calentamiento de Cache_ | 🇫🇷 _Chauffage de Cache_
    - _Conceito:_ Prática de pré-carregar ou executar componentes de software e modelos na memória antes da sua utilização principal, garantindo latência mínima (< 10ms) na primeira requisição do usuário.

- **Árvores de Dependência (`node_modules`)**
    - _Mapeamento:_ 🇬🇧 _Dependency Trees_ | 🇪🇸 _Árboles de Dependencias_ | 🇫🇷 _Arbres de Dépendances_
    - _Conceito:_ A estrutura de pastas aninhadas e encadeadas onde o ecossistema Node guarda todas as sub-bibliotecas e pacotes de terceiros que um determinado projeto precisa para ser executado.

- **Autoatendimento (Self-Attention)**
    - _Mapeamento:_ 🇬🇧 _Self-Attention Mechanism_ | 🇪🇸 _Mecanismo de Autoatención_ | 🇫🇷 _Mécanisme d'Auto-attention_
    - _Conceito:_ O algoritmo matemático central dos _Transformers_ que permite ao modelo calcular a relevância correlativa entre diferentes palavras (ou tokens) dentro de uma mesma janela de contexto, independente da distância física entre elas.
#### 🅱️ B

- **BPE (Byte Pair Encoding)**
    - _Mapeamento:_ 🇬🇧 _Byte Pair Encoding_ | 🇪🇸 _Codificación de Pares de Bytes_ | 🇫🇷 _Codage par Pares de Octets_
    - _Conceito:_ Algoritmo de tokenização que compacta strings de texto em subpalavras baseando-se na frequência de ocorrência de pares de bytes, impactando diretamente a contagem de tokens em idiomas latinos.
## 🅲 C

- **Cache Efêmero**
    - _Mapeamento:_ 🇬🇧 _Ephemeral Cache_ | 🇪🇸 _Caché Efímero_ | 🇫🇷 _Cache Éphémère_
    - _Conceito:_ Área de armazenamento temporário no disco que retém ficheiros descarregados da internet para acelerar execuções subsequentes, podendo ser limpa sem corromper o núcleo do sistema operacional.
    
- **Caminho Absoluto (Absolute Path)**
    - _Mapeamento:_ 🇬🇧 _Absolute Path_ | 🇪🇸 _Ruta Absoluta_ | 🇫🇷 _Chemin Absolu_
    - _Conceito:_ O endereço completo e inequívoco de um ficheiro ou diretório a partir da raiz do sistema operacional (ex: `/home/lucasrocha/...`), garantindo que um comando ou processo funcione em qualquer escopo de execução em background.
    
- **Ciclo de Vida (Lifecycle)**
    - _Mapeamento:_ 🇬🇧 _Software Lifecycle_ | 🇪🇸 _Ciclo de Vida del Software_ | 🇫🇷 _Cycle de Vie du Logiciel_
    - _Conceito:_ O fluxo completo de fases operacionais de um software, abrangendo a sua instalação, carregamento em memória RAM, execução ativa, até ao seu encerramento seguro e limpeza de resíduos no sistema.
    
- **Cold Start (Arranque a Frio)**
    - _Mapeamento:_ 🇬🇧 _Cold Start_ | 🇪🇸 _Arranque en Frío_ | 🇫🇷 _Démarrage à Froid_
    - _Conceito:_ O atraso ou latência que ocorre quando um sistema/modelo precisa carregar pesos, compilar código ou ler ficheiros do zero na primeiríssima vez que é instanciado na máquina.
    
- **Context Stuffing (Injeção Excessiva de Contexto)**
    - _Mapeamento:_ 🇬🇧 _Context Stuffing_ | 🇪🇸 _Saturación de Contexto_ | 🇫🇷 _Surcharge de Contexte_
    - _Conceito:_ Fenômeno ou técnica de preencher agressivamente a janela de contexto de um LLM com documentos recuperados, exigindo do modelo forte resiliência para não ignorar informações dispostas no meio do prompt (_Lost in the Middle_).
## 🅳 D

- **Dependências**
    - _Mapeamento:_ 🇬🇧 _Dependencies_ | 🇪🇸 _Dependencias_ | 🇫🇷 _Dépendances_
    - _Conceito:_ Bibliotecas, frameworks ou blocos de código desenvolvidos por terceiros que o teu programa principal necessita obrigatoriamente para compilar ou funcionar.
    
- **Diretórios de Escopo do Sistema**
    - _Mapeamento:_ 🇬🇧 _System-wide Directories_ | 🇪🇸 _Directorios de Ámbito del Sistema_ | 🇫🇷 _Répertoires à l'Échelle du Système_
    - _Conceito:_ Pastas globais e protegidas pelo Kernel do Linux (como `/usr/bin` ou `/usr/lib`), onde residem os executáveis principais acessíveis a todos os utilizadores do sistema operacional.
    
- **DPO (Direct Preference Optimization)**
    - _Mapeamento:_ 🇬🇧 _Direct Preference Optimization_ | 🇪🇸 _Optimización de Preferencia Directa_ | 🇫🇷 _Optimisation Directe des Préférences_
    - _Conceito:_ Uma técnica de pós-treinamento utilizada para alinhar LLMs diretamente com as preferências humanas (pares de respostas "escolhida" vs "rejeitada"), eliminando a necessidade complexa de treinar um modelo de recompensa separado como se faz no RLHF tradicional.
    
- **`du -sh` (Disk Usage)**
    - _Mapeamento:_ 🇬🇧 _Disk Usage Utility_ | 🇪🇸 _Uso de Disco_ | 🇫🇷 _Utilisation du Disque_
    - _Conceito:_ Comando nativo do Linux utilizado para auditar o armazenamento, onde `-s` resume o tamanho total de uma pasta e `-h` formata o output em escala legível para humanos (ex: Megabytes em vez de bytes puros).
## 🅴 E

- **Embeddings (Vetores de Incorporação)**
    - _Mapeamento:_ 🇬🇧 _Embeddings_ | 🇪🇸 _Incrustaciones / Embeddings_ | 🇫🇷 _Plongements Lexicaux / Embeddings_
    - _Conceito:_ Representações numéricas de conceitos textuais, visuais ou de áudio em um espaço multidimensional denso. Permitem que computadores calculem a proximidade semântica (significado) entre palavras através de geometria matemática.
## 🅵 F

- **Fine-Tuning (Ajuste Fino)**
    - _Mapeamento:_ 🇬🇧 _Fine-Tuning_ | 🇪🇸 _Ajuste Fino_ | 🇫🇷 _Réglage Fin / Fine-Tuning_
    - _Conceito:_ Processo de pegar um modelo de linguagem já pré-treinado em larga escala e continuar o seu treinamento em um conjunto de dados especializado e menor para adaptá-lo a um domínio ou comportamento estilístico muito específico.
    
- **Function Calling (Chamada de Funções)**
    - _Mapeamento:_ 🇬🇧 _Function Calling / Tool Use_ | 🇪🇸 _Llamada de Funciones_ | 🇫🇷 _Appel de Fonctions_
    
    - _Conceito:_ A capacidade de um LLM detectar de forma determinista quando uma ferramenta externa precisa ser acionada, gerando um objeto JSON estruturado contendo os argumentos exatos para que a aplicação execute a função.
## 🅶 G

- **GraphRAG (RAG Baseado em Grafos)**
    - _Mapeamento:_ 🇬🇧 _Graph-based RAG_ | 🇪🇸 _RAG Basado en Grafos_ | 🇫🇷 _RAG Basé sur les Graphes_
    - _Conceito:_ Uma evolução do RAG que combina buscas vetoriais clássicas com Gráficos de Conhecimento (Knowledge Graphs), mapeando entidades e relacionamentos estruturados para responder perguntas macro e globais sobre múltiplos documentos.
## 🅷 H

- **Hashes SHA-256**
    - _Mapeamento:_ 🇬🇧 _SHA-256 Hashes_ | 🇪🇸 _Hashes SHA-256_ | 🇫🇷 _Hachages SHA-256_
    - _Conceito:_ Um identificador criptográfico único de comprimento fixo (uma string hexadecimal de letras e números) que funciona como a "impressão digital" digital e imutável de um ficheiro, bloco de código ou diretório de cache.
    
- **Host Nativo**
    - _Mapeamento:_ 🇬🇧 _Native Host_ | 🇪🇸 _Anfitrión Nativo / Host_ | 🇫🇷 _Hôte Natif_
    - _Conceito:_ O aplicativo cliente principal e definitivo (ex: Claude Desktop) instalado no sistema operacional que consome, gerencia permissões e orquestra servidores MCP em background.
## 🅻 L

- **Latência de Download**
    - _Mapeamento:_ 🇬🇧 _Download Latency_ | 🇪🇸 _Latencia de Descarga_ | 🇫🇷 _Latence de Téléchargement_
    - _Conceito:_ O tempo de atraso e espera despendido enquanto a ligação de rede comunica com servidores remotos para descarregar pacotes, modelos ou atualizações.
    
- **LoRA (Low-Rank Adaptation)**
    
    - _Mapeamento:_ 🇬🇧 _Low-Rank Adaptation_ | 🇪🇸 _Adaptación de Bajo Rango_ | 🇫🇷 _Adaptation de Bas Rang_
    - _Conceito:_ Técnica de PEFT que congela os pesos originais do modelo e injeta matrizes de decomposição de classificação menor (_low-rank matrices_) nas camadas de atenção, reduzindo drasticamente a memória e o hardware necessários para o Fine-Tuning.
## 🅼 M

- **Mapeamento Físico de Execução**
    - _Mapeamento:_ 🇬🇧 _Physical Execution Mapping_ | 🇪🇸 _Mapeo Físico de Ejecución_ | 🇫🇷 _Mappage Physique d'Exécution_
    - _Conceito:_ O ato de engenharia de rastrear o endereço de memória ou a pasta física real no disco onde o sistema operacional armazenou e está a rodar os ficheiros de um programa ativo.
    
- **Model Context Protocol (MCP)**
    - _Mapeamento:_ 🇬🇧 _Model Context Protocol_ | 🇪🇸 _Protocolo de Contexto de Modelo_ | 🇫🇷 _Protocole de Contexte de Modèle_
    - _Conceito:_ Um protocolo padrão aberto unificado (criado pela Anthropic) baseado em JSON-RPC que permite que modelos de IA se conectem de forma segura e padronizada a fontes de dados locais/remotas (_Resources_), ferramentas de execução (_Tools_) e modelos de prompt (_Prompts_).
    
- **Multiplexação**
    - _Mapeamento:_ 🇬🇧 _Multiplexing_ | 🇪🇸 _Multiplexación_ | 🇫🇷 _Multiplexage_
    - _Conceito:_ Técnica de arquitetura de redes e sistemas que permite que múltiplos canais ou fluxos de dados independentes (como os canais Stdio de servidores diferentes) trafeguem de forma concorrente e paralela através do mesmo meio lógico de comunicação sem que ocorra colisão de pacotes.
## 🅿️ P

- **Pydantic**
    - _Mapeamento:_ 🇬🇧 _Pydantic Validation_ | 🇪🇸 _Validación con Pydantic_ | 🇫🇷 _Validation Pydantic_
    - _Conceito:_ Biblioteca de validação de dados para Python baseada em hints de tipo. É amplamente usada no desenvolvimento de IA para forçar os LLMs a responderem em formatos JSON estritos e tipados sem falhas estruturais.
## 🆁 Q

- **QLoRA (Quantized Low-Rank Adaptation)**
    
    - _Mapeamento:_ 🇬🇧 _Quantized LoRA_ | 🇪🇸 _LoRA Cuantizado_ | 🇫🇷 _LoRA Quantifié_
    - _Conceito:_ Uma otimização avançada do LoRA onde o modelo base é compactado em uma precisão de alta fidelidade de 4 bits (NormalFloat4), permitindo treinar modelos gigantescos em GPUs comerciais ou locais.
## 🆁 R

- **RAG (Retrieval-Augmented Generation)**
    - _Mapeamento:_ 🇬🇧 _Retrieval-Augmented Generation_ | 🇪🇸 _Generación Aumentada por Recuperación_ | 🇫🇷 _Génération Augmentée de Récupération_
    - _Conceito:_ Arquitetura sistêmica que estende o conhecimento de um LLM injetando dinamicamente trechos de documentos relevantes extraídos de uma base de dados externa diretamente no prompt do sistema em tempo de execução.
    
- **Rebase (Git)**
    - _Mapeamento:_ 🇬🇧 _Git Rebase_ | 🇪🇸 _Reajuste / Rebase_ | 🇫🇷 _Rebase Git_
    - _Conceito:_ Mecanismo do Git que pega a série de commits criados em uma ramificação local e os reaplica linearmente no topo de uma outra ramificação de referência, mantendo o histórico de desenvolvimento limpo e livre de nós de merge.
    
- **Reranking (Reordenamento Neuronal)**
    - _Mapeamento:_ 🇬🇧 _Reranking Models_ | 🇪🇸 _Modelos de Reordenamiento_ | 🇫🇷 _Modèles de Reranking / Réordonnancement_
    - _Conceito:_ Segunda etapa crítica de um pipeline RAG que pega os top-$K$ documentos recuperados por similaridade vetorial grosseira e usa um modelo de classificação cruzada focado para reordená-los com precisão absoluta de relevância conceitual antes de enviá-los ao LLM.
## 🆂 S

- **Sandboxing de Binários**
    - _Mapeamento:_ 🇬🇧 _Binary Sandboxing_ | 🇪🇸 _Aislamiento de Binarios / Sandboxing_ | 🇫🇷 _Bac à sable de Binaires / Sandboxing_
    - _Conceito:_ Técnica de segurança avançada que isola ficheiros executáveis dentro de perímetros lógicos fechados ("caixas de areia"), impedindo que um script malicioso ou instável corrompa, leia ou polua o resto do sistema operacional do utilizador.
    
- **stderr (Standard Error)**
    - _Mapeamento:_ 🇬🇧 _Standard Error Channel_ | 🇪🇸 _Canal de Error Estándar_ | 🇫🇷 _Canal d'Erreur Standard_
    - _Conceito:_ O canal de saída padrão do Linux reservado nativamente para o direcionamento de mensagens de erro, diagnósticos de falhas e logs críticos gerados por processos de background.
    
- **Stdio (Standard Input/Output)**
    - _Mapeamento:_ 🇬🇧 _Standard I/O Streams_ | 🇪🇸 _Flujos de E/S Estándar_ | 🇫🇷 _Flux d'E/S Standard_
    - _Conceito:_ O canal bidirecional padrão do Kernel do Linux de entrada (_stdin_) e saída (_stdout_) de dados, utilizado para estabelecer comunicação de latência zero entre dois programas em background.
    

## 🆃 T

- **`tail -f` (Follow)**
    - _Mapeamento:_ 🇬🇧 _Tail Follow Command_ | 🇪🇸 _Comando de Seguimiento de Logs_ | 🇫🇷 _Commande de Suivi de Flux_
    - _Conceito:_ Utilitário nativo do Ubuntu utilizado para ler as linhas finais de um ficheiro de texto de forma viva e assíncrona, imprimindo no terminal novas atualizações no exato milissegundo em que são gravadas no disco.
    
- **Tokenização (Tokenization)**
    - _Mapeamento:_ 🇬🇧 _Tokenization_ | 🇪🇸 _Tokenización_ | 🇫🇷 _Tokenisation_
    - _Conceito:_ O processo de quebrar uma string de texto bruta em pequenos pedaços numéricos (caracteres, subpalavras ou palavras inteiras) chamados _tokens_, que servem como a unidade atômica fundamental que os modelos de IA conseguem processar matematicamente.
## 🆆 W

- **WBS (Work Breakdown Structure)**
    - _Mapeamento:_ 🇬🇧 _Work Breakdown Structure (WBS)_ | 🇪🇸 _Estructura de Desglose de Trabajo (EDT)_ | 🇫🇷 _Structure de Découpage do Projet (SDP)_
    - _Conceito:_ Uma decomposição hierárquica e probabilística do escopo total de um projeto em tarefas menores e gerenciáveis. É o framework ideal para estimar horas precisas e estruturar cronogramas complexos de engenharia.

Guarde este repositório! Conforme avançar pelas semanas do bootcamp e os termos começarem a surgir na sua tela preta do terminal, volte aqui para correlacionar a mecânica física do sistema operacional com a lógica abstrata da inteligência artificial.


# Apendice


### Vector Search 2.0

- **Fundamentos:**
    
    - **Embeddings:** Vetores numéricos que capturam a semântica de dados multimodais.
        
    - **Vector Database:** Sistema especializado em busca por similaridade semântica.
        
    - **ScaNN:** Algoritmo de busca do Google focado em performance e escala (bilhões de vetores).
        
- **Mecanismos de Busca:**
    
    - **kNN (k-Nearest Neighbors):** Busca exata, ideal para desenvolvimento e datasets pequenos.
        
    - **ANN (Approximate Nearest Neighbor):** Busca aproximada, ideal para produção em larga escala, focando em baixíssima latência.
        
    - **Hybrid Search:** Integração de busca semântica + busca textual (keyword), essencial para cobrir SKUs e termos novos.
        
    - **RRF (Reciprocal Rank Fusion):** Técnica que normaliza e mescla scores de busca semântica e textual.
        
- **Arquitetura e Operação:**
    
    - **Collection:** Container que unifica armazenamento de dados (metadados) e vetores (dispensa banco de dados externo/Feature Store).
        
    - **Auto-Embeddings:** Geração automática de vetores pelo modelo, eliminando complexidade de infra de embedding.
        
    - **Task Type Embeddings:** Técnica de otimização de "assimetria" (ex: definir se o dado é `RETRIEVAL_DOCUMENT` ou `YoutubeING`) que pode aumentar a relevância em até 40%.



# Glossary - 01 Build Your Own Small Language Model

This document is a quick-reference guide of terms, definitions, and concepts featured in the course. 

  

**Artificial intelligence (AI):** A broad field encompassing the development of computer systems capable of performing tasks that typically require human intelligence, such as learning, problem-solving, and decision-making.   

  

**Batching:** A training technique where the dataset is divided into smaller groups (batches), and the model's parameters are updated after processing each batch. This improves computational efficiency and can lead to more stable training.

  

**Corpus (text):** A large and structured set of texts used for training language models and other natural language processing tasks.

  

**Continuation:** The text a language model generates following a given input, known as a prompt. The model produces this output by sequentially predicting the most probable next word or token, building upon the provided context. 

  

**Dataset:** A collection of data, often organized in a structured format, used for training, evaluating, and testing machine learning models.

  

**Deterministic:** A system where the output is uniquely determined by the input. In language models, always selecting the token with the highest probability during decoding would be a deterministic (or "greedy") approach.

  

**Encode and decode functions:** In the context of sequence-to-sequence models (like some transformer architectures), the encode function processes the input sequence into a fixed-length representation (context vector), and the decode function generates the output sequence based on this context vector.

  

**Epoch:** A complete pass through the entire training dataset during the training process. Multiple epochs are often required for the model to learn effectively.

  

**Evaluation:** The process of assessing the performance of a machine learning model using specific metrics.

  

**Generation:** The overarching process of creating new text from scratch or in response to a specific prompt. This is a broader term than continuation. While **continuation** is a specific method of generation (predicting the next part of an existing text), **generation** can also refer to creating a summary, translating text, or writing a creative story based on a single instruction. It's the overall act of producing new language, often with a specific goal in mind.

  

**Hyperparameters:** Parameters of a machine learning model that are set before the training process begins. They control various aspects of the training, such as the learning rate, batch size, and the number of layers in a neural network. These are tuned to optimize the model's performance.

  

**Language model (LM)**: A system that learns to predict the next word in a sequence based on previous words or offers a way to assign probability to a sequence of words.

  

**Large language model (LLM):** A language model with a very large number of parameters (the variables the model learns during training), typically resulting in enhanced capabilities in understanding and generating human-like text.

  

**Loss:** A measure of the error between the model's predictions and the actual target values during training. The goal of training is to minimize this loss.

  

**Machine learning:** A subfield of artificial intelligence that enables computer systems to learn from data without being explicitly programmed.  

  

**N-grams:** A contiguous sequence of n words in a text. Examples include:  
  

- Unigram: One word (e.g., "the").
    
- Bigram: Two words (e.g., "the cat").
    
- Trigram: Three words (e.g., "the cat sat").  
      
    

**Natural language processing (NLP):** A field of artificial intelligence focused on enabling computers to understand, interpret, and generate human language.  

  

**Optimization:** The process of adjusting the parameters of a machine learning model during training to minimize the loss function and improve its performance.

  

**Padding:** A technique used to ensure that all sequences within a batch have the same length. Shorter sequences are padded with special tokens (e.g., _<pad>_) so they can be processed uniformly.

  

**Parameters:** The internal variables of a machine learning model that are learned from the training data. These weights and biases are adjusted during the optimization process to improve the model's predictions.

  

**Probabilities:** Numerical values between 0 and 1 representing the likelihood of an event occurring. In language models, probabilities are assigned to words or sequences of words.

  

**Probability distribution:** A mathematical function that describes the likelihood of different outcomes or values for a random variable. In machine learning, especially in language models, it often represents the probability of different words or tokens occurring in a given context.

  

**Prompt:** An initial input given to a language model to elicit a desired response or generation of text.

  

**Small language model (SLM):** A language model with a relatively smaller number of parameters compared to large language models.

  

**Sparsity:** A characteristic of language data where most possible combinations of words do not occur. This results in many zero or near-zero values in the statistical representations of language.

  

**Stochastic:** A system that involves randomness, meaning the output is not fixed for a given input. In language models, stochastic decoding involves sampling from the probability distribution of the next possible tokens. This introduces variability in the generated text.

  

**Tokenization:** The process of breaking down text into smaller units called tokens, which can be words, subwords, or characters. This is a fundamental step in preparing text data for natural language processing.

  

**Transformer models:** A type of neural network architecture that has achieved strong results in various natural language processing tasks. These models work auto-regressively by generating one token at a time and using the previous context for the next one.

  

**Truncation:** A technique used to shorten sequences that exceed a predefined maximum length. This is often necessary to manage computational resources and ensure compatibility with model architectures that have fixed input size limitations.

  

**Tuples:** In the context of data, a tuple is an ordered sequence of elements. In machine learning, data points are often represented as tuples of features.

  

**Unknown tokens:** Tokens (e.g., words) that were not encountered in the training data. These are often represented by a special _<unk>_ token during pre-processing to allow the model to handle unseen vocabulary.