# built-in
from abc import ABC, abstractmethod

# third-party

# own
from src.domain.entities.tournament import Tournament

class TournamentRepository(ABC):
    @abstractmethod
    async def save(self, tournament: Tournament) -> Tournament:
        pass
