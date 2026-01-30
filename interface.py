import streamlit as st

locais_de_busca = [
    "Mercado Livre"
]

def generate_interface():
    st.set_page_config("Hunter Monitor", layout="wide")
    st.title("Hunter Monitor")

    # termo de busca
    term = st.sidebar.text_input(
        label="Termo de busca",
        placeholder="RTX 4060"
    )
    # Locais de busca
    search_places = st.sidebar.multiselect(
        label="Locais de Busca",
        options = locais_de_busca,
        default = locais_de_busca
    )

    # botoes
    btn_execute = st.sidebar.button(label="Executar")
    
    return term, search_places, btn_execute

def generate_graphics(df):
    st.subheader("Top 10 Menores Preços")
    top_10 = df.head(10)
    st.bar_chart(data = top_10, x="produto", y="preco")

    st.dataframe(df)

# tabela interativa para download(csv)
def download_results(df):
    if not df.empty:
        csv = df.to_csv(index=False).encode('utf-8')
        
        st.sidebar.download_button(
            label="Baixar resultados (CSV)",
            data=csv,
            file_name='resultados_hunter.csv',
            mime='text/csv',
        )