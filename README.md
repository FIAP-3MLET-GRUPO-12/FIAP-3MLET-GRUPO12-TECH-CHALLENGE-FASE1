
# Project

## Structure
```
fiap-3mlet-grupo12-tech-challenge-fase1/
├── app/
│   ├── main.py                 # Arquivo principal do FastAPI
│   ├── config.py               # Configurações e variáveis de ambiente
│   ├── models/                 # Modelos do banco de dados Beanie
│   │   └── user_model.py       # Modelo de exemplo `User` com Beanie
│   ├── db/                     # Configurações de conexão com banco de dados
│   │   └── database.py         # Inicialização do MongoDB com Beanie
│   ├── routers/                # Rotas da aplicação
│   │   └── user_router.py      # Rotas para `User`
│   ├── schemas/                # Schemas/Pydantic para validar dados
│   │   └── user_schema.py      # Schema para o `User`
│   └── utils/                  # Funções utilitárias e helpers
│       └── some_util.py        # Exemplo de utilidade
├── .env                        # Arquivo de variáveis de ambiente
├── .gitignore                  # Arquivo .gitignore
├── requirements.txt            # Lista de dependências
└── README.md                   # Documentação do projeto

```

## Local Run
```
uvicorn main:app --reload
```