# 📑 Papers Científicos de Referência: Playlist de Modelos de Sequência (Andrew Ng)

Este documento mapeia cronologicamente os artigos fundamentais e publicações acadêmicas utilizados como base teórica para as aulas da playlist. Eles representam os marcos históricos que revolucionaram o Processamento de Linguagem Natural (PLN).

---

## 🔬 1. A Revolução dos Embeddings (Vetorização Semântica)

### 📄 Paper 1: representações Iniciais do Word2Vec
* **Título Oficial:** *Efficient Estimation of Word Representations in Vector Space* (2013)
* **Autores:** Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean.
* **Instituição:** Google Research
* **Temas Principais:** * Introdução dos modelos preditivos **CBOW** (Continuous Bag-of-Words) e **Skip-gram**.
  * Codificação de semântica e sintaxe em vetores contínuos de baixa dimensão.
  * Descoberta das propriedades algébricas de analogia (ex: $\text{Rei} - \text{Homem} + \text{Mulher} \approx \text{Rainha}$).
* **Vídeos Relacionados:** `RNN17` e `RNN18`

### 📄 Paper 2: Otimização por Amostragem Negativa
* **Título Oficial:** *Distributed Representations of Words and Phrases and their Compositionality* (2013)
* **Autores:** Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg Corrado, Jeffrey Dean.
* **Instituição:** Google Research
* **Temas Principais:**
  * **Negative Sampling (Amostragem Negativa):** Modificação matemática na função de custo para substituir a camada Softmax global. O algoritmo passa a atualizar apenas o token correto e uma pequena amostra de tokens errados, tornando o treinamento computacionalmente viável.
* **Vídeos Relacionados:** `RNN19`

### 📄 Paper 3: Abordagem Estatística Global (GloVe)
* **Título Oficial:** *GloVe: Global Vectors for Word Representation* (2014)
* **Autores:** Jeffrey Pennington, Richard Socher, Christopher D. Manning.
* **Instituição:** Stanford University
* **Temas Principais:**
  * Crítica aos modelos puramente locais (Word2Vec).
  * Uso de matrizes globais de co-ocorrência termo a termo de corpora massivos.
  * Combinação de vantagens de fatoração de matrizes globais com abordagens de janelas de contexto locais.
* **Vídeos Relacionados:** `RNN20`

---

## ⚖️ 2. Ética e IA Responsável (Mitigação de Vieses)

### 📄 Paper 4: Desenviesamento Vetorial (Debiasing)
* **Título Oficial:** *Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings* (2016)
* **Autores:** Tolga Bolukbasi, Kai-Wei Chang, James Zou, Venkatesh Saligrama, Adam Kalai.
* **Instituição:** Boston University & Microsoft Research
* **Temas Principais:**
  * Demonstração empírica de como os embeddings absorvem e amplificam preconceitos e estereótipos históricos de gênero e raça contidos na internet.
  * Desenvolvimento do algoritmo de 3 passos: 
    1. Identificação da direção do viés (via PCA sobre pares definicionais).
    2. Neutralização (projeção ortogonal de palavras de gênero socioeconomicamente neutro).
    3. Equalização (ajuste simétrico de termos definicionais morfológicos).
* **Vídeos Relacionados:** `RNN22`

---

## ⚡ 3. Modelos de Tradução e Mecanismos de Atenção

### 📄 Paper 5: Fundamentos do Sequence-to-Sequence (Seq2Seq)
* **Título Oficial:** *Sequence to Sequence Learning with Neural Networks* (2014)
* **Autores:** Ilya Sutskever, Oriol Vinyals, Quoc V. Le.
* **Instituição:** Google Users / Google Brain
* **Temas Principais:**
  * Introdução da arquitetura **Encoder-Decoder** utilizando redes recorrentes profundas (LSTMs).
  * Mapeamento de sequências de comprimento variável para outras sequências de comprimento variável (essencial para tradução automática e sistemas de diálogo).
* **Vídeos Relacionados:** `RNN23`, `RNN24`, `RNN25`, `RNN26` e `RNN27`

