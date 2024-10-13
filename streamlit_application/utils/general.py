import streamlit as st
import pandas as pd

import utils.metrics as mtc

# streamlit_application developer:     Enzo Schitini
# Date:              2 Outubro 2024

@st.cache_data
def general(olist):
    # Definindo as datas
    data_inicio = pd.to_datetime(olist.head(1)['order_estimated_delivery_date'].values[0]) # 2017-09-29 00:00:00
    data_fim = pd.to_datetime(olist.tail(1)['order_estimated_delivery_date'].values[0]) # 2018-04-30 00:00:00

    # Calculando a diferença
    diferenca_dias = (data_fim - data_inicio).days

    col1, col2, col3 = st.columns(3)
    # <p>Este é um exemplo de um grupo com borda personalizada no Streamlit.</p>
    
    with col1:
        mtc.markdown(mtc.formatar_numero_grande(len(list(olist['order_id']))), ' Produtos Vendidos', 
                 f'{round(len(list(olist['order_id'])) / diferenca_dias)} Vendas/Dia', '#F8F8FF')
    with col2:
        mtc.markdown(mtc.formatar_numero_grande(sum(list(olist['payment_value']))), ' de faturamento', 
                 f'{mtc.formatar_numero_grande(round(sum(list(olist['payment_value'])) / diferenca_dias))}/Dia', '#F8F8FF')
    with col3:
        mtc.markdown(mtc.formatar_numero_grande(sum(list(olist['payment_value']))), ' de faturamento', 
                 f'{mtc.formatar_numero_grande(round(sum(list(olist['payment_value'])) / diferenca_dias))}/Dia', '#F8F8FF')
    
    mtc.order_id(olist)
    

        