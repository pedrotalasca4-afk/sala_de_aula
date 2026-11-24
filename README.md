# Confeitaria

## O Problema
* **Qual é o problema?** O dono não sabe quais tipos de doces são os menos vendidos no mês, o que dificulta ajustar a produção e evitar desperdício de insumos.
* **Quem sofre com ele?** O dono da confeitaria.
* **Como é hoje?** Olhando manualmente os pedidos.
* **Como saber que resolveu?** Quando a tela exibir todos os tipos de doces cadastrados e quantas vezes aparecem nos pedidos do mês (inclusive os com 0 vendas, em ordem crescente), além do aviso quando não houver doces/vendas no mês.

---

### Estórias

#### Estória 1
> **Como** dono, **quero** ver os tipos de doces menos vendidos no mês, **para** ajustar a produção e evitar desperdício de insumos.

**Critérios de Aceitação**
* Tipo de doce que não esteja cadastrado no sistema não aparece na listagem.
* Tipos de doces cadastrados que tiveram 0 pedidos no mês aparecem no topo da listagem com contagem 0, pois são os menos vendidos.
* Tipos de doces com vendas no mês aparecem com a contagem de aparição nos pedidos, ordenados de forma crescente (dos menos vendidos para os mais vendidos).
* Quando não houver doces cadastrados ou nenhuma venda registrada no mês, a tela exibe `"nenhuma venda este mês"` e não fica em branco.

**Tarefas**
* **Issue 1A (`regra`)**: Implementar contagem mensal por tipo de doce (mantendo os de 0 vendas), ordenação crescente para destacar os menos vendidos e retorno de `"nenhuma venda este mês"` quando aplicável | **Milestone:** `Aula 02` | **Assignee:** Talasca
* **Issue 1B (`dados`)**: Criar consulta no banco (`LEFT JOIN`) para obter todos os tipos de doces cadastrados e respectivas ocorrências nos itens de pedido do mês | **Milestone:** `Aula 02` | **Assignee:** Weslei
* **Issue 1C (`interface`)**: Exibir na tela a lista de doces menos vendidos ordenada ou a mensagem `"nenhuma venda este mês"` | **Milestone:** `Aula 03` | **Assignee:** Talasca

---

#### Estória 2
> **Como** atendente, **quero** ver os pedidos ainda não entregues com os respectivos doces e datas, **para** organizar a entrega no balcão sem me perder nas anotações.

**Critérios de Aceitação**
* Pedidos já entregues ou cancelados não aparecem na lista de pendentes.
* Cada pedido pendente exibe cliente, itens/doces e data prevista de entrega.
* Quando não houver nenhum pedido pendente, a tela exibe `"nenhum pedido pendente"` e não fica em branco.

**Tarefas**
* **Issue 2A (`regra`)**: Filtrar apenas pedidos com estado pendente, ordenar por data prevista e devolver `"nenhum pedido pendente"` quando vazio | **Milestone:** `Aula 03` | **Assignee:** Weslei
* **Issue 2B (`dados`)**: Consultar pedidos em aberto juntando dados do cliente e dos itens/doces associados | **Milestone:** `Aula 03` | **Assignee:** Talasca
* **Issue 2C (`interface`)**: Apresentar na tela os pedidos pendentes com cliente, doces e data, ou o aviso de ausência de pendentes | **Milestone:** `Aula 04` | **Assignee:** Weslei

---

#### Estória 3
> **Como** atendente, **quero** consultar rapidamente o preço unitário de cada tipo de doce cadastrado, **para** responder aos clientes no balcão sem procurar em vários lugares.

**Critérios de Aceitação**
* Tipos de doces inativos ou removidos não aparecem na consulta.
* Cada tipo de doce ativo é exibido com o respectivo preço unitário formatado.
* Se não existir nenhum tipo de doce ativo cadastrado, a tela exibe `"nenhum doce cadastrado"` e não fica em branco.

**Tarefas**
* **Issue 3A (`regra`)**: Filtrar tipos de doces ativos, formatar valores unitários e retornar `"nenhum doce cadastrado"` quando a lista estiver vazia | **Milestone:** `Aula 04` | **Assignee:** Talasca
* **Issue 3B (`dados`)**: Consultar na base de dados os tipos de doces ativos e os respectivos preços | **Milestone:** `Aula 04` | **Assignee:** Weslei
* **Issue 3C (`interface`)**: Mostrar na tela a listagem de preços por tipo de doce ou a mensagem de lista vazia | **Milestone:** `Aula 04` | **Assignee:** Talasca