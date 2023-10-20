import os
import json
from typing import List

from config import settings
from schemas.InterfaceDTO import InterfaceDTO
from utils.file_utils import raw_json_to_DTO, read_csv_file


class InterfaceService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InterfaceService, cls).__new__(cls)
        return cls._instance

    def get_interface_detail(self, pdb_list: list[str] | None = None) -> List[InterfaceDTO]:
        raw_json = read_csv_file(os.path.join(settings.file_root, "interface_data.csv"))
        all_interfaces: List[InterfaceDTO] = json.loads(raw_json)
        return [interface for interface in all_interfaces if interface["pdb_id"] in pdb_list]
