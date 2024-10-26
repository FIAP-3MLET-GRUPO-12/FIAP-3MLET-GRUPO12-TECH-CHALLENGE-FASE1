
# Project

> Python Version: 3.11.9

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
├── hypercorn.toml              # Settings para o servidor de produção
├── requirements.txt            # Lista de dependências
├── scpt-freeze-requeriments.sh # Faz o freeze do pip para o txt, execute para atualizaro txt
├── start-dev.sh                # Iniciar o servidor em modo desenvolvimento
└── README.md                   # Documentação do projeto

```

# Running
## Local Development

Garanta ter o Python instalado na máquina.
> sugestão: [Simple Python Version Management: pyenv](https://github.com/pyenv/pyenv)

### Ativando virtual env

1. Na raiz do projeto execute:

Mac/Linux: ```source venv/bin/activate```

Windows: ```venv\Scripts\activate```


2. Instale as dependências

```pip install -r requeriments.txt```

> Sempre que desinstalar ou instalar novos pacotes, execute o script ```sh scpt-freeze-requeriments.sh```  para atualizar o requeriments.txt e commit o update do arquivo

3. Execute o script sh ```start-dev.sh```

```bash
sh start-dev.sh
```

O projeto iniciará na porta 8000 e estará pronto para desenvolvimento com _reload_

## Local Production

[ ] TO DO