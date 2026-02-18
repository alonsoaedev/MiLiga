# built-in
from abc import ABC, abstractmethod

# third-party

# own
from src.domain.entities.team import Team

class TeamRepository(ABC):
    @abstractmethod
    async def save(self, team: Team) -> Team:
        pass
