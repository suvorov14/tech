import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 700, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Арканоид")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

x = 10

pl_x = WIDTH // 2
pl_y = HEIGHT - 50
pl_size = 30
paddle = pygame.draw.rect(screen, WHITE, (pl_x - pl_size*5//2, pl_y, pl_size*5, pl_size))

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_size = 30
ball_speed_y = 5
ball_speed_x = -5
ball = pygame.draw.rect(screen, WHITE, (ball_x - ball_size//2, ball_y - ball_size//2, ball_size, ball_size))

running = True
clock = pygame.time.Clock()

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

class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, dx):
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (pl_x - pl_size*5//2, pl_y, pl_size*5, pl_size))
    pygame.draw.rect(screen, WHITE, (ball_x - ball_size//2, ball_y - ball_size//2, ball_size, ball_size))
    pygame.draw.rect(screen, WHITE, (x, x, pl_size* 4, pl_size ))
    pygame.draw.rect(screen, WHITE, (x, x*5, pl_size* 4, pl_size ))
    pygame.draw.rect(screen, WHITE, (x, x*9, pl_size* 4, pl_size ))
    pygame.draw.rect(screen, WHITE, (x*15, x, pl_size* 4, pl_size ))
    pygame.draw.rect(screen, WHITE, (x*15, x*5, pl_size* 4, pl_size ))
    pygame.draw.rect(screen, WHITE, (x*15, x*9, pl_size* 4, pl_size ))
    pygame.draw.rect(screen, WHITE, (x*29, x, pl_size* 4, pl_size ))
    pygame.draw.rect(screen, WHITE, (x*29, x*5, pl_size* 4, pl_size))
    pygame.draw.rect(screen, WHITE, (x*29, x*9, pl_size* 4, pl_size))
    pygame.draw.rect(screen, WHITE, (x*43, x, pl_size* 4, pl_size ))
    pygame.draw.rect(screen, WHITE, (x*43, x*5, pl_size* 4, pl_size))
    pygame.draw.rect(screen, WHITE, (x*43, x*9, pl_size* 4, pl_size))
    pygame.draw.rect(screen, WHITE, (x*57, x, pl_size* 4, pl_size ))
    pygame.draw.rect(screen, WHITE, (x*57, x*5, pl_size* 4, pl_size))
    pygame.draw.rect(screen, WHITE, (x*57, x*9, pl_size* 4, pl_size))
    pygame.draw.rect(screen, WHITE, (x, x*13, pl_size* 4, pl_size ))
    pygame.draw.rect(screen, WHITE, (x*15, x*13, pl_size* 4, pl_size))
    pygame.draw.rect(screen, WHITE, (x*29, x*13, pl_size* 4, pl_size))
    pygame.draw.rect(screen, WHITE, (x*43, x*13, pl_size* 4, pl_size ))
    pygame.draw.rect(screen, WHITE, (x*57, x*13, pl_size * 4, pl_size))



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pl_x -= 10
    if keys[pygame.K_RIGHT]:
        pl_x += 10
    '''if keys[pygame.K_UP]:
        pl_y -= 10    
    if keys[pygame.K_DOWN]:
        pl_y += 10'''

    if pl_x == 0:
        pl_x = 50
    if pl_x == 700:
        pl_x = 700 - 50

    if ball_x == 0 or ball_x == 700:
        ball_speed_x = -ball_speed_x
    if ball_y == 0 or ball_y == 800:
        ball_speed_y = -ball_speed_y
    
    if ball_y == pl_y and ball_x == pl_x:
        ball_speed_y = -ball_speed_y
        ball_speed_x = -ball_speed_x

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x == pl_x or ball_x == pl_x + 37.5 or ball_x == pl_x - 37.5 or ball_x == pl_x + 18.75 or ball_x == pl_x - 18.75 and ball_y - 75 == pl_y: 
        ball_speed_y = -ball_speed_y

    if ball.colliderect(paddle):
        ball.speed_y = -ball.speed_y
        ball.rect.bottom = paddle.rect.top


    draw_objects()
    clock.tick(60)
    pygame.display.flip()
