from pydantic import BaseModel, Field

class InterfaceDTO(BaseModel):
    pdb_id: str = Field(alias="pdb_id")
    interface_id: str = Field(alias="interface_id")
    chain_1: str = Field(alias="chain_1")
    chain_2: str = Field(alias="chain_2")
    num_chain_1: float = Field(alias="num_chain_1")
    num_chain_2: float = Field(alias="num_chain_2")
    total: float = Field(alias="total")
