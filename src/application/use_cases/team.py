# built-in
# third-party

# own
from src.application.dtos.team import PlayerDTO, TeamDTO
from src.domain.entities.team import Player, Team
from src.domain.repositories.team import TeamRepository

class CreateTeamUseCase:
    def __init__(self, team_repository: TeamRepository):
        self.team_repository = team_repository

    async def execute(self, dto: TeamDTO) -> TeamDTO:
        team = Team(
            id=dto.id,
            name=dto.name,
            players=[
                Player(name=player.name, last_name=player.last_name)
                for player in dto.players
            ]
        )
        saved_team = await self.team_repository.save(team)
        return TeamDTO(
            id=saved_team.id,
            name=saved_team.name,
            players=[
                PlayerDTO(name=player.name, last_name=player.lat_name)
                for player in saved_team.players
            ]
        )
