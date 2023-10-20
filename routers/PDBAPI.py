from typing import Annotated, List
from fastapi import APIRouter, HTTPException, status, Depends, Query

from services.PDBService import PDBService
from schemas.PDBDTO import PDBDTO


pdbRouter = APIRouter(prefix="/pdb")

@pdbRouter.get(
    "/get_pdb_detail",
    summary="Get PDB detail",
    description="This endpoint returns the detailed list of requested PDBs",
    response_description="List of PDBs with their metadata"
)
def get_pdb_detail(
    pdbService: Annotated[PDBService, Depends(PDBService)],
    pdb_list: Annotated[list[str] | None, Query(title="PDB List", description="List of PDBs or single PDB")] = None
) -> List[PDBDTO]:

    if pdb_list is None or len(pdb_list) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="pdb_list cannot be empty")

    try:
        return pdbService.get_pdb_detail(pdb_list)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.args[0])

# class PDBAPI:
#     def __init__(self) -> None:
#         self.router = APIRouter(prefix="/pdb")
#         self.router.add_api_route("/get_pdb_detail", self.get_pdb_detail, methods=["GET"], response_model=List[PDBDTO], status_code=status.HTTP_200_OK)

#     def get_pdb_detail(self, pdbService: Annotated[PDBService, Depends(PDBService)], pdb_list: Annotated[list[str] | None, Query()] = None) -> List[PDBDTO]:
#         if pdb_list is None or len(pdb_list) == 0:
#             raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="pdb_list cannot be empty")

#         try:
#             return pdbService.get_pdb_detail(pdb_list)
#         except Exception as e:
#             raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.args[0])

# router = APIRouter(prefix="/pdb")

# @router.get("/get_pdb_detail")
# def get_pdb_detail(pdb_list: Annotated[list[str] | None, Query()] = None):
#     return {}
