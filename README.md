
Group Components

* [Ricardo Matos](https://www.linkedin.com/in/ricardo-matos-mobile-dev/)
* [José Diôgo](https://www.linkedin.com/in/jozediogo/)

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
├── Dockerfile                  # Definição criação imagem docker
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

run ```python -m venv venv```

Mac/Linux: ```source venv/bin/activate```

Windows: ```venv\Scripts\activate```


2. Install the dependencies:

```pip install -r requeriments.txt```

> Whenever you uninstall or install new packages, run the command (MAC/Linux) ```pip freeze > requirements.txt``` and (windows) ```pip freeze > requirements-windows.txt``` to update the requirements.txt and commit the file update

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

# Project Archtecture

## Components

The project has 3 main components:

* An API REST using Framework Fastapi
* A non -relational database (Mongodb)
* The Embrapa portal with the data.

Initially, we make a load of existing data on the portal in Mongodb. This is performed due to the occurrence of instability on the portal, so we guarantee data availability for our customers and, in the worst case, we could not upgrade with new data at some point.

The load and update is by processing CSV files provided by downloading by the portal itself.

Abaixo é apresentado um esquema do fluxo de dados da aplicação.

![Archtecture Model](/docs/archtecture.drawio.png)

## Infrastructure




# Swegger Snapshot

## FastAPI

### /users/

#### POST
##### Summary:

Create User

##### Description:

Create a new user.

Args:
    user (UserSchema): The user data.

Returns:
    dict: A message indicating successful user creation.

Raises:
    HTTPException: If the email is already registered.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 400 | Email already registered |
| 422 | Validation Error |

### /users/login

#### POST
##### Summary:

Login

##### Description:

Login a user.

Args:
    user (UserSchema): The user data.

Returns:
    TokenSchema: The access token.

Raises:
    HTTPException: If the credentials are wrong.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 401 | Wrong Credentials |
| 422 | Validation Error |

### /production/

#### GET
##### Summary:

Get product production report for last year

##### Description:

Retrieves the production product report for the last year.
Args:
- _: Dependency that verifies the token.
Returns:
- The production product report for the last year.
Raises:
- HTTPException: If no production products are found.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 404 | No production products found |

##### Security

| Security Schema | Scopes |
| --- | --- |
| OAuth2PasswordBearer | |

### /production/{year}

#### GET
##### Summary:

Get product production report for a specific year

##### Description:

Retrieves the production product report for a specific year.
Args:
- year: The year for which the production product report is to be retrieved.
Returns:
- The production product report for the specified year.
Raises:
- HTTPException: If no production products are found for the given year.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| year | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 404 | No production products found for the given year |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| OAuth2PasswordBearer | |

### /processing/{processing_category}

#### GET
##### Summary:

Get Processing report for last year

##### Description:

Get the processing report for the last year for a given category.

Args:
    processing_category (Literal): The category of processing products. 
        Must be one of the following:
        - processing_american
        - processing_table_grapes
        - processing_unrated
        - processing_vines

Returns:
    report: The processing report for the last year.

Raises:
    HTTPException: If no processing products are found for the given category.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| processing_category | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 404 | No processing products found for the given category |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| OAuth2PasswordBearer | |

### /processing/{processing_category}/{year}

#### GET
##### Summary:

Get Processing report for a specific year

##### Description:

Get the processing report for a specific year for a given category.

Args:
    processing_category (Literal): The category of processing products. 
        Must be one of the following:
        - processing_american
        - processing_table_grapes
        - processing_unrated
        - processing_vines
    year (int): The specific year for which the report is requested.

Returns:
    report: The processing report for the specified year.

Raises:
    HTTPException: If no processing products are found for the given category and year.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| processing_category | path |  | Yes | string |
| year | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 404 | No processing products found for the given category and year |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| OAuth2PasswordBearer | |

### /commercialization/

#### GET
##### Summary:

Get product commercialization report for last year

##### Description:

Fetch the commercialization report for the year 2023.
Args:
    _ (Depends): Dependency to verify the token.
Returns:
    report (list): List of products for the year 2023.
Raises:
    HTTPException: If no commercialization products are found, raises a 404 error.

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 404 | No commercialization products found |

##### Security

| Security Schema | Scopes |
| --- | --- |
| OAuth2PasswordBearer | |

### /commercialization/{year}

#### GET
##### Summary:

Get product commercialization report for a specific year

##### Description:

Fetch the commercialization report for a specified year.
Args:
    year (int): The year for which to fetch the report.
Returns:
    report (list): List of products for the specified year.
Raises:
    HTTPException: If no commercialization products are found for the given year, raises a 404 error.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| year | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 404 | No commercialization products found for the given year |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| OAuth2PasswordBearer | |

### /trade/import/{derivative}

#### GET
##### Summary:

Get import trades by derivative

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| derivative | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| OAuth2PasswordBearer | |

### /trade/import/{derivative}/{year}

#### GET
##### Summary:

Get import trades by derivative and year

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| derivative | path |  | Yes | string |
| year | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| OAuth2PasswordBearer | |

### /trade/export/{derivative}

#### GET
##### Summary:

Get export trades by derivative

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| derivative | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| OAuth2PasswordBearer | |

### /trade/export/{derivative}/{year}

#### GET
##### Summary:

Get export trades by derivative and year

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| derivative | path |  | Yes | string |
| year | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| OAuth2PasswordBearer | |

> Generated on [swagger-markdown UI](https://swagger-markdown-ui.netlify.app/)