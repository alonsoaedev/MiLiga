# built-in
from uuid import UUID

# third-party
from pydantic import BaseModel

# own

class PlayerDTO(BaseModel):
    name: str
    last_name: str

class TeamDTO(BaseModel):
    id: UUID
    name: str
    players: list[PlayerDTO]
