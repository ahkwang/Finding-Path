from fileProcessing import *
from background import *
from Astar import *
from DFS import *
from menu import *
from DFSTSP import *
from Greedy import *
import random

def main():
    # read from input 
    filename = "input4.txt"
    cols, rows, startPoint, endPoint, pickupPoints, polygons = readFile(filename)
    #return 2d array assigned to graph 
    graph = createMap(cols, rows, startPoint, endPoint, pickupPoints, polygons)
    points = ASTAR(graph)

    # Initialize Pygame
    pygame.init()
    # Set up the displays

    map = Map(graph)
    pygame.display.set_caption('Map Grid')
    # Main loop
    running = True
    update = 1
    functionList = ['DFS', 'GBFS', 'A*']
    buttonList = drawButtonList(map.win, map.cols * WIDTH + 20, 20, BUTTON_WIDTH, BUTTON_HEIGHT, functionList)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    xPos, yPos = pygame.mouse.get_pos()
                    choice(xPos, yPos, buttonList)
        if (update == 1):
            map.initMap()
            map.drawGrid()
            if points is None:
                print("no path found.")
            else:
                map.drawPath(points)
            update = 0
        # Update the display
        pygame.display.flip()
    path = []
    # Clean up
    pygame.quit()
    
if __name__ == "__main__":
    main()