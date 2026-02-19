# built-in
from uuid import UUID

# third-party

# own
from src.domain.entities.team import Team
from src.domain.repositories.team import TeamRepository

class InMemoryTeamRepository(TeamRepository):
    def __init__(self):
        self.teams: dict[UUID, Team] = {}

    async def save(self, team: Team) -> Team:
        self.teams[team.id] = team
        return team

    async def get_by_id(self, team_id: UUID) -> Team:
        return self.teams.get(team_id)