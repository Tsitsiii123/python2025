import pygame
pygame.init()

# Ορισμός παραθύρου
WIDTH, HEIGHT = 800, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Mario")

# Χρώματα
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)

# Mario (τετράγωνο προσωρινά)
x, y = 100, 300
width, height = 40, 60
vel = 5
jump = False
jumpCount = 10

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Κίνηση
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < WIDTH - width:
        x += vel

    # Άλμα
    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            jump = False
            jumpCount = 10

    # Σχεδίαση
    win.fill(WHITE)
    pygame.draw.rect(win, BLUE, (x, y, width, height))
    pygame.display.update()

pygame.quit()
