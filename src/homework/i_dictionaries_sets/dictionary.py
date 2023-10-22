#

def get_p_distance(list1, list2):
    count = 0
    for n in range(len(list1)):
        if(list1[n] != list2[n]):
            count += 1          
    return count

def get_p_distance_matrix(matrix1):
    maxValue = len(matrix1)
    listTable = []

    for r in range(0, maxValue):
        row = []

        for c in range(0, maxValue):
                row.append(get_p_distance(matrix1[r], matrix1[c]) / 10)
        listTable.append(row)

    return listTable