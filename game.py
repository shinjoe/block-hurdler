from Player import *
from Hurdle import *

BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
FPS = 30
SCORE_LABEL_POS = (5, 5)
GAME_OVER_POS = (180, 100)
RESTART_POS = (180, 160)

pygame.init()
size = [600, 250]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Block Hurdler")
font = pygame.font.SysFont("monospace", 20)
game_over_font = pygame.font.SysFont("monospace", 40)
score = 0

hurdle = Hurdle(screen)
player = Player(screen)
done = False
game_over = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
            elif event.key == pygame.K_r:
                score = 0
                game_over = False
                # reinitialize the hurdle and the player
                hurdle = Hurdle(screen)
                player = Player(screen)

    if not game_over:
        hurdle.update()
        player.update()
        score += 10

    if player.collides_with(hurdle):
        game_over = True

    screen.fill(WHITE)
    hurdle.draw()
    player.draw()
    if game_over:
        game_over_label = game_over_font.render("Game Over!", 1, RED)
        screen.blit(game_over_label, GAME_OVER_POS)
        restart_label = font.render("press 'r' to restart", 1, GRAY)
        screen.blit(restart_label, RESTART_POS)

    score_label = font.render("Score: " + str(score), 1, BLACK)
    screen.blit(score_label, SCORE_LABEL_POS)

    clock.tick(FPS)
    pygame.display.flip()


pygame.quit()