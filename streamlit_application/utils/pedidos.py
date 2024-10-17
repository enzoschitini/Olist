import streamlit as st
import pandas as pd

import utils.metrics as mtc
import utils.elements as elements

# App developer:     Enzo Schitini
# Date:              2 Outubro 2024

#@st.cache_data
def metricas_pedidos(olist):
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

    st.title(f"Análise dos Pedidos")

    col1, col2 = st.columns(2) # [3, 1.5]

    with col1:
        col001, col002 = st.columns([1.5, 3])
        with col001:
            st.image('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-3-unboxing.png', width=150)
        with col002:
            elements.grupo_azul(f'Média {dicionario_medias['Kg']}Kg')
            #st.write('Ok')

    with col2:
        col001, col002 = st.columns([1.5, 3])
        with col001:
            st.image('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-3-unboxing.png', width=150)
        with col002:
            st.write('Ok')
    
    mtc.espaco()
    col01, col02 = st.columns([1, 3])

    with col01:
        st.write('### Boxplot')
        st.image('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-200-presentation.png')

        col_boxplot = st.selectbox('Selecione uma coluna para o boxplot', list(olist.select_dtypes('number')))
        st.write(f'## Média: {round(olist[col_boxplot].mean(), 2)}')

        com_frete = olist[olist['freight_value'] > 0.0].shape[0]
        sem_frete = olist[olist['freight_value'] == 0.0].shape[0]

        com_frete = round((com_frete / olist.shape[0]) * 100, 2)
        sem_frete = round((sem_frete / olist.shape[0]) * 100, 2)

        st.write(f'#### Percentual com frete: {com_frete}')
        st.write(f'#### Percentual sem frete: {sem_frete}')
    with col02:
        mtc.boxplot(olist, col_boxplot)

    mtc.espaco()
    col1, col2 = st.columns(2) # [3, 1.5]

    with col1:
        col001, col002 = st.columns([1.5, 3])
        with col001:
            st.image('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-3-unboxing.png', width=150)
        with col002:
            st.write('Ok')

    with col2:
        col001, col002 = st.columns([1.5, 3])
        with col001:
            st.image('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-3-unboxing.png', width=150)
        with col002:
            st.write('Osk')

    
    
        
    