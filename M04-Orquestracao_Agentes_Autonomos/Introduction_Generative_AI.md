
## 1. Princípios de "Prompts Simples" (Unfancy Prompts)
O objetivo principal é reduzir o ruído e evitar ambiguidades para que o modelo entenda exatamente a intenção.

* **Seja Conciso:** Evite explicações excessivas. Vá direto ao ponto.
* **Seja Específico e Bem-Definido:** Prompts genéricos levam a respostas genéricas. Defina claramente o que deseja (ex: "Liste formas que tornam a Terra única" em vez de "Fale sobre a Terra").
* **Uma Tarefa por Vez:** Não empilhe múltiplas perguntas complexas em um único prompt. Divida-as para melhorar a precisão da resposta.

![[Screenshot_20260618_111130.png]]
![[Screenshot_20260618_111238.png]]
![[Screenshot_20260618_111410.png]]
## 2. Lidando com Desafios Comuns
* **Alucinações:** LLMs podem inventar fatos com confiança.
    * *Dica:* Se precisar de fatos críticos, não confie cegamente.
    * *System Instructions:* Utilize instruções de sistema para definir guardrails (regras) para o modelo, limitando o escopo do que ele pode ou não responder.
* **Variabilidade:** Respostas generativas (criativas) são úteis para brainstorming, mas variam muito. 
    * *Técnica:* Converta tarefas generativas em tarefas de **classificação** (ex: dar opções de escolha) para maior controle sobre a saída.

![[Screenshot_20260618_111817.png]]
![[Screenshot_20260618_111924.png]]
![[Screenshot_20260618_112037.png]]
![[Screenshot_20260618_112140.png]]
![[Screenshot_20260618_112229.png]]
## 3. Melhorando a Qualidade com Exemplos (In-Context Learning)
Fornecer exemplos ajuda o modelo a entender o formato e o comportamento esperado.

* **Zero-shot:** Sem exemplos. Mais criativo, menos previsível.
* **One-shot:** Um exemplo. Guia o modelo sobre o formato desejado.
* **Few-shot:** Alguns exemplos (geralmente 1-5). Melhora drasticamente a consistência e a qualidade para tarefas específicas.

![[Screenshot_20260618_112331.png]]
![[Screenshot_20260618_112405.png]]


Experiment with **Temperature**:

- **Explanation:** Temperature controls randomness. Lower values (e.g., 0.0-0.2) make the output more focused and deterministic. Higher values (e.g., 1.5-2) encourage more diverse or creative responses.

Experiment with **Output Token Limit**:

- **Explanation:** This sets the maximum number of tokens (parts of words) the model can generate for its response.

Experiment with **Top-P**:

- **Explanation:** Top-P (nucleus sampling) also controls randomness. It considers only the most probable tokens whose combined probability mass exceeds the Top-P value. A value of `1.0` considers all tokens. Lowering Top-P (e.g., to `0.8`) makes the output more focused, similar to lowering temperature.

1. Briefly review other settings in the **Advanced** Model Settings panel:
    
    - **Safety Filter Settings:** These are active by default to help block harmful content. For this lab, you'll use the default settings.
    - **Thinking Budget**: This parameter guides the model on the number of thinking tokens to use when generating a response. A higher token count generally allows for more detailed reasoning, which can be beneficial for tackling more complex tasks. It defaults to **Auto**, but can also be set to **Off** or **Manual**. When set to Manual, the model stops analyzing after reaching the specified token limit; you can set a lower limit for simpler tasks and a higher limit for more complex ones.
    - **Structured output**: Forces the model to generate a response that strictly follows a predefined schema (like JSON).
    - **Grounding: Google Search**: Connects the model to Google Search or Maps, enabling it to answer with real-time, public information.
    - **Grounding: Your data**: Allows the model to retrieve information from your own data sources (like Agent Platform Search or RAG Engine) to answer context-specific questions.

#### Glossário

| Termo                   | Definição                                                                                                                  |
| :---------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| **LLM**                 | *Large Language Model*. Modelo treinado em grandes volumes de texto para processar linguagem natural.                      |
| **Prompt**              | O comando ou instrução de entrada enviado para o modelo.                                                                   |
| **Alucinação**          | Resposta gerada pelo LLM que parece correta e confiante, mas não é baseada em fatos ou na realidade.                       |
| **System Instruction**  | Instrução de alto nível enviada ao modelo que define seu comportamento, missão e restrições.                               |
| **In-Context Learning** | Capacidade do modelo de aprender ou adaptar seu comportamento a partir de exemplos fornecidos dentro do próprio prompt.    |
| **Zero/One/Few-shot**   | Técnicas que variam a quantidade de exemplos (0, 1 ou vários) fornecidos no prompt para guiar a resposta.                  |
| **Guardrail**           | Mecanismo (geralmente via System Instruction) para impedir que o chatbot saia do tópico ou responda perguntas indesejadas. |
| **Temperature**         | Parâmetro que controla a aleatoriedade da resposta (ex: 0.0 é determinístico, 1.0 é mais criativo/arriscado).              |
