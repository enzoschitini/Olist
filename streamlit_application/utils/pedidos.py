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
        "year_of_purchase": "Ano da compra",
        "shipping_duration_days": "Duração de envio (dias)"
    }

    # Função para encontrar chave a partir do valor
    def encontrar_chave(dicionario, valor_procurado):
        for chave, valor in dicionario.items():
            if valor == valor_procurado:
                return chave
        return None  # Se não encontrar

    colunas_numericas = ['payment_value', 'price', 'freight_value', 'payment_installments', 'installments_price', 'shipping_duration_days',
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
        st.image('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-3-unboxing.png', width=150)
        st.title(f"Análise dos Pedidos")
        #elements.grupo_azul(f'Média {dicionario_medias['price']} Preço')
        

        mtc.markdown(f'{dicionario_medias['payment_value']}', ' - Valor médio dos pedidos', f'Preço médio: {dicionario_medias['price']} Frete médio: {dicionario_medias['freight_value']}', '#F8F8FF')
        mtc.markdown(f'{dicionario_medias['payment_installments']}', ' - Número médio de parcelas', f'Valor médio por parcela: {dicionario_medias['installments_price']}', '#F8F8FF')

    with col2:
        st.write('## Gráfico de Dispersão com Plotly')
        #Gráfico de Pizza
        fig = go.Figure(data = go.Pie(labels = ['Preço do produto', 'Preço do frete'],
                                    values = [dicionario_medias['price'], dicionario_medias['freight_value']],
                                    marker_colors = ["MediumSeaGreen", "khaki"], # "khaki", "MediumSeaGreen", "crimson", "limegreen", "tomato"
                                    hole = 0.5,
                                    pull = [0, .10, 0.0, 0, 0]))

        #Rótulos
        fig.update_traces(textposition = "outside", textinfo = "percent+label")

        #Legenda
        fig.update_layout(title='Partes do valor total', legend_title_text = "Partes:",
                        legend = (dict(orientation = "h",
                                    xanchor = "auto",
                                    x = 0.5)))

        #Texto
        fig.update_layout(annotations = [dict(text = "Percentual",
                                            x = 0.5,
                                            y = 0.5,
                                            font_size = 18,
                                            showarrow = False)])
        
        st.plotly_chart(fig)

    with col3:
        import plotly.express as px

        # Interface do usuário para selecionar as variáveis
        st.write('## Gráfico de Dispersão com Plotly')

        # Criar o gráfico de dispersão
        fig = px.scatter(olist, x='price', y='freight_value', color='payment_type', title='Gráfico de Dispersão')

        # Exibir o gráfico na aplicação Streamlit
        st.plotly_chart(fig)
    
    mtc.espaco()










    col01, col02 = st.columns([1, 4])

    def card():
        # Custom HTML and CSS
        html_code = """
            <div style="display: flex; align-items: center; background-color: #F0F7FC; padding: 20px; border-radius: 10px; border: 1px solid #E0E0E0; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                <div>
                    <h3 style="margin: 0; color: #4561FF;">Enter your OpenAI API Key?</h3>
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

    with col01:
        #st.write('### Boxplot')

        select = st.selectbox('Selecione uma coluna', colunas_numericas_ptbr)
        col_plot = encontrar_chave(colunas_renomeadas, select)

        st.image('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-9.png')
        st.write(f'## {round(olist[col_plot].mean(), 2)} {select} (Média)')

        #mtc.markdown(f'{round(olist[col_plot].mean(), 2)}', f'{select} (Média)', '', '#F8F8FF')

    with col02:
        boxplot, dispersao = st.columns(2)
        with boxplot:
            mtc.boxplot(olist, col_plot)
        with dispersao:
            st.write('Escolha mais uma variável para gráfico de dispersão')
            select = st.selectbox('Selecioane uma coluna', colunas_numericas_ptbr)
            col_disp = encontrar_chave(colunas_renomeadas, select)
            # Criar o gráfico de dispersão
            fig = px.scatter(olist, x=col_plot, y=col_disp, title='Gráfico de Dispersão')

            #fig.update_layout(width=800, height=800)

            # Exibir o gráfico na aplicação Streamlit
            st.plotly_chart(fig)
    
    mtc.partes(olist, col_plot)

    mtc.espaco()










    olist['shipping_duration'] = pd.to_timedelta(olist['shipping_duration'])
    olist['shipping_duration_days'] = olist['shipping_duration'].dt.days

    st.write(f'## Envio dos pedidos ') # - Duração média de {dicionario_medias['shipping_duration_days']} dias
    
    col1, col2 = st.columns([2, 3]) # [3, 1.5]

    with col1:
        col001, col002 = st.columns([1.5, 2])
        with col001:
            st.image('streamlit_application/img/Commerce Illustrations/Order.png', width=150)
        with col002:
            st.write('Ok')
        
        
        group_by = olist.groupby('month/year_of_purchase', as_index=False)
        mtc.line_metrics_time(group_by['shipping_duration_days'].mean(), 'shipping_duration_days', 'Duração das entregas em dias')

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




    
    

    