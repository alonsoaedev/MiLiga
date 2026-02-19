# built-in
from datetime import datetime
from uuid import UUID

# third-party
from pydantic import BaseModel, Field, field_validator

# own

class LocationDTO(BaseModel):
    name: str
    address: str

class CreateTournamentDTO(BaseModel):
    id: UUID
    name: str
    max_teams: int = Field(8, ge=2, le=20)
    locations: list[LocationDTO]

    @field_validator("locations")
    def validate_locations(cls, value):
        if not value:
            raise ValueError("At least one location must be provided")
        return value

class TournamentResponseDTO(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    status: str
    max_teams: int
    locations: list[LocationDTO]
    registered_teams_count: int
    team_ids: set[UUID]
