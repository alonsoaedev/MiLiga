# built-in
from uuid import UUID

# third-party
from fastapi import APIRouter, Depends, HTTPException, status

# own
from src.application.dtos.tournament import CreateTournamentDTO, TournamentResponseDTO
from src.infrastructure.config.dependencies import DependencyContainer, get_container

router = APIRouter(prefix="/tournaments", tags=["Tournaments"])

@router.get("/", response_model=list[TournamentResponseDTO])
async def get_all_tournaments(container: DependencyContainer = Depends(get_container)):
    try:
        use_case = container.get_all_tournaments_use_case()
        return await use_case.execute()
    except Exception as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exception))

@router.post("/", response_model=TournamentResponseDTO, status_code=status.HTTP_201_CREATED)
async def create_tournament(dto: CreateTournamentDTO, container: DependencyContainer = Depends(get_container)):
    try:
        use_case = container.get_create_tournament_use_case()
        return await use_case.execute(dto)
    except Exception as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exception))
    
@router.post("/{tournament_id}/teams/{team_id}", response_model=TournamentResponseDTO)
async def register_team_to_tournament(tournament_id: UUID, team_id: UUID, container: DependencyContainer = Depends(get_container)):
    try:
        use_case = container.get_register_team_to_tournament_use_case()
        return await use_case.execute(tournament_id, team_id)
    except Exception as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exception))