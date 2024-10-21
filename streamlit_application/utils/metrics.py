import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
import locale

# App Developer:     Enzo Schitini -- Data Science
# Date:              2 Outubro 2024 -- 22 Outubro 2024

@st.cache_data
def formatar_numero_grande(numero):
    if numero >= 1_000_000_000:
        return f"{numero / 1_000_000_000:.1f} bilhões"
    elif numero >= 1_000_000:
        return f"{numero / 1_000_000:.1f} milhões"
    elif numero >= 1_000:
        return f"{numero / 1_000:.1f} mil"
    else:
        return str(numero)

def formatar_timedelta_em_portugues(td):
    # Extrair os dias, horas, minutos e segundos do Timedelta
    dias = td.days
    horas, resto = divmod(td.seconds, 3600)
    minutos, segundos = divmod(resto, 60)
    
    # Montar a string no formato desejado
    partes = []
    resumo = []
    if dias > 0:
        partes.append(f"{dias} Dias")
        resumo.append(f"{dias} Dias")
    if horas > 0:
        partes.append(f"{horas} Horas")
    if minutos > 0:
        partes.append(f"{minutos} Minutos")
    if segundos > 0:
        partes.append(f"{segundos} Segundos")
    
    return ' • '.join(partes), ''.join(resumo)

def formatar_timedelta_em_numero(td):
    # Extrair os dias, horas, minutos e segundos do Timedelta
    dias = td.days
    dias = int(dias)
    horas, resto = divmod(td.seconds, 3600)
    minutos, segundos = divmod(resto, 60)
    
    return dias

def markdown(text_01, text02, text_03, color):
    # Estilos personalizados usando HTML e CSS
    st.markdown(f"""
        <style>
        .custom-box {{
            border: 5px solid {color};
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
        .blue-bold {{
            color: blue;
            font-weight: bold;
        }}
        </style>
        <div class="custom-box">
            <h3><span class="blue-bold">{text_01}</span> {text02}</h3>
            <h5>{text_03}</h5>
        </div>
        """, unsafe_allow_html=True)

def markdown_pedidos(text_01, text02, text_03, text_04, text_05, text_06, color):
    # Estilos personalizados usando HTML e CSS
    st.markdown(f"""
        <style>
        .custom-box {{
            border: 5px solid {color};
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
        .blue-bold {{
            color: blue;
            font-weight: bold;
        }}
        </style>
        <div class="custom-box">
            <h3><span class="blue-bold">{text_01}</span> {text02}</h3>
            <h5>{text_03}</h5>
            <h5>{text_04}</h5>
            <h5>{text_05}</h5>
            <h5>{text_06}</h5>
        </div>
        """, unsafe_allow_html=True)

@st.cache_data
def grafico(olist):
    # Converter coluna de data para o formato datetime
    olist['order_purchase_timestamp'] = pd.to_datetime(olist['order_purchase_timestamp'])

    # Ordenar o DataFrame pela coluna de data
    olist = olist.sort_values(by='order_purchase_timestamp')

    # Criar o gráfico de linha usando Plotly
    fig = px.line(olist, x='order_purchase_timestamp', y='price', title='Lucro ao Longo do Tempo')

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)

@st.cache_data
def order_id(olist):
    # Definir o locale para português (Brasil)
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')  # Use 'pt_BR.UTF-8' para Linux/Mac e 'Portuguese_Brazil.1252' no Windows

    # Converter a coluna de data para o formato datetime
    olist['order_purchase_timestamp'] = pd.to_datetime(olist['order_purchase_timestamp'])

    # Agrupar os dados por mês e contar o número de pedidos (order_id)
    olist['month_year'] = olist['order_purchase_timestamp'].dt.to_period('M')  # Extrai ano-mês
    orders_per_month = olist.groupby('month_year').size().reset_index(name='order_count')

    # Converter o período para string no formato de mês em português
    orders_per_month['month_year'] = orders_per_month['month_year'].dt.strftime('%B %Y')  # Nome completo do mês em português

    # Criar o gráfico de linha usando Plotly
    fig = px.bar(orders_per_month, x='month_year', y='order_count', title='Quantidade de Pedidos por Mês')

    # Ajustar o layout do eixo x para exibir corretamente os nomes
    fig.update_layout(xaxis_title='Mês', yaxis_title='Quantidade de Pedidos')

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)

