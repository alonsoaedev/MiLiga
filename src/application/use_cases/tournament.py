# built-in
from uuid import UUID

# third-party

# own
from src.application.dtos.tournament import CreateTournamentDTO, TournamentResponseDTO, LocationDTO
from src.domain.entities.team import Team
from src.domain.entities.tournament import Location, Tournament
from src.domain.repositories.team import TeamRepository
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

class RegisterTeamToTournamentUseCase:
    def __init__(self, tournament_repository: TournamentRepository, team_repository: TeamRepository):
        self._tournament_repository = tournament_repository
        self._team_repository = team_repository

    async def execute(self, tournament_id: UUID, team_id: UUID) -> TournamentResponseDTO:
        tournament: Tournament = await self._tournament_repository.get_by_id(tournament_id)
        team: Team = await self._team_repository.get_by_id(team_id)
        
        if not tournament:
            raise ValueError("Tournament not found")
        
        if not team:
            raise ValueError("Team not found")

        tournament.add_team(team.id)
        updated_tournament: Tournament = await self._tournament_repository.save(tournament)

        return TournamentResponseDTO(
            id=updated_tournament.id,
            name=updated_tournament.name,
            created_at=updated_tournament.created_at,
            status=updated_tournament.status.value,
            max_teams=updated_tournament.max_teams,
            locations=[
                LocationDTO(name=location.name, address=location.address)
                for location in updated_tournament.locations
            ],
            registered_teams_count=updated_tournament.registered_teams_count,
            team_ids=updated_tournament.team_ids
        )

