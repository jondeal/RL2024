import pygame
import Game
import controls
import render_level
import render_ui
import physics
from StateManager import StateManager

pygame.init()

game = Game.Game([], None, None)

game.generate_new_level()

game.current_level = game.levels[0]

game.current_level.spawn_actor('player', game.current_level.get_random_open_tile())
game.current_level.spawn_actor('small moebus', game.current_level.get_random_open_tile())
# game.current_level.spawn_actor('small moebus', game.current_level.get_random_open_tile())
# game.current_level.spawn_actor('large moebus', game.current_level.get_random_open_tile())
# game.current_level.spawn_actor('massive moebus', game.current_level.get_random_open_tile())

game.current_level.spawn_item('GenoScribe', game.current_level.get_random_open_tile())
game.current_level.spawn_item('YeetStick', game.current_level.get_random_open_tile())
# game.current_level.spawn_item('GenoQuery', game.current_level.get_random_open_tile())

game.current_level.give_gene(game.current_level.actors[1], 'mobility')
game.current_level.give_gene(game.current_level.actors[1], 'photosynthesis')

player = game.current_level.actors[0]

state_manager = StateManager(game, player)

game.state_manager = state_manager


running = True
clock = pygame.time.Clock()
FPS = 10

while running:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYUP:
            if event.key == controls.keybinds['quit'] and event.mod == controls.keybinds['mod key']:
                running = False
    state_manager.update(events)
    physics.resolve_physics(game.current_level)
    render_ui.render_ui(player)
    render_level.render_level(game.current_level)
    pygame.display.flip()
