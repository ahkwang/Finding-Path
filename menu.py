from background import *

functionList = ['DFS', 'GBFS', 'A*']
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
def drawButton(win, x, y, width, height, text, color):
    pygame.draw.rect(
        win,
        color,
        (x, y, width, height)
    )
    algoName = pygame.font.SysFont('Helvetica',35).render(text, True, (255, 255, 255))
    algoNameRect = algoName.get_rect(center = (x + width/2, y + height/2))
    win.blit(algoName, algoNameRect)
    return pygame.Rect(x, y, width, height)

def choice(xPos, yPos, buttonList):
    for butt in buttonList: 
        if butt.button.collidepoint(xPos, yPos):
            return 1

def mapChoice():
    mapWidth = 500
    mapHeight = 500
    win = pygame.display.set_mode((mapWidth, mapHeight))
    pygame.display.set_caption('Map choice')
    win.fill((255, 255, 255))
    mapList = ['MAP 1', 'MAP 2', 'MAP 3', 'MAP 4', 'MAP 5']
    c = 0
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
        pygame.display.flip()
        if c != 0: 
            return c 



