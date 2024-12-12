import streamlit as st

st.title("Bibliografia do Curso")

# Lista de bibliografias
bibliografias = [
    {
        "titulo": "Livro A",
        "autor": "Autor A",
        "ano": 2023,
        "editora": "Editora A",
        "local": "Cidade A",
        "isbn": "123-456-789",
        "paginas": "1-100",
        "edicao": "1ª Edição",
        "url": "http://exemplo.com/livroA",
        "descricao": "Descrição do Livro A."
    },
    {
        "titulo": "Livro B",
        "autor": "Autor B",
        "ano": 2022,
        "editora": "Editora B",
        "local": "Cidade B",
        "isbn": "987-654-321",
        "paginas": "101-200",
        "edicao": "2ª Edição",
        "url": "http://exemplo.com/livroB",
        "descricao": "Descrição do Livro B."
    },
    # Adicione mais itens conforme necessário
]


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