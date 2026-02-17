# built-in

# third-party
from fastapi import APIRouter, Depends, HTTPException, status

# own
from src.application.dtos.tournament import CreateTournamentDTO, CreateTournamentResultDTO
from src.infrastructure.config.dependencies import DependencyContainer, get_container

router = APIRouter(prefix="/tournaments", tags=["Tournaments"])

@router.post("/", response_model=CreateTournamentResultDTO, status_code=status.HTTP_201_CREATED)
async def create_tournament(
    dto: CreateTournamentDTO,
    container: DependencyContainer = Depends(get_container)
):
    try:
        use_case = container.get_create_tournament_use_case()
        return await use_case.execute(dto)
    except Exception as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exception))