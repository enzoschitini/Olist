# Olist: - E-Commerce Customer Data - Manual de análise

![x](https://img.notionusercontent.com/s3/prod-files-secure%2F591dff13-5117-425d-a983-ca995144a283%2Fa3119321-46eb-47aa-9e5d-648920e181b6%2FFrame_2.png/size/w=2000?exp=1727884335&sig=SAmwn0L1lk8QH_MnrV-3FqoP62FeMol-PUJtnl69ZSI)


# Análise de Dados de um E-commerce: Desvendando Padrões e Otimizando a Experiência do Cliente
### Identificando Oportunidades de Crescimento e Melhoria Através da Exploração de Dados de Vendas

Este projeto visa analisar dados de um e-commerce, com o objetivo de identificar padrões de comportamento do cliente, tendências de mercado e oportunidades de otimização. Através da exploração de dados, pretende-se obter insights valiosos sobre a performance da plataforma, a satisfação do cliente e os fatores que influenciam o sucesso das vendas. A análise abrangerá diversos aspectos, desde a análise de produtos mais vendidos até a identificação de gargalos no processo de entrega, passando pela análise de comportamento do cliente e a segmentação de público. 

A análise exploratória dos dados será realizada utilizando técnicas estatísticas e ferramentas de visualização de dados, permitindo a construção de dashboards e relatórios que possibilitem uma compreensão aprofundada do negócio. A partir da identificação de padrões e tendências, o projeto visa gerar recomendações estratégicas para a tomada de decisão em áreas como:

### 1. Marketing e Vendas:  Identificar produtos e categorias com maior potencial de venda, segmentar campanhas de marketing e personalizar ofertas para o cliente.

## Importância:
A análise de dados de e-commerce é crucial para o sucesso do negócio em um mercado cada vez mais competitivo. Através da análise, as empresas podem:

- ###  1. **Tomar decisões estratégicas baseadas em dados:** Em vez de depender de intuições, as empresas podem basear suas decisões em evidências concretas, aumentando a probabilidade de sucesso.

- ###  2. **Melhorar a experiência do cliente:** Identificar e solucionar problemas que prejudicam a experiência do cliente, aumentando a fidelidade e a receita.

- ### 3. **Aumentar a lucratividade:** Otimizar processos, reduzir custos e aumentar as vendas através de decisões baseadas em dados.

- ### 4. **Concorrer em um mercado competitivo:**  A análise de dados permite que as empresas se diferenciem da concorrência e se adaptem às mudanças do mercado.

- ### 5. **Entender o comportamento do consumidor:** Através da análise dos dados de compras, a empresa pode identificar os hábitos e preferências do cliente, personalizando a experiência e aumentando a satisfação.








---


### Amostra dos dados
| order_id                          | order_item_id | customer_id                        | customer_unique_id                  | customer_zip_code_prefix | customer_city         | customer_state | product_id                        | product_category_name | product_name_lenght | product_description_lenght | product_photos_qty | product_weight_g | product_length_cm | product_height_cm | product_width_cm | seller_id                         | seller_city      | seller_state | seller_zip_code_prefix | payment_type | payment_sequential | payment_installments | installments_price | price | freight_value | payment_value | shipping_limit_date  | order_purchase_timestamp | order_approved_at     | order_delivered_carrier_date | order_delivered_customer_date | order_estimated_delivery_date | shipping_duration   | day_of_purchase | month_of_purchase | year_of_purchase | month/year_of_purchase | order_status | order_unique_id                    |
|------------------------------------|---------------|------------------------------------|------------------------------------|-------------------------|-----------------------|----------------|------------------------------------|-----------------------|--------------------|--------------------------|-------------------|-----------------|------------------|------------------|-----------------|------------------------------------|-----------------|--------------|-----------------------|--------------|-------------------|----------------------|--------------------|-------|---------------|---------------|----------------------|--------------------------|----------------------|-----------------------------|-----------------------------|----------------------------|---------------------|-----------------|-------------------|-----------------|-----------------------|--------------|------------------------------------|
| 00010242fe8c5a6d1ba2dd792cb16214   | 1             | 3ce436f183e68e07877b285a838db11a   | 871766c5855e863f6eccc05f988b23cb   | 28013                   | campos dos goytacazes | RJ             | 4244733e06e7ecb4970a6e2683c13e61   | cool_stuff            | 58.0               | 598.0                    | 4.0               | 650.0           | 28.0             | 9.0              | 14.0            | 48436dade18ac8b2bce089ec2a041202   | volta redonda    | SP           | 27277                 | credit_card  | 1                 | 2                    | 36.0               | 58.9  | 13.29         | 72.19         | 2017-09-19 09:45:35   | 2017-09-13 08:59:02       | 2017-09-13 09:45:35   | 2017-09-19 18:34:16          | 2017-09-20 23:43:48          | 2017-09-29 00:00:00         | 7 days 14:44:46      | Wednesday       | September         | 2017            | September-2017            | delivered    | 00010242fe8c5a6d1ba2dd792cb16214-1 |
| 130898c0987d1801452a8ed92a670612   | 1             | e6eecc5a77de221464d1c4eaff0a9b64   | 0fb8e3eab2d3e79d92bb3fffbb97f188   | 75800                   | jatai                | GO             | 4244733e06e7ecb4970a6e2683c13e61   | cool_stuff            | 58.0               | 598.0                    | 4.0               | 650.0           | 28.0             | 9.0              | 14.0            | 48436dade18ac8b2bce089ec2a041202   | volta redonda    | SP           | 27277                 | boleto       | 1                 | 1                    | 74.0               | 55.9  | 17.96         | 73.86         | 2017-07-05 02:44:11   | 2017-06-28 11:52:20       | 2017-06-29 02:44:11   | 2017-07-05 12:00:33          | 2017-07-13 20:39:29          | 2017-07-26 00:00:00         | 15 days 08:47:09     | Wednesday       | June              | 2017            | June-2017                | delivered    | 130898c0987d1801452a8ed92a670612-1 |
| 532ed5e14e24ae1f0d735b91524b98b9   | 1             | 4ef55bf80f711b372afebcb7c715344a   | 3419052c8c6b45daf79c1e426f9e9bcb   | 30720                   | belo horizonte        | MG             | 4244733e06e7ecb4970a6e2683c13e61   | cool_stuff            | 58.0               | 598.0                    | 4.0               | 650.0           | 28.0             | 9.0              | 14.0            | 48436dade18ac8b2bce089ec2a041202   | volta redonda    | SP           | 27277                 | credit_card  | 1                 | 2                    | 41.5               | 64.9  | 18.33         | 83.23         | 2018-05-23 10:56:25   | 2018-05-18 10:25:53       | 2018-05-18 12:31:43   | 2018-05-23 14:05:00          | 2018-06-04 18:34:26          | 2018-06-07 00:00:00         | 17 days 08:08:33     | Friday          | May               | 2018            | May-2018                 | delivered    | 532ed5e14e24ae1f0d735b91524b98b9-1 |
| 6f8c31653edb8c83e1a739408b5ff750   | 1             | 30407a72ad8b3f4df4d15369126b20c9   | e7c828d22c0682c1565252deefbe334d   | 83070                   | sao jose dos pinhais  | PR             | 4244733e06e7ecb4970a6e2683c13e61   | cool_stuff            | 58.0               | 598.0                    | 4.0               | 650.0           | 28.0             | 9.0              | 14.0            | 48436dade18ac8b2bce089ec2a041202   | volta redonda    | SP           | 27277                 | credit_card  | 1                 | 3                    | 25.0               | 58.9  | 16.17         | 75.07         | 2017-08-07 18:55:08   | 2017-08-01 18:38:42       | 2017-08-01 18:55:08   | 2017-08-02 19:07:36          | 2017-08-09 21:26:33          | 2017-08-25 00:00:00         | 8 days 02:47:51      | Tuesday         | August            | 2017            | August-2017              | delivered    | 6f8c31653edb8c83e1a739408b5ff750-1 |
| 7d19f4ef4d04461989632411b7e588b9   | 1             | 91a792fef70ecd8cc69d3c7feb3d12da   | 0bb98ba72dcc08e95f9d8cc434e9a2cc   | 36400                   | conselheiro lafaiete  | MG             | 4244733e06e7ecb4970a6e2683c13e61   | cool_stuff            | 58.0               | 598.0                    | 4.0               | 650.0           | 28.0             | 9.0              | 14.0            | 48436dade18ac8b2bce089ec2a041202   | volta redonda    | SP           | 27277                 | credit_card  | 1                 | 4                    | 18.0               | 58.9  | 13.29         | 72.19         | 2017-08-16 22:05:11   | 2017-08-10 21:48:40       | 2017-08-10 22:05:11   | 2017-08-11 19:43:07          | 2017-08-24 20:04:21








Aqui está a tabela com as informações fornecidas:

| **Coluna**                        | **Descrição**                                                                 |
|------------------------------------|-------------------------------------------------------------------------------|
| `order_id`                        | Identificador único do pedido.                                                |
| `orderitemid`                     | Identificador único do item dentro do pedido.                                 |
| `customer_id`                     | Identificador único do cliente.                                               |
| `customeruniqueid`                | Identificador único do cliente (não necessariamente o mesmo que `customer_id`).|
| `customerzipcode_prefix`          | Prefixo do CEP do cliente.                                                    |
| `customer_city`                   | Cidade do cliente.                                                           |
| `customer_state`                  | Estado do cliente.                                                           |
| `product_id`                      | Identificador único do produto.                                               |
| `productcategoryname`             | Nome da categoria do produto.                                                 |
| `productnamelenght`               | Comprimento do nome do produto (em caracteres).                               |
| `productdescriptionlenght`        | Comprimento da descrição do produto (em caracteres).                          |
| `productphotosqty`                | Quantidade de fotos do produto.                                               |
| `productweightg`                  | Peso do produto (em gramas).                                                  |
| `productlengthcm`                 | Comprimento do produto (em centímetros).                                      |
| `productheightcm`                 | Altura do produto (em centímetros).                                           |
| `productwidthcm`                  | Largura do produto (em centímetros).                                          |
| `seller_id`                       | Identificador único do vendedor.                                              |
| `seller_city`                     | Cidade do vendedor.                                                          |
| `seller_state`                    | Estado do vendedor.                                                          |
| `sellerzipcode_prefix`            | Prefixo do CEP do vendedor.                                                   |
| `payment_type`                    | Tipo de pagamento utilizado (e.g., cartão de crédito, boleto).                |
| `payment_sequential`              | Sequência do pagamento (e.g., 1 para o primeiro pagamento).                   |
| `payment_installments`            | Número de parcelas do pagamento.                                              |
| `price`                           | Preço do produto.                                                            |
| `freight_value`                   | Valor do frete.                                                              |
| `payment_value`                   | Valor total do pagamento.                                                     |
| `shippinglimitdate`               | Data limite para o envio do pedido.                                           |
| `orderpurchasetimestamp`          | Data e hora do pedido.                                                        |
| `orderapprovedat`                 | Data e hora da aprovação do pedido.                                           |
| `orderdeliveredcarrier_date`      | Data e hora em que o pedido foi entregue ao transportador.                    |
| `orderdeliveredcustomer_date`     | Data e hora em que o pedido foi entregue ao cliente.                          |
| `orderestimateddelivery_date`     | Data estimada de entrega do pedido.                                           |
| `dayofpurchase`                   | Dia da semana da compra.                                                      |
| `monthofpurchase`                 | Mês da compra.                                                               |
| `yearofpurchase`                  | Ano da compra.                                                               |
| `month/yearofpurchase`            | Mês e ano da compra.                                                         |
| `order_status`                    | Status do pedido.                                                            |
| `orderuniqueid`                   | Identificador único do pedido (não necessariamente o mesmo que `order_id`).   |

Essa tabela organiza e descreve as colunas de um dataset de pedidos de forma clara e padronizada.