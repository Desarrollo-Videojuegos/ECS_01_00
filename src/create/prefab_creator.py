import pygame
import esper
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity


def crear_cuadrado(ecs_world: esper.World, pos: pygame.Vector2, enemy: dict):
        cuad_entity = ecs_world.create_entity()
        ecs_world.add_component(cuad_entity, CSurface(pygame.Vector2(enemy['size']['x'], enemy['size']['y']), pygame.Color(enemy['color']['r'],enemy['color']['g'],enemy['color']['b'])))
        ecs_world.add_component(cuad_entity, CTransform(pos))
        ecs_world.add_component(cuad_entity, CVelocity(pygame.Vector2(enemy['velocity_max'],enemy['velocity_min'])))

def crear_spawner(ecs_world: esper.World, level: dict):
        spawner = CEnemySpawner(level['enemy_spawn_events'])
        enemy_spawner_entity = ecs_world.create_entity()
        ecs_world.add_component(enemy_spawner_entity, spawner)