import esper
from src.create.prefab_creator import crear_cuadrado
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.miembro.m_spawn_event_data import SpawnEventData


def system_enemy_spawner(world: esper.World, enemies:dict, delta_time: float):
    components = world.get_components(CEnemySpawner)

    c_e:CEnemySpawner
    for entity, (c_e) in components:
        c_e[0].time += delta_time
        m_e:SpawnEventData
        print(c_e[0].spawn)
        for event, (m_e) in enumerate(c_e[0].spawn):
            if c_e[0].time >= m_e.time and m_e.created == False:
                m_e.created = True
                crear_cuadrado(world, m_e.position, enemies[m_e.type])