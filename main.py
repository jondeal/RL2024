import random

import pygame
import Game
import animation
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
game.current_level.spawn_actor('small moebus', game.current_level.get_random_open_tile())
game.current_level.spawn_actor('small moebus', game.current_level.get_random_open_tile())
game.current_level.spawn_actor('large moebus', game.current_level.get_random_open_tile())
game.current_level.spawn_actor('massive moebus', game.current_level.get_random_open_tile())

game.current_level.spawn_item('GenoScribe', game.current_level.get_random_open_tile())
game.current_level.spawn_item('YeetStick', game.current_level.get_random_open_tile())
# game.current_level.spawn_item('GenoQuery', game.current_level.get_random_open_tile())

for actor in game.current_level.actors:
    game.current_level.give_gene(actor, 'photosynthesis')

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
    if player.turn_complete is False:
        state_manager.update(events)
    else:
        for actor in game.current_level.actors[1:]:
            if 'can_move' in actor.abilities:
                direction_list = [direction[1] for direction in controls.direction_keys.values()]
                actor.direction = random.choice(direction_list)
                actor.move()
            else:
                pass
        player.turn_complete = False
    physics.resolve_physics(game.current_level)
    animation.update()
    render_ui.render_ui(player)
    render_level.render_level(game.current_level)
    pygame.display.flip()
