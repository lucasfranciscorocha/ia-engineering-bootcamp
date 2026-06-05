
### 1. Algoritmos de Decomposição de Tarefas (Task Decomposition)

**Agentes autônomos falham miseravelmente quando recebem um objetivo macro e abstrato (ex: _"Otimize o SEO do site inteiro"_). O planejamento avançado força o modelo a quebrar o problema em subproblemas tratáveis.
- **Decomposição por Prompting (Chain of Thought / Least-to-Most):** O agente escreve explicitamente uma lista de sub-tarefas antes de agir.
- **Decomposição por Código:** O framework (como LangGraph ou CrewAI) intercepta o objetivo e distribui sub-tarefas específicas para agentes especialistas ou funções atômicas menores.

### 2. Padrões Avançados de Raciocínio: Além do ReAct

**Embora o ciclo _Reason + Act_ (Pensar e Executar) seja o padrão industrial, tarefas complexas exigem ramificações e buscas em árvore:
- **Tree of Thoughts (ToT):** O agente não segue apenas um caminho de raciocínio. Ele gera múltiplas ramificações alternativas de pensamentos para resolver um problema, avalia o progresso de cada ramificação (atuando como seu próprio crítico) e decide se faz um _backtracking_ (volta atrás) se perceber que entrou em um beco sem saída.

### 3. Loops de Autoreflexão e Crítica (Self-Reflection / Critique Loops)

**Permite que o agente avalie a qualidade do seu próprio output ou do resultado de uma ferramenta antes de considerá-lo finalizado.
- **Fluxo de Reflexão:** O agente executa uma tarefa $\rightarrow$ Um prompt de crítica avalia o resultado buscando falhas ou violações de restrições $\rightarrow$ O agente original recebe o feedback e refaz o trabalho corrigindo os erros.

Imagine o fluxo do agente estruturado sob a lógica do **Tree of Thoughts / Self-Reflection**:
## Ajuste automatizado de espaçamento CSS em um formulário de contato.
```
[Objetivo Macro] -> Reduzir o espaçamento vertical excessivo do formulário de parcerias.

1. FASE DE PLANEJAMENTO (Decomposição):
   └─ Tarefa 1: Ler o arquivo CSS local do tema.
   └─ Tarefa 2: Identificar as classes associadas aos campos do formulário (.wpcf7-form-control ou similares).
   └─ Tarefa 3: Calcular a redução ideal de padding/margin.
   └─ Tarefa 4: Sobrescrever as propriedades mantendo a responsividade.

2. FASE DE EXECUÇÃO E REFLEXÃO (O Loop Crítico):
   ├─ [Ação]: Agente altera o CSS para 'margin-bottom: 5px;'.
   ├─ [Reflexão/Crítica]: "A redução quebrou o alinhamento do label com o input no mobile?"
   ├─ [Avaliação]: Se SIM, faz o Backtracking -> Tenta 'margin-bottom: 12px; e padding-top: 2px;'.
   └─ [Resultado]: Valida contra as restrições de acessibilidade visual e finaliza.
```

## Exercício - Planejamento de Agente.

[Objetivo Macro] -> Verificação de Paddings formulários.

1. FASE DE PLANEJAMENTO (Decomposição):
   └─ Tarefa 1: Ler o arquivo CSS local do tema.
   └─ Tarefa 2: Identificar os espaçamentos dos campos do formulário.
   └─ Tarefa 3: Ler valor enviado para padding.
   └─ Tarefa 4: Sobrescrever valores antigos garantindo padronização.

2. FASE DE EXECUÇÃO E REFLEXÃO (O Loop Crítico):
   ├─ [Ação]: Agente altera o CSS para 'Padding: Y px , Y px , Y px , Y px ;'.
   ├─ [Reflexão/Crítica]: "Comparar todos os campos de input no mobile e desktop?"
   ├─ [Avaliação]: Se Não, faz o Backtracking -> Reinserção 'padding:  Y px , Y px , Y px , Y px ;'.
   └─ [Resultado]: Valida comparnando os valores inseridos com o enviado pelo operador.


## 🧠 Engenharia do Prompt de Reflexão (O Agente Crítico)

Para que a sua **Tarefa 4** e a **Fase de Avaliação** funcionem de maneira determinística, o agente validador precisa operar sob o seguinte perfil:

## ROLE
Você é um Engenheiro de Qualidade de Software especialista em CSS Orientado a Componentes e Acessibilidade UI/UX. Sua única função é auditar as alterações de código propostas pelo Agente Desenvolvedor.

## TASK
Analise o bloco CSS gerado e compare os valores inseridos (`Padding: Ypx Ypx Ypx Ypx;`) com os parâmetros originais enviados pelo operador humano.

### CONSTRAINTS (Restrições Rígidas)
1. QUEBRA DE LAYOUT: Se a alteração remover ou sobrescrever propriedades de Media Queries (`@media`) sem replicar o comportamento responsivo para Mobile e Desktop, o output DEVE ser rejeitado.
2. SINTAXE: Verifique se a sintaxe do short-hand de padding está correta (ex: `padding: 12px 16px;` ou `padding: 12px 16px 12px 16px;`). Se houver vírgulas separando os valores dentro da propriedade (ex: `padding: Ypx, Ypx`), rejeite imediatamente.
3. VALIDAÇÃO DE ESCOPO: Certifique-se de que a alteração afeta estritamente as classes do formulário (.wpcf7-form-control ou correlatas) e não propriedades globais de input do tema que possam impactar outras páginas.

### OUTPUT FORMAT (JSON Rigoroso)
Você deve responder estritamente neste formato JSON:
```
{
  "status": "APPROVED" | "REJECTED",
  "reason": "Explicação concisa do motivo da aprovação ou falha",
  "suggested_backtracking_action": "Instrução clara de correção caso seja rejeitado"
}
```

## 🔄 Como o Sistema Executa o seu Backtracking

Na prática (usando frameworks como LangGraph), o loop que você desenhou se comporta como uma estrutura condicional baseada no JSON do crítico:

1. O **Agente Desenvolvedor** propõe a alteração.
    
2. O **Agente Crítico** roda o prompt acima sobre a alteração.
    
3. Se o `status` retornar `"REJECTED"`, a aresta condicional do grafo intercepta o fluxo, lê a `suggested_backtracking_action`, e joga o contexto de volta para a **Tarefa 3** ou **Tarefa 4** para o Desenvolvedor tentar novamente.
    
4. Se retornar `"APPROVED"`, o código é persistido no arquivo local do seu Ubuntu.

