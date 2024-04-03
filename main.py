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
# game.current_level.spawn_actor('large moebus', game.current_level.get_random_open_tile())
# game.current_level.spawn_actor('massive moebus', game.current_level.get_random_open_tile())

game.current_level.spawn_item('GenoScribe', game.current_level.get_random_open_tile())
game.current_level.spawn_item('YeetStick', game.current_level.get_random_open_tile())
# game.current_level.spawn_item('GenoQuery', game.current_level.get_random_open_tile())

for actor in game.current_level.actors:
    game.current_level.give_gene(actor, 'mobility')

player = game.current_level.actors[0]

state_manager = StateManager(game, player)

game.state_manager = state_manager

GAME_STATE = 'waiting for input'


running = True
clock = pygame.time.Clock()
FPS = 20

while running:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYUP:
            keys = pygame.key.get_pressed()
            if keys[controls.keybinds['mod key']]:
                if event.key == controls.keybinds['quit']:
                    running = False
            elif event.key == pygame.K_F1:  # DEBUG
                if FPS == 20:
                    FPS = 1
                else:
                    FPS = 20
            elif event.key == pygame.K_F2:  # DEBUG
                for entity in game.current_level.actors + game.current_level.items:
                    print(entity.name, entity.direction)
    if GAME_STATE == 'waiting for input':
        if player.turn_complete is False:
            state_manager.update(events)
        else:
            for actor in game.current_level.actors[1:]:
                if 'can_move' in actor.abilities:
                    neighboring_tile = game.current_level.get_random_open_neighboring_tile(actor)
                    actor.direction = (neighboring_tile.position[0] - actor.position[0],
                                       neighboring_tile.position[1] - actor.position[1])
                    if actor.direction == (0, 0):  # DEBUG
                        actor.current_glyph_color = [0, 0, 255, 255]
                    else:
                        actor.current_glyph_color = actor.default_glyph_color
                    actor.move(game.current_level)
                else:
                    pass
            player.turn_complete = False
            GAME_STATE = 'resolving physics'
    elif GAME_STATE == 'resolving physics':
        physics_resolved = False
        while physics_resolved is False:
            if physics.resolve_physics(game.current_level) is True:
                physics_resolved = True
                GAME_STATE = 'waiting for input'
            else:
                continue
        else:
            pass
    render_ui.render_ui(player)
    # animation.update(game.current_level)
    animation.animate(game.current_level)
    render_level.render_level(game.current_level)
    pygame.display.flip()
