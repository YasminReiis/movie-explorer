📽️ Movie Explorer

Movie Explorer é uma aplicação web simples e interativa que permite adicionar, visualizar, atualizar e deletar filmes em uma lista online. O projeto combina frontend moderno com backend FastAPI totalmente funcional, hospedado online, para praticar desenvolvimento web full-stack.

Este projeto é 100% online, usando GitHub Pages para o frontend e Render para o backend.

🔗 Acesse o site funcionando

Frontend online: https://YasminReiis.github.io/movie-explorer/

Backend API online: https://movie-explorer-ck1b.onrender.com

Todos os botões do site interagem com a API online em tempo real.

🛠️ Tecnologias utilizadas

Frontend: HTML, CSS, JavaScript

Backend: Python, FastAPI, Uvicorn

Hospedagem:

Frontend: GitHub Pages

Backend: Render (Free Tier)

⚡ Funcionalidades

Adicionar filmes:

Informe o título e a descrição do filme

Clique em “Adicionar” para enviar para a API

Listar filmes:

Todos os filmes cadastrados aparecem automaticamente

Atualizar filmes:

Edite qualquer filme da lista clicando em “Atualizar”

Deletar filmes:

Remova qualquer filme clicando em “Deletar”

API online:

Todas as operações são enviadas diretamente para a API hospedada no Render

📂 Estrutura do projeto
movie-explorer/
├── app/                  # Backend FastAPI
│   └── main.py           # Código principal da API
├── docs/                 # Frontend hospedado no GitHub Pages
│   ├── index.html
│   ├── style.css
│   └── script.js
├── requirements.txt      # Dependências Python do backend
└── README.md             # Documentação do projeto
🚀 Como funciona na prática

Abra o frontend online aqui

Interaja com os botões para adicionar, atualizar ou deletar filmes

Cada ação envia dados para a API no Render, que salva as alterações

Você verá a lista de filmes atualizada em tempo real

Exemplo de resposta da API ao acessar https://movie-explorer-ck1b.onrender.com/tasks:

[
  {
    "title": "O Poderoso Chefão",
    "description": "Clássico do cinema sobre a máfia"
  },
  {
    "title": "Matrix",
    "description": "Filme de ficção científica com realidade virtual"
  }
]
