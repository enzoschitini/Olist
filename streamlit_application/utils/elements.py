import streamlit as st

# App Developer:     Enzo Schitini -- Data Science
# Date:              2 Outubro 2024 -- 22 Outubro 2024

def grupo_azul(titolo): # width: 300px;
    # Define HTML and CSS
    html_code = f"""
        <style>
            .container {{
                background-color: #4561FF;
                padding: 20px;
                
                text-align: center;
                border: 10px solid #93C5FD;
                font-family: Arial, sans-serif;
                color: white;
                border-radius: 8px;
            }}
            .container h1 {{
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 10px;
            }}
            .container p {{
                font-size: 16px;
                margin-bottom: 20px;
            }}
            .btn {{
                font-size: 16px;
                padding: 10px 20px;
                margin: 10px;
                border: none;
                cursor: pointer;
                border-radius: 5px;
            }}
            .btn-download {{
                background-color: white;
                color: #4561FF;
            }}
            .btn-signin {{
                background-color: transparent;
                color: white;
                border: 1px solid white;
            }}
            .btn:hover {{
                opacity: 0.8;
            }}
        </style>
        <div class="container">
            <h1>{titolo}</h1>
            <p>Download illustrations about business</p>
        </div>
    """

    # Display HTML in Streamlit
    st.components.v1.html(html_code, height=180)

  
def out():
        # Define the HTML and CSS code
        html_code3 = """
            <style>
                .portfolio-container {
                    text-align: left;
                    padding: 20px;
                    font-family: Arial, sans-serif;
                }
                .portfolio-title {
                    font-size: 22px;
                    font-weight: bold;
                }
                .portfolio-subtitle {
                    font-size: 16px;
                    color: #333;
                    margin-bottom: 20px;
                }
                .grid-container {
                    display: grid;
                    grid-template-columns: repeat(2, 1fr);
                    gap: 20px;
                }
                .grid-item {
                    text-align: center;
                }
                .grid-item img {
                    width: 100%;
                    border-radius: 10px;
                }
                .grid-item p {
                    font-size: 14px;
                    font-weight: bold;
                    margin: 10px 0 5px 0;
                }
                .grid-item span {
                    font-size: 12px;
                    color: gray;
                }
            </style>

            <div class="portfolio-container">
                <p class="portfolio-title">Our Portfolio</p>
                <p class="portfolio-subtitle">
                    We envision a world where every idea, product, or service is brought to life through exceptional design.
                </p>
                <div class="grid-container">
                    <div class="grid-item">
                        <img src="https://via.placeholder.com/300x200.png?text=App+1" alt="App 1">
                        <p>Daily App</p>
                        <span>Increasing your productivity</span>
                    </div>
                    <div class="grid-item">
                        <img src="https://via.placeholder.com/300x200.png?text=App+2" alt="App 2">
                        <p>Daily App</p>
                        <span>Increasing your productivity</span>
                    </div>
                    <div class="grid-item">
                        <img src="https://via.placeholder.com/300x200.png?text=App+3" alt="App 3">
                        <p>Daily App</p>
                        <span>Increasing your productivity</span>
                    </div>
                    <div class="grid-item">
                        <img src="https://via.placeholder.com/300x200.png?text=App+4" alt="App 4">
                        <p>Daily App</p>
                        <span>Increasing your productivity</span>
                    </div>
                </div>
            </div>
        """

        # Display the HTML and CSS in Streamlit
        st.components.v1.html(html_code3, height=700)

        html_code2 = """
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <title>Good Design is Good Business</title>
                        <style>
                        body {
                            font-family: Arial, sans-serif;
                            text-align: center;
                            background-color: #2ecc71; /* Verde simile all'immagine */
                            margin: 0;
                        }

                        h1 {
                            color: #fff;
                            font-size: 36px;
                            margin-top: 50px;
                        }

                        p {
                            color: #fff;
                            font-size: 20px;
                            margin-top: 20px;
                        }

                        button {
                            background-color: #fff;
                            color: #2ecc71;
                            border: none;
                            padding: 15px 32px;
                            text-align: center;
                            text-decoration: none;
                            display: inline-block;
                            font-size: 16px;
                            margin: 4px 2px;
                            cursor: pointer;
                        }
                        </style>
                    </head>
                    <body>
                        <h1>Good   
                    Design is Good Business</h1>
                        <p>Download illustrations about business</p>
                        <button>Download</button>
                        <button>Sign In</button>
                    </body>
                    </html>

                    """
        st.components.v1.html(html_code2)



        # Circolo

        # HTML e CSS per creare l'elemento circolare allineato a sinistra con distanza tra il cerchio e il testo sotto
        st.markdown(
            f"""
            <div style="display: flex; flex-direction: column; align-items: flex-start;">
                <div style="width: 150px; height: 150px; background-color: #2563EB; border-radius: 50%; border: 10px solid #93C5FD;">
                    <p style="font-size: 30px; color: white; text-align: center; line-height: 130px; margin: 0;">dd</p>
            """,
            unsafe_allow_html=True
        )