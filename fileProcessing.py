from background import *

def readFile(filename):
    f = open(filename, "r")
    # Read the space limits
    cols, rows = [int(x) for x in f.readline().split(',')]
    
    # Read the start point, end point and pickup points
    pointList = [int(x) for x in f.readline().split(',')]
    startPoint = Cell(pointList[0], pointList[1])
    endPoint = Cell(pointList[2], pointList[3])
    pickupPoints = []
    if len(pointList) > 4:
        pickupPoints = [Cell(pointList[i], pointList[i+1]) for i in range(4, len(pointList), 2)]
    
    # Read the number of polygons
    numPolygons = int(f.readline())
    polygons = []
    for _ in range(numPolygons):
        # Read each polygon
        polygonPoints = [int(x) for x in f.readline().split(',')]
        polygon = [Cell(polygonPoints[i], polygonPoints[i+1]) for i in range(0, len(polygonPoints), 2)]
        polygons.append(polygon)
    
    f.close()
    
    return cols, rows, startPoint, endPoint, pickupPoints, polygons
def createMap(cols, rows, startPoint, endPoint, pickupPoints, polygons):
    #initialize map
    map = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
    
    #initialize start and end point 
    map[rows - startPoint.y][startPoint.x] = 2
    map[rows - endPoint.y][endPoint.x] = 3
    
    #initialize pickup point
    for pickupPoint in pickupPoints:
        map[rows - pickupPoint.y][pickupPoint.x] = 4
    
    for polygon in polygons:   
        map = markPolygon(map, polygon, rows)
    return map

def markPolygon(grid, polygon, rows):
    def bresenham(x0, y0, x1, y1):
        """Bresenham's Line Algorithm"""
        points = []
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        x, y = x0, y0
        sx = -1 if x0 > x1 else 1
        sy = -1 if y0 > y1 else 1
        if dx > dy:
            err = dx / 2.0
            while x != x1:
                points.append((x, y))
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y1:
                points.append((x, y))
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy        
        points.append((x, y))
        return points

    for i in range(len(polygon)):
        x0, y0 = polygon[i].x, polygon[i].y
        x1, y1 = polygon[(i+1)%len(polygon)].x, polygon[(i+1)%len(polygon)].y
        for x, y in bresenham(x0, y0, x1, y1):
            grid[rows - y][x] = 1
    return grid
