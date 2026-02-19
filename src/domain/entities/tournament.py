# built-in
from datetime import datetime
from enum import Enum
from uuid import UUID

# third-party
# own

class Location:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

class TournamentStatus(str, Enum):
    REGISTRATION = "registration"
    IN_PROGRESS = "in_progress"
    PAUSED = "paused"
    FINISHED = "finished"
    CANCELLED = "cancelled"

class Tournament:
    def __init__(self, id: UUID, name: str, max_teams: int, locations: list[Location]):
        if not name:
            raise ValueError("Tournament name cannot be empty")
        if max_teams < 2 or max_teams > 30:
            raise ValueError("max_teams must be between 2 and 30")
        if not locations:
            raise ValueError("At least one location must be provided")
        
        self.id = id
        self.name = name
        self.created_at = datetime.now()
        self.status: TournamentStatus = TournamentStatus.REGISTRATION
        self.max_teams = max_teams
        self.locations = locations
        self.team_ids: set[UUID] = set()

    @property
    def registered_teams_count(self) -> int:
        return len(self.team_ids)
    
    def add_team(self, team_id: UUID):
        if self.status != TournamentStatus.REGISTRATION:
            raise ValueError("Cannot register teams when tournament is not in registration status")
        if self.registered_teams_count >= self.max_teams:
            raise ValueError("Tournament has reached maximum number of teams")
        if team_id in self.team_ids:
            raise ValueError("Team is already registered in the tournament")
        
        self.team_ids.add(team_id)
