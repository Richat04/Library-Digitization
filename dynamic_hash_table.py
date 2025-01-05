from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        old_table = self.table
        self.size = get_next_size()
        self.table = [None]*self.size
        self.ele = 0

        if self.collision == "Chain":

            for i in old_table:
                if i != None:
                    for j in i:
                        self.insert(j)
        
        else:
            for i in old_table:
                if i != None:
                    self.insert(i)
        # IMPLEMENT THIS FUNCTION
        
        
    def insert(self, x):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(x)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        old_table = self.hashmap
        self.table_size = get_next_size()
        self.hashmap = [None]*self.table_size
        self.num_of_ele = 0

        if self.collision_type == "Chain":

            for i in old_table:
                if i != None:
                    for j in i:

                        self.insert(j)
        
        else:
            for i in old_table:
                if i != None:
                    self.insert(i)
        # IMPLEMENT THIS FUNCTION
        
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()