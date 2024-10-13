import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import locale

import utils.metrics as mtc

# App developer:     Enzo Schitini
# Date:              2 Outubro 2024

def metricas_produtos(olist, opcao):
    olist = pd.DataFrame(olist)
    total = len(list(set(olist['product_category_name'].to_list())))

    def calculo_categoria(dataframe:pd.DataFrame, categoria):
            dataframe_filtrado = dataframe[dataframe['product_category_name'] == categoria]

            total_vendas = dataframe_filtrado.shape[0]
            percentual_vendas = round((total_vendas / dataframe.shape[0]) * 100, 2)
            valor_total_vendas = round(dataframe_filtrado['payment_value'].sum(), 2)

            valor_medio_vendas = round(dataframe_filtrado['payment_value'].mean(), 2)
            preco_medio = round(dataframe_filtrado['price'].mean(), 2)
            valor_medio_frete = round(dataframe_filtrado['freight_value'].mean(), 2)

            taxa_frete = round((valor_medio_frete/preco_medio) * 100, 2)
            nota_media = round(dataframe_filtrado['review_score'].mean(), 2)
            quantidade_vendedores = len(list(set(dataframe_filtrado['seller_id'].to_list())))

            payment_installments = round(dataframe_filtrado['payment_installments'].mean())
            installments_price = round(dataframe_filtrado['installments_price'].mean(), 2)

            dataframe = dataframe[dataframe['order_item_id'] > 1]
            order_item_id = dataframe[dataframe['product_category_name'] == categoria].shape[0]

            dataframe_filtrado['shipping_duration'] = pd.to_timedelta(dataframe_filtrado['shipping_duration'])
            tempo_de_envio = dataframe_filtrado['shipping_duration'].mean()
            tempo_de_envio = mtc.formatar_timedelta_em_portugues(tempo_de_envio)[1]

            dsp = mtc.avaliar_categoria(valor_total_vendas, total_vendas, nota_media, taxa_frete, valor_medio_frete, preco_medio)

            return (valor_total_vendas, total_vendas, valor_medio_vendas, percentual_vendas, preco_medio, 
                    valor_medio_frete, nota_media, taxa_frete, quantidade_vendedores, payment_installments, 
                    installments_price, order_item_id, tempo_de_envio, dsp)

    categorias = list(set(olist['product_category_name'].to_list()))
    resultados = []

    for categoria in categorias:
        resultado = calculo_categoria(olist, categoria)
        resultados.append({
            "Categoria": categoria,
            "Valor total de vendas": resultado[0],
            "Volume de vendas": resultado[1],
            "Valor médio da venda": resultado[2],
            "Percentual de Vendas": resultado[3],
            "Preço médio": resultado[4],
            "Valor médio do frete": resultado[5],
            "Avaliação dos clientes": resultado[6],
            "Taxa frete": resultado[7],
            "Quantidade de vendedores": resultado[8],
            "Número de parcelas": resultado[9],
            "Preço médio por parcela": resultado[10],
            "Vezes em que foi comprado com outro produto": resultado[11],
            "Tempo de envio": resultado[12],
            "Desempenho": resultado[13]
        })
    
    dados_categorias = pd.DataFrame(resultados)

    def list_products(categoria):
        dicionario_categoria = dados_categorias[dados_categorias['Categoria'] == categoria].to_dict(orient='records')[0]

        categoria_nome = str(dicionario_categoria['Categoria']).replace('_', ' ').capitalize()
        desempenho = dicionario_categoria['Desempenho']
        taxa_frete = dicionario_categoria['Taxa frete']
        quantidade_vendedores = dicionario_categoria['Quantidade de vendedores']
        avaliacaos = dicionario_categoria["Avaliação dos clientes"]
        valor_medio_venda = dicionario_categoria['Valor médio da venda']
        preco_medio = dicionario_categoria['Preço médio']
        numero_percelas = dicionario_categoria['Número de parcelas']
        preco_por_parcela = dicionario_categoria['Preço médio por parcela']
        outros_itens = dicionario_categoria['Vezes em que foi comprado com outro produto']
        envio = dicionario_categoria['Tempo de envio']
        lucro_total_de_vendas = dicionario_categoria['Valor total de vendas']
        total_de_vendas = dicionario_categoria['Volume de vendas']
        valor_medio_frete = dicionario_categoria['Valor médio do frete']

        st.write('')
        nome_categoria = f'{categoria_nome} • Desempenho: 🌟 {desempenho}'

        st.write(f'### {nome_categoria}')
        linha_01 = (f'Taxa do frete: {taxa_frete}% • Total de vendedores: {quantidade_vendedores}' 
                    )
        
        # Avaliação dos clientes:
        linha_02 = f'Avaliação dos clientes: {avaliacaos}'

        linha_03 = (f'Valor por venda: {mtc.formatar_numero_grande(valor_medio_venda)}  •  Preço: {preco_medio}  •  '
                    f'Frete: {valor_medio_frete} (Média)')
        
        # Parcelas
        linha_04 = (f'N° parcelas: {numero_percelas} • Preço/Parcela: {preco_por_parcela}'
                    f' • Vezes em que foi comprado com outro produto: {outros_itens} Tempo de envio: {envio}')

        mtc.markdown_pedidos(f'${mtc.formatar_numero_grande(lucro_total_de_vendas)}', f'em {total_de_vendas} vendas', 
                                linha_01, linha_02, linha_03, linha_04, '#F8F8FF')
        







    
    
    #opcao = mtc.escolher_opcao('Escolha como quer ver as categorias', ['Análise geral', 'Análise de uma categoria'])
    st.write('')
    st.image('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-16.png', width=150)

    # Lista com as categorias #################################################################################################
    # -------------------------------------------------------------------------------------------------------------------------
    if opcao == 'Análise geral':
        st.title(f'Análise das {total} categorias de produtos')

        col_list, col_pizza = st.columns([3, 1.5])
        
        with col_list:
            ordenar_por = mtc.escolher_opcao('Ordenar por', list(dados_categorias.drop(columns='Categoria').columns))
            
            df_ordenado = dados_categorias.sort_values(by=ordenar_por, ascending=False)
            categorias = df_ordenado['Categoria'].to_list()

            for categoria in categorias:
                list_products(categoria)

        with col_pizza:
             pass


    # Lista com as categorias #################################################################################################
    # -------------------------------------------------------------------------------------------------------------------------
    elif opcao == 'Análise de uma categoria':
        col1, col2 = st.columns([4, 1])

        with col1: 
            st.title(f'Análise temporal por categoria')
        with col2:
            categoria_escolhida = mtc.escolher_opcao('Escolha uma categoria', list(set(olist['product_category_name'].to_list())))

        
        group_by = olist[olist['product_category_name'] == categoria_escolhida].groupby('month/year_of_purchase', as_index=False)
        
        st.write('#### Grupo 01')
        col1_l1, col2_l1, col3_l1 = st.columns(3)

        with col1_l1:
             mtc.markdown(f'Valor arrecadado', ' em 10 Vendas', 
                        f'{round(len(list(olist['order_id'])) / 22)} Vendas/Dia', '#F8F8FF')
             
             mtc.line_metrics_time(group_by['order_id'].count(), 'order_id', 'Volume de vendas')
             mtc.line_metrics_time(group_by['freight_value'].count(), 'freight_value', 'Preço do frete')

        with col2_l1:
             mtc.markdown('200', ' Valor medio venda', 
                        f'{round(len(list(olist['order_id'])) / 22)} Vendas/Dia', '#F8F8FF')
             
             mtc.line_metrics_time(group_by['payment_value'].mean(), 'payment_value', 'Faturamento')
             mtc.line_metrics_time(group_by['seller_id'].count(), 'seller_id', 'Quantidade de vendedores')

        with col3_l1:
             mtc.markdown(mtc.formatar_numero_grande(len(list(olist['order_id']))), ' Produtos Vendidos', 
                        f'{round(len(list(olist['order_id'])) / 22)} Vendas/Dia', '#F8F8FF')
             
             mtc.line_metrics_time(group_by['price'].mean(), 'price', 'Média do preço')
        
            
