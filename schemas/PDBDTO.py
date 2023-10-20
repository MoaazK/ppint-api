from datetime import date
from pydantic import BaseModel, Field

class PDBDTO(BaseModel):
    pdb_id: str = Field(alias="pdb_id")
    num_of_interface: int = Field(alias="num_interface")
    status: str | None = Field(alias="status")
    accession_date: date | None = Field(alias="accession_date")
    resolution: float | None = Field(alias="resolution")
    experiment_type: str | None = Field(alias="experiment_type")

    class Config:
        json_encoders = {
            date: lambda v: v.strftime("%Y-%d-%m")
        }
