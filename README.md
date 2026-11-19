# Confeitaria

## O Problema
- Qual é o problema? 
    - O dono não sabe quais tipos de doces são os menos vendidos no mês, o que dificulta ajustar a produção e evitar desperdício de insumos
- Quem sofre com ele?
    - o dono
- Como é hoje?
    - olhando manualmente os pedidos
- Como saber que resolveu?
     - Quando a tela exibir os tipos de doces e quantas vezes aparecem nos pedidos do mês, incluindo o aviso de quando não houver vendas no mês permitindo identificar os menos vendidos

### Estórias
- Estória 1
    - Como dono, quero ver os tipos de doces menos vendidos no mês, para ajustar a produção e evitar desperdício de insumos
    - Critérios de Aceitação
        - Tipo de doce que não esteja cadastrado no sistema não aparece na listagem.
        - Tipo de doce que possui 0 na contagens de pedidos não aparece
        - Tipos de doces com vendas no mês aparecem com a contagem de aparição nos pedidos, ordenados de forma crescente
        - Quando todos os tipos tiverem zero vendas no mês, a tela exibe "nenhuma venda este mês" e não fica em branco.
    - Tarefas
        - Issue 1A (regra): Implementar contagem mensal por tipo de doce, ordenação para destacar os menos vendidos e retorno de "nenhuma venda este mês" sem vendas | Milestone: Aula 02 | Assignee: (Talasca e Weslei)
        - Issue 1B (dados): Criar consulta no banco para obter tipos de doces cadastrados e respetivas ocorrências nos itens de pedido do mês | Milestone: Aula 02 ou Aula 03 | Assignee: (Talasca e Weslei)
        - Issue 1C (interface): Exibir na tela a lista de doces menos vendidos ou a mensagem "nenhuma venda este mês" | Milestone: Aula 03 | Assignee: (Talasca e Weslei)

- Estória 2
    - Como atendente, quero ver os pedidos ainda não entregues com os respetivos doces e datas, para organizar a entrega no balcão sem me perder nas anotações
    - Critérios de Aceitação
        - Pedidos já entregues ou cancelados não aparecem na lista de pendentes
        - Cada pedido pendente exibe cliente, itens/doces e data prevista de entrega
        - Quando não houver nenhum pedido pendente, a tela exibe "nenhum pedido pendente" e não fica em branco.
    - Tarefas
        - Issue 2A (regra): Filtrar apenas pedidos com estado pendente, ordenar por data prevista e devolver "nenhum pedido pendente" quando vazio | Milestone: Aula 03 | Assignee: (Talasca e Weslei)
        - Issue 2B (dados): Consultar pedidos em aberto juntando dados do cliente e dos itens/doces associados | Milestone: Aula 03 | Assignee: (Talasca E Weslei)
        - Issue 2C (interface): Apresentar na tela os pedidos pendentes com cliente, doces e data, ou o aviso de ausência de pendentes | Milestone: Aula 04 | Assignee: (Talasca e Weslei)

- Estória 3
    - Como atendente, quero consultar rapidamente o preço unitário de cada tipo de doce cadastrado, para responder aos clientes no balcão sem procurar em vários lugares
    - Critérios de Aceitação
        - Tipos de doces inativos ou removidos não aparecem na consulta ativa
        - Cada tipo de doce ativo é exibido com o respetivo preço unitário formatado
        - Se não existir nenhum tipo de doce ativo cadastrado, a tela exibe "nenhum doce cadastrado" e não fica em branco
    - Tarefas
        - ssue 3A (regra): Filtrar tipos de doces ativos, formatar valores unitários e retornar "nenhum doce cadastrado" quando a lista estiver vazia | Milestone: Aula 04 | Assignee: (Talasca e Weslei)
        - Issue 3B (dados): Consultar na base de dados os tipos de doces ativos e os respetivos preços | Milestone: Aula 04 | Assignee: (Talasca e Weslei)
        - Issue 3C (interface): Mostrar na tela a listagem de preços por tipo de doce ou a mensagem de lista vazia | Milestone: Aula 04 | Assignee: (Talasca e Weslei)