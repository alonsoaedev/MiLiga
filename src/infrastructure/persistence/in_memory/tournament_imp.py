# built-in
from uuid import UUID

# third-party

# own
from src.domain.entities.tournament import Tournament
from src.domain.repositories.tournament import TournamentRepository

class InMemoryTournamentRepository(TournamentRepository):
    def __init__(self):
        self._tournaments: dict[UUID, Tournament] = {}
    
    async def save(self, tournament: Tournament) -> Tournament:
        self._tournaments[tournament.id] = tournament
        return tournament
    
    async def get_by_id(self, tournament_id: UUID) -> Tournament:
        return self._tournaments.get(tournament_id)
    
    async def get_all(self) -> list[Tournament]:
        return list(self._tournaments.values())

