from background import *
from aStar import *
from DFSTSP import *
from Greedy import *

FILENAME = ['input0.txt', 'input1.txt', 'input2.txt', 'input3.txt']
BACKGROUND_COLOR = (255, 2, 3)
TEXT_COLOR = (204, 204, 255)
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 60

class Button:
    def __init__(self, button, name):
        self.button = button
        self.name = name
def drawButtonList(win, x, y, width, height, functionList):
    buttonList = []
    i = 0
    for function in functionList:
        buttonList.append(Button(drawButton(win, x, y + height*1.5*i, width, height, function, BACKGROUND_COLOR), function))
        i+=1
    return buttonList
def drawButton(win, x, y, width, height, text, buttonColor, textColor = (255, 255, 255), size = 35):
    pygame.draw.rect(
        win,
        buttonColor,
        (x, y, width, height)
    )
    algoName = pygame.font.SysFont('Helvetica', size).render(text, True, textColor)
    algoNameRect = algoName.get_rect(center = (x + width/2, y + height/2))
    win.blit(algoName, algoNameRect)
    return pygame.Rect(x, y, width, height)

def choice(xPos, yPos, buttonList):
    for i in range(len(buttonList)): 
        if buttonList[i].button.collidepoint(xPos, yPos):
            return i
    return -1 
def findPath(graph, i):
    if (i == 0):
        return dfsTSP(graph)
    if (i == 1):
        return Greedy(graph)
    if (i == 2):
        return ASTAR(graph)
def mapChoice():
    mapWidth = 500
    mapHeight = 400
    win = pygame.display.set_mode((mapWidth, mapHeight))
    pygame.display.set_caption('Map choice')
    win.fill((255, 255, 255))
    mapList = ['MAP 1', 'MAP 2', 'MAP 3', 'MAP 4']
    c = -1
    buttonList = drawButtonList(win, 250 - BUTTON_WIDTH/2, 20, BUTTON_WIDTH, BUTTON_HEIGHT, mapList)
    while True:
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
                    c = choice(xPos, yPos, buttonList)
                    if c is not None and c >= 0 and c < len(FILENAME):  # Check if the index is valid
                        return FILENAME[c]
        pygame.display.flip()




