from fileProcessing import *
from background import *
#from Astar import *
from AstarTSP import *
from DFS import *
import random

def main():
    filename = "input.txt"
    cols, rows, startPoint, endPoint, pickupPoints, polygons = readFile(filename)
    graph = createMap(cols, rows, startPoint, endPoint, pickupPoints, polygons)
    # Initialize Pygame
    pygame.init()
    # Set up the display
    points = aStarTSP(graph)
    map = Map(cols + 1, rows + 1, graph)
    pygame.display.set_caption('Map Grid')
    # Main loop
    running = True
    update = 1
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        if (update == 1):
            map.initMap()
            map.drawGrid()
            map.drawPath(points)
            update = 0
        # Update the display
        pygame.display.flip()
    path = []
    # Clean up
    pygame.quit()
    
if __name__ == "__main__":
    main()