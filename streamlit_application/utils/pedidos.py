import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import utils.metrics as mtc
import utils.elements as elements
import utils.AnalyticsSetup as ast

# App developer:     Enzo Schitini
# Date:              2 Outubro 2024

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

    colunas_numericas = list(olist.select_dtypes('number'))
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

    st.title(f"Análise dos Pedidos")

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
        # Variabile per il valore nel cerchio
        valor = f'${dicionario_medias['price']}'

        # HTML e CSS per creare l'elemento circolare allineato a sinistra con distanza tra il cerchio e il testo sotto
        st.markdown(
            f"""
            <div style="display: flex; flex-direction: column; align-items: flex-start;">
                <div style="width: 150px; height: 150px; background-color: #2563EB; border-radius: 50%; border: 10px solid #93C5FD;">
                    <p style="font-size: 30px; color: white; text-align: center; line-height: 130px; margin: 0;">{valor}</p>
                </div>
                <div class="custom-box" style="text-align: center; width: 150px; margin-top: 30px;">
                    <h5 style="color: #333;">Preço médio</h5>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:
        mtc.grafico_pizza_rank(olist, 'payment_value', "Categorias de Produtos que mais geram lucro", 'sum')
    
    with col3:
        elements.grupo_azul(f'Média {dicionario_medias['Kg']}Kg')
    
    mtc.espaco()
    col01, col02 = st.columns([1, 3])

    with col01:
        st.write('### Boxplot')
        st.image('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-200-presentation.png')

        col_plot = st.selectbox('Selecione uma coluna para o boxplot', colunas_numericas_ptbr)
        col_plot = encontrar_chave(colunas_renomeadas, col_plot)
        st.write(f'## Média: {round(olist[col_plot].mean(), 2)}')

        com_frete = olist[olist['freight_value'] > 0.0].shape[0]
        sem_frete = olist[olist['freight_value'] == 0.0].shape[0]

        com_frete = round((com_frete / olist.shape[0]) * 100, 2)
        sem_frete = round((sem_frete / olist.shape[0]) * 100, 2)

        st.write(f'#### Percentual com frete: {com_frete}')
        st.write(f'#### Percentual sem frete: {sem_frete}')
    with col02:
        mtc.boxplot(olist, col_plot)
    
    mtc.partes(olist, col_plot)

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




    
    

    