from fileProcessing import *
from background import *
from Astar import *
from menu import *
from DFSTSP import *
from Greedy import *

def main():
    pygame.init()
    filename = mapChoice()
    cols, rows, startPoint, endPoint, pickupPoints, polygons = readFile(filename)
    graph = createMap(cols, rows, startPoint, endPoint, pickupPoints, polygons)
    map = Map(graph)
    running = True
    funcChoice = -1
    functionList = ['DFS', 'GBFS', 'A*', 'BACK']
    buttonList = drawButtonList(map.win, map.cols * WIDTH + 20, 20, BUTTON_WIDTH, BUTTON_HEIGHT, functionList)
    pygame.display.set_caption('Robot Finding Path')
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
                running = False
            else:
                map.initMap()
                points, cost = findPath(graph, funcChoice) #path 
                map.drawPath(points, cost)
                funcChoice = -1
        # Update the display
        pygame.display.flip()
    # Clean up
    pygame.quit()
    if not running:
        main()
    
if __name__ == "__main__":
    main()