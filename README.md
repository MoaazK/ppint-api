# PPInt API

This project was generated with [FastAPI](https://fastapi.tiangolo.com/) version 0.103.2.

## Quick Start
1. Clone the project
```bash
git clone https://github.com/...
```
2. Navigate inside the folder
3. Create Environment
```bash
conda create -n ppint-api python=3.11
conda activate ppint-api
pip install -r requirements.txt
```
4. Change `file_root` to the the path of `ppint-api`
5. Run the API
```bash
uvicorn main:app --reload
```
6. Navigate to `localhost:8000/docs`

## API Structure
- `routers/` directory contains the API endpoints
- `schemas/` directory contains models
- `services/` directory contains backend services that are totally separate of API endpoints
  - Fetching of data from files
  - Processing of data
  - [Optional] Connecting to database and saving/loading data from/to database (Not implemented yet)
- `config.py` contains application wide configurations
- `main.py` is application's entry point