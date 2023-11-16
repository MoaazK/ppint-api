from typing import Annotated, List
from fastapi import APIRouter, HTTPException, status, Depends, Query

from services.StatisticsService import StatisticsService


statisticsRouter = APIRouter(prefix="/statistics")

@statisticsRouter.get(
    "/get_statistics",
    summary="Get Interface Detail",
    description="This endpoint returns the statistics of interfaces and PDBs for chart data",
    response_description="Dictionary of List of interfaces and PDBs"
)
def get_statistics(
    statisticsService: Annotated[StatisticsService, Depends(StatisticsService)]
):

    try:
        return statisticsService.get_statistics()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.args[0])
