import streamlit as st

# App Developer:     Enzo Schitini -- Data Science
# Date:              2 Outubro 2024 -- 22 Outubro 2024

schema = 'https://raw.githubusercontent.com/enzoschitini/Data-Science-Portfolio/refs/heads/main/01%20An%C3%A1lise%20explorat%C3%B3ria%20e%20limpeza%20de%20dados/E-commerce%20Customer%20Data%20For%20Behavior%20Analysis/Image/Schema.png'
copertina = 'img/cover.png'

@st.cache_data
def about(olist):
    col1, col2 = st.columns(2)
    
    with col1:
        st.title("Olist - Análise de Dados do E-commerce")
        st.write("### Identificando Oportunidades de Crescimento e Melhoria Através da Exploração de Dados de Vendas")

        st.write("""

        Este projeto visa analisar dados de um e-commerce, com o objetivo de identificar padrões de comportamento do cliente, tendências de mercado e oportunidades de otimização. Através da exploração de dados, pretende-se obter insights valiosos sobre a performance da plataforma, a satisfação do cliente e os fatores que influenciam o sucesso das vendas. A análise abrangerá diversos aspectos, desde a análise de produtos mais vendidos até a identificação de gargalos no processo de entrega, passando pela análise de comportamento do cliente e a segmentação de público. 
        https://github.com/enzoschitini/Data-Science-Portfolio

        
        """)

    with col2:
        st.image(copertina) # 'img/Enzo Schitini.png' width=800

    
    st.write("""
    Aqui está a tabela com as informações fornecidas:

    | **Coluna**                          | **Descrição**                                                                                     |
    |-------------------------------------|---------------------------------------------------------------------------------------------------|
    | **order_id**                        | Identificador único do pedido.                                                                    |
    | **order_item_id**                   | ID do item dentro de um pedido específico (indica qual item é dentro do pedido).                  |
    | **order_unique_id**                 | Um identificador único combinado para identificar cada pedido e item.                             |
    | **order_status**                    | Status do pedido (ex.: "delivered" indica que foi entregue).                                      |
    | **order_purchase_timestamp**        | Data e hora de compra do pedido.                                                                  |
    | **order_approved_at**               | Data e hora em que o pagamento foi aprovado.                                                      |
    | **order_delivered_carrier_date**    | Data em que o pedido foi entregue ao transportador.                                               |
    | **order_delivered_customer_date**   | Data em que o pedido foi entregue ao cliente.                                                     |
    | **order_estimated_delivery_date**   | Data estimada para a entrega do pedido.                                                           |
    | **shipping_limit_date**             | Data limite para envio do pedido.                                                                 |
    | **shipping_duration**               | Tempo total de envio do pedido, incluindo os dias e horas.                                        |
    | **customer_id**                     | Identificador do cliente.                                                                         |
    | **customer_unique_id**              | ID único que representa um cliente.                                                               |
    | **customer_zip_code_prefix**        | Prefixo do código postal do cliente.                                                              |
    | **customer_city**                   | Cidade do cliente.                                                                                |
    | **customer_state**                  | Estado do cliente.                                                                                |
    | **customer_zone**                   | Região geográfica do cliente (ex.: Sudeste, Sul, etc.).                                           |
    | **product_id**                      | Identificador único do produto.                                                                   |
    | **product_category_name**           | Categoria do produto.                                                                             |
    | **product_name_lenght**             | Comprimento do nome do produto (quantidade de caracteres).                                        |
    | **product_description_lenght**      | Comprimento da descrição do produto (quantidade de caracteres).                                   |
    | **product_photos_qty**              | Quantidade de fotos do produto.                                                                   |
    | **product_weight_g**                | Peso do produto em gramas.                                                                        |
    | **product_length_cm**               | Comprimento do produto em centímetros.                                                            |
    | **product_height_cm**               | Altura do produto em centímetros.                                                                 |
    | **product_width_cm**                | Largura do produto em centímetros.                                                                |
    | **Kg**                              | Peso do produto em quilogramas.                                                                   |
    | **seller_id**                       | Identificador do vendedor.                                                                        |
    | **seller_zip_code_prefix**          | Prefixo do código postal do vendedor.                                                             |
    | **seller_city**                     | Cidade do vendedor.                                                                               |
    | **seller_state**                    | Estado do vendedor.                                                                               |
    | **seller_zone**                     | Região geográfica do vendedor.                                                                    |
    | **payment_sequential**              | Sequência dos pagamentos relacionados ao pedido.                                                  |
    | **payment_type**                    | Tipo de pagamento utilizado (ex.: cartão de crédito).                                             |
    | **payment_installments**            | Quantidade de parcelas para o pagamento.                                                          |
    | **installments_price**              | Valor de cada parcela.                                                                            |
    | **price**                           | Preço do produto.                                                                                 |
    | **freight_value**                   | Valor do frete.                                                                                   |
    | **payment_value**                   | Valor total pago pelo pedido.                                                                     |
    | **review_id**                       | Identificador único para a avaliação.                                                             |
    | **review_score**                    | Nota dada pelo cliente para o pedido (ex.: de 1 a 5).                                             |
    | **review_comment_title**            | Título do comentário do cliente sobre o pedido.                                                   |
    | **review_comment_message**          | Mensagem do comentário do cliente.                                                                |
    | **review_creation_date**            | Data de criação da avaliação.                                                                     |
    | **review_answer_timestamp**         | Data e hora em que a avaliação foi respondida.                                                    |
    | **day_of_purchase**                 | Dia da compra.                                                                                    |
    | **month_of_purchase**               | Mês da compra.                                                                                    |
    | **year_of_purchase**                | Ano da compra.                                                                                    |
    | **month/year_of_purchase**          | Mês e ano da compra combinados.                                                                   |
    | **purchase_approval_time**          | Tempo até a aprovação da compra.                                                                  |
    | **difference_sought_and_expected**  | Diferença entre a entrega estimada e a efetiva.                                                   |
             
             """)
    

    #st.image('https://avatars.githubusercontent.com/u/70824630?s=400&u=5da7469a6e31d8823f89933b83c2450af0817589&v=4', width=100)
    st.image(schema)