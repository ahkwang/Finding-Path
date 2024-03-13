from background import *

functionList = ['DFS', 'GBFS', 'A*']
BACKGROUND_COLOR = (255, 2, 3)
TEXT_COLOR = (204, 204, 255)
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 60

def drawButtonList(win, x, y, width, height, functionList):
    buttonList = []
    i = 0
    for function in functionList:
        buttonList.append(drawButton(win, x, y + height*1.5*i, width, height, function, BACKGROUND_COLOR))
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
    for button in buttonList: 
        if button.collidepoint(xPos, yPos):
            print("Clicked")

def mapChoice()
