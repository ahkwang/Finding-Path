from fileProcessing import *
from background import *

def main():
    filename = "input.txt"
    cols, rows, startPoint, endPoint, pickupPoints, polygons = readFile(filename)
    graph = createMap(cols, rows, startPoint, endPoint, pickupPoints, polygons)
    # Initialize Pygame
    pygame.init()
    # Set up the display
    map = Map(cols + 1, rows + 1, graph)
    pygame.display.set_caption('Map Grid')
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        map.initMap()
        map.drawGrid()
        # Update the display
        pygame.display.flip()

    # Clean up
    pygame.quit()
    
if __name__ == "__main__":
    main()