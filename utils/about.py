import streamlit as st

# App Developer:     Enzo Schitini -- Data Science
# Date:              2 Outubro 2024 -- 22 Outubro 2024

schema = 'https://raw.githubusercontent.com/enzoschitini/Data-Science-Portfolio/refs/heads/main/01%20An%C3%A1lise%20explorat%C3%B3ria%20e%20limpeza%20de%20dados/E-commerce%20Customer%20Data%20For%20Behavior%20Analysis/Image/Schema.png'
copertina = 'img/cover.png'

@st.cache_data
def about(olist):

    st.write("""

# **Olist Insights** • Análise de Dados do E-commerce
---
## **Identificando Oportunidades de Crescimento e Melhoria Através da Exploração de Dados de Vendas**
Este dashboard interativo apresenta uma análise interativa baseada nos dados do Olist, oferecendo insights sobre vendas, logística e comportamento do cliente. Por meio de visualizações claras, você poderá explorar tendências e identificar oportunidades para otimizar processos e alavancar resultados no e-commerce.             

**Data Science** Portfólio | *01 Outubro 2024* - *21 Novembro 2024*

---

![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/cover.png)

#####

### O que você vai encontrar nesta análise? 👋

O projeto Olist Insights foi desenvolvido para explorar de forma abrangente os dados disponibilizados pelo Olist, utilizando técnicas de análise e visualização de dados para transformar informações brutas em insights estratégicos. O dashboard é estruturado para responder perguntas-chave sobre vendas, logística, produtos, comportamento do cliente e avaliações, permitindo uma compreensão detalhada do funcionamento de uma operação de e-commerce.

Com base em colunas que abrangem desde características de pedidos até dados geográficos e de avaliação, o objetivo é fornecer ferramentas que auxiliem na tomada de decisões mais assertivas. A análise permite identificar gargalos logísticos, avaliar a experiência do cliente com base em comentários e notas, entender o impacto de categorias de produtos e descobrir tendências regionais que podem direcionar estratégias de marketing e logística.

Além disso, este projeto é uma oportunidade prática de aplicar conceitos de ciência de dados ao mundo real, com foco no entendimento de como cada aspecto do e-commerce contribui para o sucesso da operação como um todo. Seja para otimizar o tempo de entrega, priorizar categorias mais lucrativas ou expandir para regiões específicas, o Olist Insights se apresenta como uma ferramenta valiosa para quem deseja alavancar resultados no comércio eletrônico.

### Os pilares da análise:

- **Visão Geral** Uma introdução ao comportamento geral das vendas, com métricas como receita total, número de pedidos e avaliações médias.
- **Pedidos e Encomendas** Insights sobre o comportamento dos clientes, prazos de entrega, e padrões de compra ao longo do tempo.
- **Produtos e Categorias** Análise detalhada sobre os produtos mais vendidos, categorias populares e desempenho por segmento.
- **Análise Geográfica** Exploração de dados regionais para identificar os estados e cidades com maior potencial de crescimento no e-commerce.

> Além disso, exploraremos o impacto das variáveis sociorraciais nas condições de nascimento e nos indivíduos
> 

######
  
    """)

    st.video('video/Olist Video.mp4')

    st.write("""
        ### Importância do Projeto

        Este projeto destaca a relevância da análise de dados como uma ferramenta essencial para o crescimento de negócios digitais. Ao transformar dados brutos em insights acionáveis, empresas podem tomar decisões mais informadas, otimizando seus processos e aumentando sua competitividade no mercado. No contexto do e-commerce, a análise permite identificar gargalos na logística, entender melhor o comportamento dos clientes e alinhar os esforços de marketing com as preferências regionais. Além disso, ao explorar os dados do Olist, este dashboard exemplifica como a inteligência de mercado pode ser usada para melhorar a experiência do cliente, prever demandas futuras e aproveitar oportunidades de expansão em áreas geográficas estratégicas. Este é um exemplo prático do impacto da ciência de dados no ambiente corporativo.
             
        ######

        ### Contexto e Origem dos Dados do Olist

        Os dados utilizados foram disponibilizados pelo Olist no Kaggle, contendo informações reais sobre vendas, avaliações de clientes, prazos de entrega e localização. Esta base de dados é amplamente reconhecida por sua riqueza de informações e potencial para estudos na área de ciência de dados e análise de negócios.

                    
        ######  
             """)

    st.write('### Desenvolvedor:')

    col1, col2 = st.columns([3, 2])

    with col1:
        st.write('![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/Enzo%20Schitini.png)')
    with col2:
        st.write("""
        ##### [Enzo Schitini - Linkedin](https://www.linkedin.com/in/enzoschitini/)
        Minha conexão com os dados do Olist começou há algum tempo, quando realizei uma análise mais simples focada em EDA e tratamento de dados. Naquele momento, minha intenção era explorar a estrutura da base e praticar abordagens iniciais para entender melhor como o e-commerce funciona. Foi uma experiência enriquecedora, mas ficou claro que o potencial daquela base ia muito além de uma análise exploratória básica.
    
        Sempre admirei a proposta da Olist de conectar pequenos e médios vendedores ao universo digital. Essa visão de democratizar o acesso ao e-commerce me inspirou a revisitar o projeto com um objetivo maior: criar algo que unisse profundidade analítica e um formato mais acessível, como um dashboard interativo. A ideia foi transformar os dados em algo realmente funcional, que ajudasse a revelar oportunidades, destacar desafios e, ao mesmo tempo, celebrar a riqueza que esses dados oferecem.
        
        Este projeto é mais do que um exercício técnico. É uma forma de aprofundar minha compreensão sobre o mercado e reforçar minha conexão com uma marca que admiro. Trabalhar nesse dashboard tem sido desafiador e inspirador, e espero que ele não só entregue valor analítico, mas também represente o cuidado e o respeito que tenho pelos dados e pela proposta da Olist.

        """)
    
    









    st.write("""

---
      
## Preparação dos dados e análise exploratória

Como estes dados são fornecidos por uma loja online, ou seja, uma plataforma, significa que teremos algumas tabelas interligadas através de um ID. Então, para analisar esses dados temos que mesclar todas essas tabelas em uma só, levando em consideração que primeiro elas devem ser analisadas sozinhas, para que os erros sejam tratados.

Um **banco de dados relacional (BDR)**   é um modelo de organização de dados que utiliza tabelas para representar informações e suas relações. É amplamente usado em sistemas corporativos e aplicações devido à sua flexibilidade, eficiência e integridade.
             
A imagem abaixo é um diagrama e nos ajuda a entender melhor como funciona a conexão entre as tabelas dos dados brancos do site.

![](https://raw.githubusercontent.com/enzoschitini/Data-Science-Portfolio/refs/heads/main/01%20An%C3%A1lise%20explorat%C3%B3ria%20e%20limpeza%20de%20dados/E-commerce%20Customer%20Data%20For%20Behavior%20Analysis/Image/Schema.png)

                  
             """)
    
    st.write('### Veja mais ↓')
    with st.expander('Preparação dos dados e análise exploratória'):
        st.write("""

    ### Preparação dos dados
        
    > ##### Neste projeto temos 9 conjuntos de dados vinculados por ID. Por uma questão de organização, vamos colocá-los em uma lista, também para facilitar o acesso a esses dados em branco.

    #### Conjunto de dados dos clientes (olist_customers_dataset)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/conjunto%20de%20dados%20dos%20clientes.png)

    #### Conjunto de dados de geolocalização (olist_geolocation_dataset)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/conjunto%20de%20dados%20de%20geolocaliza%C3%A7%C3%A3o.png)

    #### Conjunto de dados de itens de pedido (olist_order_items_dataset)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/conjunto%20de%20dados%20de%20itens%20de%20pedido.png)

    #### Conjunto de dados de pagamentos de pedidos (olist_order_payments_dataset)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/conjunto%20de%20dados%20de%20pagamentos%20de%20pedidos.png)

    #### Conjunto de análises de pedidos (olist_order_reviews_dataset)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/conjunto%20de%20dados%20de%20an%C3%A1lises%20de%20pedidos.png)

    #### Conjunto de dados de pedidos (olist_orders_dataset)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/conjunto%20de%20dados%20de%20pedidos.png)

    #### Conjunto de dados de produtos (olist_products_dataset)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/conjunto%20de%20dados%20de%20produtos.png)

    #### Conjunto de dados de vendedores (olist_sellers_dataset)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/conjunto%20de%20dados%20de%20vendedores.png)

    #### Conjunto de dados da tradução do nome da categoria do produto (product_category_name_translation)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/tradu%C3%A7%C3%A3o%20do%20nome%20da%20categoria%20do%20produto.png)

    ---

    ### Entendendo a estruturas de dados e colunas:

    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/info.png)
    
    #####
                 
    ## Dados faltantes:
    
    Entre os conjuntos de dados que possuem dados nulos estão: olist_order_reviews_dataset.csv -> (dfs[4]); olist_orders_dataset.csv -> (dfs[5]); olist_products_dataset.csv -> (dfs[6]). Agora vamos analisá-los para entender melhor como são e pensar em como removê-los.

    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/dados%20nulos%20tabela.png)
    
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/dados%20faltantes%20grafico.png)
    
    #### Agora vamos analisar os dados nulos de cada Data Frame da lista
    
    - **olist_order_reviews_dataset.csv** -> (dfs[4]) -> existem duas colunas que possuem muitos dados nulos. Portanto não é mais possível reparar essas colunas, basta removê-las.
    - **olist_orders_dataset.csv** -> (dfs[5]) & olist_products_dataset.csv -> (dfs[6]) -> Essas colunas, no entanto, não possuem tantos dados nulos e eles estão espalhadas entre os outros registros. Portanto pode ser uma perda de tempo recuperar esses dados nulos, até porque são poucos. Portanto, não precisamos deletar a coluna inteira, apenas as nulas são suficientes.

    #####
    
    ### Engenharia de atributos:
    
    | **Nova coluna**                          | **Criação**                                                                                     |
    |-------------------------------------|---------------------------------------------------------------------------------------------------|
    | **Duração da aprovação do pagamento** | df['purchase_approval_time'] = df['order_approved_at'] - df['order_purchase_timestamp']|
    | **Diferença entre a data de chegada e a data prevista** | df['difference_sought_and_expected'] = df['order_purchase_timestamp'] - df['order_delivered_customer_date']|
    | **Peso do produto (Kg)** | df['Kg'] = df['product_weight_g'] / 1000 |
    | **order_purchase_timestamp** | df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'].astype(str), format='%Y-%m-%d %H:%M:%S')|
    | **day_of_purchase** | df['day_of_purchase'] = df['order_purchase_timestamp'].dt.day_name() |
    | **month_of_purchase** | df['month_of_purchase'] = df['order_purchase_timestamp'].dt.month_name() |
    | **year_of_purchase** | df['year_of_purchase'] = df['order_purchase_timestamp'].dt.year |
    | **month/year_of_purchase** | df['month/year_of_purchase'] = df['month_of_purchase'].astype(str) + '-' + df['year_of_purchase'].astype(str) |
    | **shipping_duration** | df['shipping_duration'] = df['order_delivered_customer_date'] - df['order_purchase_timestamp'] |
    | **Id único para cada pedido** | df['order_unique_id'] = df['order_id'].astype(str) + '-' + df['order_item_id'].astype(str) df['order_unique_id'] = df['order_unique_id'].astype('category') |
    | **Preço das parcelas** | df['installments_price'] = df['payment_value'].round() / df['payment_installments'].round() |
  
    ## Organizando final as colunas:

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
    
    #####
    
    ### Visualização:  
    
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/cat1.png)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/cat2.png)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/cat3.png)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/cat4.png)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/cat5.png)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/cat6.png)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/cat7.png)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/cat8.png)
    ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/EDA/cat9.png)

        """)






























    st.write("""
#####

## Avaliação das categorias com uma fórmula

Para criar uma fórmula que gere uma pontuação para avaliar se uma categoria de produto é boa ou não, podemos considerar as principais métricas fornecidas na imagem:
             
- **Vendas totais (1.7 milhões)** 
- **Número de vendas (11684)**      
- **Taxa de frete (19.86%)**
- **Score médio (3.92)**
- **Valor (146.09)**
- **Preço (92.6)**
- **Frete médio (18.39)**

Uma abordagem poderia ser criar uma fórmula que leve em conta esses fatores, ponderando-os conforme sua importância no sucesso de uma categoria de produtos.
                  
             """)
    
    st.write('### Veja mais ↓')
    with st.expander('Fórmula Proposta:'):
        st.write("""
        ### Fórmula Proposta:
        Vamos supor que uma pontuação mais alta é considerada melhor, e que os fatores que mais influenciam essa pontuação são:
        
        - **Número de vendas** (quanto mais, melhor).
        - **Taxa de frete** (quanto menor, melhor).
        - **Score médio** (quanto mais alto, melhor).
        - **Preço** (um preço competitivo pode ser atrativo).
        - **Frete médio** (quanto mais baixo, melhor).

        ### Pontuação (P):
        ######
        ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/f1.png)
        
        ######
        #### Explicação dos componentes:

        - **Vendas Totais / Número de Vendas**: A relação entre vendas totais e o número de vendas dá uma ideia do volume médio de receita por venda.
        - **Score**: Pontuação dada pelos consumidores.
        - **Taxa de Frete**: Penaliza taxas de frete mais altas.
        - **Frete Médio**: Penaliza o frete alto, já que fretes menores são mais atrativos para os consumidores.
        - **1/Preço**: Incentiva preços mais baixos.

        ### Aplicando os valores da imagem:

        ![image.png](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/f1.png)

        Isso resultará em uma pontuação numérica que pode ser comparada com outras categorias para determinar se a categoria "Cama mesa banho" é boa em relação às métricas fornecidas.

        ### Fórmula de normalização:

        Para tornar a pontuação mais compreensível e numa escala de 0 a 100, podemos aplicar uma normalização ou escalonamento dos valores. Uma abordagem simples seria:

        1. **Definir limites mínimos e máximos**: A pontuação mínima e máxima observada entre várias categorias de produtos (você pode ajustar esses limites com base nos dados reais).
        2. **Normalizar**: Escalar a pontuação para a faixa de 0 a 100.

        A fórmula de normalização para transformar um valor \(P\) em uma escala de 0 a 100 seria:
        
        ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/f3.png)

        Como não temos outras categorias para definir \(P_{min}\) e \(P_{max}\), vou sugerir que assumamos valores razoáveis com base na distribuição dos dados:

        - \(P_{min} = 0\) (pontuação mais baixa possível)
        - \(P_{max} = 1000\) (um limite superior hipotético)

        Vamos calcular a pontuação normalizada usando esses valores.

        A pontuação normalizada para a categoria "Cama mesa banho" seria **53.21** em uma escala de 0 a 100. Isso torna o valor mais palpável e fácil de comparar com outras categorias.
        """)






    st.write("""
#####
             
## Uploads - Atualizações

Desde que terminei de desenvolver este Dashboard com dados Olist, tive ideias para melhorá-lo, aqui estão algumas que talvez você verá nas próximas versões:
             
- **Marketing Funnel by Olist:** Analisar os dados do funil de vendas do Olist.
- **Análise geográfica com mapas:** Usar o Folium para gerar mapas.
                  
             """)





    st.write("""
#####
             
## Execute no seu computador

Este aplicativo foi criado usando Streamlit e os códigos estão localizados em um repositório GitHub não no branch principal, mas sim no branch streamlit. Aqui tudo o que você fará é baixar uma cópia para o seu computador e executar no VScode. Os arquivos são:
             
- **olist.py** O arquivo inicial é o que precisamos para iniciar o aplicativo

Depois temos uma coleção chamada 'utils' na qual existem códigos python para fazer certas páginas funcionarem:
             
- **general.py** Para a página inicial
- **pedidos.py** Onde estão todas as funções e cálculos da página de pedidos
- **produtos.py** Onde estão todas as funções e cálculos da página com os produtos
- **geodata** Em que são retirados dados geográficos para análise de cidades, regiões e áreas
- **metrics.py** Todos os outros códigos compartilham certas funções de cálculos, formatação e etc. encontradas em métricas.py
                  
             """)
    
    st.write('### Veja mais ↓')
    with st.expander('Como executá-lo do seu pc'):
        st.write("""
        #### Link para acessar a Branch Streamlit:
        [Link da branch](https://github.com/enzoschitini/Olist/tree/streamlit)

        
        ![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/git.png)
        #####
        """)

        st.write('### Clonar o repositório:')
        st.code("git clone https://github.com/enzoschitini/Olist.git")

        st.write('### requirements.txt')
        st.code("""
                streamlit-option-menu
                pandas
                plotly
                matplotlib
                seaborn
                numpy
                xlsxwriter
                """)

















    st.write('####')
    st.write('### Mais Informações:')

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
            <style>
            .custom-box {{
                border: 5px solid #F8F8FF;
                padding: 20px;
                border-radius: 5px;
                margin-bottom: 20px;
            }}
            .blue-bold {{
                color: blue;
                font-weight: bold;
            }}
            </style>
            <div class="custom-box">
                <h3><span class="blue-bold">GitHub</span> Repositório</h3>
                <h5><a href="https://github.com/enzoschitini/Olist/tree/main" target="_blank" style="text-decoration: none; color: inherit;">clique aqui</a></h5>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <style>
            .custom-box {{
                border: 5px solid #F8F8FF;
                padding: 20px;
                border-radius: 5px;
                margin-bottom: 20px;
            }}
            .blue-bold {{
                color: blue;
                font-weight: bold;
            }}
            </style>
            <div class="custom-box">
                <h3><span class="blue-bold">Kaggle</span> Notebook</h3>
                <h5><a href="https://www.kaggle.com/code/enzoschitini/brazilian-e-commerce-analysis-olist" target="_blank" style="text-decoration: none; color: inherit;">clique aqui</a></h5>
            </div>
            """, unsafe_allow_html=True)

    
    st.write("""
            
            ######
                        
            ### Algoritmo & Metodologia: Informações sobre o sistema
             
            A análise foi conduzida utilizando técnicas estatísticas avançadas e métodos de visualização de dados para identificar padrões, tendências e possíveis anomalias no conjunto de dados. O Python foi empregado como a principal ferramenta para manipulação, análise e visualização, oferecendo uma ampla gama de bibliotecas como Pandas, NumPy, Matplotlib, Seaborn e Plotly. Durante o processo, foi realizada a limpeza e a preparação dos dados para garantir que as informações estivessem consistentes, completas e confiáveis, assegurando a qualidade necessária para uma análise robusta.
            
            - [Licença de uso: O algoritmo é de livre acesso a qualquer pessoa que queira estudar ou ler os resultados da análise](https://github.com/enzoschitini/Olist/blob/streamlit/LICENCE)
            - [Aplicação Streamlit](https://github.com/enzoschitini/Olist/tree/streamlit)
            - [Acesse aqui aos dados ainda não tratados do Olist](https://github.com/enzoschitini/Olist/tree/main/Exploratory%20Data%20Analysis%20(EDA)/Data)
""")