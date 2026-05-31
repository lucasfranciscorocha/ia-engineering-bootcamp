
# 📐 Similaridade de Cosseno (Geometria do Contexto)

### ⚙️ O Conceito
É a métrica matemática usada para medir a proximidade semântica entre duas ideias dentro de um espaço multidimensional. Ela não mede o tamanho dos vetores, mas sim o **ângulo** entre eles.

$$\text{Similaridade} = \cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|}$$

* **Ângulo de 0° (Cosseno = 1):** Ideias idênticas ou altamente correlacionadas.
* **Ângulo de 90° (Cosseno = 0):** Ideias ortogonais, totalmente irrelevantes entre si.

### 🛠️ Aplicação
É o motor por trás de qualquer sistema de RAG (Geração Aumentada por Recuperação). Permite que o seu agente autônomo pegue um briefing de design de um cliente em texto bruto, calcule os vetores, e encontre nas suas pastas os trechos exatos de código CSS ou componentes WordPress que resolvem aquele problema específico.