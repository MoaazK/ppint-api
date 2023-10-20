import os
from typing import List

from config import settings
from schemas.PDBDTO import PDBDTO
from utils.file_utils import raw_json_to_DTO, read_csv_file


class PDBService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PDBService, cls).__new__(cls)
        return cls._instance

    def get_pdb_detail(self, pdb_list: list[str] | None = None) -> List[PDBDTO]:
        raw_json = read_csv_file(os.path.join(settings.file_root, "pdb_combined_data.csv"))
        all_pdbs: List[PDBDTO] = raw_json_to_DTO(List[PDBDTO], raw_json)
        return [pdb for pdb in all_pdbs if pdb.pdb_id in pdb_list]
