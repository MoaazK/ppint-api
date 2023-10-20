import json
import pandas as pd
from pydantic import BaseModel
from pydantic.tools import parse_obj_as

def read_csv_file(file_path: str) -> str:
    data = pd.read_csv(file_path)
    return data.to_json(orient="records", date_format="iso")

def raw_json_to_DTO(data_type: type, raw_json: str) -> BaseModel:
    json_parsed = json.loads(raw_json)
    return parse_obj_as(data_type, json_parsed)
    