@st.cache_data
def boxplot(olist, col):
    # Calcola i limiti per gli outliers usando IQR
    Q1 = olist[col].quantile(0.25)
    Q3 = olist[col].quantile(0.75)
    IQR = Q3 - Q1

    # Limiti per definire gli outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Filtra i dati per escludere gli outliers
    df_filtered = olist[(olist[col] >= lower_bound) & (olist[col] <= upper_bound)]

    # Configura il grafico
    plt.figure(figsize=(12, 12))

    # Crea boxplot per le colonne numeriche senza outliers
    sns.boxplot(data=df_filtered[[col]])

    # Aggiungi titolo e etichette
    plt.title('Boxplot (Sem Outliers)')
    plt.ylabel('Valor')
    #plt.xlabel('')

    # Mostra il grafico
    st.pyplot(plt)

@st.cache_data
def grafico_categoria(coluna: str, dataframe, titolo):
    # Contar a frequência de cada categoria na coluna
    coluna_dic = dataframe[coluna].value_counts().to_dict()
    
    # Criar o gráfico de barras
    fig = px.bar(
        x=list(coluna_dic.values()), 
        y=list(coluna_dic.keys()), 
        orientation='h',  # Coloca o gráfico na horizontal
        title=titolo,
        labels={'x': 'Frequência', 'y': coluna},  # Renomeia os eixos
        color=list(coluna_dic.keys()),  # Colore as barras por categoria
        color_discrete_sequence=px.colors.qualitative.Set2  # Melhora a paleta de cores
    )
    
    # Ajuste da formatação do layout
    fig.update_layout(
        xaxis_title='Frequência',
        yaxis_title=coluna,
        title_x=0.5,  # Centraliza o título
        template='plotly_white',  # Aplica um layout mais limpo
        yaxis=dict(categoryorder='total ascending')  # Ordena as categorias pelo valor
    )
    
    # Exibir o gráfico
    st.plotly_chart(fig)

def escolher_opcao(pergunta, opcoes):
    resposta = st.selectbox(pergunta, opcoes)
    return resposta

def escolher_opcao_sidbar(pergunta, opcoes):
    resposta = st.sidebar.selectbox(pergunta, opcoes)
    return resposta

# Avaliação das categorias com uma fórmula

def avaliar_categoria(valor_total_vendas, total_vendas, nota_media, taxa_frete, valor_medio_frete, preco_medio):
    # Cálculos dos componentes de desempenho
    g1 = (valor_total_vendas / total_vendas) * nota_media
    g2 = taxa_frete + valor_medio_frete
    g3 = 1 / preco_medio

    # Desempenho bruto
    desempenho = g1 - g2 + g3

    # Ajuste no normalizador com um P_max maior
    P_min = 0  # Pontuação mínima
    P_max = 2000  # Aumentado para refletir melhor os valores de desempenho

    # Normalizando o valor para uma escala de 0 a 100
    normalizador = ((desempenho - P_min) / (P_max - P_min)) * 100

    return round(normalizador, 2)

@st.cache_data
def line_metrics_time(sales_data, categoria, title):
    # Rename the column 'month/year_of_purchase' to 'year_month' if needed
    sales_data.rename(columns={'month/year_of_purchase': 'year_month'}, inplace=True)

    # Convert 'year_month' to datetime format, allowing pandas to infer the format  
    sales_data['year_month'] = pd.to_datetime(sales_data['year_month'], format='mixed', errors='coerce')

    # Check for any NaT values after conversion
    if sales_data['year_month'].isna().sum() > 0:
        st.write("Warning: Some dates couldn't be parsed and have been set to NaT.")

    # Sort the data by 'year_month'
    sales_data = sales_data.sort_values('year_month')

    # Create the line plot
    fig = px.line(sales_data, 
                x='year_month', 
                y=categoria, 
                title=title,
                labels={'year_month': 'Mês/Ano', categoria: f'Valor {categoria}'},
                markers=True,
                template='ygridoff') 
    
    # plotly_white plotly_dark plotly ggplot2 seaborn simple_white presentation xgridoff ygridoff none

    # Update y-axis for currency format
    fig.update_yaxes(tickprefix="")

    # Optional: Add grid lines
    fig.update_layout(xaxis=dict(showgrid=True), yaxis=dict(showgrid=True))

    # Display in Streamlit
    st.plotly_chart(fig)

