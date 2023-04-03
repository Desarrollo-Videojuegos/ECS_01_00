import pygame
import json
import esper
from src.create.prefab_creator import crear_cuadrado, crear_enemy_spawner
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.systems.s_enemy_spawner import system_enemy_spawner
from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_screen_bounce import system_screen_bounce
from src.miembro.m_spawn_event_data import SpawnEventData


class GameEngine:
    

    def __init__(self) -> None:
        self._load_json()
        pygame.init()
        pygame.display.set_caption(self.window['title'])
        self.framerate = self.window['framerate']
        size = self.window['size']
        x = size['w']
        y = size['h']
        self.bg_color = self.window['bg_color']
        self.screen = pygame.display.set_mode((x,y), pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.delta_time = 0

        self.ecs_world = esper.World()
    
    def _load_json(self):
        with open('assets/cfg/window.json') as win:
            self.window = json.load(win)
        with open('assets/cfg/enemies.json') as ene:
            self.enemies = json.load(ene)
        with open('assets/cfg/level_01.json') as lev:
            self.level = json.load(lev)

    def run(self) -> None:
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        self._clean()

    def _create(self):
        crear_enemy_spawner(self.ecs_world, self.level)
        ##crear_cuadrado(self.ecs_world)

    def _calculate_time(self):
        self.clock.tick(self.framerate)
        self.delta_time = self.clock.get_time() / 1000.0

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        system_enemy_spawner(self.ecs_world, self.enemies, self.delta_time)
        system_movement(self.ecs_world, self.delta_time)
        system_screen_bounce(self.ecs_world, self.screen)

    def _draw(self):
        self.screen.fill((self.bg_color['r'],self.bg_color['g'],self.bg_color['b']))

        system_rendering(self.ecs_world, self.screen)

        pygame.display.flip()

    def _clean(self):
        pygame.quit()
