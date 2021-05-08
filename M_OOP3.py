class Square():
    
    def __init__(self):
        pass

    def same(obj1, obj2):
      if obj1 == obj2:
        return obj1 is obj2
      else:
        return obj1 is not obj2
    
sq_1 = Square()
sq_2 = sq_1

print (same(sq_1, sq_2))



class Square:
    def __init__(self):
        pass
 
def same(object1, object2):
    return object1 is object2
