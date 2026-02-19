# built-in
# third-party

# own
from src.application.dtos.tournament import CreateTournamentDTO, TournamentResponseDTO, LocationDTO
from src.domain.entities.tournament import Location, Tournament
from src.domain.repositories.tournament import TournamentRepository

class CreateTournamentUseCase:
    def __init__(self, tournament_repository: TournamentRepository):
        self._tournament_repository = tournament_repository

    async def execute(self, dto: CreateTournamentDTO) -> TournamentResponseDTO:
        tournament: Tournament = Tournament(
            id=dto.id,
            name=dto.name,
            max_teams=dto.max_teams,
            locations=[
                Location(name=location.name, address=location.address)
                for location in dto.locations
            ]
        )

        saved_tournament = await self._tournament_repository.save(tournament)
        return TournamentResponseDTO(
            id=saved_tournament.id,
            name=saved_tournament.name,
            created_at=saved_tournament.created_at,
            status=saved_tournament.status.value,
            max_teams=saved_tournament.max_teams,
            locations=[
                LocationDTO(name=location.name, address=location.address)
                for location in saved_tournament.locations
            ],
            registered_teams_count=saved_tournament.registered_teams_count,
            team_ids=saved_tournament.team_ids
        )
