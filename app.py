import streamlit as st

st.title("Bibliografia do Curso")

# Lista de bibliografias
bibliografias = [
    {
        "titulo": "Livro A",
        "autor": "Autor A",
        "descricao": "Descrição do Livro A."
    },
    {
        "titulo": "Livro B",
        "autor": "Autor B",
        "descricao": "Descrição do Livro B."
    },
    {
        "titulo": "Livro C",
        "autor": "Autor C",
        "descricao": "Descrição do Livro C."
    },
    # Adicione mais itens conforme necessário
]

for item in bibliografias:
    st.header(item["titulo"])
    st.write(f"**Autor:** {item['autor']}")
    st.write(item["descricao"])
    st.markdown("---")