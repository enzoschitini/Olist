import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import locale

import utils.metrics as mtc

# App developer:     Enzo Schitini
# Date:              2 Outubro 2024

def metricas_produtos(olist):
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
            "valor_medio_frete": resultado[5],
            "nota_media": resultado[6],
            "taxa_frete": resultado[7],
            "quantidade_vendedores": resultado[8],
            "numero_de_parcelas": resultado[9],
            "preco_por_parcela": resultado[10],
            "order_item_id": resultado[11],
            "tempo_de_envio": resultado[12],
            "desempenho": resultado[13]
        })
    
    dados_categorias = pd.DataFrame(resultados)

    def list_products(categoria):
        dicionario_categoria = dados_categorias[dados_categorias['Categoria'] == categoria].to_dict(orient='records')[0]

        st.write('')
        nome_categoria = f'{str(dicionario_categoria['Categoria']).replace('_', ' ').capitalize()} • Desempenho: 🌟 {dicionario_categoria['desempenho']}'

        st.write(f'### {nome_categoria}')
        linha_01 = (f'Taxa do frete: {dicionario_categoria['taxa_frete']}% • Total de vendedores: {dicionario_categoria['quantidade_vendedores']}' 
                    )
        
        # Avaliação dos clientes:
        linha_02 = f'Avaliação dos clientes: {dicionario_categoria["nota_media"]}'

        linha_03 = (f'Valor por venda: {mtc.formatar_numero_grande(dicionario_categoria['Valor médio da venda'])}  •  Preço: {dicionario_categoria['Preço médio']}  •  '
                    f'Frete: {dicionario_categoria['valor_medio_frete']} (Média)')
        
        # Parcelas
        linha_04 = (f'N° parcelas: {dicionario_categoria['numero_de_parcelas']} • Preço/Parcela: {dicionario_categoria['preco_por_parcela']}'
                    f' • Valor: {dicionario_categoria['order_item_id']} tempo_de_envio: {dicionario_categoria['tempo_de_envio']}')

        mtc.markdown_pedidos(f'${mtc.formatar_numero_grande(dicionario_categoria['Valor total de vendas'])}', f'em {dicionario_categoria['Volume de vendas']} vendas', 
                                linha_01, linha_02, linha_03, linha_04, '#F8F8FF')








    col1, col2 = st.columns([3, 1.5]) # [3, 1.5]

    with col1:
        st.image('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-16.png', width=150)

        st.title(f'Análise das {total} categorias de produtos')
        #st.write(list(olist.columns))
        #st.write(olist.groupby('product_category_name')['payment_value'].mean().sort_values(ascending=False))

        # Caixa de filtros ########################################################################################################
        # -------------------------------------------------------------------------------------------------------------------------

        opcao = mtc.escolher_opcao('Escolha como quer ver as categorias', ['Separadamente', 'Análise Temporal'])

        if opcao == 'Separadamente':

            # Lista com as categorias #################################################################################################
            # -------------------------------------------------------------------------------------------------------------------------
            ordenar_por = mtc.escolher_opcao('Ordenar por', list(dados_categorias.columns))
            
            df_ordenado = dados_categorias.sort_values(by=ordenar_por, ascending=False)
            categorias = df_ordenado['Categoria'].to_list()

            for categoria in categorias:
                list_products(categoria)
        
        elif opcao == 'Análise Temporal':
            col001, col002 = st.columns([3, 1.5])

            with col001:
                metrica = mtc.escolher_opcao('Defina uma métrica', ['Quantidade de Vendas', 'Faturamento', 'Frete', 'Vendedores'])
            with col002:
                categoria_escolhida = mtc.escolher_opcao('Escolha uma categoria', list(set(olist['product_category_name'].to_list())))
            
            list_products(categoria_escolhida)

            if metrica == 'Quantidade de Vendas':
                mtc.line_metrics_time(olist[olist['product_category_name'] == categoria_escolhida].groupby('month/year_of_purchase', as_index=False)['payment_value'].sum(), 
                                  'payment_value', 'Faturamento')

                mtc.line_metrics_time(olist[olist['product_category_name'] == categoria_escolhida].groupby('month/year_of_purchase', as_index=False)['order_id'].count(), 
                                  'order_id', 'Volume de vendas')


                mtc.line_metrics_time(olist[olist['product_category_name'] == categoria_escolhida].groupby('month/year_of_purchase', as_index=False)['freight_value'].mean(), 
                                  'freight_value', 'Média do custo com frete')

                mtc.line_metrics_time(olist[olist['product_category_name'] == categoria_escolhida].groupby('month/year_of_purchase', as_index=False)['seller_id'].count(), 
                                  'seller_id', 'Vendedores')

                mtc.line_metrics_time(olist[olist['product_category_name'] == categoria_escolhida].groupby('month/year_of_purchase', as_index=False)['review_score'].mean(), 
                                  'review_score', 'Avaliações')


                mtc.line_metrics_time(olist[olist['product_category_name'] == categoria_escolhida].groupby('month/year_of_purchase', as_index=False)['payment_installments'].mean(), 
                                  'payment_installments', 'Média de parcelas')

                mtc.line_metrics_time(olist[olist['product_category_name'] == categoria_escolhida].groupby('month/year_of_purchase', as_index=False)['installments_price'].mean(), 
                                  'installments_price', 'Média do valor das parcelas')
                
                olist['shipping_duration'] = pd.to_timedelta(olist['shipping_duration'])
                olist['duracao_em_dias'] = olist['shipping_duration'].apply(mtc.formatar_timedelta_em_numero)
                
                mtc.line_metrics_time(olist[olist['product_category_name'] == categoria_escolhida].groupby('month/year_of_purchase', as_index=False)['duracao_em_dias'].mean(), 
                                  'duracao_em_dias', 'Média da duração da entrega')
        
















    # Gráficos de pizza na lateral ############################################################################################
    # -------------------------------------------------------------------------------------------------------------------------

    with col2:
        #Dados de entrada
        regioes = ['Sul','Sudeste','Centro-Oeste','Nordeste', "Norte"]
        populacao = [29933315, 84847187, 16287809, 54644582, 17349619]
        cores_marcadores = ["khaki", "MediumSeaGreen", "crimson", "limegreen", "tomato"]

        #Gráfico de Pizza
        fig = go.Figure(data = go.Pie(labels = regioes,
                                    values = populacao,
                                    marker_colors = cores_marcadores,
                                    hole = 0.5,
                                    pull = [0, 0, 0.15, 0, 0]))

        #Rótulos
        fig.update_traces(textposition = "outside", textinfo = "percent+label")

        #Legenda
        fig.update_layout(legend_title_text = "Regiões brasileiras",
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

        with st.expander("Click to expand"):
                st.write('ok')

        #Dados de entrada
        regioes = ['Sul','Sudeste','Centro-Oeste','Nordeste', "Norte"]
        populacao = [29933315, 84847187, 16287809, 54644582, 17349619]
        cores_marcadores = ["khaki", "MediumSeaGreen", "crimson", "limegreen", "tomato"]

        #Gráfico de Pizza
        fig = go.Figure(data = go.Pie(labels = regioes,
                                    values = populacao,
                                    marker_colors = cores_marcadores,
                                    hole = 0.5,
                                    pull = [0, 0, 0.15, 0, 0]))

        #Rótulos
        fig.update_traces(textposition = "outside", textinfo = "percent+label")

        #Legenda
        fig.update_layout(legend_title_text = "Regiões brasileiras",
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

        with st.expander("Click to expand"):
                st.write('ok')

    #st.write('---')

    #st.title(f'Análise dos produtos {total}')

