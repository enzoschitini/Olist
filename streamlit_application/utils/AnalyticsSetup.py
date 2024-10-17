import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

#df['default_cat'] = df['default']
#df['default_cat'] = df['default_cat'].astype('object')

# Função para análise bivariada de variáveis numéricas
def AB2N(dataframe, x_coluna, y_coluna):
    tabela = dataframe.groupby(x_coluna)[y_coluna].mean().to_dict()
    fig = px.line(x=list(tabela.keys()), y=list(tabela.values()), 
                  title=f'Média de: {x_coluna} vs {y_coluna}', 
                  labels={'x': x_coluna, 'y': 'Média de ' + y_coluna})
    st.plotly_chart(fig)

# Função para análise bivariada entre variável categórica e numérica
def num_cat_analysis(dataframe, num_col, cat_col):
    fig = go.Figure()
    for cat in dataframe[cat_col].unique():
        filtered_data = dataframe[dataframe[cat_col] == cat][num_col]
        fig.add_trace(go.Box(
            y=filtered_data,
            name=cat,
            boxmean='sd',
            marker_color='rgba(255, 100, 102, 0.7)',
            line_color='rgba(255, 100, 102, 0.9)'
        ))
    fig.update_layout(
        title=f"Análise Bivariada: {num_col} por {cat_col}",
        xaxis_title=cat_col,
        yaxis_title=num_col,
        boxmode='group',
    )
    st.plotly_chart(fig)

# Função para análise bivariada entre variável categórica e numérica usando um gráfico de barras
def num_cat_analysis_bar(dataframe, num_col, cat_col):
    # Calcular a média da variável numérica para cada categoria
    mean_values = dataframe.groupby(cat_col)[num_col].mean().reset_index()

    # Criar o gráfico de barras
    fig = go.Figure(data=[
        go.Bar(
            x=mean_values[cat_col],  # Categorias no eixo x
            y=mean_values[num_col],  # Médias no eixo y
            marker_color='rgba(255, 100, 102, 0.7)',  # Cor das barras
            text=mean_values[num_col],  # Exibir valores como texto nas barras
            textposition='auto'  # Posição do texto
        )
    ])

    # Atualizar layout do gráfico
    fig.update_layout(
        title=f"Análise Bivariada: {num_col} por {cat_col}",
        xaxis_title=cat_col,
        yaxis_title=f"Média de {num_col}",
        yaxis=dict(tickformat=".2f")  # Formato dos ticks no eixo y
    )

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)

# Função para análise bivariada entre variáveis categóricas
def AB2C(dataframe, col1, col2, metric):
    if metric == 'qtd':
        title = 'Análise Bivariada de Variáveis Categóricas'
        yaxis_title = 'Frequência'
        crosstab = pd.crosstab(dataframe[col1], dataframe[col2])
    elif metric == 'prct':
        title = 'Análise Bivariada de Variáveis Categóricas'
        yaxis_title = 'Percentual %'
        crosstab = pd.crosstab(dataframe[col1], dataframe[col2], normalize='index')

    color_palette = [
        'blue', 'orange', 'green', 'red', 'purple', 'cyan', 'magenta', 'yellow', 'brown', 'pink',
        'lime', 'indigo', 'teal', 'navy', 'gold', 'silver', 'gray', 'lightblue', 'darkgreen', 'lightcoral',
        'coral', 'lightgreen', 'darkviolet', 'crimson', 'salmon', 'khaki', 'plum', 'wheat', 'lavender',
        'peachpuff', 'lightpink', 'lightyellow', 'mediumseagreen'
    ]

    colors = {col: color for col, color in zip(crosstab.columns, color_palette[:len(crosstab.columns)])}
    
    fig = go.Figure()

    for col in crosstab.columns:
        fig.add_trace(go.Bar(
            name=col,
            x=crosstab.index,
            y=crosstab[col],
            marker_color=colors.get(col, 'gray')
        ))

    fig.update_layout(
        title=title,
        xaxis_title=col1,
        yaxis_title=yaxis_title,
        barmode='stack',
        legend_title=col2,
    )
    st.plotly_chart(fig)
