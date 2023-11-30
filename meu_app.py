import streamlit as st
import pandas as pd
import altair as alt
import base64

st.set_page_config(page_title="Trabalho BI", layout='centered')

path_para_logo = "23.png"

# Centralizando a logo com HTML
st.markdown(
    f'<p style="text-align:center;"><img src="data:image/png;base64,{base64.b64encode(open(path_para_logo, "rb").read()).decode()}" alt="Logo" width="200"></p>',
    unsafe_allow_html=True
)
st.markdown("<br>", unsafe_allow_html=True)

with st.container():
        st.write("---")
st.markdown("""
    **Curso:** Sistemas de Informação  \n
    **Disciplina:** Sistemas de Informação \n
    **Orientador:** Clóvis Lemos Tavares \n
    **Alunos:** Symon Breno Brandão, Victor Rafael da Silva Santos.
""")

with st.container():
   st.markdown("<br>", unsafe_allow_html=True)
# Título da Página
st.title("ANÁLISE PARA CASAS DE SHOWS EM BELO HORIZONTE E NOVA LIMA")

with st.container():
        st.write("---")
# Introdução
st.markdown("A base de dados a seguir contém informações valiosas sobre casas noturnas e estabelecimentos de entretenimento em Belo Horizonte e Nova Lima, MG. Aqui estão alguns insights potenciais e benefícios para utilizar esses dados:")


st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
# Avaliação e Classificação
st.header("Avaliação e Classificação")
with st.container():
        st.markdown(
    "- A avaliação média fornece uma indicação rápida da qualidade percebida de cada estabelecimento. Pode ser útil para os frequentadores de casas noturnas escolherem locais com avaliações mais altas.\n"
    "- Pode-se realizar uma análise mais detalhada, como identificar os estabelecimentos com as classificações mais altas e entender os fatores que contribuem para sua popularidade."
    )

st.markdown("<br>", unsafe_allow_html=True)
# Preços e Categorias de Estabelecimentos
st.header("Preços e Categorias de Estabelecimentos")
with st.container():
        st.markdown(
    "- A informação sobre os preços pode ser útil para quem procura opções que se encaixem em diferentes faixas de orçamento."
    )

st.markdown("<br>", unsafe_allow_html=True)
# Localização e Ambiente
st.header("Localização e Ambiente")
with st.container():
        st.markdown(
    "- Os endereços fornecem dados de localização valiosos para análises geoespaciais. Pode-se mapear a distribuição dos estabelecimentos e identificar áreas com uma concentração maior de casas noturnas.\n"
    "- A indicação do ambiente (aberto, fechado) pode ser relevante para aqueles que preferem um tipo específico de experiência."
    )
st.markdown("<br>", unsafe_allow_html=True)

# Horários de Funcionamento
st.header("Horários de Funcionamento")
with st.container():
        st.markdown(
    "- A informação sobre horários de funcionamento ajuda a entender a dinâmica do cenário noturno na região. Pode-se analisar quais estabelecimentos têm horários mais flexíveis ou específicos.\n"
    "- Isso pode ser valioso para quem procura opções para diferentes momentos do dia."
    )
st.markdown("<br>", unsafe_allow_html=True)

# Tomada de Decisão Informada
st.header("Tomada de Decisão Informada")
with st.container():
        st.markdown(
    "- Para empresários do setor, os dados podem informar decisões estratégicas, como ajustes nos preços, melhorias no ambiente ou expansão para novas áreas.\n"
    "- Os frequentadores podem tomar decisões mais informadas sobre onde passar seu tempo com base em avaliações e preferências pessoais."
    )
st.markdown("<br>", unsafe_allow_html=True)

# Visualizações e Dashboards
st.header("Visualizações e Dashboards")
with st.container():
        st.markdown(
    "- Utilizando ferramentas de visualização de dados como Streamlits e Altair, é possível criar dashboards interativos que oferecem insights visuais e rápidos."
    )

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Conclusão
with st.container():
        st.markdown(
    "Em resumo, o objetivo é apresentar que com os conhecimentos repassados durante a disciplina é possível criar uma visualização crítica e para tomada de decisão até mesmo em momentos de lazer ou possíveis investimentos."
    )

with st.container():
    st.write("---")
    dados = pd.read_csv("TesteCasadeShow.csv")
    
    # Filtro para Belo Horizonte
    dados_bool = dados['Cidade'] == ' Belo Horizonte'
    dados_bh = dados[dados_bool]

    c = (
        alt.Chart(dados_bh)
        .mark_bar()
        .encode(x="Nome", y="Preco", size='Cidade', color=alt.Color('Cidade', legend=None), tooltip=["Nome", "Ambiente", "Horario"])
    ).interactive()
    
    d = (
        alt.Chart(dados_bh)
        .mark_bar()
        .encode(x="Avaliacao", y="Nome", color="Nome", tooltip=["Nome", "Avaliacao", "Horario", "Ambiente"])
    ).interactive()

    dados = pd.read_csv("TesteCasadeShow.csv")

    with st.container():
        st.title("TABELA DE DADOS")
        st.dataframe(dados)
    
    # Agrupar dados por Nome e Cidade e contar o número de ocorrências
    grouped_data = dados.groupby(['Nome', 'Cidade']).size().reset_index(name='Quantidade')

    # Criar o gráfico de área usando Altair
    area_cidade = (
               alt.Chart(grouped_data)
                .mark_area()
                .encode(
                x=alt.X("Nome:N", title="Nome da Casa"),
                y=alt.Y("Quantidade:Q", title="Quantidade de Locais"),
                color=alt.Color("Cidade:N", title="Cidade"),
                tooltip=["Cidade:N", "Quantidade:Q", "Nome:N"]
        )
        .properties(width=600, height=400)
        .configure_axisY(title=None)
    )

    with st.container():
        st.write("---")
        st.title("VISUALIZAÇÕES GRÁFICAS")

    tab1, tab2, tab3 = st.tabs(["Casas de Show / Avaliação", "Preço / Local", "Local / Cidade"])
    with tab1:
            st.altair_chart(d, theme="streamlit", use_container_width=True)
    with tab2:
            st.altair_chart(c, use_container_width=True)
    with tab3:
            st.altair_chart(area_cidade, use_container_width=True)
    
    with st.container():
        st.write("---")
    st.markdown("Link para visualização detalhada do PowerBI: [TrabalhoBI](https://app.powerbi.com/view?r=eyJrIjoiNjM4MTEzZTMtMTkxZC00OTg2LWJjN2QtZDNhNTU2OWRmNzE2IiwidCI6IjE0Y2JkNWE3LWVjOTQtNDZiYS1iMzE0LWNjMGZjOTcyYTE2MSIsImMiOjh9)")
    st.markdown("Fonte de dados: Pesquisa Google.")
    # dados.head()
    # a = (dados.sort_values(by='Avaliacao'))
    # a.plot(kind="bar", x=a["Cidade"],
    #        title="Cidade / Ambiente Casa de Show",
    #        legend=False)