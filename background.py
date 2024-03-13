import pygame
import math
from pygame.locals import *
import time
import sys

WIDTH = 35
HEIGHT = 35
GRAPH = []
GRID_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)

# read file

def mapColor(num):
    color_dict = {
        1: (255, 51, 51),
        2: (255, 255, 51),
        3: (0, 204, 102),
        4: (0, 0, 204)
    }
    return color_dict.get(num, (255, 255, 255))
class Map:
    def __init__(self, graph):
        self.rows = len(graph) 
        self.cols = len(graph[0]) 
        self.graph = graph
        self.win = pygame.display.set_mode((self.cols * WIDTH + 300, self.rows * HEIGHT))
        self.win.fill((255, 255, 255))
    def drawGrid(self):
        for c in range(self.cols + 1):
            pygame.draw.line(self.win, GRID_COLOR, (c * WIDTH, 0), (c * WIDTH, self.rows * HEIGHT))
        for r in range(self.rows + 1):
            pygame.draw.line(self.win, GRID_COLOR, (0, r * HEIGHT), (self.cols * WIDTH, r * HEIGHT))
    def initMap(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if row == 0 or row == self.rows - 1 or col == 0 or col == self.cols - 1: 
                    color = (160, 160, 160)
                else:
                    color = mapColor(self.graph[row][col])  
                pygame.draw.rect(self.win, color, (col * WIDTH, row * HEIGHT, WIDTH, HEIGHT))
        self.drawGrid()
    def drawPath(self, points):
        for point in points:
            pygame.draw.rect(self.win, (255, 0, 255), (point[1] * WIDTH, point[0] * HEIGHT, WIDTH, HEIGHT))
            self.drawGrid()
            pygame.display.flip()
            time.sleep(0.1)
            pygame.draw.rect(self.win, (255, 255, 255), (point[1] * WIDTH, point[0] * HEIGHT, WIDTH, HEIGHT))
            self.drawGrid()
            pygame.display.flip()
            
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y


