import pygame

# pygame setup:
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 730
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
running = True
FPS = 60
background_colour = (232,190,232)
SCREEN.fill(background_colour)

#circle properties:
circle_x = SCREEN_HEIGHT // 2
circle_y = SCREEN_HEIGHT // 2
circle_radius = 64
circle_width = 8
circle_x_velocity = 0
circle_y_velocity = 0
circle_x_past = 99
circle_y_past = 99
CIRCLE_X_VELOCITY_MULTIPLIER = 1
CIRCLE_Y_VELOCITY_MULTIPLIER = 1

# circle colours:
COLOUR_INTERVAL = 48
circle_colour_primary = (circle_colour_primary_r := 128, circle_colour_primary_g := 0, circle_colour_primary_b := 128)
if circle_colour_primary_r + COLOUR_INTERVAL > 255: 
    circle_colour_secondary_r = circle_colour_primary_r - COLOUR_INTERVAL
else: 
    circle_colour_secondary_r = circle_colour_primary_r + COLOUR_INTERVAL
if circle_colour_primary_g + COLOUR_INTERVAL > 255: 
    circle_colour_secondary_g = circle_colour_primary_g - COLOUR_INTERVAL
else: 
    circle_colour_secondary_g = circle_colour_primary_g + COLOUR_INTERVAL
if circle_colour_primary_b + COLOUR_INTERVAL > 255: 
    circle_colour_secondary_b = circle_colour_primary_b - COLOUR_INTERVAL
else: 
    circle_colour_secondary_b = circle_colour_primary_b + COLOUR_INTERVAL
circle_colour_secondary = (circle_colour_secondary_r, circle_colour_secondary_g, circle_colour_secondary_b)

while running:
    # pygame.QUIT event means the user clicked X to close your window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    circle_x_velocity_previous = circle_x_velocity
    circle_y_velocity_previous = circle_y_velocity

    # accelerates the circle in the direction it is moving in:
    if (keys[pygame.K_SPACE]):
        if circle_x_velocity_previous >= 0 and circle_y_velocity_previous >= 0:
            circle_x_velocity += CIRCLE_X_VELOCITY_MULTIPLIER
            circle_y_velocity += CIRCLE_Y_VELOCITY_MULTIPLIER
        if circle_x_velocity_previous >= 0 and circle_y_velocity_previous < 0:
            circle_x_velocity += CIRCLE_X_VELOCITY_MULTIPLIER
            circle_y_velocity -= CIRCLE_Y_VELOCITY_MULTIPLIER
        if circle_x_velocity_previous < 0 and circle_y_velocity_previous >= 0:
            circle_x_velocity -= CIRCLE_X_VELOCITY_MULTIPLIER
            circle_y_velocity += CIRCLE_Y_VELOCITY_MULTIPLIER
        if circle_x_velocity_previous < 0 and circle_y_velocity_previous < 0:
            circle_x_velocity -= CIRCLE_X_VELOCITY_MULTIPLIER
            circle_y_velocity -= CIRCLE_Y_VELOCITY_MULTIPLIER

    # deccelerates the circle in the direction it is moving in:
    if (keys[pygame.K_BACKSPACE]):
        if circle_x_velocity != 0:
            if circle_x_velocity > 0:
                circle_x_velocity -= CIRCLE_X_VELOCITY_MULTIPLIER
            elif circle_x_velocity < 0:
                circle_x_velocity += CIRCLE_X_VELOCITY_MULTIPLIER
        if circle_y_velocity != 0:
            if circle_y_velocity > 0:
                circle_y_velocity -= CIRCLE_Y_VELOCITY_MULTIPLIER
            elif circle_y_velocity < 0:
                circle_y_velocity += CIRCLE_Y_VELOCITY_MULTIPLIER

    

    # fill the space of the circle before movement with background_colour to wipe away anything from last frame:
    pygame.draw.circle(SCREEN, background_colour, (circle_x_past,circle_y_past), circle_radius)

    # render the circle:
    pygame.draw.circle(SCREEN, circle_colour_primary, (circle_x,circle_y), circle_radius, circle_width, True, False, True)
    pygame.draw.circle(SCREEN, circle_colour_secondary, (circle_x,circle_y), circle_radius, circle_width, False, True, False, True)
    
    circle_x_past = circle_x
    circle_y_past = circle_y

    # move the circle according to its velocity:
    circle_x += circle_x_velocity
    circle_y += circle_y_velocity

    pygame.display.flip() # flip() the display to put your work on screen

    CLOCK.tick(FPS)  # limits FPS to 60

pygame.quit()