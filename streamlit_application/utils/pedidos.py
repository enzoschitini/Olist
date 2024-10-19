import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

import utils.metrics as mtc
import utils.elements as elements
import utils.AnalyticsSetup as ast

# App Developer:     Enzo Schitini -- Data Science
# Date:              2 Outubro 2024 -- 22 Outubro 2024

#@st.cache_data
def metricas_pedidos(olist):

    colunas_renomeadas = {
        "order_item_id": "ID do item do pedido",
        "customer_zip_code_prefix": "Prefixo do CEP do cliente",
        "product_name_lenght": "Comprimento do nome do produto",
        "product_description_lenght": "Comprimento da descrição do produto",
        "product_photos_qty": "Quantidade de fotos do produto",
        "product_weight_g": "Peso do produto (g)",
        "product_length_cm": "Comprimento do produto (cm)",
        "product_height_cm": "Altura do produto (cm)",
        "product_width_cm": "Largura do produto (cm)",
        "Kg": "Peso (Kg)",
        "seller_zip_code_prefix": "Prefixo do CEP do vendedor",
        "payment_sequential": "Sequência de pagamento",
        "payment_installments": "Parcelas de pagamento",
        "installments_price": "Valor das parcelas",
        "price": "Preço",
        "freight_value": "Valor do frete",
        "payment_value": "Valor do pagamento",
        "review_score": "Pontuação da avaliação",
        "year_of_purchase": "Ano da compra"
    }

    # Função para encontrar chave a partir do valor
    def encontrar_chave(dicionario, valor_procurado):
        for chave, valor in dicionario.items():
            if valor == valor_procurado:
                return chave
        return None  # Se não encontrar

    colunas_numericas = ['payment_value', 'price', 'freight_value', 'payment_installments', 'installments_price',
                         'product_name_lenght', 'product_description_lenght', 'product_photos_qty', 'product_weight_g', 
                         'product_length_cm', 'product_height_cm', 'product_width_cm', 'Kg']
    colunas_numericas_ptbr = []

    for x in colunas_numericas:
        col = colunas_renomeadas[x]
        colunas_numericas_ptbr.append(col)


    # Definindo as datas
    data_inicio = pd.to_datetime(olist.head(1)['order_estimated_delivery_date'].values[0]) # 2017-09-29 00:00:00
    data_fim = pd.to_datetime(olist.tail(1)['order_estimated_delivery_date'].values[0]) # 2018-04-30 00:00:00

    # Calculando a diferença
    diferenca_dias = (data_fim - data_inicio).days

    def means(olist):
        dicionario_medias = {}  
        for col in list(olist.select_dtypes('number').columns):
            dicionario_medias[col] = round(olist[col].mean(), 2) 

        return dicionario_medias
    
    dicionario_medias = means(olist)

    # price freight_value payment_type customer_zone

    # Função para análise bivariada de variáveis numéricas AB2N
    # Função para análise bivariada entre variável categórica e numérica num_cat_analysis
    # Função para análise bivariada entre variável categórica e numérica usando um gráfico de barras num_cat_analysis_bar
    # Função para análise bivariada entre variáveis categóricas AB2C

    #ast.AB2N(olist, 'price', 'freight_value')
    #ast.num_cat_analysis_bar(olist, 'price', 'payment_type')
    #ast.AB2C(olist, 'payment_type', 'customer_zone', 'qtd') 
    #ast.AB2C(olist, 'payment_type', 'customer_zone', 'prct') 

    col1, col2, col3 = st.columns(3) # [3, 1.5]

    with col1:
        #st.image('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-3-unboxing.png', width=150)
        st.title(f"Análise dos Pedidos")
        elements.grupo_azul(f'Média {dicionario_medias['price']} Preço')
        

        mtc.markdown('h', 'j', 'k', '#F8F8FF')
        mtc.markdown('h', 'j', 'k', '#F8F8FF')

    with col2:
        st.write('## Gráfico de Dispersão com Plotly')
        #Gráfico de Pizza
        fig = go.Figure(data = go.Pie(labels = ['Sul','Sudeste','Centro-Oeste','Nordeste', "Norte"],
                                    values = [29933315, 84847187, 16287809, 54644582, 17349619],
                                    marker_colors = ["khaki", "MediumSeaGreen", "crimson", "limegreen", "tomato"],
                                    hole = 0.5,
                                    pull = [0, 0, 0.15, 0, 0]))

        #Rótulos
        fig.update_traces(textposition = "outside", textinfo = "percent+label")

        #Legenda
        fig.update_layout(title='Texto com o títolo', legend_title_text = "Regiões brasileiras",
                        legend = (dict(orientation = "h",
                                    xanchor = "auto",
                                    x = 0.5)))

        #Texto
        fig.update_layout(annotations = [dict(text = "População",
                                            x = 0.5,
                                            y = 0.5,
                                            font_size = 18,
                                            showarrow = False)])
        
        st.plotly_chart(fig)

    with col3:
        def card():
            # Custom HTML and CSS
            html_code = """
                <div style="display: flex; align-items: center; background-color: #F0F7FC; padding: 10px; border-radius: 10px; border: 1px solid #E0E0E0; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                    <div style="border-radius: 5px; padding: 10px; margin-right: 10px;">
                        <img src="https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/main/streamlit_application/img/Commerce%20Illustrations/order.png" width="100px" />
                    </div>
                    <div>
                        <h3 style="margin: 0; color: #2E8E59;">Enter your OpenAI API Key?</h3>
                        <p style="margin: 0; color: #808080;">Enter your OpenAI API Key?Enter your OpenAI API Key?Enter your OpenAI API Key?</p>
                    </div>
                </div>
                <style>
                    h3 {
                        font-family: Arial, sans-serif;
                        font-size: 18px;
                    }
                    p {
                        font-family: Arial, sans-serif;
                        font-size: 14px;
                    }
                </style>
            """

            # Display the custom HTML in Streamlit
            st.markdown(html_code, unsafe_allow_html=True)
        
        import plotly.express as px

        # Interface do usuário para selecionar as variáveis
        st.write('## Gráfico de Dispersão com Plotly')

        # Criar o gráfico de dispersão
        fig = px.scatter(olist, x='price', y='freight_value', color='payment_type', title='Gráfico de Dispersão')

        # Exibir o gráfico na aplicação Streamlit
        st.plotly_chart(fig)
    
    mtc.espaco()
    col01, col02 = st.columns([1, 3])

    with col01:
        #st.write('### Boxplot')

        select = st.selectbox('Selecione uma coluna', colunas_numericas_ptbr)
        col_plot = encontrar_chave(colunas_renomeadas, select)

        st.image('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-9.png')
        #st.write(f'## Média: {round(olist[col_plot].mean(), 2)}')

        mtc.markdown(f'Média: {round(olist[col_plot].mean(), 2)}', f'{select}', 'd', '#F8F8FF')

    with col02:
        mtc.boxplot(olist, col_plot)
    
    mtc.partes(olist, col_plot)

    mtc.espaco()
    st.write('## Envio dos pedidos')
    
    col1, col2 = st.columns([2, 3]) # [3, 1.5]

    with col1:
        col001, col002 = st.columns([1.5, 2])
        with col001:
            st.image('streamlit_application/img/Commerce Illustrations/Order.png', width=150)
        with col002:
            st.write('Ok')

    with col2:
        col001, col002 = st.columns(2)
        with col001:
            card()
            st.write('')
            card()
            st.write('')
            card()
            st.write('')
            card()
        with col002:
            pass




    
    

    