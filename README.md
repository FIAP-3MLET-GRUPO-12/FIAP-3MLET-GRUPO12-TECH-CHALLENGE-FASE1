
# Project

> Python Version: 3.11.9

## Structure
```
fiap-3mlet-grupo12-tech-challenge-fase1/
├── app/
│   ├── main.py                 # Main FastAPI file
│   ├── config.py               # Configuration and environment variables
│   ├── models/                 # Beanie database models
│   │   └── user_model.py       # Example `User` model with Beanie
│   ├── db/                     # Database connection configurations
│   │   └── database.py         # MongoDB initialization with Beanie
│   ├── routers/                # Application routes
│   │   └── user_router.py      # Routes for `User`
│   ├── schemas/                # Pydantic schemas for data validation
│   │   └── user_schema.py      # Schema for `User`
│   └── utils/                  # Utility functions and helpers
│       └── some_util.py        # Example utility
├── .env                        # Environment variables file
├── .gitignore                  # .gitignore file
├── hypercorn.toml              # Production server settings
├── requirements.txt            # List of dependencies
├── scpt-freeze-requirements.sh # Freezes pip requirements to txt, run to update the txt
├── start-dev.sh                # Start the server in development mode
└── README.md                   # Project documentation

```

# Running
## Local Development

Ensure Python is installed on the machine.
> suggestion: [Simple Python Version Management: pyenv](https://github.com/pyenv/pyenv)

### Activating virtual env

1. At the root of the project, run:

Mac/Linux: ```source venv/bin/activate```

Windows: ```venv\Scripts\activate```


2. Install the dependencies:

```pip install -r requeriments.txt```

> Whenever you uninstall or install new packages, run the script ```sh scpt-freeze-requeriments.sh``` to update the requirements.txt and commit the file update

3. run the script sh ```start-dev.sh```

```bash
sh start-dev.sh
```

The project will start on port 8000 and will be ready for development with reload

## Swagger Documentation

Access the API documentation at:

```
http://localhost:8000/docs
```