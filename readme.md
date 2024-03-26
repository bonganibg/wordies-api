# Wordies API 
API for handling letter generation and validation for the Wordies game.

![Static Badge](https://img.shields.io/badge/0.11.0-FastAPI-blue)  ![Static Badge](https://img.shields.io/badge/0.28.1-uvicorn-blue) ![Static Badge](https://img.shields.io/badge/1.0.1-dotenv-blue)
## Install 

##### Set Up Virtual Environment

<aside>
If the command does not work on mac or linux try `python3` and `pip3`
</aside>

```shell 
python -m venv .venv
```

Activate Environment
```shell 
source .venv/Scripts/activate
```
or 
```shell 
source .venv/bin/activate
```

##### Install Packages 
```shell
pip install -r requirements.txt
```


### Running Locally 

To run the application locally, you will need to firstly create a `.env` file where the parameters will be defined.

```text 
HOST=127.0.0.1
PORT=8080
RELOAD=True
```

Run the following command in the root directory

```shell 
python main.py
```

### Running Unit Tests 

Run the following command in the root directory.

```shell 
python -m unittest
```

### Navigation 

#### Documentation 
[Swagger Interactive](http://localhost:8080/docs)
[Main Documentation](http://localhost:8080/redoc)