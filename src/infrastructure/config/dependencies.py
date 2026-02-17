# built-in
from functools import lru_cache

# third-party

# own
from src.application.use_cases.tournament import CreateTournamentUseCase
from src.infrastructure.persistence.in_memory.tournament_imp import InMemoryTournamentRepository

class DependencyContainer:
    def __init__(self):
        self._tournament_repository = InMemoryTournamentRepository()

    def get_create_tournament_use_case(self) -> CreateTournamentUseCase:
        return CreateTournamentUseCase(tournament_repository=self._tournament_repository)
    
@lru_cache()
def get_container() -> DependencyContainer:
    return DependencyContainer()