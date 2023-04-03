
import pygame


class SpawnEventData:
    def __init__(self, data: dict) -> None:
        self.position: pygame.Vector2 = pygame.Vector2(data['position']['x'],data['position']['y'])
        self.time: float = data['time']
        self.type: str = data['enemy_type']
        self.created: bool = False
        
