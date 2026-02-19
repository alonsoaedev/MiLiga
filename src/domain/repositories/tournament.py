# built-in
from abc import ABC, abstractmethod
from uuid import UUID

# third-party

# own
from src.domain.entities.tournament import Tournament

class TournamentRepository(ABC):
    @abstractmethod
    async def save(self, tournament: Tournament) -> Tournament:
        pass

    @abstractmethod
    async def get_by_id(self, tournament_id: UUID) -> Tournament:
        pass
