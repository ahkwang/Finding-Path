import math
import sys
MAX = 10000



def read_Array(array2D, startPoint, endPoint, pickupPoint):
    
    for i, row in enumerate(array2D):
        for j, element in enumerate(row):
            if element == 3:
                endPoint[0] = i
                endPoint[1] = j
            if element == 2:
                startPoint[0] = i
                startPoint[1] = j
            if element == 4:
                indexPoint=[0,0]
                indexPoint[0] = i
                indexPoint[1] = j
                pickupPoint.append(indexPoint)       


def PytagoDistance ( point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def check_Valid(point, array2D, arrayPath):
    if  point[0] < 1 or point[0] > len(array2D)-2 or point[1] < 1 or point[1] > len(array2D[0])-2 or array2D[point[0]][point[1]] == 1 :
        return False
    if point in arrayPath:
        return False
    return True

def Gready_Travel (startPoint, endPoint, array2D, cost ):

    indexPoint = startPoint[:]
    Path = []
    cost[0] = 0
    while (indexPoint != endPoint):
        Path.append(indexPoint)

        right=[indexPoint[0]+1,indexPoint[1]]
        left=[indexPoint[0]-1,indexPoint[1]]
        up=[indexPoint[0],indexPoint[1]+1]
        down=[indexPoint[0],indexPoint[1]-1]


        distance = MAX
        
        if(check_Valid(up,array2D,Path) and distance > PytagoDistance(up,endPoint)):
            indexPoint=up[:]
            distance = PytagoDistance(up,endPoint)
        if(check_Valid(right,array2D,Path) and distance > PytagoDistance(right,endPoint)):
            indexPoint=right[:]
            distance = PytagoDistance(right,endPoint)
        if(check_Valid(down,array2D,Path) and distance > PytagoDistance(down,endPoint)):
            indexPoint=down[:]
            distance = PytagoDistance(down,endPoint)
        if(check_Valid(left,array2D,Path) and distance > PytagoDistance(left,endPoint)):
            indexPoint=left[:]
            distance = PytagoDistance(down,endPoint)
            
        
        if distance == MAX:
            return None
        
        
        cost[0] += 1

    return Path


def dp_TSP(endPoint, pickupPoint, array2D, main_Path): 
    if len(pickupPoint) == 2 :
        sub_cost = [0]
        sub_cost [0] = 0
        main_Path += Gready_Travel(pickupPoint[0], endPoint, array2D, sub_cost)
        return sub_cost[0]

    cost = MAX
    temp_pickupPoint = pickupPoint.copy()
    temp_pickupPoint.remove(endPoint)
    res_Path=[]

    for indexPoint in temp_pickupPoint[1:]:
        sub_Path=[]
        
        sub_cost = [0]
        sub_cost [0] = 0
        endPath = Gready_Travel(indexPoint, endPoint, array2D, sub_cost)

        temp = min(cost, dp_TSP(indexPoint, temp_pickupPoint, array2D, sub_Path) + sub_cost[0])

        if (temp < cost):
            cost = temp 
            sub_Path += endPath
            res_Path = sub_Path[:]
    
    main_Path += res_Path
    return cost


def Greedy(array2D):
    startPoint = [0, 0]
    endPoint = [0, 0]
    pickupPoint = []
    main_Path = []

    read_Array(array2D, startPoint, endPoint, pickupPoint)

    cost = [0]
    cost[0] = MAX

    if len(pickupPoint) == 0:
        path = Gready_Travel(startPoint, endPoint, array2D, cost)
        if path is not None:
            main_Path += path
        else:
            return None  # Or any appropriate handling

    pickupPoint.insert(0, startPoint)
    temp_pickupPoint = pickupPoint.copy()
    res_Path = []  # save the path has less cost after the recur

    for indexPoint in temp_pickupPoint[1:]:
        sub_Path = []  # save the path at each recursion 
        sub_cost = [0]
        sub_cost[0] = 0
        endPath = Gready_Travel(indexPoint, endPoint, array2D, sub_cost)
        if endPath is not None:
            endPath.append(endPoint)

            temp = min(cost[0], dp_TSP(indexPoint, temp_pickupPoint, array2D, sub_Path) + sub_cost[0])

            if temp < cost[0]:
                cost[0] = temp 
                sub_Path += endPath
                res_Path = sub_Path[:]
        else:
            return None  # Or any appropriate handling

    main_Path += res_Path
    return main_Path

    

def main():
    array2D = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 2, 0, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],       
    ]
    
    try:

        path = Greedy(array2D)
        
    except EnvironmentError as e:
        print ("Error: ", e)
    else:
        print(path,"\n")

if __name__ == "__main__":
    main()

