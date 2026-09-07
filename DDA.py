import pygame

pygame.init()

# Window
WIDTH = 900
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (210, 210, 210)
BLUE = (0, 100, 255)
RED = (255, 0, 0)

# Graph settings
scale = 50
origin_x = 100
origin_y = 600


def draw_graph():
    # Vertical grid lines
    for x in range(origin_x, WIDTH, scale):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))

    # Horizontal grid lines
    for y in range(origin_y, 0, -scale):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

    # X-axis
    pygame.draw.line(screen, BLACK,
                     (0, origin_y),
                     (WIDTH, origin_y), 3)

    # Y-axis
    pygame.draw.line(screen, BLACK,
                     (origin_x, 0),
                     (origin_x, HEIGHT), 3)


def graph_to_screen(x, y):
    """Convert graph coordinates to screen coordinates."""
    screen_x = origin_x + x * scale
    screen_y = origin_y - y * scale

    return screen_x, screen_y


def dda_line(x1, y1, x2, y2):

    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1

    points = []

    for i in range(steps + 1):

        # Round because pixels use integer coordinates
        px = round(x)
        py = round(y)

        points.append((px, py))

        x += x_increment
        y += y_increment

    return points


# DDA input points
x1, y1 = 2, 2
x2, y2 = 10, 6

# Calculate DDA points
points = dda_line(x1, y1, x2, y2)

running = True

while running:

    screen.fill(WHITE)

    # Draw graph
    draw_graph()

    # Draw line connecting DDA points
    for i in range(len(points) - 1):

        p1 = graph_to_screen(points[i][0], points[i][1])
        p2 = graph_to_screen(points[i + 1][0], points[i + 1][1])

        pygame.draw.line(screen, BLUE, p1, p2, 3)

    # Draw individual DDA points
    for x, y in points:

        px, py = graph_to_screen(x, y)

        pygame.draw.circle(screen, RED, (px, py), 6)

    # Mark starting point
    start = graph_to_screen(x1, y1)
    pygame.draw.circle(screen, BLACK, start, 9)

    # Mark ending point
    end = graph_to_screen(x2, y2)
    pygame.draw.circle(screen, BLACK, end, 9)

    pygame.display.flip()

    # Close window
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

pygame.quit()