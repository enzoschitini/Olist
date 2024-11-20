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

*Diz algorítimo de Machine Learning • 03 Junho 2024*
Uma pesquisa abrangente sobre tendências demográficas e de saúde em 2019 no estado de Rondônia, no Brasil. Comecemos por analisar os dados do sistema de informação sobre nascidos vivos (SINASC), o objetivo é realizar uma análise aprofundada do tema, este projeto visa encontrar ideias e responder a uma série de questões cruciais.

**Data Science** Portfólio | *27 Abril 2024* - *03 junho 2024*

---

![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/cover.png)

#####

### O que você vai encontrar nesta análise? 👋

Vamos explorar os dados do *Sistema de Informação sobre Nascidos Vivos (SINASC)* relativos aos recém-nascidos nascidos no estado de Rondônia, Brasil, no ano de 2019. Assim que a análise exploratória for concluída, prosseguiremos para identificar insights e avaliar a saúde pública no estado.


Usaremos abordagens estatísticas e analíticas para identificar correlações, padrões e associações entre variáveis, além disso vamos criar um Modelo de Machine Learning para fazer inferências de dados faltantes.

### Os pilares da análise:

- **Visão Geral** Entender melhor as raças e o nível educacional das mães.
- **Pedidos e Encomendas** Entender melhor as raças e o nível educacional das mães.
- **Produtos e Categorias** Analisaremos as menores de idade, meninas que constroem família antes dos 18 anos.
- **Análise Geográfica** O que nos diz a escolha do parto entre cesariana ou parto vaginal?

> Além disso, exploraremos o impacto das variáveis sociorraciais nas condições de nascimento e nos indivíduos
> 

######

### Importância do Projeto

A análise dos dados do SINASC para Rondônia em 2019 é vital para entender melhor as condições de nascimento e saúde materno-infantil no estado. As informações derivadas desse estudo podem auxiliar gestores públicos, pesquisadores e profissionais de saúde na tomada de decisões informadas, visando a melhoria contínua dos serviços de saúde e o bem-estar da população.

Ao fornecer uma visão detalhada sobre os nascimentos, este projeto contribui para um entendimento mais profundo das dinâmicas de saúde e demografia de Rondônia, promovendo ações mais eficazes e direcionadas no campo da saúde pública.

######

### Contexto e origem dos Dados do SINASC em Rondônia - 2019

O Sistema de Informação sobre Nascidos Vivos (SINASC) é uma base de dados administrada pelo Ministério da Saúde do Brasil, que tem como objetivo coletar e disponibilizar informações detalhadas sobre todos os nascimentos ocorridos no país. No âmbito do estado de Rondônia, o SINASC fornece dados abrangentes e específicos sobre os nascimentos ocorridos no ano de 2019, sendo uma fonte crucial para análises de saúde pública, planejamento e avaliação de políticas sociais.

Os dados utilizados neste projeto foram extraídos do portal do governo, mais precisamente do Departamento de Informática do SUS (DATASUS). Essa instituição é responsável pela coleta, armazenamento e divulgação das informações de saúde no Brasil, garantindo a integridade e a precisão dos dados disponibilizados.

O conjunto de dados pode ser encontrado no site do governo brasileiro e segue políticas de privacidade, o que significa que não há nomes de pessoas ou qualquer coisa que nos permita saber quem são os indivíduos.

             
######   
    """)

    st.write('### Desenvolvedor:')

    col1, col2 = st.columns([3, 2])

    with col1:
        st.write('![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/Enzo%20Schitini.png)')
    with col2:
        st.write("""
        ##### [Enzo Schitini](https://www.linkedin.com/in/enzoschitini/) - Data Scientist • Expert Bubble.io • UX & UI @ Nugus creator
        Este projeto visa analisar dados de um e-commerce, com o objetivo de identificar padrões de comportamento do cliente, tendências de mercado e oportunidades de otimização. Através da exploração de dados, pretende-se obter insights valiosos sobre a performance da plataforma, a satisfação do cliente e os fatores que influenciam o sucesso das vendas. A análise abrangerá diversos aspectos, desde a análise de produtos mais vendidos até a identificação de gargalos no processo de entrega, passando pela análise de comportamento do cliente e a segmentação de público. 
        ######
        https://github.com/enzoschitini/Data-Science-Portfolio

        """)
    
    st.video('video/Olist Video.mp4')









    st.write("""
######
---
######
      
## Preparação dos dados e análise exploratória

#####

## Como a análise será realizada:

O gráfico mostra a quantidade de nascimentos ao longo do ano de 2019 em Rondônia. O gráfico apresenta flutuações ao longo do ano, com vários picos e vales. Isso sugere que a quantidade de nascimentos variou mês a mês. Os meses com os maiores picos podem indicar períodos de maior atividade de nascimentos, enquanto os vales podem representar momentos de menor atividade.

- **Padrões Sazonais:** Pode ser interessante investigar se existem padrões sazonais. Por exemplo, ***há mais nascimentos em determinadas estações do ano?*** Esses padrões podem estar relacionados a fatores como clima, feriados ou eventos culturais.
- **Eventos Específicos:** Podemos verificar se algum evento específico (como feriados ou datas comemorativas) está correlacionado com os picos de nascimentos.

**Impacto na Saúde Pública:** Essa análise pode ajudar a avaliar a demanda por serviços de saúde materna e neonatal em diferentes momentos do ano. Também pode fornecer insights sobre recursos necessários para atender a essas demandas.

                  
             """)
    
    st.write('### Veja mais ↓')
    with st.expander('Preparação dos dados e análise exploratória'):
        st.write("""

### Preparação dos dados

![](https://raw.githubusercontent.com/enzoschitini/Data-Science-Portfolio/refs/heads/main/01%20An%C3%A1lise%20explorat%C3%B3ria%20e%20limpeza%20de%20dados/E-commerce%20Customer%20Data%20For%20Behavior%20Analysis/Image/Schema.png)
    
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

        

    ## 
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
    
        st.image(schema)

























    st.write("""
#####
             
## Insights
#####

![](https://media.licdn.com/dms/image/v2/D5612AQGTWZtZzbXyHA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721195567492?e=1735776000&v=beta&t=9vLZBrov8c6Xs2WIlOg6pPPmMZFU5lhejHq_a9XbDto)

## Como a análise será realizada:

O gráfico mostra a quantidade de nascimentos ao longo do ano de 2019 em Rondônia. O gráfico apresenta flutuações ao longo do ano, com vários picos e vales. Isso sugere que a quantidade de nascimentos variou mês a mês. Os meses com os maiores picos podem indicar períodos de maior atividade de nascimentos, enquanto os vales podem representar momentos de menor atividade.

- **Padrões Sazonais:** Pode ser interessante investigar se existem padrões sazonais. Por exemplo, ***há mais nascimentos em determinadas estações do ano?*** Esses padrões podem estar relacionados a fatores como clima, feriados ou eventos culturais.
- **Eventos Específicos:** Podemos verificar se algum evento específico (como feriados ou datas comemorativas) está correlacionado com os picos de nascimentos.

**Impacto na Saúde Pública:** Essa análise pode ajudar a avaliar a demanda por serviços de saúde materna e neonatal em diferentes momentos do ano. Também pode fornecer insights sobre recursos necessários para atender a essas demandas.

                  
             """)
    
    st.write('### Veja mais ↓')
    with st.expander('Preparação dos dados e análise exploratória'):
        st.write("""

        st.expander('teste')

        """)




























    st.write("""
#####
             
## Fórmula de desempenho
#####

![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/f2.png)

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