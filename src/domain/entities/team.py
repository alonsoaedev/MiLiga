# built-in
from uuid import UUID

# third-party
# own

class Player:
    def __init__(self, name: str, last_name: str):
        if not name:
            raise ValueError("Player name cannot be empty")
        
        self.name = name
        self.lat_name = last_name

class Team:
    def __init__(self, id: UUID, name: str, players: list[Player] = None):
        if not name:
            raise ValueError("Team name cannot be empty")
        if not players:
            players = []
        
        self.id = id
        self.name = name
        self.players: list[Player] = players