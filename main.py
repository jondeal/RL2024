import pygame
import Game
import constants
import render
import physics

pygame.init()

game = Game.Game([], None)
game.generate_new_level()
game.current_level = game.levels[0]
game.current_level.spawn_actor('player', game.current_level.get_random_open_tile())
game.current_level.spawn_actor('small slime', game.current_level.get_random_open_tile())

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
                player.impulse += 1

    physics.resolve_physics(game.current_level)
    render.render(game.current_level)
    pygame.display.flip()
