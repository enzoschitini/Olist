import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import locale
import io

import utils.metrics as mtc

# App Developer:     Enzo Schitini -- Data Science
# Date:              2 Outubro 2024 -- 22 Outubro 2024

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

    def info(categoria):
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

        return (categoria_nome, desempenho, taxa_frete, quantidade_vendedores, avaliacaos, valor_medio_venda, 
                preco_medio, numero_percelas, preco_por_parcela, outros_itens, envio, lucro_total_de_vendas, total_de_vendas, valor_medio_frete)

    def list_products(categoria):
        (categoria_nome, desempenho, taxa_frete, quantidade_vendedores, avaliacaos, valor_medio_venda, preco_medio, numero_percelas, 
         preco_por_parcela, outros_itens, envio, lucro_total_de_vendas, total_de_vendas, valor_medio_frete) = info(categoria)

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

    # Tradução das colunas ####################################################################################################
    # -------------------------------------------------------------------------------------------------------------------------
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





    # Análise geral ###########################################################################################################
    # -------------------------------------------------------------------------------------------------------------------------
    if opcao == 'Análise geral':
        st.image('img/Commerce Illustrations/vctrly-business-illustrations-16.png', width=150)
        st.title(f'Análise das {total} categorias de produtos')

        col_pizza_1, col_pizza_2, col_pizza_3 = st.columns(3)

        with col_pizza_1:
             mtc.grafico_pizza_rank(olist, 'payment_value', "Categorias de Produtos que mais geram lucro", 'sum')
        with col_pizza_2:
             mtc.grafico_pizza_rank(olist, 'order_id', "Total de vendas por categoria", 'count')
        with col_pizza_3:
             mtc.grafico_pizza_rank(olist, 'freight_value', "Categorias de Produtos que mais gastam com frete", 'sum')

        mtc.espaco()

        col, col_list = st.columns([1, 3])
        
        with col:
            st.image('img/Commerce Illustrations/vctrly-business-illustrations-6-onlineshop.png', width=200)
            st.write('### Escolha uma métrica para ordenar as categorias')

            # Função para converter o DataFrame para XLSX
            def convert_df_to_excel(df):
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                    df.to_excel(writer, index=False)
                return buffer

            # CSS para personalizar o botão e remover a borda vermelha
            st.markdown("""
                <style>
                .stDownloadButton button {
                    background-color: #007bff;
                    color: white;
                    transition: background-color 0.3s ease;
                    border: none;  /* Remove a borda padrão */
                    outline: none;  /* Remove a borda de foco */
                }
                .stDownloadButton button:hover {
                    background-color: #0056b3;
                    color: white;
                }
                .stDownloadButton button:active {
                    background-color: #004080;
                    color: white;
                }
                .stDownloadButton button:focus {
                    outline: none;  /* Remove a borda ao focar */
                    box-shadow: none;  /* Remove o sombreado ao focar */
                }
                </style>
                """, unsafe_allow_html=True)

            # Botão para download
            st.write("Tabela com informações sobre as categorias (XLSX)")

            # Gerando o buffer do Excel
            excel_buffer = convert_df_to_excel(dados_categorias)

            # Botão de download
            st.download_button(
                label="Baixar XLSX",
                data=excel_buffer,
                file_name='Tabela das Categorias - Olist.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )

        with col_list:
            ordenar_por = mtc.escolher_opcao('Ordenar por', list(dados_categorias.drop(columns='Categoria').columns))

            df_ordenado = dados_categorias.sort_values(by=ordenar_por, ascending=False)
            categorias = df_ordenado['Categoria'].to_list()

            for categoria in categorias:
                list_products(categoria)





    # Análise de uma categoria ################################################################################################
    # -------------------------------------------------------------------------------------------------------------------------
    elif opcao == 'Análise de uma categoria':
        olist['volume'] = olist['product_length_cm'] * olist['product_height_cm'] * olist['product_width_cm']
        col1, col2 = st.columns([4, 1])

        with col1: 
            st.title(f'Análise temporal por categoria')
        with col2:
            # list(set(olist['product_category_name'].to_list()))
            categoria_escolhida_list = list(olist['product_category_name'].value_counts().to_dict().keys())
            categoria_escolhida_list = [cat.replace('_', ' ').capitalize() for cat in categoria_escolhida_list]

            categoria_escolhida = mtc.escolher_opcao('Escolha uma categoria', categoria_escolhida_list)
            categoria_escolhida = categoria_escolhida.lower().replace(' ', '_')
            
        olist['shipping_duration'] = pd.to_timedelta(olist['shipping_duration'])
        group_by = olist[olist['product_category_name'] == categoria_escolhida].groupby('month/year_of_purchase', as_index=False)
        (categoria_nome, desempenho, taxa_frete, quantidade_vendedores, avaliacaos, valor_medio_venda, preco_medio, numero_percelas, 
         preco_por_parcela, outros_itens, envio, lucro_total_de_vendas, total_de_vendas, valor_medio_frete) = info(categoria_escolhida)
        
        mtc.espaco()
        titolo_01, titolo_02 = st.columns([1, 2])

        with titolo_01:
             st.image('img/Commerce Illustrations/vctrly-business-illustrations-200-presentation.png')
             st.title(f'{categoria_nome}')
             st.write(f'#### Tempo de entrega: {envio}')
        with titolo_02:
             mtc.markdown(f'${mtc.formatar_numero_grande(lucro_total_de_vendas)}', f'em {total_de_vendas} vendas', 
                        f'Total de vendedores: {quantidade_vendedores} • Desempenho da categoria {desempenho}', '#F8F8FF')
             
             mtc.markdown(f'{mtc.formatar_numero_grande(valor_medio_venda)}', ' Valor médio da venda', 
                        f'Preço Médio: {preco_medio} • Frete Médio: {valor_medio_frete}({taxa_frete}%) • Total de parcelas: {numero_percelas} • Preço médio(parcela): {preco_por_parcela}', '#F8F8FF')

             mtc.markdown(f'{avaliacaos} ', 'Avaliação dos clientes', 
                        f'Comprado com outros itens: {outros_itens}', '#F8F8FF')

        mtc.espaco()
        col1_l2, col2_l2, col3_l2 = st.columns(3)

        with col1_l2:
             mtc.line_metrics_time(group_by['order_id'].count(), 'order_id', 'Volume de vendas')
             mtc.line_metrics_time(group_by['freight_value'].mean(), 'freight_value', 'Preço do frete')

        with col2_l2:        
             mtc.line_metrics_time(group_by['payment_value'].mean(), 'payment_value', 'Faturamento')
             mtc.line_metrics_time(group_by['seller_id'].nunique(), 'seller_id', 'Quantidade de vendedores')

        with col3_l2:
             mtc.line_metrics_time(group_by['price'].mean(), 'price', 'Média do preço')
             mtc.line_metrics_time(group_by['review_score'].mean(), 'review_score', 'Avaliação dos clientes')
        
        order_item_id = olist[olist['product_category_name'] == categoria_escolhida]
        order_item_id = order_item_id[order_item_id['order_item_id'] > 1]

        order_item_id_list = list(order_item_id['order_id'].unique())
        order_item_id = olist[olist['order_id'].isin(order_item_id_list)]
        order_item_id = order_item_id.loc[order_item_id['product_category_name'] != categoria_escolhida]

        col1, col2 = st.columns([3, 1])

        with col1:
            st.write(f'## Análise dos quartis:')
        with col2:
            col_select = st.selectbox('Selecione uma coluna para o boxplot', colunas_numericas_ptbr)
            col_select = encontrar_chave(colunas_renomeadas, col_select)
        mtc.partes(olist[olist['product_category_name'] == categoria_escolhida], col_select)

        if order_item_id.shape[0] > 1:
             mtc.grafico_categoria('product_category_name', order_item_id, f'Categorias associadas')
            
