import pygame
import Game
import controls
import constants
import render_level
import render_ui
from GameStateManager import GameStateManager
from PlayerStateManager import PlayerStateManager


pygame.init()

game = Game.Game([], None, None, None)

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

for actor in game.current_level.actors[1:]:
    game.current_level.give_gene(actor, 'mobility')

player = game.current_level.actors[0]

game.current_level.give_gene(player, 'mobility')

player_state_manager = PlayerStateManager(game, player)
game_state_manager = GameStateManager(game, player)

game.game_state_manager = game_state_manager
game.player_state_manager = player_state_manager

running = True
clock = pygame.time.Clock()
FPS = constants.FPS

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
                if FPS == constants.FPS:
                    FPS = 1
                else:
                    FPS = constants.FPS
            elif event.key == pygame.K_F2:  # DEBUG
                for entity in game.current_level.actors + game.current_level.items:
                    print(entity.name, entity.direction)

    game.game_state_manager.current_state.update(events)

    render_ui.render_ui(player)
    render_level.render_level(game.current_level)
    pygame.display.flip()
