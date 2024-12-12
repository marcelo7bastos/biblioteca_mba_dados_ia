# frontend/pages/page1.py

import streamlit as st
from app.backend.services import get_bibliografias

st.title("Bibliografia do Curso")

# Obtenha a lista de bibliografias do backend
bibliografias = get_bibliografias()

for item in bibliografias:
    st.header(item["titulo"])
    st.write(f"**Autor:** {item['autor']}")
    st.write(f"**Ano:** {item['ano']}")
    st.write(f"**Editora:** {item['editora']}")
    st.write(f"**Local:** {item['local']}")
    st.write(f"**ISBN:** {item['isbn']}")
    st.write(f"**Páginas:** {item['paginas']}")
    st.write(f"**Edição:** {item['edicao']}")
    st.write(f"**Descrição:** {item['descricao']}")
    st.write(f"[Link para o livro]({item['url']})")
    st.markdown("---")