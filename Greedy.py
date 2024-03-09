import math
def read_Array(array2D, startPoint, endPoint, pickupPoint):
    for i, row in enumerate(array2D):
        for j, element in enumerate(row):
            if element == 3:
                endPoint[0] = j
                endPoint[1] = len(array2D)-1-i
            if element == 2:
                startPoint[0] = j
                startPoint[1] = len(array2D)-1-i
            


def caculate_Distance ( point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def check_Valid(point, array2D, arrayPath):
    if  point[0] < 0 or (point[0] > len(array2D[0])-1) or point[1] < 0 or point[1] > len(array2D)-1 or array2D[len(array2D)-1-point[1]][point[0]] == 1 :
        return False
    if point in arrayPath:
        return False
    return True


def Greedy (array2D):
    startPoint=[0,0]
    endPoint=[0,0]
    pickupPoint=[]
    read_Array(array2D, startPoint, endPoint, pickupPoint)


    indexPoint= startPoint[:]

    arrayPath=[]
    arrayPath.append(indexPoint)
    
    while (array2D[len(array2D)-1-indexPoint[1]][indexPoint[0]]!=3):

        right=[indexPoint[0]+1,indexPoint[1]]
        left=[indexPoint[0]-1,indexPoint[1]]
        up=[indexPoint[0],indexPoint[1]+1]
        down=[indexPoint[0],indexPoint[1]-1]


        distance=len(array2D)+len(array2D[0]) # có thể gán là một số rất lớn bất kì 
        
        if(check_Valid(up,array2D,arrayPath) and distance > caculate_Distance(up,endPoint)):
            indexPoint=up[:]
            distance = caculate_Distance(up,endPoint)
        if(check_Valid(right,array2D,arrayPath) and distance > caculate_Distance(right,endPoint)):
            indexPoint=right[:]
            distance = caculate_Distance(right,endPoint)
        if(check_Valid(down,array2D,arrayPath) and distance > caculate_Distance(down,endPoint)):
            indexPoint=down[:]
            distance = caculate_Distance(down,endPoint)
        if(check_Valid(left,array2D,arrayPath) and distance > caculate_Distance(left,endPoint)):
            indexPoint=left[:]
            distance = caculate_Distance(left,endPoint)
        
        arrayPath.append(indexPoint)

    return arrayPath
    
    
    
    
    
def main():
    array = [
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 3, 0],
        [0, 0, 2, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
       
    ]
    
    
    res = Greedy(array)
    print(res)
    

if __name__ == "__main__":
    main()

