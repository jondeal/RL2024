import pygame
import Game
import constants
import controls
import render_level
import render_ui
import physics
import Message

pygame.init()

game = Game.Game([], None, None, 'choosing action')

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


running = True
clock = pygame.time.Clock()
FPS = 10

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == controls.keybinds['quit'] and event.mod == controls.keybinds['mod key']:
                running = False
            if game.current_state == 'choosing action':
                if event.key in controls.direction_keys:
                    render_ui.prompt_to_render = None
                    player.direction = controls.direction_keys[event.key][1]
                    player.move()
                    if event.mod == controls.keybinds['mod key']:
                        player.shove()
                if event.key == controls.keybinds['pickup']:
                    render_ui.prompt_to_render = None
                    player.pickup(game, game.current_level)
                if event.key == controls.keybinds['drop']:
                    if player.inventory:
                        render_ui.prompt_to_render = Message.Message(constants.PROMPT_RECT,
                                                                     'Select item to drop.', [255, 255, 255, 255])
                        player.inventory[0].is_selected = True
                        game.previous_state = game.current_state
                        game.current_state = 'dropping item'
                    else:
                        render_ui.prompt_to_render = Message.Message(constants.PROMPT_RECT,
                                                                     'You have nothing to drop.', [255, 255, 255, 255])
                if event.key == controls.keybinds['apply']:
                    if player.inventory:
                        render_ui.prompt_to_render = Message.Message(constants.PROMPT_RECT,
                                                                     'Apply what?', [255, 255, 255, 255])
                        game.previous_state = game.current_state
                        game.current_state = 'applying item'
                    else:
                        render_ui.prompt_to_render = Message.Message(constants.PROMPT_RECT,
                                                                     'You have nothing to apply.', [255, 255, 255, 255])
            elif game.current_state == 'dropping item':
                direction_keys_list = list(controls.direction_keys.keys())
                selected_item_index = 0
                for item in player.inventory:
                    if item.is_selected is True:
                        selected_item_index = player.inventory.index(item)
                if event.key == direction_keys_list[1]:  # up
                    if selected_item_index == 0:
                        selected_item_index = player.inventory.index(player.inventory[-1])
                    else:
                        selected_item_index -= 1
                elif event.key == direction_keys_list[7]:  # down
                    if selected_item_index == player.inventory.index(player.inventory[-1]):
                        selected_item_index = player.inventory.index(player.inventory[0])
                    else:
                        selected_item_index += 1
                elif event.key == controls.keybinds['confirm']:
                    for item in player.inventory:
                        item.is_selected = False
                    player.drop(game, game.current_level, player.inventory[selected_item_index])
                    selected_item_index = None
                    render_ui.prompt_to_render = None
                for item in player.inventory:
                    if player.inventory.index(item) == selected_item_index:
                        item.is_selected = True
                    else:
                        item.is_selected = False
            elif game.current_state == 'applying item':
                for item in player.inventory:
                    if event.key == item.inventory_slot[0]:
                        player.action_item = item
                        render_ui.prompt_to_render = Message.Message(constants.PROMPT_RECT,
                                                                     'Apply ' +
                                                                     item.glyph + item.name +
                                                                     ' in which direction?',
                                                                     [255, 255, 255, 255])
                        game.previous_state = game.current_state
                        game.current_state = 'choosing direction'
            elif game.current_state == 'choosing direction':
                if event.key in controls.direction_keys:
                    player.direction = controls.direction_keys[event.key][1]
                    if game.previous_state == 'applying item':
                        player.apply(game, player.action_item, player.direction)

    physics.resolve_physics(game.current_level)
    render_ui.render_ui(player)
    render_level.render_level(game.current_level)
    pygame.display.flip()
