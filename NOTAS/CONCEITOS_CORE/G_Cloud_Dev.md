
### Núcleo de IA e Agentes

- **Agent Platform API**: Base para criar e gerenciar agentes conversacionais.
    
- **Agent Registry API**: Gerencia o catálogo de agentes disponíveis.
    
- **Model Armor API**: Protege modelos de IA contra abusos e ataques.
    
- **Cloud Text-to-Speech API**: Converte texto em fala natural.
    

### Desenvolvimento, Apps e Dados

- **App Hub / Topology API**: Gerenciam a organização e a estrutura de aplicações no projeto.
    
- **Dataform API**: Gerencia e automatiza transformações de dados.
    
- **Notebooks API**: Ambiente para desenvolvimento e execução de código de ciência de dados.
    
- **App Lifecycle Manager**: Gerencia o ciclo de vida completo de aplicações.
    

### Infraestrutura e Segurança

- **Compute Engine API**: Cria e gerencia máquinas virtuais (essencial para muitos serviços).
    
- **IAM / Connectors API**: Gerencia identidades, permissões e conexões seguras.
    
- **Cloud Identity-Aware Proxy (IAP)**: Controla acesso seguro a aplicações sem VPN.
    
- **Network Security / Services API**: Gerenciam as regras de tráfego e proteção da rede.
    
- **Cloud Storage**: Armazenamento de arquivos e dados em nuvem.
    

### Observabilidade e Monitoramento

- **Cloud Logging / Monitoring / Telemetry / Trace / Observability API**: Conjunto de ferramentas essenciais para rastrear, monitorar desempenho, diagnosticar falhas e coletar logs das aplicações.
    

**Dica:** Os serviços que você já tem **Enabled** (como Logging, Monitoring, Storage e Agent Platform) são a base operacional necessária para o seu projeto atual. Os que estão **Not enabled** são específicos para funcionalidades avançadas de rede, segurança e computação que, por enquanto, não são essenciais para o seu backend rodar.