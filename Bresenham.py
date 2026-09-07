import pygame

pygame.init()

# Window
WIDTH = 900
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham Line Drawing Algorithm")

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
    pygame.draw.line(
        screen, BLACK,
        (0, origin_y),
        (WIDTH, origin_y), 3
    )

    # Y-axis
    pygame.draw.line(
        screen, BLACK,
        (origin_x, 0),
        (origin_x, origin_y), 3
    )


def graph_to_screen(x, y):

    screen_x = origin_x + x * scale
    screen_y = origin_y - y * scale

    return screen_x, screen_y


def bresenham_line(x1, y1, x2, y2):

    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Direction of movement
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    # Decision parameter
    error = dx - dy

    while True:

        points.append((x1, y1))

        # Stop when endpoint is reached
        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * error

        if e2 > -dy:
            error = error - dy
            x1 = x1 + sx

        if e2 < dx:
            error = error + dx
            y1 = y1 + sy

    return points


# Starting and ending points
x1, y1 = 2, 2
x2, y2 = 10, 6

# Calculate Bresenham points
points = bresenham_line(x1, y1, x2, y2)


running = True

while running:

    screen.fill(WHITE)

    # Draw coordinate graph
    draw_graph()

    # Draw line between points
    for i in range(len(points) - 1):

        p1 = graph_to_screen(points[i][0], points[i][1])
        p2 = graph_to_screen(points[i + 1][0], points[i + 1][1])

        pygame.draw.line(
            screen, BLUE,
            p1, p2, 3
        )

    # Draw individual pixels/points
    for x, y in points:

        px, py = graph_to_screen(x, y)

        pygame.draw.circle(
            screen, RED,
            (px, py), 6
        )

    # Starting point
    start = graph_to_screen(x1, y1)
    pygame.draw.circle(screen, BLACK, start, 9)

    # Ending point
    end = graph_to_screen(x2, y2)
    pygame.draw.circle(screen, BLACK, end, 9)

    pygame.display.flip()

    # Close window
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


pygame.quit()