import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FONT = pygame.font.Font(None, 24)
OPTIONS = ["Map 1", "Map 2", "Map 3", "Map 4"]
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a class for the dropdown
class Dropdown:
    def __init__(self, x, y, w, h, options, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.options = options
        self.active_option = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        text_surface = FONT.render(self.options[self.active_option], True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active_option = (self.active_option + 1) % len(self.options)

def choose_map():
    # Create a dropdown menu
    dropdown = Dropdown(50, 50, 200, 50, OPTIONS, COLOR_INACTIVE)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            dropdown.handle_event(event)

        screen.fill((255, 255, 255))
        dropdown.draw(screen)
        pygame.display.flip()

    return dropdown.active_option

# Call the choose_map function to let the user choose a map
chosen_map = choose_map()

# Now you can use chosen_map to load the chosen map and run your algorithms