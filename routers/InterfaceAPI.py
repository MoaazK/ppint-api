from typing import Annotated, List
from fastapi import APIRouter, HTTPException, status, Depends, Query

from services.InterfaceService import InterfaceService
from schemas.InterfaceDTO import InterfaceDTO


interfaceRouter = APIRouter(prefix="/interface")

@interfaceRouter.get(
    "/get_interface_detail",
    summary="Get Interface detail",
    description="This endpoint returns the detailed list of interfaces against the requested PDBs",
    response_description="List of interfaces with their metadata"
)
def get_interface_detail(
    interfaceService: Annotated[InterfaceService, Depends(InterfaceService)],
    pdb_list: Annotated[list[str] | None, Query(title="PDB List", description="List of PDBs or single PDB")] = None
) -> List[InterfaceDTO]:

    if pdb_list is None or len(pdb_list) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="pdb_list cannot be empty")

    try:
        return interfaceService.get_interface_detail(pdb_list)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.args[0])
