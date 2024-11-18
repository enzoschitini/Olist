import streamlit as st

# App Developer:     Enzo Schitini -- Data Science
# Date:              2 Outubro 2024 -- 22 Outubro 2024

schema = 'https://raw.githubusercontent.com/enzoschitini/Data-Science-Portfolio/refs/heads/main/01%20An%C3%A1lise%20explorat%C3%B3ria%20e%20limpeza%20de%20dados/E-commerce%20Customer%20Data%20For%20Behavior%20Analysis/Image/Schema.png'
copertina = 'img/cover.png'

@st.cache_data
def about(olist):

    st.write("""

# **Olist Insights** • Análise de Dados do E-commerce
---
## **Identificando Oportunidades de Crescimento e Melhoria Através da Exploração de Dados de Vendas**

*Diz algorítimo de Machine Learning • 03 Junho 2024*
Uma pesquisa abrangente sobre tendências demográficas e de saúde em 2019 no estado de Rondônia, no Brasil. Comecemos por analisar os dados do sistema de informação sobre nascidos vivos (SINASC), o objetivo é realizar uma análise aprofundada do tema, este projeto visa encontrar ideias e responder a uma série de questões cruciais.

**Data Science** Portfólio | *27 Abril 2024* - *03 junho 2024*

[Enzo Schitini](https://www.linkedin.com/in/enzoschitini/) - Data Scientist • Expert Bubble.io • UX & UI @ Nugus creator

##

Este projeto visa analisar dados de um e-commerce, com o objetivo de identificar padrões de comportamento do cliente, tendências de mercado e oportunidades de otimização. Através da exploração de dados, pretende-se obter insights valiosos sobre a performance da plataforma, a satisfação do cliente e os fatores que influenciam o sucesso das vendas. A análise abrangerá diversos aspectos, desde a análise de produtos mais vendidos até a identificação de gargalos no processo de entrega, passando pela análise de comportamento do cliente e a segmentação de público. https://github.com/enzoschitini/Data-Science-Portfolio

---

![](https://raw.githubusercontent.com/enzoschitini/Olist/refs/heads/streamlit/img/cover.png)

### O que você vai encontrar nesta análise? 👋

Vamos explorar os dados do *Sistema de Informação sobre Nascidos Vivos (SINASC)* relativos aos recém-nascidos nascidos no estado de Rondônia, Brasil, no ano de 2019. Assim que a análise exploratória for concluída, prosseguiremos para identificar insights e avaliar a saúde pública no estado.

Usaremos abordagens estatísticas e analíticas para identificar correlações, padrões e associações entre variáveis, além disso vamos criar um Modelo de Machine Learning para fazer inferências de dados faltantes.

### Os pilares da análise:

- Descobrir os fatores que influenciam a saúde dos bebês.
- Entender melhor as raças e o nível educacional das mães.
- Analisaremos as menores de idade, meninas que constroem família antes dos 18 anos.
- O que nos diz a escolha do parto entre cesariana ou parto vaginal?
- E finalmente melhor compreender a população do estado de Rondônia no Brasil em 2019 e construir a um pouco do que seria o 'Rosto da população'.

> Além disso, exploraremos o impacto das variáveis sociorraciais nas condições de nascimento e nos indivíduos
> 

---

### Contexto dos Dados do SINASC em Rondônia - 2019

O Sistema de Informação sobre Nascidos Vivos (SINASC) é uma base de dados administrada pelo Ministério da Saúde do Brasil, que tem como objetivo coletar e disponibilizar informações detalhadas sobre todos os nascimentos ocorridos no país. No âmbito do estado de Rondônia, o SINASC fornece dados abrangentes e específicos sobre os nascimentos ocorridos no ano de 2019, sendo uma fonte crucial para análises de saúde pública, planejamento e avaliação de políticas sociais.

### Origem dos Dados

Os dados utilizados neste projeto foram extraídos do portal do governo, mais precisamente do Departamento de Informática do SUS (DATASUS). Essa instituição é responsável pela coleta, armazenamento e divulgação das informações de saúde no Brasil, garantindo a integridade e a precisão dos dados disponibilizados.

O conjunto de dados pode ser encontrado no site do governo brasileiro e segue políticas de privacidade, o que significa que não há nomes de pessoas ou qualquer coisa que nos permita saber quem são os indivíduos.

![](https://media.licdn.com/dms/image/v2/D5612AQE76Xz3ennuWg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721183271678?e=1735776000&v=beta&t=32OR12vK97itnlRHz60ogvc_GfHg3Dh-SvHGZCgr00Q)

### Metodologia

A análise será conduzida utilizando técnicas estatísticas e de visualização de dados para identificar padrões e anomalias. Será empregado o Python como ferramentas de manipulação e análise dos dados, na limpeza e preparação dos dados para garantir a qualidade das análises e do modelo de Machine Learning.

### Importância do Projeto

A análise dos dados do SINASC para Rondônia em 2019 é vital para entender melhor as condições de nascimento e saúde materno-infantil no estado. As informações derivadas desse estudo podem auxiliar gestores públicos, pesquisadores e profissionais de saúde na tomada de decisões informadas, visando a melhoria contínua dos serviços de saúde e o bem-estar da população.

Ao fornecer uma visão detalhada sobre os nascimentos, este projeto contribui para um entendimento mais profundo das dinâmicas de saúde e demografia de Rondônia, promovendo ações mais eficazes e direcionadas no campo da saúde pública.

## 🔥 Vamos começar!!!

![](https://media.licdn.com/dms/image/v2/D5612AQGTWZtZzbXyHA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721195567492?e=1735776000&v=beta&t=9vLZBrov8c6Xs2WIlOg6pPPmMZFU5lhejHq_a9XbDto)

## Como a análise será realizada:

![](https://media.licdn.com/dms/image/v2/D5612AQEyNedMIW7yaQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1721179457444?e=1735776000&v=beta&t=lX72CYo5yDTjJmgFN5Nj7aH7UcsKH9y-gIK87v4TLkE)

## O rosto da sociedade

### Nascimentos no ano de 2019:

![](https://media.licdn.com/dms/image/v2/D5612AQEACiw9c_fGEw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721178996817?e=1735776000&v=beta&t=VINzROK-UnpHQz-y9qwmnIh5qViBVjT2GcynUUAXih8)

O gráfico mostra a quantidade de nascimentos ao longo do ano de 2019 em Rondônia. O gráfico apresenta flutuações ao longo do ano, com vários picos e vales. Isso sugere que a quantidade de nascimentos variou mês a mês. Os meses com os maiores picos podem indicar períodos de maior atividade de nascimentos, enquanto os vales podem representar momentos de menor atividade.

- **Padrões Sazonais:** Pode ser interessante investigar se existem padrões sazonais. Por exemplo, ***há mais nascimentos em determinadas estações do ano?*** Esses padrões podem estar relacionados a fatores como clima, feriados ou eventos culturais.
- **Eventos Específicos:** Podemos verificar se algum evento específico (como feriados ou datas comemorativas) está correlacionado com os picos de nascimentos.

**Impacto na Saúde Pública:** Essa análise pode ajudar a avaliar a demanda por serviços de saúde materna e neonatal em diferentes momentos do ano. Também pode fornecer insights sobre recursos necessários para atender a essas demandas.

    """)













    st.write("""

### [ACESSE O PROJETO >>>](https://www.kaggle.com/code/enzoschitini/sinasc-estado-de-rond-nia-em-2019#Projeto-de-An%C3%A1lise-e-Ci%C3%AAncia-de-Dados-com-Machine-Learning)

<img src="https://raw.githubusercontent.com/enzoschitini/Data-Science-Portfolio/main/01%20An%C3%A1lise%20explorat%C3%B3ria%20e%20limpeza%20de%20dados/Sinasc/image/Copetina.png" alt="capa">

---

# **SINASC** • Sistema de Informação sobre Nascidos Vivos
---
## **Quase 12% dos partos registrados no estado de Rondônia em 2019 foram adolescentes grávidas com marido maior de idade!**

*Diz algorítimo de Machine Learning • 03 Junho 2024*
Uma pesquisa abrangente sobre tendências demográficas e de saúde em 2019 no estado de Rondônia, no Brasil. Comecemos por analisar os dados do sistema de informação sobre nascidos vivos (SINASC), o objetivo é realizar uma análise aprofundada do tema, este projeto visa encontrar ideias e responder a uma série de questões cruciais.

**Data Science** Portfólio | *27 Abril 2024* - *03 junho 2024*

[Enzo Schitini](https://www.linkedin.com/in/enzoschitini/) - Data Scientist • Expert Bubble.io • UX & UI @ Nugus creator

### • [GitHub](https://github.com/enzoschitini/Data-Science-Portfolio/blob/main/01%20An%C3%A1lise%20explorat%C3%B3ria%20e%20limpeza%20de%20dados/Sinasc/Sinasc.ipynb)
### • [Kaggle - 🤰 Sinasc • Estado de Rondônia em 2019](https://www.kaggle.com/code/enzoschitini/sinasc-estado-de-rond-nia-em-2019#Projeto-de-An%C3%A1lise-e-Ci%C3%AAncia-de-Dados-com-Machine-Learning)
### • [Artigo no Linkedin](https://www.linkedin.com/pulse/sinasc-sistema-de-informa%2525C3%2525A7%2525C3%2525A3o-sobre-nascidos-vivos-enzo-schitini-vvvsc/?trackingId=tuJlf8rZRkOGZK96w9J2TA%3D%3D)

---

**Bem-vindo(a)!!!** Meu nome é [Enzo Schitini](https://www.linkedin.com/in/enzoschitini/) , sou cientista de dados e fiz algumas pesquisas sobre os dados do SINASC [GOVERNANÇABRASIL - GOVBR](https://www.linkedin.com/company/governancabrasil/) no estado de *Rondônia (BR) no ano de 2019.*

O meu objetivo era realizar uma análise aprofundada do tema, encontrar padrões nos dados e conectar à realidade. Definitivamente um dos projetos em que mais me esforcei para obter bons resultados, espero que você, assim como eu, ache interessante.

Link do projeto no Kaggle com os códigos: [🤰 Sinasc • Estado de Rondônia em 2019 (](https://www.kaggle.com/code/enzoschitini/sinasc-estado-de-rond-nia-em-2019)[kaggle.com](http://kaggle.com/)[)](https://www.kaggle.com/code/enzoschitini/sinasc-estado-de-rond-nia-em-2019)

---

![](https://media.licdn.com/dms/image/v2/D4D12AQH4GQbvIhIgWg/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1721194113117?e=1735776000&v=beta&t=wMGiFS3JWy09TtaegcOaM3fYm-CSOw2FqrOv-funOnQ)

### O que você vai encontrar nesta análise? 👋

Vamos explorar os dados do *Sistema de Informação sobre Nascidos Vivos (SINASC)* relativos aos recém-nascidos nascidos no estado de Rondônia, Brasil, no ano de 2019. Assim que a análise exploratória for concluída, prosseguiremos para identificar insights e avaliar a saúde pública no estado.

Usaremos abordagens estatísticas e analíticas para identificar correlações, padrões e associações entre variáveis, além disso vamos criar um Modelo de Machine Learning para fazer inferências de dados faltantes.

### Os pilares da análise:

- Descobrir os fatores que influenciam a saúde dos bebês.
- Entender melhor as raças e o nível educacional das mães.
- Analisaremos as menores de idade, meninas que constroem família antes dos 18 anos.
- O que nos diz a escolha do parto entre cesariana ou parto vaginal?
- E finalmente melhor compreender a população do estado de Rondônia no Brasil em 2019 e construir a um pouco do que seria o 'Rosto da população'.

> Além disso, exploraremos o impacto das variáveis sociorraciais nas condições de nascimento e nos indivíduos
> 

---

### Contexto dos Dados do SINASC em Rondônia - 2019

O Sistema de Informação sobre Nascidos Vivos (SINASC) é uma base de dados administrada pelo Ministério da Saúde do Brasil, que tem como objetivo coletar e disponibilizar informações detalhadas sobre todos os nascimentos ocorridos no país. No âmbito do estado de Rondônia, o SINASC fornece dados abrangentes e específicos sobre os nascimentos ocorridos no ano de 2019, sendo uma fonte crucial para análises de saúde pública, planejamento e avaliação de políticas sociais.

### Origem dos Dados

Os dados utilizados neste projeto foram extraídos do portal do governo, mais precisamente do Departamento de Informática do SUS (DATASUS). Essa instituição é responsável pela coleta, armazenamento e divulgação das informações de saúde no Brasil, garantindo a integridade e a precisão dos dados disponibilizados.

O conjunto de dados pode ser encontrado no site do governo brasileiro e segue políticas de privacidade, o que significa que não há nomes de pessoas ou qualquer coisa que nos permita saber quem são os indivíduos.

![](https://media.licdn.com/dms/image/v2/D5612AQE76Xz3ennuWg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721183271678?e=1735776000&v=beta&t=32OR12vK97itnlRHz60ogvc_GfHg3Dh-SvHGZCgr00Q)

### Metodologia

A análise será conduzida utilizando técnicas estatísticas e de visualização de dados para identificar padrões e anomalias. Será empregado o Python como ferramentas de manipulação e análise dos dados, na limpeza e preparação dos dados para garantir a qualidade das análises e do modelo de Machine Learning.

### Importância do Projeto

A análise dos dados do SINASC para Rondônia em 2019 é vital para entender melhor as condições de nascimento e saúde materno-infantil no estado. As informações derivadas desse estudo podem auxiliar gestores públicos, pesquisadores e profissionais de saúde na tomada de decisões informadas, visando a melhoria contínua dos serviços de saúde e o bem-estar da população.

Ao fornecer uma visão detalhada sobre os nascimentos, este projeto contribui para um entendimento mais profundo das dinâmicas de saúde e demografia de Rondônia, promovendo ações mais eficazes e direcionadas no campo da saúde pública.

## 🔥 Vamos começar!!!

![](https://media.licdn.com/dms/image/v2/D5612AQGTWZtZzbXyHA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721195567492?e=1735776000&v=beta&t=9vLZBrov8c6Xs2WIlOg6pPPmMZFU5lhejHq_a9XbDto)

## Como a análise será realizada:

![](https://media.licdn.com/dms/image/v2/D5612AQEyNedMIW7yaQ/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1721179457444?e=1735776000&v=beta&t=lX72CYo5yDTjJmgFN5Nj7aH7UcsKH9y-gIK87v4TLkE)

## O rosto da sociedade

### Nascimentos no ano de 2019:

![](https://media.licdn.com/dms/image/v2/D5612AQEACiw9c_fGEw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1721178996817?e=1735776000&v=beta&t=VINzROK-UnpHQz-y9qwmnIh5qViBVjT2GcynUUAXih8)

O gráfico mostra a quantidade de nascimentos ao longo do ano de 2019 em Rondônia. O gráfico apresenta flutuações ao longo do ano, com vários picos e vales. Isso sugere que a quantidade de nascimentos variou mês a mês. Os meses com os maiores picos podem indicar períodos de maior atividade de nascimentos, enquanto os vales podem representar momentos de menor atividade.

- **Padrões Sazonais:** Pode ser interessante investigar se existem padrões sazonais. Por exemplo, ***há mais nascimentos em determinadas estações do ano?*** Esses padrões podem estar relacionados a fatores como clima, feriados ou eventos culturais.
- **Eventos Específicos:** Podemos verificar se algum evento específico (como feriados ou datas comemorativas) está correlacionado com os picos de nascimentos.

**Impacto na Saúde Pública:** Essa análise pode ajudar a avaliar a demanda por serviços de saúde materna e neonatal em diferentes momentos do ano. Também pode fornecer insights sobre recursos necessários para atender a essas demandas.
    
    """)



















    
    st.write("""
    Aqui está a tabela com as informações fornecidas:

    | **Coluna**                          | **Descrição**                                                                                     |
    |-------------------------------------|---------------------------------------------------------------------------------------------------|
    | **order_id**                        | Identificador único do pedido.                                                                    |
    | **order_item_id**                   | ID do item dentro de um pedido específico (indica qual item é dentro do pedido).                  |
    | **order_unique_id**                 | Um identificador único combinado para identificar cada pedido e item.                             |
    | **order_status**                    | Status do pedido (ex.: "delivered" indica que foi entregue).                                      |
    | **order_purchase_timestamp**        | Data e hora de compra do pedido.                                                                  |
    | **order_approved_at**               | Data e hora em que o pagamento foi aprovado.                                                      |
    | **order_delivered_carrier_date**    | Data em que o pedido foi entregue ao transportador.                                               |
    | **order_delivered_customer_date**   | Data em que o pedido foi entregue ao cliente.                                                     |
    | **order_estimated_delivery_date**   | Data estimada para a entrega do pedido.                                                           |
    | **shipping_limit_date**             | Data limite para envio do pedido.                                                                 |
    | **shipping_duration**               | Tempo total de envio do pedido, incluindo os dias e horas.                                        |
    | **customer_id**                     | Identificador do cliente.                                                                         |
    | **customer_unique_id**              | ID único que representa um cliente.                                                               |
    | **customer_zip_code_prefix**        | Prefixo do código postal do cliente.                                                              |
    | **customer_city**                   | Cidade do cliente.                                                                                |
    | **customer_state**                  | Estado do cliente.                                                                                |
    | **customer_zone**                   | Região geográfica do cliente (ex.: Sudeste, Sul, etc.).                                           |
    | **product_id**                      | Identificador único do produto.                                                                   |
    | **product_category_name**           | Categoria do produto.                                                                             |
    | **product_name_lenght**             | Comprimento do nome do produto (quantidade de caracteres).                                        |
    | **product_description_lenght**      | Comprimento da descrição do produto (quantidade de caracteres).                                   |
    | **product_photos_qty**              | Quantidade de fotos do produto.                                                                   |
    | **product_weight_g**                | Peso do produto em gramas.                                                                        |
    | **product_length_cm**               | Comprimento do produto em centímetros.                                                            |
    | **product_height_cm**               | Altura do produto em centímetros.                                                                 |
    | **product_width_cm**                | Largura do produto em centímetros.                                                                |
    | **Kg**                              | Peso do produto em quilogramas.                                                                   |
    | **seller_id**                       | Identificador do vendedor.                                                                        |
    | **seller_zip_code_prefix**          | Prefixo do código postal do vendedor.                                                             |
    | **seller_city**                     | Cidade do vendedor.                                                                               |
    | **seller_state**                    | Estado do vendedor.                                                                               |
    | **seller_zone**                     | Região geográfica do vendedor.                                                                    |
    | **payment_sequential**              | Sequência dos pagamentos relacionados ao pedido.                                                  |
    | **payment_type**                    | Tipo de pagamento utilizado (ex.: cartão de crédito).                                             |
    | **payment_installments**            | Quantidade de parcelas para o pagamento.                                                          |
    | **installments_price**              | Valor de cada parcela.                                                                            |
    | **price**                           | Preço do produto.                                                                                 |
    | **freight_value**                   | Valor do frete.                                                                                   |
    | **payment_value**                   | Valor total pago pelo pedido.                                                                     |
    | **review_id**                       | Identificador único para a avaliação.                                                             |
    | **review_score**                    | Nota dada pelo cliente para o pedido (ex.: de 1 a 5).                                             |
    | **review_comment_title**            | Título do comentário do cliente sobre o pedido.                                                   |
    | **review_comment_message**          | Mensagem do comentário do cliente.                                                                |
    | **review_creation_date**            | Data de criação da avaliação.                                                                     |
    | **review_answer_timestamp**         | Data e hora em que a avaliação foi respondida.                                                    |
    | **day_of_purchase**                 | Dia da compra.                                                                                    |
    | **month_of_purchase**               | Mês da compra.                                                                                    |
    | **year_of_purchase**                | Ano da compra.                                                                                    |
    | **month/year_of_purchase**          | Mês e ano da compra combinados.                                                                   |
    | **purchase_approval_time**          | Tempo até a aprovação da compra.                                                                  |
    | **difference_sought_and_expected**  | Diferença entre a entrega estimada e a efetiva.                                                   |
             
             """)
    

    #st.image('https://avatars.githubusercontent.com/u/70824630?s=400&u=5da7469a6e31d8823f89933b83c2450af0817589&v=4', width=100)
    st.image(schema)