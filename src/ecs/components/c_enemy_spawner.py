import pygame

from src.miembro.m_spawn_event_data import SpawnEventData

##.Font(None,30).render("hh", 0, (0,0,0))
class CEnemySpawner:
    def __init__(self, level: dict) -> None:
        self.spawn: list[SpawnEventData] = []
        self.time:float = 0
        for spawn_1 in level:
            self.spawn.append(SpawnEventData(spawn_1))

