from typing import Annotated, List
from fastapi import APIRouter, HTTPException, status, Depends, Query

from services.PDBService import PDBService
from services.InterfaceService import InterfaceService
from schemas.InterfaceDTO import InterfaceDTO
from schemas.PDBDTO import PDBDTO


interfaceRouter = APIRouter(prefix="/interface")

@interfaceRouter.get(
    "/get_interface_detail",
    summary="Get Interface detail",
    description="This endpoint returns the detailed list of interfaces against the requested PDBs",
    response_description="List of interfaces with their metadata"
)
def get_interface_detail(
    pdbService: Annotated[PDBService, Depends(PDBService)],
    interfaceService: Annotated[InterfaceService, Depends(InterfaceService)],
    pdb_ids: Annotated[str | None, Query(title="PDB List", description="List of PDBs or single PDB")] = None
):

    if pdb_ids is None or len(pdb_ids) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="pdb_list cannot be empty")

    try:
        pdb_list = pdb_ids.split(",") if pdb_ids else []
        interfaceData = {}
        interfaceData['pdb'] = pdbService.get_pdb_detail(pdb_list)
        interfaceData['interface'] = interfaceService.get_interface_detail(pdb_list)
        return interfaceData
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.args[0])
