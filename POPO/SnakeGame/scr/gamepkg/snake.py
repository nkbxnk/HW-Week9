import pygame
import random

def rungame():
    pygame.init()

    WIDTH = 600
    HEIGHT = 400
    BLOCK = 20

    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    BLACK = (20, 20, 20)
    GREEN = (0, 255, 0)
    RED = (255, 50, 50)
    WHITE = (255, 255, 255)

    CLOCK = pygame.time.Clock()
    FONT = pygame.font.SysFont("arial", 25)

    def draw_score(score):
        text = FONT.render(f"Score: {score}", True, WHITE)
        SCREEN.blit(text, (10, 10))

    def game_over(score):
        while True:
            SCREEN.fill(BLACK)

            text1 = FONT.render(
                f"Game Over! Score: {score}",
                True, WHITE
            )
            text2 = FONT.render(
                "Press R to Restart or Q to Quit",
                True, WHITE
            )

            SCREEN.blit(text1, (150, 150))
            SCREEN.blit(text2, (80, 200))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return rungame()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        return

    snake = [[100, 100]]
    dx, dy = BLOCK, 0

    food = [
        random.randrange(0, WIDTH, BLOCK),
        random.randrange(0, HEIGHT, BLOCK)
    ]

    score = 0
    running = True

    while running:

        CLOCK.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK
                elif event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK, 0

        head = [snake[0][0] + dx, snake[0][1] + dy]

        if (
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or
            head in snake
        ):
            running = False
            break

        snake.insert(0, head)

        if head == food:
            score += 1
            food = [
                random.randrange(0, WIDTH, BLOCK),
                random.randrange(0, HEIGHT, BLOCK)
            ]
        else:
            snake.pop()

        SCREEN.fill(BLACK)

        pygame.draw.rect(
            SCREEN,
            RED,
            (food[0], food[1], BLOCK, BLOCK)
        )

        for segment in snake:
            pygame.draw.rect(
                SCREEN,
                GREEN,
                (segment[0], segment[1], BLOCK, BLOCK)
            )

        draw_score(score)
        pygame.display.update()

    game_over(score)


if __name__ == "__main__":
    rungame()