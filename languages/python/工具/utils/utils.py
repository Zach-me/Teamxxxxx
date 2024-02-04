# swap list index

class utils(object):
    def __init__(self) -> None:
        
        pass

    def swap(list, left, right):
        temp = list[left]
        list[left] = list[right]
        list[right]= temp
        return list
    
list = [1,2,3,4,5]
list1 = utils.swap(list, 2, 3)
print(list1)
