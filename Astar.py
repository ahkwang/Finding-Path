import heapq

class Cell:
    def __init__(self):
        self.point=[0,0]
        self.f = float('inf')
        self.g = 0
        self.h = 0


def reverse_rows_using_loop(array):
  num_rows = len(array)
  for i in range(num_rows // 2):
    array[i], array[num_rows - 1 - i] = array[num_rows - 1 - i], array[i]
  return array


def find_positions(array, x):
    for i, row in enumerate(array):
        for j, element in enumerate(row):
            if element == x:
                return [i,j]


def heuristicFunction(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def isValid(a):
    return (a[0] >= 0) and (a[1] >= 0) and (a[0]<N) and (a[1]<M)

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



def aStar(array):
    array=reverse_rows_using_loop(array)
    global N,M
    N = len(array)
    M = len(array[0]) if array else 0
    start = find_positions(array,2)
    end = find_positions(array,3)
    d4i=[(1,0),(0,1),(-1,0),(0,-1)]
    if not isValid(start) or not isValid(end) :
        print("Source or destination is invalid")
        return
    
    if (array[start[0]][start[1]]==1) or (array[end[0]][end[1]]==1):
        print("Source or destination is invalid")
        return
    
    if (start[0]==end[0]) and (start[1] == end[1]):
        print("Source is equal Destination ,Source are already at the destination")
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
            if isValid(newPoint) and (array[xNew][yNew]!=1) and not close_list[xNew][yNew]:
                if isDestination(newPoint,end):
                    flagCheck = True
                    infoArray[xNew][yNew].point=t
                    print("Path cost ", (infoArray[t[0]][t[1]].g + 1))
                    return tracePath(end,infoArray)
                else:
                    gNew = infoArray[t[0]][t[1]].g + 1
                    hNew = heuristicFunction(newPoint,end)
                    fNew = gNew + hNew
                    
                    if (infoArray[xNew][yNew].f== float("inf")) or (infoArray[xNew][yNew].f > fNew):
                        heapq.heappush(open_list, (fNew,[xNew,yNew]))
                        # Update the cell details
                        infoArray[xNew][yNew].f = fNew
                        infoArray[xNew][yNew].h = hNew
                        infoArray[xNew][yNew].g = gNew
                        infoArray[xNew][yNew].point = t



def main():
    array = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0 ],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 1, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],   
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    ]
    
    res = aStar(array)
    print(res)
    

if __name__ == "__main__":
    main()

