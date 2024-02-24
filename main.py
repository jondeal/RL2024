import pygame
import Game
import constants
import render_level
import render_ui
import physics

pygame.init()

game = Game.Game([], None)

game.generate_new_level()

game.current_level = game.levels[0]

game.current_level.spawn_actor('player', game.current_level.get_random_open_tile())
game.current_level.spawn_actor('small mœbus', game.current_level.get_random_open_tile())
game.current_level.spawn_actor('large mœbus', game.current_level.get_random_open_tile())

game.current_level.spawn_item('GenoScribe', game.current_level.get_random_open_tile())

player = game.current_level.actors[0]


running = True
clock = pygame.time.Clock()
FPS = 10

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q and event.mod == pygame.KMOD_LSHIFT:
                running = False
            if event.key in constants.move_keys:
                player.direction = constants.move_keys[event.key]
                if event.mod == pygame.KMOD_LSHIFT:
                    player.speed = 2
                else:
                    player.speed = 1

    physics.resolve_physics(game.current_level)
    render_level.render_level(game.current_level)
    render_ui.render_ui(player)
    pygame.display.flip()
