import pygame

# pygame setup:
pygame.init()
SCREEN = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()
CLOCK = pygame.time.Clock()
running = True
FPS = 60
background_colour = (232,190,232)
SCREEN.fill(background_colour)

#circle properties:
circle_centre_x = SCREEN_HEIGHT // 2
circle_centre_y = SCREEN_HEIGHT // 2
circle_radius = 64
circle_width = 0 # 0 for a filled circle
circle_x_velocity = 0
circle_y_velocity = 0
circle_x_acceleration = 2
circle_y_acceleration = 2
circle_x_past = 100
circle_y_past = 100
GRAVITY = 0.25
HORIZONTAL_GRAVITY = 1
has_trail = False

circle_x_velocity_max = 20
circle_x_velocity_min = 0

circle_y_velocity_max = 10
circle_y_velocity_min = -10

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
    
    keys_pressed = pygame.key.get_pressed()
    circle_x_past = circle_centre_x
    circle_y_past = circle_centre_y

    # fill the screen with background_colour to wipe away anything from last frame: 
    if has_trail == False:
        SCREEN.fill(background_colour)

    # render the circle:
    pygame.draw.circle(SCREEN, circle_colour_primary, (circle_centre_x,circle_centre_y), circle_radius, circle_width, True, False, True)
    pygame.draw.circle(SCREEN, circle_colour_secondary, (circle_centre_x,circle_centre_y), circle_radius, circle_width, False, True, False, True)
    
    # move the circle according to the player's input:
    if keys_pressed[pygame.K_w]:
       circle_y_velocity += -1 * circle_y_acceleration
    if keys_pressed[pygame.K_s]:
       circle_y_velocity += 1 * circle_y_acceleration
    if keys_pressed[pygame.K_a]:
       circle_x_velocity += -1 * circle_x_acceleration
    if keys_pressed[pygame.K_d]:
       circle_x_velocity += 1 * circle_x_acceleration
    
    # keep the velocities within a range:
    if circle_x_velocity > circle_x_velocity_max:
        circle_x_velocity = circle_x_velocity_max
    if circle_x_velocity < circle_x_velocity_min:
        circle_x_velocity = circle_x_velocity_min
    if circle_y_velocity > circle_y_velocity_max:
        circle_y_velocity = circle_y_velocity_max
    if circle_y_velocity < circle_y_velocity_min:
        circle_y_velocity = circle_y_velocity_min

    circle_y_velocity += GRAVITY
    circle_x_velocity += HORIZONTAL_GRAVITY

    circle_centre_x += circle_x_velocity
    circle_centre_y += circle_y_velocity

    # keep the circle within the borders of the screen:w
    if circle_centre_y - circle_radius < 0:
        circle_y_velocity = 0
        circle_centre_y = 0 + circle_radius # stops the circle from getting stuck
    if circle_centre_y + circle_radius > SCREEN_HEIGHT:
        circle_y_velocity = 0
        circle_centre_y = SCREEN_HEIGHT - circle_radius # stops the circle from getting stuck

    # transitions to the next screen
    if circle_centre_x - circle_radius > SCREEN_WIDTH:
        circle_centre_x = -circle_radius
        SCREEN.fill(background_colour)

    pygame.display.flip() # flip() the display to put your work on screen

    CLOCK.tick(FPS)  # limits FPS to 60

pygame.quit()