import streamlit as st

def data_filter(olist):

    # Aggiungi CSS personalizzato per impostare lo sfondo bianco
    st.markdown(
        """
        <style>
        .stApp {
            background-color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.image('streamlit_application/img/Commerce Illustrations/vctrly-business-illustrations-3-unboxing.png', width=150)
    st.title(f"Análise dos Pedidos")