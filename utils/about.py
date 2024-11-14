import streamlit as st

# App Developer:     Enzo Schitini -- Data Science
# Date:              2 Outubro 2024 -- 22 Outubro 2024

schema = 'https://raw.githubusercontent.com/enzoschitini/Data-Science-Portfolio/refs/heads/main/01%20An%C3%A1lise%20explorat%C3%B3ria%20e%20limpeza%20de%20dados/E-commerce%20Customer%20Data%20For%20Behavior%20Analysis/Image/Schema.png'

@st.cache_data
def about(olist):
    st.title("Olist - Análise de Dados do E-commerce")
    st.write("### Identificando Oportunidades de Crescimento e Melhoria Através da Exploração de Dados de Vendas")

    st.image('img/Enzo Schitini.png', width=800)

    st.write("""

    Este projeto visa analisar dados de um e-commerce, com o objetivo de identificar padrões de comportamento do cliente, tendências de mercado e oportunidades de otimização. Através da exploração de dados, pretende-se obter insights valiosos sobre a performance da plataforma, a satisfação do cliente e os fatores que influenciam o sucesso das vendas. A análise abrangerá diversos aspectos, desde a análise de produtos mais vendidos até a identificação de gargalos no processo de entrega, passando pela análise de comportamento do cliente e a segmentação de público. 
    https://github.com/enzoschitini/Data-Science-Portfolio

    A análise exploratória dos dados será realizada utilizando técnicas estatísticas e ferramentas de visualização de dados, permitindo a construção de dashboards e relatórios que possibilitem uma compreensão aprofundada do negócio. A partir da identificação de padrões e tendências, o projeto visa gerar recomendações estratégicas para a tomada de decisão em áreas como:

    ### 1. Marketing e Vendas:  Identificar produtos e categorias com maior potencial de venda, segmentar campanhas de marketing e personalizar ofertas para o cliente.
    
    ## Importância:
    A análise de dados de e-commerce é crucial para o sucesso do negócio em um mercado cada vez mais competitivo. Através da análise, as empresas podem:

    - ###  1. **Tomar decisões estratégicas baseadas em dados:** Em vez de depender de intuições, as empresas podem basear suas decisões em evidências concretas, aumentando a probabilidade de sucesso.

    - ###  2. **Melhorar a experiência do cliente:** Identificar e solucionar problemas que prejudicam a experiência do cliente, aumentando a fidelidade e a receita.

    - ### 3. **Aumentar a lucratividade:** Otimizar processos, reduzir custos e aumentar as vendas através de decisões baseadas em dados.

    - ### 4. **Concorrer em um mercado competitivo:**  A análise de dados permite que as empresas se diferenciem da concorrência e se adaptem às mudanças do mercado.

    - ### 5. **Entender o comportamento do consumidor:** Através da análise dos dados de compras, a empresa pode identificar os hábitos e preferências do cliente, personalizando a experiência e aumentando a satisfação.
    
     """)
    
    st.write("""
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
    | `orderstreamlit_applicationrovedat`                 | Data e hora da aprovação do pedido.                                           |
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
             
             """)
    

    #st.image('https://avatars.githubusercontent.com/u/70824630?s=400&u=5da7469a6e31d8823f89933b83c2450af0817589&v=4', width=100)
    st.image(schema)