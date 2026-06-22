
| **Plataforma**                       | **Perfil de Usuário** | **Caso de Uso Principal**                           | **Nível de Complexidade** |
| ------------------------------------ | --------------------- | --------------------------------------------------- | ------------------------- |
| **Gemini Enterprise App**            | Business / Equipes    | Agentes de produtividade interna (chat e busca)     | Baixa (Out-of-the-box)    |
| **Conversational Agents**            | Business              | Bots de atendimento (voz ou chat) para clientes     | Média (Low-code)          |
| **CX Agent Studio**                  | Business / Design     | Jornadas não lineares (suporte + vendas) multicanal | Média (Low-code/Visual)   |
| **Gemini Enterprise Agent Platform** | Desenvolvedores       | Agentes customizados via código e frameworks        | Alta (Customizável)       |

### Detalhamento por Categoria

#### Para Usuários de Negócios (Foco em Experiência do Cliente e Produtividade)

- **Gemini Enterprise App:** O ponto de entrada mais simples. Ideal para criar rapidamente ferramentas de chat e pesquisa para uso interno de equipes.
    
- **Conversational Agents:** Plataforma gerenciada para conversas estruturadas. É a escolha certa quando o objetivo é um bot de atendimento que exige múltiplos turnos de conversa.
    
- **CX Agent Studio:** Focado em fluxos complexos. Diferencia-se por permitir a troca de contexto entre diferentes tópicos (ex: mudar de suporte para vendas) sem perder a linha do atendimento em diversos canais (web ou telefone).
    

#### Para Desenvolvedores (Foco em Customização)

- **Gemini Enterprise Agent Platform:** Plataforma voltada para quem precisa definir a lógica do agente via código.
    
    - **Como funciona:** Utiliza o **ADK (Agent Development Kit)** para customização profunda.
        
    - **Implantação:** Uma vez desenvolvido, o agente é implantado via **Agent Runtime** na própria infraestrutura do Google Cloud.
        

Qual dessas plataformas parece se adequar melhor ao projeto que você está planejando agora?


# Gemini Enterprise
A no-code UI and centralized hub for discovering, creating, and running AI Agents focused on internal employee productivity.

# Agent Development Kit (ADK)
The code-first, open-source framework that simplifies the end-to-end development of complex, multi-agent systems with full programmatic control via a Python SDK.

# Vertex AI Agent Builder
The comprehensive platform that provides the tools for grounding agents to enterprise data, managing their lifecycle, and deploying them to a fully managed runtime environment called Agent Engine.

# Conversational Agents
Designed for building customer-facing AI applications (like voice or chat bots) that utilize a reliable, visual state-machine flow model to manage and direct conversations.

### Third-party agents

Third-party agents in Gemini Enterprise are designed to seamlessly integrate with and leverage data from external applications and platforms that are not part of the Google ecosystem, such as Salesforce, Jira, SharePoint, and Microsoft Copilot. Gemini Enterprise supports pre-built connectors for a wide array of these popular third-party tools, ensuring secure and controlled data access by respecting the original access control lists (ACLs) of the source systems. This allows organizations to unify their information across various systems, creating a single point of access for enterprise data. Developers can upload, access, and deploy agents built on these external platforms.