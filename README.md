# Biblioteca MBA Dados IA

## Descrição

O projeto "Biblioteca MBA Dados IA" é uma aplicação web construída com Streamlit, servindo como um hub abrangente de recursos para a bibliografia de um curso de MBA focado em ciência de dados e inteligência artificial. A aplicação permite a inserção manual de dados bibliográficos e está estruturada para futuras melhorias, incluindo frontend, backend, banco de dados e resumos automáticos usando modelos de IA.

## Estrutura do Projeto

```plaintext
biblioteca_mba_dados_ia/
├─ app/
│  ├─ backend/
│  │   ├─ __init__.py
│  │   ├─ data_access.py           # Funções de acesso ao banco de dados
│  │   ├─ services.py              # Lógica de negócio, processamento de dados
│  │   └─ utils.py                 # Funções utilitárias (ex: validações, conversões)
│  │
│  ├─ frontend/
│  │   ├─ __init__.py
│  │   ├─ components/
│  │   │   ├─ layout.py            # Layout principal (header, sidebar, footer)
│  │   │   ├─ widgets.py           # Elementos visuais reutilizáveis (botões, sliders)
│  │   ├─ pages/
│  │   │   ├─ __init__.py
│  │   │   ├─ page1.py             # Página 1 da aplicação
│  │   │   ├─ page2.py             # Página 2 da aplicação
│  │   ├─ style/
│  │       ├─ custom.css           # Estilos personalizados
│  │
│  ├─ config/
│  │   ├─ __init__.py
│  │   ├─ settings.py              # Configurações gerais do app (chaves, paths)
│  │   ├─ secrets.toml             # Credenciais seguras (usando streamlit secrets)
│  │
│  ├─ __init__.py
│
├─ data/
│  ├─ raw/                         # Dados brutos (CSV, JSON, etc.)
│  ├─ processed/                   # Dados processados
│  ├─ database.db                  # Arquivo de banco de dados local (se SQLite)
│  ├─ schemas.sql                  # Scripts SQL, se necessário
│
├─ figures/
│  ├─ images/                      # Imagens estáticas (logos, ícones)
│  ├─ plots/                       # Gráficos gerados pela aplicação (exportados)
│
├─ tests/
│  ├─ __init__.py
│  ├─ test_backend.py              # Testes do backend
│  ├─ test_frontend.py             # Testes do frontend (limitado, dado Streamlit)
│
├─ requirements.txt                # Dependências do projeto
├─ README.md                       # Instruções do projeto
├─ .gitignore                      # Arquivos a serem ignorados pelo Git
└─ app.py                          # Ponto de entrada da aplicação Streamlit
```

## Funcionalidades

### Frontend
- **Interface do usuário** construída com Streamlit.
- **components/layout.py**: Define o layout principal da aplicação.
- **components/widgets.py**: Contém elementos visuais reutilizáveis.
- **pages/page1.py**: Página inicial da aplicação.
- **pages/page2.py**: Segunda página da aplicação (em desenvolvimento).
- **style/custom.css**: Estilos personalizados para a aplicação.

### Backend
- **data_access.py**: Funções para acessar o banco de dados.
- **services.py**: Lógica de negócio e processamento de dados.
- **utils.py**: Funções utilitárias.

### Configurações
- **settings.py**: Configurações gerais do aplicativo.
- **secrets.toml**: Credenciais seguras usando Streamlit secrets.

### Dados
- **raw/**: Dados brutos (CSV, JSON, etc.).
- **processed/**: Dados processados.
- **database.db**: Arquivo de banco de dados local (se SQLite).
- **schemas.sql**: Scripts SQL, se necessário.

### Figuras
- **images/**: Imagens estáticas (logos, ícones).
- **plots/**: Gráficos gerados pela aplicação (exportados).

### Testes
- **test_backend.py**: Testes do backend.
- **test_frontend.py**: Testes do frontend (limitado, dado Streamlit).

## Como Executar o Projeto

1. Clone o repositório:
    ```sh
    git clone git@github.com:marcelo7bastos/biblioteca_mba_dados_ia.git
    cd biblioteca_mba_dados_ia
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv .venv
    # Para Windows
    .venv\Scripts\Activate.ps1
    # Para macOS/Linux
    source .venv/bin/activate
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Execute a aplicação:
    ```sh
    streamlit run app.py
    ```

## Como Contribuir

1. Crie uma nova branch para sua funcionalidade ou correção:
    ```sh
    git checkout -b feature/nova-funcionalidade
    ```

2. Faça suas alterações e commit:
    ```sh
    git add .
    git commit -m "Descrição das alterações"
    ```

3. Envie suas alterações para o repositório remoto:
    ```sh
    git push origin feature/nova-funcionalidade
    ```

4. Abra um Pull Request no GitHub.

## Próximos Passos

- **Melhorar o Frontend**: Personalizar o layout e design.
- **Adicionar Backend e Banco de Dados**: Integrar um banco de dados para armazenar os dados bibliográficos.
- **Implementar Resumos com IA**: Utilizar modelos de linguagem para gerar resumos automáticos dos conteúdos.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

Com esse README, seus colegas terão uma visão clara do projeto, como configurá-lo, executá-lo e contribuir para ele. Sinta-se à vontade para ajustar e adicionar mais detalhes conforme necessário.