import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

import utils.general as all
import utils.pedidos as pds
import utils.produtos as pdt
import utils.metrics as mtc
import streamlit_application.utils.about as abt

# App developer:     Enzo Schitini
# Date:              2 Outubro 2024
# https://www.notion.so/enzoschitini/Bozza-113b4721c6fd80f6b86cc94f63687086?pvs=4

# 📅 Compiti
# 🕗 
# Organizzare la cartella, si prega di crearne un'altra per questioni di sicurezza ✅   

# ⌛
# 

logo = 'https://raw.githubusercontent.com/enzoschitini/Data-Science-Portfolio/refs/heads/main/01%20An%C3%A1lise%20explorat%C3%B3ria%20e%20limpeza%20de%20dados/E-commerce%20Customer%20Data%20For%20Behavior%20Analysis/Image/olistlogo.png'
icon_page = 'streamlit_application/img/icone.png'

st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_title="Olist Insights", page_icon=icon_page)
# Recupera a senha do session_state ou define como '0' inicialmente
password = st.session_state.get('password', '0')

@st.cache_data
def load_data():
    olist = pd.read_csv('streamlit_application/data/Brazilian E-Commerce Public Dataset by Olist.csv').drop(columns='Unnamed: 0')
    return olist

# Load the data
olist = load_data() 

def periodo(olist):
    olist['order_purchase_timestamp'] = pd.to_datetime(olist['order_purchase_timestamp'])

    # Get the min and max dates and convert them to 'date' format
    max_data = olist['order_purchase_timestamp'].max().date()
    min_data = olist['order_purchase_timestamp'].min().date()

    # Date inputs in the sidebar, using 'date' format
    data_iniziale = st.sidebar.date_input('Data inicial',
                value=min_data,
                min_value=min_data,
                max_value=max_data)

    data_finale = st.sidebar.date_input('Data final',
                value=max_data,
                min_value=min_data,
                max_value=max_data)

    # Filter the DataFrame based on the selected date range
    olist = olist[(olist['order_purchase_timestamp'].dt.date >= data_iniziale) & (olist['order_purchase_timestamp'].dt.date <= data_finale)]
    return olist

def init():
    # Impostazioni della barra laterale
    st.sidebar.image(logo, width=150)
    st.sidebar.write('# E-Commerce Dashboard')
    st.sidebar.write('')  

    # 1. Sidebar menu
    with st.sidebar:
        selected = option_menu(
            menu_title="",  # required
            options=["Métricas Gerais", "Pedidos", "Produtos", "Mapa", "Avaliações", "Data Base", "Sobre"],  # required
            icons=["grid", "box", "bag", "map", "award", "database", "book"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            styles={
                "container": {"padding": "5!important", "background-color": "#f0f2f6"},
                "icon": {"color": "black", "font-size": "25px"},  # Default icon color
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "blue", "color": "white", "icon": "white"},  # Selected icon color to white
            }
        )

    def try_except(funcao, pacote, error):
        mtc.markdown("Ops!", "Desculpe, ocorreu um erro!",
                        f"Verifique a função {funcao} do pacote {pacote}.py", '#F8F8FF')

        st.write("""Ou fale com: [Enzo Schitini](https://www.linkedin.com/in/enzoschitini/)""")
        with st.expander("Relatório do erro"):
            st.write(error)

    if selected == "Métricas Gerais":
        st.image('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-220-work-on-computer.png', width=200)
        st.title(f"{selected} - Painel de controle Olist")
        try:
            all.general(olist)
        except Exception as error:
            try_except('all', 'general', error)


    if selected == "Pedidos":
        try:
            pds.metricas_pedidos(olist)
        except Exception as error:
            try_except('metricas_pedidos', 'pedidos', error)


    if selected == "Produtos":
        password = "1234"
        try:
            opcao = mtc.escolher_opcao_sidbar('Escolha como quer ver as categorias', ['Análise de uma categoria', 'Análise geral'])
            pdt.metricas_produtos(olist, opcao)
        except Exception as error:
            try_except('metricas_produtos', 'produtos', error)
        


    if selected == "Sobre":
        st.write(f"### {selected}")
        abt.about(olist)


    st.sidebar.write("""
    ---
    [Enzo Schitini](https://www.linkedin.com/in/enzoschitini/)
    """)

init()

def senha():
    # Se a senha ainda não for '1', exibe o texto e o campo de input
    if password != "1234":
        col1, col2 = st.columns(2)

        with col1:
            st.image(logo, width=200)
            st.write('')
            st.title('Bem Vindo(a) • E-Commerce Analysis')

            st.write('####  Número da senha: 1234')
            password = st.text_input("Insira o número da senha e clique enter:", key="password")

        with col2:
            st.image('streamlit_application/img/cover.png')
        
    else:
        # Senha correta, exibe mensagem de sucesso
        init()


    # Create the checkbox
    toggle = st.checkbox('Enable feature')

    # Check the state of the checkbox
    if toggle:
        st.write("The feature is enabled.")
    else:
        st.write("The feature is disabled.")

    # Inject custom CSS to change the color of the slider's bar
    st.markdown(
        """
        <style>
        /* Style for the slider track */
        div[data-baseweb="slider"] > div > div {
            background: #4561FF !important;  /* Set the color for the slider bar */
        }
        
        /* Style for the slider thumb */
        div[data-baseweb="slider"] > div > div > div {
            background-color: #4561FF !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


