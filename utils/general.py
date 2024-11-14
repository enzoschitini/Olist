import streamlit as st
import pandas as pd

import utils.metrics as mtc
import utils.elements as elements

# App Developer:     Enzo Schitini -- Data Science
# Date:              2 Outubro 2024 -- 22 Outubro 2024

def general(olist):
    # Definindo as datas
    data_inicio = pd.to_datetime(olist.head(1)['order_estimated_delivery_date'].values[0]) # 2017-09-29 00:00:00
    data_fim = pd.to_datetime(olist.tail(1)['order_estimated_delivery_date'].values[0]) # 2018-04-30 00:00:00

    # Calculando a diferença
    diferenca_dias = (data_fim - data_inicio).days
    capitais_vendedores = olist['seller_city'].nunique()
    capitais_clientes = olist['customer_city'].nunique()

    col1, col2, col3 = st.columns(3)
    # <p>Este é um exemplo de um grupo com borda personalizada no Streamlit.</p>
    
    with col1:
        mtc.markdown(mtc.formatar_numero_grande(len(list(olist['order_id']))), ' Produtos Vendidos', 
                 f'{round(len(list(olist['order_id'])) / diferenca_dias)} Vendas/Dia', '#F8F8FF')
    with col2:
        mtc.markdown(mtc.formatar_numero_grande(sum(list(olist['payment_value']))), ' de faturamento', 
                 f'{mtc.formatar_numero_grande(round(sum(list(olist['payment_value'])) / diferenca_dias))}/Dia', '#F8F8FF')
    with col3:
        mtc.markdown(mtc.formatar_numero_grande(capitais_clientes), ' de cidades compradoras', 
                 f'{mtc.formatar_numero_grande(capitais_vendedores)} cidades com pontos de venda', '#F8F8FF')
    
    grafico1, grafico2 = st.columns([3, 2])
    
    with grafico1:
        mtc.order_id(olist)
    with grafico2:        
        group_by = olist.groupby('month/year_of_purchase', as_index=False)
        mtc.line_metrics_time(group_by['payment_value'].sum(), 'payment_value', 'Faturamento médio mensal') 

    col1, col2 = st.columns([1, 3])
    
    with col1:
        regioes_estados_cidades = {
            "Novos vendedores": "seller_id",
            "Novos clientes": "customer_id",

            "Novos produtos": "product_id",
            "Novas categorias de produtos": "product_category_name",

            "Novos comentários e feedbacks": "review_id"
        }

        feature = mtc.escolher_opcao('Escolha como será feita a análise', regioes_estados_cidades.keys())


    with col2:
        mtc.novos(olist, regioes_estados_cidades[feature], 1)


