import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 15
BRICK_WIDTH, BRICK_HEIGHT = 75, 20
BRICK_ROWS, BRICK_COLS = 5, 10

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 255, 255)
GREEN = (255, 255, 255)
BLUE = (255, 255, 255)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")

# Класс для мяча
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.speed_x = 5
        self.speed_y = -5

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Отскок от стен
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top < 0:
            self.speed_y = -self.speed_y

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = 5
        self.speed_y = -5

# Класс для платформы
class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, dx):
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

# Класс для блоков
class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)

# Главная функция игры
def main():
    clock = pygame.time.Clock()
    ball = Ball()
    paddle = Paddle()
    bricks = [Brick(x * (BRICK_WIDTH + 5) + 50, y * (BRICK_HEIGHT + 5) + 50)
              for y in range(BRICK_ROWS) for x in range(BRICK_COLS)]

    score = 0
    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move(-10)
        if keys[pygame.K_RIGHT]:
            paddle.move(10)

        # Движение мяча
        ball.move()

        # Отскок от платформы
        if ball.rect.colliderect(paddle.rect):
            ball.speed_y = -ball.speed_y
            ball.rect.bottom = paddle.rect.top  # Убедимся, что мяч не застрял в платформе

        # Проверка столкновений с блоками
        for brick in bricks[:]:
            if ball.rect.colliderect(brick.rect):
                ball.speed_y = -ball.speed_y
                bricks.remove(brick)
                score += 5

        # Проверка падения мяча
        if ball.rect.bottom > HEIGHT:
            ball.reset()
            score += 5  # Сбросить счёт при падении мяча

        # Рисование объектов
        pygame.draw.ellipse(screen, RED, ball.rect)
        pygame.draw.rect(screen, BLUE, paddle.rect)
        for brick in bricks:
            pygame.draw.rect(screen, GREEN, brick.rect)

        # Отображение счета
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()