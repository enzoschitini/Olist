import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

import utils.metrics as mtc
import utils.elements as elements
import utils.AnalyticsSetup as ast

# App Developer:     Enzo Schitini -- Data Science
# Date:              2 Outubro 2024 -- 22 Outubro 2024

def metricas_pedidos(olist):

    # Aggiungi CSS personalizzato per impostare lo sfondo bianco
    st.markdown(
        """
        <style>
        .stApp {
            background-color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

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
            if col != 'installments_price':
                dicionario_medias[col] = round(olist[col].mean(), 2) 
            if col == 'installments_price':
                df = olist
                # Replace infinite values with NaN, then drop NaN or 0 values if needed
                df['installments_price'].replace([np.inf, -np.inf], np.nan, inplace=True)
                df = df[df['installments_price'] != 0]  # Optionally remove rows with 0 values

                # Calculate the mean, ignoring NaN values
                dicionario_medias[col] = round(df['installments_price'].mean(), 2)

        return dicionario_medias
    
    dicionario_medias = means(olist)

    col1, col2, col3 = st.columns(3) # [3, 1.5]

    with col1:
        st.image('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-3-unboxing.png', width=150)
        st.title(f"Análise dos Pedidos")
        #elements.grupo_azul(f'Média {dicionario_medias['price']} Preço')
        

        mtc.markdown(f'{dicionario_medias['payment_value']}', ' - Valor médio dos pedidos', f'Preço médio: {dicionario_medias['price']} Frete médio: {dicionario_medias['freight_value']}', '#F8F8FF')
        mtc.markdown(f'{dicionario_medias['payment_installments']}', ' - Número médio de parcelas', f'Valor médio por parcela: {dicionario_medias['installments_price']}', '#F8F8FF')

    with col2:
        st.write('## Partes do valor total')
        #Gráfico de Pizza
        fig = go.Figure(data = go.Pie(labels = ['Preço do produto', 'Preço do frete'],
                                    values = [dicionario_medias['price'], dicionario_medias['freight_value']],
                                    marker_colors = ["MediumSeaGreen", "khaki"], # "khaki", "MediumSeaGreen", "crimson", "limegreen", "tomato"
                                    hole = 0.5,
                                    pull = [0, .10, 0.0, 0, 0]))

        #Rótulos
        fig.update_traces(textposition = "outside", textinfo = "percent+label")

        #Legenda
        fig.update_layout(title='Gráfico de pizza', legend_title_text = "Partes:",
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
        # Interface do usuário para selecionar as variáveis
        st.write('## Forma de pagamento')

        # Criar o gráfico de dispersão
        fig = px.scatter(olist, x='price', y='freight_value', color='payment_type', title='Gráfico de Dispersão')

        # Exibir o gráfico na aplicação Streamlit
        st.plotly_chart(fig)
    
    mtc.espaco()

    col01, col02 = st.columns([1, 4])
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
    
    olist['order_purchase_timestamp'] = pd.to_datetime(olist['order_purchase_timestamp'])
    olist['order_approved_at'] = pd.to_datetime(olist['order_approved_at'])
    olist['order_delivered_carrier_date'] = pd.to_datetime(olist['order_delivered_carrier_date'])
    olist['order_delivered_customer_date'] = pd.to_datetime(olist['order_delivered_customer_date'])
    olist['order_estimated_delivery_date'] = pd.to_datetime(olist['order_estimated_delivery_date'])
    olist['shipping_limit_date'] = pd.to_datetime(olist['shipping_limit_date'])
    olist['shipping_duration'] = pd.to_timedelta(olist['shipping_duration'])
    olist['shipping_duration_days'] = olist['shipping_duration'].dt.days

    olist['duracao_aprovacao'] = olist['order_approved_at'] - olist['order_purchase_timestamp']
    olist['duracao_envio_ate_correio'] = olist['order_delivered_carrier_date'] - olist['order_approved_at']
    olist['duracao_envio_ate_cliente'] = olist['order_delivered_customer_date'] - olist['order_delivered_carrier_date']
    olist['chegada_limite'] = (olist['shipping_limit_date'] - olist['order_delivered_customer_date']).dt.days
    olist['chegada_estimativa'] = (olist['order_estimated_delivery_date'] - olist['order_delivered_customer_date']).dt.days

    @st.cache_data
    def line_metrics_time(sales_data, categoria, title):
        sales_data.rename(columns={'month/year_of_purchase': 'year_month'}, inplace=True)
        sales_data['year_month'] = pd.to_datetime(sales_data['year_month'], format='mixed', errors='coerce')

        if sales_data['year_month'].isna().sum() > 0:
            st.write("Warning: Some dates couldn't be parsed and have been set to NaT.")

        sales_data = sales_data.sort_values('year_month')
        fig = px.line(sales_data, x='year_month', y=categoria, title=title,labels={'year_month': 'Mês/Ano', categoria: f'Valor {categoria}'},markers=True,template='ygridoff') 

        fig.add_shape(type='line', x0=sales_data['year_month'].min(), y0=0, x1=sales_data['year_month'].max(), y1=0, line=dict(color='red', dash='dash'), name='Linea zero')
        fig.update_yaxes(tickprefix="")
        fig.update_layout(xaxis=dict(showgrid=True), yaxis=dict(showgrid=True))
        st.plotly_chart(fig)

    percentual_atraso = round(olist[olist['chegada_estimativa'] < 0].shape[0] / olist[olist['chegada_estimativa'] >= 0].shape[0] * 100)
    media_atraso = abs(round(olist[olist['chegada_estimativa'] < 0]['chegada_estimativa'].mean(), 2))
    media_chegou_antes = abs(round(olist[olist['chegada_estimativa'] >= 0]['chegada_estimativa'].mean(), 2))

    col1, col2 = st.columns([1.5, 3])

    with col1:
        st.image('streamlit_application/img/Commerce Illustrations/Order.png', width=150)
        st.write(f'## Envio dos pedidos ')
        mtc.markdown('Duração média de 13 dias', '', f'{percentual_atraso}% dos pedidos chegam atrasados (atraso médio de {media_atraso} dias)', '4561FF')
    with col2:
        group_by = olist.groupby('month/year_of_purchase', as_index=False)
        mtc.line_metrics_time(group_by['shipping_duration_days'].mean(), 'shipping_duration_days', 'Duração das entregas em dias')
    
    col1, col2, col3 = st.columns(3)
    def convert(tempo):
        # Convert to total seconds, minutes, or hours
        mean_seconds = tempo.total_seconds()
        mean_minutes = mean_seconds / 60
        mean_hours = mean_minutes / 60
        mean_days = mean_hours / 24

        return mean_seconds, mean_minutes, mean_hours, mean_days

    with col1:
        st.image('streamlit_application/img/icons/office-stamp-document-13.png', width=150)
        mtc.markdown('Aprovação da compra:', f'{round(convert(olist['duracao_aprovacao'].mean())[2])} Horas', f'Tempo médio desde o momento da compra até a aprovação da compra', '4561FF')

    with col2:
        st.image('streamlit_application/img/icons/worldwide-web-location-pin-25.png', width=150)
        mtc.markdown('Envio até o correio:', f'{round(convert(olist['duracao_envio_ate_correio'].mean())[3])} Dias', f'Duração média desde a aprovação da compra até a chegada ao correio', '4561FF')

    with col3:
        st.image('streamlit_application/img/icons/business-coaching-strategy-1-36.png', width=150)
        mtc.markdown('Envio até o cliente:', f'{round(convert(olist['duracao_envio_ate_cliente'].mean())[3])} Dias', f'Duração média desde o correio até serem enviados aos clientes ', '4561FF')

    col1, col2 = st.columns(2)
    group_by = olist.groupby('month/year_of_purchase', as_index=False)

    with col1:
        line_metrics_time(group_by['chegada_estimativa'].mean(), 'chegada_estimativa', 'Estimativa de chagada')
    with col2:
        line_metrics_time(group_by['chegada_limite'].mean(), 'chegada_limite', 'Data limite de chagada')
  