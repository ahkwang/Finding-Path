import heapq
import itertools
import numpy as np
import math

class Cell:
    def __init__(self):
        self.point=[0,0]
        self.f = float('inf')
        self.g = 0
        self.h = 0


class PathGraph:
    def __init__(self):
        self.paths = {}

    def add_path(self, start_point, end_point, path, cost):
        start_point = tuple(start_point)
        end_point = tuple(end_point)
        if start_point not in self.paths:
            self.paths[start_point] = {}
        self.paths[start_point][end_point] = path, cost

    def get_path(self, start_point, end_point):
        start_point = tuple(start_point)
        end_point = tuple(end_point)
        return self.paths.get(start_point, {}).get(end_point, None)


def changeBorderToOne(array):
    N = len(array)
    M = len(array[0]) if array else 0
    N-=1
    M-=1
    for i in range(N):
        array[i][0]=1
        array[i][M]=1
    for i in range(M):
        array[0][i]=1
        array[N][i]=1
    array[N][M]=1
    return array
    


def reverseRowsUsingLoop(array):
  num_rows = len(array)
  for i in range(num_rows // 2):
    array[i], array[num_rows - 1 - i] = array[num_rows - 1 - i], array[i]
  return array


def findPositions(array, x):
    for i, row in enumerate(array):
        for j, element in enumerate(row):
            if element == x:
                return [i,j]
    return None


def heuristicFunction(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def isValid(a,N,M):
    return (a[0] > 0) and (a[1] > 0) and (a[0]<N-1) and (a[1]<M-1)

def isDestination(a,des):
    return (a[0] == des[0]) and (a[1] == des[1])


def tracePath(dest, infoArray):
    path = []
    x = dest[0]
    y = dest[1]
    while not (infoArray[x][y].point == [x,y]):
        path.append([x,y])
        tmpPoint=infoArray[x][y].point
        x=tmpPoint[0]
        y=tmpPoint[1]
    path.append([x,y])
  
    path.reverse()
    return path

def findPickUpPoint(array, x):
    res=[]
    for i, row in enumerate(array):
        for j, element in enumerate(row):
            if element == x:
                res.append([i,j])
    return res

def aStarPlus(array,start, end, pathsaving):

    if pathsaving.get_path(start,end)!=None:
        return pathsaving.get_path(start,end)
    N = len(array)
    M = len(array[0]) if array else 0
    d4i=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    if not isValid(start,N,M) or not isValid(end,N,M) :
        #print("Source or destination is invalid")
        return
    
    if (array[start[0]][start[1]]==1) or (array[end[0]][end[1]]==1):
        #print("Source or destination is invalid")
        return
    
    if (start[0]==end[0]) and (start[1] == end[1]):
        #print("Source is equal Destination ,Source are already at the destination")
        return
    
    close_list= [[False for _ in range(M)]for _ in range(N)]
    infoArray= [[Cell() for _ in range(M)]for _ in range(N)]


    i=start[0]
    j=start[1]

    infoArray[i][j].f = 0
    infoArray[i][j].g = 0
    infoArray[i][j].h = 0
    infoArray[i][j].point = start
    
    open_list = []
    heapq.heappush(open_list, (0, start))


    while len(open_list)>0:
        x= heapq.heappop(open_list)
        t= x[1]

        close_list[t[0]][t[1]] = True
        for change in d4i:
            xNew = t[0] + change[0]
            yNew = t[1] + change[1]
            newPoint = [xNew,yNew]
            if not isValid(newPoint,N,M):
                continue

            if change[0]==1 and change[1]==1 and array[t[0]+1][t[1]]==1 and array[t[0]][t[1]+1]==1:
                continue
            if change[0]==1 and change[1]==-1 and array[t[0]+1][t[1]]==1 and array[t[0]][t[1]-1]==1:
                continue
            if change[0]==-1 and change[1]==-1 and array[t[0]-1][t[1]]==1 and array[t[0]][t[1]-1]==1:
                continue
            if change[0]==-1 and change[1]==1 and array[t[0]-1][t[1]]==1 and array[t[0]][t[1]+1]==1:
                continue
            
            if (array[xNew][yNew]!=1) and not close_list[xNew][yNew]:
                if isDestination(newPoint,end):
                    infoArray[xNew][yNew].point=t
                    t1= tracePath(end,infoArray)

                    cheo=0
                    if change[0]==1:
                        if change[1]==1 or change[1]==-1:
                            cheo = 0.5
                    if change[0]==-1:
                        if change[1]==1 or change[1]==-1:
                            cheo=0.5

                    t2 =infoArray[t[0]][t[1]].g + 1 + cheo
                    pathsaving.add_path(start,end,t1,t2)
                    return pathsaving.get_path(start,end)
                    #return t1,t2
                else:
                    gNew = infoArray[t[0]][t[1]].g + 1
                    hNew = heuristicFunction(newPoint,end)
                    fNew = gNew + hNew
                    
                    if (infoArray[xNew][yNew].f== float("inf")) or (infoArray[xNew][yNew].f > fNew):
                        heapq.heappush(open_list, (fNew,[xNew,yNew]))
                        infoArray[xNew][yNew].f = fNew
                        infoArray[xNew][yNew].h = hNew
                        infoArray[xNew][yNew].g = gNew
                        infoArray[xNew][yNew].point = t


def ASTAR(array):
    #array=reverse_rows_using_loop(array)
    array=changeBorderToOne(array)
    N = len(array)
    M = len(array[0]) if array else 0
    start = findPositions(array,2)
    end = findPositions(array,3)
    if start==None:
        print("No Source found")
        return None
    if  end == None:
        print("No Destination found")
        return None

    if not isValid(start,N,M) or not isValid(end,N,M):
        print("Source or destination is invalid")
        return

    if (array[start[0]][start[1]] == 1) or (array[end[0]][end[1]] == 1):
        print("Source or destination is invalid")
        return

    if (start[0] == end[0]) and (start[1] == end[1]):
        print("Source is equal Destination, Source are already at the destination")
        return

    pupl = findPickUpPoint(array, 4) # pick up point list
    permutation =[list(perm) for perm in itertools.permutations(pupl)]
    

    # Example usage:
    pathSaving = PathGraph()

    optimalCost = float('inf')
    res = None
    
    for listPoint in permutation:
        listPoint.append(end)
        currentCost = 0
        currentPoint = start
        childPath = []
        for i in listPoint:
            if aStarPlus(array,currentPoint,i,pathSaving)==None:
                break
            else:
                t1,t2= aStarPlus(array,currentPoint,i,pathSaving)
                childPath+=t1
                currentCost += t2
                currentPoint = i
                if i!= end :
                    childPath= childPath[:-1]
        if currentCost < optimalCost and childPath!=[]:
            optimalCost = currentCost
            res = childPath

    #print (optimalCost)
    return res
    return res,optimalCost


def main():
    array = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0 ],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 ],
        [0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0 ],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],   
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    ]
    res = ASTAR(array)
    print(res)
    

if __name__ == "__main__":
    main()

