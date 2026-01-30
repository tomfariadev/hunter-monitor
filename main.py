import streamlit as st
import interface as face
import data_processing as dp
import data_cleaning as dc

#@st.cache_data
def main():
    term, places, btn_execute = face.generate_interface()
    
    if btn_execute:
        if not term:
            st.warning("Digite um termo de busca!")
            return

        with st.spinner("Buscando..."):
            raw_data = dp.execute_scraping(term, places)
            
        if not raw_data.empty:
            clean_data = dc.clean_data(raw_data)            
            st.success(f"{len(clean_data)} dados coletados!")

            face.generate_graphics(clean_data)
            face.download_results(clean_data)
        else:
            st.error("Nada foi encontrado!")

if __name__ == "__main__":
    main()