### 📄 Paper 6: A Métrica de Avaliação Automática (BLEU)
* **Título Oficial:** *BLEU: a Method for Automatic Evaluation of Machine Translation* (2002)
* **Autores:** Kishore Papineni, Salim Roukos, Todd Ward, Wei-Jing Zhu.
* **Instituição:** IBM T.J. Watson Research Center
* **Temas Principais:**
  * Desenvolvimento do algoritmo *Bilingual Evaluation Understudy* (BLEU score).
  * Métrica matemática baseada na precisão de n-gramas para avaliar a qualidade de textos traduzidos por máquinas em comparação com traduções humanas.
* **Vídeos Relacionados:** `RNN28`

### 📄 Paper 7: O Mecanismo de Atenção (Gênese dos Transformers)
* **Título Oficial:** *Neural Machine Translation by Jointly Learning to Align and Translate* (2014)
* **Autores:** Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio.
* **Instituição:** Jacobs University (Alemanha) & Université de Montréal (Canadá)
* **Temas Principais:**
  * Crítica ao gargalo do Seq2Seq tradicional (tentar comprimir uma frase inteira em um vetor fixo).
  * **Mecanismo de Atenção:** Permite ao modelo buscar dinamicamente e "focar" em partes específicas da sequência de entrada (Encoder) a cada palavra gerada na saída (Decoder).
  * Base conceitual direta que eliminou a necessidade de recorrência linear e deu origem à arquitetura *Transformer*.
* **Vídeos Relacionados:** `RNN29` e `RNN30`

---

## 🔍 Como usar este material no seu Obsidian:
Você pode transformar os títulos de cada paper listado acima em links internos (ex: `[[Efficient Estimation of Word Representations in Vector Space]]`). À medida que você assistir aos vídeos e fizer anotações sobre as fórmulas e intuições matemáticas de Andrew Ng, salve-as dentro destas respectivas páginas para criar um gráfico de conhecimento interconectado.


## 📘 Guia de Consulta: A Engenharia das RNNs (Dia 02)

### 1. A Estrutura do Sinal (Input/Output)

Diferente das redes neurais padrão, as Redes Neurais Recorrentes (RNNs) lidam com dados que têm uma ordem lógica.

 **x :** Representa o "Time-step" ou a posição do dado na sequência (ex: a 3ª palavra de uma frase).

**Tx​ :** O comprimento total da sequência de entrada (ex: se a frase tem 9 palavras, Tx​=9).

**Ty ​:** O comprimento da sequência de saída, que pode ou não ser igual a Tx​.

### 2. A "Memória" da Rede (Hidden State)

**O segredo das RNNs é que elas não olham apenas para o x atual, elas recebem uma "herança" do passado.

**a**: É a ativação (o estado oculto). Ela carrega a informação do que a rede aprendeu nos passos anteriores para o passo atual.

- [**Waa​ e Wax​**]: São as matrizes de pesos. [Wax]​ regula a entrada atual e [Waa]​ regula a importância da memória vinda do passado.

### 3. As Equações Fundamentais (Para o seu Cheat Sheet)

Aqui está o que faz os transistores trabalharem no seu Linux:

1. **Cálculo da Memória (a):**

$$
     a<t>=g(Waa​a<t−1>+Wax​x<t>+ba​)
$$


   _Nota:_ A função g costuma ser **tanh** ou **ReLU** para evitar que o sinal morra (o tal Vanishing Gradient).

2. **Cálculo da Previsão (y^​):**

$y^​<t>=g2​(Wya​a<t>+by​)$

- _Nota:_ Aqui o g2​ costuma ser **Sigmoid** para dar uma probabilidade entre 0 e 1.

### 4. O Sensor de Erro (Loss Function)

3. **Para cada "chute" da rede, medimos o erro com a função de perda logarítmica:

$L⟨t⟩(y^​⟨t⟩,y⟨t⟩)=−y⟨t⟩logy^​⟨t⟩−(1−y⟨t⟩)log(1−y^​⟨t⟩)$

O custo total (J) é simplesmente a **soma de todos os erros** da sequência.

### 🧠 Dica de Dev para o Lucas:

Nos vídeos de amanhã sobre **Vetorização**, você verá o Andrew Ng simplificar isso tudo para uma única matriz [Waa​⋮Wax​]. Isso é o que permite que o hardware processe a frase inteira como se fosse uma única operação matemática gigante.