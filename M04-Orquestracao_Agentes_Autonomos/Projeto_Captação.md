
### Ativar as Portas de Comunicação (APIs)

Para que o nosso futuro contêiner consiga conversar com o mundo externo e com o Google Workspace, precisamos habilitar três chaves mestras no menu de **APIs e Serviços > Biblioteca**:

- **Google Places API:** Permite que o agente pesquise os estabelecimentos e nichos comerciais diretamente na base de dados de mapas do Google.

**Chave API =**
   
- **Google Sheets API:** Permite que o agente escreva os resultados diretamente na planilha que você vai compartilhar com ele.

   **Chave API =**  .JSON > 
   
- **Cloud Run API / Cloud Functions API:** O ecossistema _serverless_ onde o nosso contêiner Docker vai morar e rodar o Python de forma assíncrona.

   **Chave API "Cloud Run Admin API"=**  

   **Chave API "Cloud Run Admin API"=**  


## INFORMAÇÕES DA PLANILHA

- **A (DATA):** Data de entrada.
    
- **B (STATUS):** Essa primeira variação controla o canal de abordagem aberta no seu dropdown (`✉️ E-mail`, `⏳ Seguir`, `📧 E-mail`, `📞 Whatsapp`, `📬 Ambos`).
    
- **C (Empresa):** Nome do lead.
    
- **D (Tempe):** Temperatura do lead `(☀️,🔥,🎯)
    
- **E (E-mail):** Endereço eletrônico.
    
- **F (Coluna sem nome, mas com ícones):** É aqui que estão os seus seletores visuais redondos com bandeiras/ícones (azul/laranja), provavelmente para controle interno ou status de envio.
    
- **G (Telefone):** Esta coluna está com o título "Telefone", mas repare que ela está **totalmente em branco** nas suas linhas atuais!
    
- **H (WhatsApp):** É aqui que você jogou todos os números de telefone atuais (sejam fixos ou celulares).
    
- **I (Segmento):** Ramo de atuação.
    
- **J (Bairro):** Coluna para o bairro (atualmente vazia no seu histórico).
    
- **K (Cidade):** Coluna para o município (`SBC`, `Ribeirão P`, `Campinas`).
    
- **L (Gatilho de Venda):** Classificação do site (`Site Robusto / Recém feito`, etc.).
