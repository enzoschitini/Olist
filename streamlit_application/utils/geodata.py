import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

import utils.metrics as mtc

def maps(olist, opcao):

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

    geo = pd.read_csv('streamlit_application/data/olist_geolocation_dataset.csv')

    olist = pd.DataFrame(olist)
    olist['geolocation_zip_code_prefix'] = olist['customer_zip_code_prefix']

    #st.write(olist[['geolocation_zip_code_prefix', 'order_id', 'customer_zip_code_prefix', 'customer_state', 'customer_city', 'customer_zone', 
                    #'seller_zip_code_prefix', 'seller_city', 'seller_state', 'seller_zone']])

    
    customer_zip_code_prefix = olist['customer_zip_code_prefix'].to_list()
    geolocation_zip_code_prefix = geo['geolocation_zip_code_prefix'].to_list()
    #st.write(geo) # geolocation_zip_code_prefix

    def grafico_radar():
        # Definisci i dati
        categorie = ['A', 'B', 'C', 'D', 'E']
        valori = [4, 3, 2, 5, 4]

        # Creazione del grafico radar
        fig = go.Figure()

        # Aggiungi il tracciato per il valore
        fig.add_trace(go.Scatterpolar(
            r=valori + [valori[0]],  # Aggiungi il primo valore alla fine per chiudere il grafico
            theta=categorie + [categorie[0]],  # Aggiungi la prima categoria alla fine per chiudere il grafico
            fill='toself',
            name='Valori'
        ))

        # Aggiungi annotazioni al grafico
        fig.update_layout(
            annotations=[
                dict(
                    text="Valori delle Categorie",  # Testo che desideri visualizzare
                    x=0.5,  # Posizione x (0-1)
                    y=1.2,  # Posizione y (0-1), sopra il grafico
                    showarrow=False,
                    font=dict(size=16, color="black")
                )
            ],
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 5]  # Definisci l'intervallo degli assi radiali
                )
            ),
            showlegend=True,
        )

        # Mostra il grafico nell'app Streamlit
        st.plotly_chart(fig)

    def grafico_barra(regioes, valores):
        # Creazione del grafico con barre principali e etichette
        fig = go.Figure(
            data=[
                go.Bar(
                    x=list(regioes),  # Specifica i dati x come colonna 'Mesi'
                    y=list(valores),  # Specifica i dati y come colonna 'Vendite'
                    marker_color='#4561FF',  # Colore delle barre
                    text=list(valores),  # Aggiunta dei valori delle vendite
                    textposition='outside',  # Posizione del testo sopra la barra
                    texttemplate='%{text}',  # Formattazione del testo
                    width=0.6  # Larghezza delle barre
                )
            ]
        )

        # Personalizzazione del layout
        fig.update_layout(
            title='Vendite Mensili con Etichette',
            xaxis_title='Mese',
            yaxis_title='Numero di Vendite',
            template='ygridoff'  # Tema del grafico (opzionale)
        )

        # Mostra il grafico in Streamlit
        st.plotly_chart(fig)

    def grafico_linea(meses, listas, territorios):
        # Creazione del grafico di linea
        fig = go.Figure()

        # Lista di colori
        colori = ['blue', 'green', 'red', 'orange', 'purple', 'pink', 'cyan', 'magenta', 'yellow', 'brown']
        
        # Loop su entrambe le liste
        for idx, (x, terra) in enumerate(zip(listas, territorios)):
            # Seleziona un colore dall'elenco, usa l'indice modulato per evitare IndexError
            colore = colori[idx % len(colori)]
            
            # Aggiunta della linea
            fig.add_trace(go.Scatter(
                x=meses,  # Asse x
                y=x,  # Asse y
                mode='lines+markers',  # Modalità di visualizzazione: linea e marcatori
                line=dict(color=colore, width=2),  # Colore e larghezza della linea
                marker=dict(size=8),  # Dimensione dei marcatori
                name=f'{terra}'  # Nome della traccia
            ))

        # Personalizzazione del layout
        fig.update_layout(
            title='Confronto Vendite Mensili',
            xaxis_title='Mese',
            yaxis_title='Numero di Vendite',
            template='ygridoff',  # Tema del grafico (opzionale)
            legend=dict(x=0, y=1)  # Posizione della legenda
        )

        # Mostra il grafico in Streamlit
        st.plotly_chart(fig)
    
    st.image('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-4.png', width=150)
    st.title(f"Análise Geográfica - {opcao}")
    st.write('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-4.png')
    st.write('')



















    if opcao == 'Geral':
        col1, col2 = st.columns([1.5, 2])
        with col1:
            capitais_vendedores = olist['seller_city'].nunique()
            capitais_clientes = olist['customer_city'].nunique()
            
            mtc.markdown(mtc.formatar_numero_grande(capitais_clientes), ' de cidades compradoras', 
                    f'{mtc.formatar_numero_grande(capitais_vendedores)} cidades com pontos de venda', '#F8F8FF')
        with col2:
            col01, col02, col03 = st.columns(3)
            with col01:
                coluna = mtc.escolher_opcao('Fator', list(olist.select_dtypes('number').columns))
            with col02:
                metrica = mtc.escolher_opcao('Métrica', ['Quantidade', 'Média'])
            with col03:
                territorio = mtc.escolher_opcao('Território', ['Estado', 'Região'])

            def calc(coluna, metrica, territorio):
                if territorio == 'Região':
                    territorio = 'customer_zone'
                if territorio == 'Estado':
                    territorio = 'customer_state'

                if metrica == 'Quantidade':
                    regioes = olist.groupby(territorio)[coluna].sum().to_dict().keys()
                    valores = round(olist.groupby(territorio)[coluna].sum(), 2).to_dict().values()

                if metrica == 'Média':
                    regioes = olist.groupby(territorio)[coluna].mean().to_dict().keys()
                    valores = round(olist.groupby(territorio)[coluna].mean(), 2).to_dict().values()

                return regioes, valores
            
            regioes, valores = calc(coluna, metrica, territorio)
            grafico_barra(regioes, valores)

        col1, col2 = st.columns([1, 3])
        with col1:
            territorio_escolhido = mtc.escolher_opcao('', ['Estado', 'Região'])

            if territorio_escolhido == 'Estado':
                colonne_selezionate = mtc.multiselect(list(olist['customer_state'].unique()), 'Selecione o território')
                vetor = 'customer_state'
            elif territorio_escolhido == 'Região':
                colonne_selezionate = mtc.multiselect(list(olist['customer_zone'].unique()), 'Selecione o território')
                vetor = 'customer_zone'

        def ordem(sales_data, dic):
            # Rename the column 'month/year_of_purchase' to 'year_month' if needed
            sales_data.rename(columns={'month/year_of_purchase': 'year_month'}, inplace=True)

            # Convert 'year_month' to datetime format, allowing pandas to infer the format  
            sales_data['year_month'] = pd.to_datetime(sales_data['year_month'], format='mixed', errors='coerce')

            # Sort the data by 'year_month'
            sales_data = sales_data.sort_values('year_month')
            sales_data['month/year_of_purchase'] = sales_data['month_of_purchase'].astype(str) + '-' + sales_data['year_of_purchase'].astype(str)

            sales_data = list(sales_data['month/year_of_purchase'].unique())

            dic_ordinato = {key: dic.get(key, 0) for key in sales_data}

            return sales_data, dic_ordinato
        
        with col2:
            #st.write(ordem(olist, olist.groupby('month/year_of_purchase')['price'].mean().to_dict()))[0]

            tempo_em_ordem = ordem(olist.copy(), olist.groupby('month/year_of_purchase')['price'].mean().to_dict())[1].keys()
            traces = []

            for x in colonne_selezionate:
                linea = list(ordem(olist.copy(), 
                                olist[olist[vetor] == x].groupby('month/year_of_purchase')['price'].mean().to_dict())[1].values())
                
                traces.append(linea)
            
            grafico_linea(list(tempo_em_ordem), traces, colonne_selezionate)
            
            
            
            #st.write(ordem(olist, olist.groupby('month/year_of_purchase')['price'].mean().to_dict())[0])















    if opcao == 'Pontos de venda':
        col1, col2 = st.columns([1, 3])
        with col1:
            pass
        with col2:
            fig = go.Figure()

            fig.add_bar(x=['Data1', 'Data2', 'Data3'], y=[3, 5, 9], 
                        name='Atividade dos usuários', marker_color='turquoise')# violet turquoise wheat yellowgreen
            fig.add_bar(x=['Data1', 'Data2', 'Data3'], y=[2, 7, 6], 
                        name='Novos usuários', marker_color='yellowgreen')

            fig.update_layout(plot_bgcolor = "white", barmode='group', xaxis_title='Usuários', yaxis_title='Valore')
            st.plotly_chart(fig)














    if opcao == 'Comparar regiões':
        col1, col2, col3 = st.columns(3)
        with col1:
            grafico_radar()
        with col2:
            grafico_radar()
        with col3:
            grafico_radar()

        col1, col2, col3 = st.columns(3)
        with col1:
            grafico_radar()
        with col2:
            grafico_radar()
        with col3:
            grafico_radar()   

    #st.write()

    




















































    # Supponiamo di avere un DataFrame con le colonne 'latitudine', 'longitudine', e 'tipo' (venditore o cliente)
    data = {
        'latitudine': [-23.5505, -22.9068, -15.8267, -19.9167, -3.1190, -8.0476],
        'longitudine': [-46.6333, -43.1729, -47.9218, -43.9345, -60.0217, -34.8770],
        'tipo': ['vendedor', 'cliente', 'vendedor', 'cliente', 'vendedor', 'cliente']
    }

    df = pd.DataFrame(data)

    olist_cliente = olist['customer_zip_code_prefix'].to_list()
    olist_cliente = olist_cliente[:10]
    #st.write(olist_cliente)

    olist_vendedor = olist['seller_zip_code_prefix'].to_list()
    olist_vendedor = olist_vendedor[:10]
    #st.write(olist_vendedor)

    # Creiamo il grafico con Plotly Express
    fig = px.scatter_mapbox(df, 
                            lat='latitudine', 
                            lon='longitudine', 
                            color='tipo', 
                            mapbox_style='open-street-map', 
                            title="Mappa dei venditori e clienti",
                            zoom=1)

    # Mostriamo il grafico
    #st.plotly_chart(fig)