@st.cache_data
def grafico_pizza_rank(olist, coluna, title, calcolo):
    # Agrupar as categorias e somar o valor de pagamento
    if calcolo == 'sum':
        grouped = olist.groupby('product_category_name')[coluna].sum().reset_index()
    if calcolo == 'count':
        grouped = olist.groupby('product_category_name')[coluna].count().reset_index()

    # Ordenar pela soma de payment_value
    grouped = grouped.sort_values(by=coluna, ascending=False)

    # Definir quantas categorias principais serão mantidas (exemplo: 5)
    top_n = 6
    top_categories = grouped[:top_n]
    other_categories = grouped[top_n:]

    # Calcular a soma dos "outros"
    if calcolo == 'sum':
        other_sum = other_categories[coluna].sum()
    if calcolo == 'count':
        other_sum = other_categories[coluna].count()

    # Adicionar a categoria "outros"
    other_row = pd.DataFrame({'product_category_name': ['outros'], coluna: [other_sum]})
    top_categories = pd.concat([top_categories, other_row], ignore_index=True)

    # Definir cores para as categorias
    cores_marcadores = ["khaki", "MediumSeaGreen", "crimson", "limegreen", "tomato", "lightgrey"]

    # Criar o gráfico de pizza do tipo donut
    fig = go.Figure(data=go.Pie(labels=top_categories['product_category_name'],
                                values=top_categories[coluna],
                                marker_colors=cores_marcadores,
                                hole=0.5,  # Buraco central
                                pull=[0.10, 0.10, 0.10, 0.10, 0.10, 0.10]))  # Destaque na terceira categoria

    # Rótulos fora da pizza com percentuais e nome da categoria
    fig.update_traces(textposition="outside", textinfo="percent+label")

    # Legenda e título
    fig.update_layout(legend_title_text="Categorias de Produtos",
                    legend=dict(orientation="h", xanchor="auto", x=0.5),
                    title=title)

    # Texto no centro do gráfico
    fig.update_layout(annotations=[dict(text="Percentual", x=0.5, y=0.5, font_size=18, showarrow=False)])

    # Exibir o gráfico
    st.plotly_chart(fig)

def espaco():
    st.write('')
    st.write('---')
    st.write('')

@st.cache_data
def partes(olist, coluna):
    olist['order_purchase_timestamp'] = pd.to_datetime(olist['order_purchase_timestamp'])
    # Assuming olist DataFrame is already defined and 'order_purchase_timestamp' is in datetime format
    # Extract year and month
    olist['year_month'] = olist['order_purchase_timestamp'].dt.to_period('M')

    # Calculate monthly statistics
    monthly_stats = olist.groupby('year_month')[coluna].agg(['mean', lambda x: x.quantile(0.25), 
                                                                lambda x: x.quantile(0.5), 
                                                                lambda x: x.quantile(0.75)]).reset_index()
    monthly_stats.columns = ['year_month', 'mean', '25%', '50%', '75%']

    # Create the Plotly figure
    fig = go.Figure()

    # Add traces for mean and percentiles
    fig.add_trace(go.Scatter(x=monthly_stats['year_month'].astype(str), 
                            y=monthly_stats['mean'], 
                            mode='lines+markers', 
                            name='Média'))

    fig.add_trace(go.Scatter(x=monthly_stats['year_month'].astype(str), 
                            y=monthly_stats['25%'], 
                            mode='lines+markers', 
                            name='25%', 
                            line=dict(dash='dash')))

    fig.add_trace(go.Scatter(x=monthly_stats['year_month'].astype(str), 
                            y=monthly_stats['50%'], 
                            mode='lines+markers', 
                            name='50%', 
                            line=dict(dash='dash')))

    fig.add_trace(go.Scatter(x=monthly_stats['year_month'].astype(str), 
                            y=monthly_stats['75%'], 
                            mode='lines+markers', 
                            name='75%', 
                            line=dict(dash='dash')))

    # Update layout
    fig.update_layout(title=f'Quartis da coluna {coluna}',
                    xaxis_title='Meses',
                    yaxis_title=coluna,
                    xaxis_tickangle=-45,
                    legend_title='Estatísticas',
                    template='plotly_white')

    # Show the figure
    st.plotly_chart(fig)