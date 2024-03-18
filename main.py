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
    pygame.init()
    filename = mapChoice()
    cols, rows, startPoint, endPoint, pickupPoints, polygons = readFile(filename)
    #return 2d array assigned to graph 
    graph = createMap(cols, rows, startPoint, endPoint, pickupPoints, polygons)
    # Set up the displays
    # Main loop
    map = Map(graph)
    running = True
    funcChoice = -1
    functionList = ['DFS', 'GBFS', 'A*', 'BACK']
    buttonList = drawButtonList(map.win, map.cols * WIDTH + 20, 20, BUTTON_WIDTH, BUTTON_HEIGHT, functionList)
    map.initMap()
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
                    funcChoice = choice(xPos, yPos, buttonList)
        if (funcChoice != -1):
            if (funcChoice == 3):
                main()
            else:
                map.initMap()
                points = findPath(graph, funcChoice)
                if points is None:
                    print("no path found.")
                else:
                    map.drawPath(points)
                funcChoice = -1
        # Update the display
        pygame.display.flip()
    path = []
    # Clean up
    pygame.quit()
    
if __name__ == "__main__":
    main()