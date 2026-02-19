# built-in
from functools import lru_cache

# third-party

# own
from src.application.use_cases.team import CreateTeamUseCase
from src.application.use_cases.tournament import CreateTournamentUseCase
from src.application.use_cases.tournament import RegisterTeamToTournamentUseCase
from src.infrastructure.persistence.in_memory.team_imp import InMemoryTeamRepository
from src.infrastructure.persistence.in_memory.tournament_imp import InMemoryTournamentRepository

class DependencyContainer:
    def __init__(self):
        self._tournament_repository = InMemoryTournamentRepository()
        self._team_repository = InMemoryTeamRepository()

    # Tournament use cases
    def get_create_tournament_use_case(self) -> CreateTournamentUseCase:
        return CreateTournamentUseCase(tournament_repository=self._tournament_repository)
    
    def get_register_team_to_tournament_use_case(self) -> RegisterTeamToTournamentUseCase:
        return RegisterTeamToTournamentUseCase(tournament_repository=self._tournament_repository, team_repository=self._team_repository)
    
    def get_create_team_use_case(self) -> CreateTeamUseCase:
        return CreateTeamUseCase(team_repository=self._team_repository)
    
@lru_cache()
def get_container() -> DependencyContainer:
    return DependencyContainer()