import pygame
import Game
import controls
import render_level
import render_ui
import physics

pygame.init()

game = Game.Game([], None)

game.generate_new_level()

game.current_level = game.levels[0]

game.current_level.spawn_actor('player', game.current_level.get_random_open_tile())
game.current_level.spawn_actor('small moebus', game.current_level.get_random_open_tile())
game.current_level.spawn_actor('small moebus', game.current_level.get_random_open_tile())
game.current_level.spawn_actor('large moebus', game.current_level.get_random_open_tile())
game.current_level.spawn_actor('massive moebus', game.current_level.get_random_open_tile())

game.current_level.spawn_item('GenoScribe', game.current_level.get_random_open_tile())
game.current_level.spawn_item('YeetStick', game.current_level.get_random_open_tile())
game.current_level.spawn_item('GenoQuery', game.current_level.get_random_open_tile())

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
            if event.key in controls.move_keys:
                player.direction = controls.move_keys[event.key][1]
                player.move()
                if event.mod == controls.keybinds['mod key']:
                    player.shove()
            if event.key == controls.keybinds['pickup']:
                player.pickup(game.current_level)

    physics.resolve_physics(game.current_level)
    render_level.render_level(game.current_level)
    render_ui.render_ui(player)
    pygame.display.flip()
