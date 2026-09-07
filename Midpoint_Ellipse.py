import pygame

pygame.init()

WIDTH = 900
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Ellipse Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (210, 210, 210)
BLUE = (0, 100, 255)
RED = (255, 0, 0)

# Graph settings
scale = 35
origin_x = 450
origin_y = 350


def draw_graph():

    # Vertical grid lines
    for x in range(origin_x, WIDTH, scale):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))

    for x in range(origin_x, 0, -scale):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))

    # Horizontal grid lines
    for y in range(origin_y, HEIGHT, scale):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

    for y in range(origin_y, 0, -scale):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

    # X-axis
    pygame.draw.line(
        screen, BLACK,
        (0, origin_y),
        (WIDTH, origin_y), 2
    )

    # Y-axis
    pygame.draw.line(
        screen, BLACK,
        (origin_x, 0),
        (origin_x, HEIGHT), 2
    )


def graph_to_screen(x, y):

    screen_x = origin_x + x * scale
    screen_y = origin_y - y * scale

    return screen_x, screen_y


def midpoint_ellipse(cx, cy, rx, ry):

    points = []

    x = 0
    y = ry

    rx2 = rx * rx
    ry2 = ry * ry

    dx = 2 * ry2 * x
    dy = 2 * rx2 * y

    # Region 1 decision parameter
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)

    # Region 1
    while dx < dy:

        # 4-way symmetry
        points.append((cx + x, cy + y))
        points.append((cx - x, cy + y))
        points.append((cx + x, cy - y))
        points.append((cx - x, cy - y))

        if p1 < 0:

            x += 1
            dx = dx + 2 * ry2
            p1 = p1 + dx + ry2

        else:

            x += 1
            y -= 1

            dx = dx + 2 * ry2
            dy = dy - 2 * rx2

            p1 = p1 + dx - dy + ry2

    # Region 2 decision parameter
    p2 = (
        ry2 * (x + 0.5) * (x + 0.5)
        + rx2 * (y - 1) * (y - 1)
        - rx2 * ry2
    )

    # Region 2
    while y >= 0:

        # 4-way symmetry
        points.append((cx + x, cy + y))
        points.append((cx - x, cy + y))
        points.append((cx + x, cy - y))
        points.append((cx - x, cy - y))

        if p2 > 0:

            y -= 1
            dy = dy - 2 * rx2
            p2 = p2 + rx2 - dy

        else:

            y -= 1
            x += 1

            dx = dx + 2 * ry2
            dy = dy - 2 * rx2

            p2 = p2 + dx - dy + rx2

    return points


# Ellipse center
cx = 0
cy = 0

# Horizontal and vertical radius
rx = 8
ry = 5

points = midpoint_ellipse(cx, cy, rx, ry)


running = True

while running:

    screen.fill(WHITE)

    draw_graph()

    # Draw ellipse points
    for x, y in points:

        px, py = graph_to_screen(x, y)

        pygame.draw.circle(
            screen,
            RED,
            (px, py),
            4
        )

    # Draw center
    center = graph_to_screen(cx, cy)

    pygame.draw.circle(
        screen,
        BLACK,
        center,
        7
    )

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


pygame.quit()