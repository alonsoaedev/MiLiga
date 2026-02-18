# built-in

# third-party
from fastapi import APIRouter, Depends, HTTPException, status

# own
from src.application.dtos.team import TeamDTO
from src.infrastructure.config.dependencies import DependencyContainer, get_container

router = APIRouter(prefix="/teams", tags=["Teams"])

@router.post("/", response_model=TeamDTO, status_code=status.HTTP_201_CREATED)
async def create_team(
    dto: TeamDTO,
    container: DependencyContainer = Depends(get_container)
):
    try:
        use_case = container.get_create_team_use_case()
        return await use_case.execute(dto)
    except Exception as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exception))
