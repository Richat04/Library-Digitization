from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        pass
    
    def insert(self, x):
        pass
    
    def find(self, key):
        pass
    
    def get_slot(self, key):
        pass
    
    def get_load(self):
        pass
    
    def __str__(self):
        pass
    
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        pass
    
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        self.table = [None]*params[-1]
        self.collision = collision_type
        self.params = params
        self.ele = 0                 #gives the number of elements in the table
        self.size = self.params[-1]
        
    
    def insert(self, key):
        if self.collision == "Chain":
            p = self.get_slot(key)
            if self.table[p] is None:
                self.table[p] = []
                self.table[p].append(key)
            else:
                l = self.table[p]
                for i in l:
                    if i == key:
                        return
                l.append(key)
            self.ele+=1

        elif self.collision == "Linear":
            p = self.get_slot(key)
            original_index = p

            while self.table[p] is not None and self.table[p] != key:
                p = (p+1)%self.size

                if p == original_index:
                    raise Exception("Table is full")
            
            if self.table[p] is None:
                self.table[p] = key
                self.ele+=1

        else:
            index = self.get_slot(key)
            
            step = self.hash2(key)
            original_index = index

            while self.table[index] is not None and self.table[index] != key:
                index = (index + step)%self.size

                if index == original_index:
                    raise Exception("Table is full")
                
            if self.table[index] is None:
                self.table[index] = key
                self.ele+=1

        
    def diff_words(self):
        if self.collision == "Chain":
            l=[]
            for i in self.table:
                if i!=None:
                    for j in i:
                        l.append(j)
            return l
        
        else:
            l=[]
            for i in self.table:
                if i!= None:
                    l.append(i)
            return l


    
    def find(self, key):
        if self.collision == "Chain":
            p = self.get_slot(key)
            if self.table[p] is None:
                return False
            else:
                l = self.table[p]
                for i in l:
                    if i==key:
                        return True
                return False
        
        elif self.collision == "Linear":
            p = self.get_slot(key)
            original_index = p
            while self.table[p] is not None:
                if self.table[p] == key:
                    return True
                p = (p+1)%self.size
                if p == original_index:
                    break
            return False
        
        else:
            index = self.get_slot(key)
            step = self.hash2(key)
            original_index = index

            while self.table[index] is not None:
                if self.table[index] == key:
                    return True
                index = (index+step)%self.size
                if index == original_index:
                    break

            return False

        

    
    def get_slot(self, key):
        a = self.params[0]
        b = self.params[-1]
        hash_code = 0
        for i in range(len(key)):
            if str(key[i]).islower():
                hash_code+= (ord(key[i])-97)*(a**i)
            
            else: # if str(key[i]).isupper():
                hash_code+= (ord(key[i])-39)*(a**i)

            # if isinstance(key[i], int):
            #     hash_code+= key[i]*(a**i)
        return hash_code % self.size
        
        
    
    def get_load(self):
        return (self.ele / self.size)
    
    def __str__(self):
        if self.collision == "Chain":
            l=[]
            for i in self.table:
                if i == None:
                    l.append("<EMPTY>")
                else:
                    # p=[]
                    # for j in i:
                    #     p.append(j)
                    y = " ; ".join(i)
                    l.append(y)
            s = " | ".join(l)
            return s
        
        else:
            
            l=[]
            for i in self.table:
                if i == None:
                    l.append("<EMPTY>")
                else:
                    l.append(i)
            s= " | ".join(l)
            return s


    def hash2(self,key):
        h2=0
        n = self.params[1]
        p = self.params[2]
        for i in range(len(key)):
            if str(key[i]).islower():
                h2+= (ord(key[i])-97)*(n**i)
            
            else: # if str(key[i]).isupper():
                h2+= (ord(key[i])-39)*(n**i)

            # if isinstance(key[i], int):
            #     h2+= key[i]*(n**i)
        x = p - (h2 % p)
        if x !=0:
            return x
        else:
            return 1
    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        self.hashmap = [None]*params[-1]
        self.collision_type = collision_type
        self.params = params
        self.num_of_ele = 0                    #gives the number of items present in the map
        self.table_size = self.params[-1]        
        pass
    
    def insert(self, x):

        if self.collision_type == "Chain":
            p = self.get_slot(x[0])
            if self.hashmap[p] == None:
                self.hashmap[p] = []
                self.hashmap[p].append(x)
            else:
                self.hashmap[p].append(x)
            self.num_of_ele+=1
        
        elif self.collision_type == "Linear":
            p = self.get_slot(x[0])
            original_index = p

            while self.hashmap[p] is not None:
                p = (p+1)%self.table_size

                if p == original_index:
                    raise Exception("Table is full")
            
            if self.hashmap[p] is None:
                self.hashmap[p] = x
                self.num_of_ele+=1
        
        else:
            index = self.get_slot(x[0])
            step = self.hash2(x[0])
            original_index = index

            while self.hashmap[index] is not None:
                index = (index + step)%self.table_size

                if index == original_index:
                    raise Exception("Table is full")
                
            if self.hashmap[index] is None:
                self.hashmap[index] = x
                self.num_of_ele+=1
        
        # x = (key, value)
    
    def find(self, key):

        if self.collision_type == "Chain":
            p = self.get_slot(key)
            if self.hashmap[p] is None:
                return None
            else:
                l = self.hashmap[p]
                for i in l:
                    if i[0]==key:
                        return i[1]
                return None
        
        elif self.collision_type == "Linear":
            p = self.get_slot(key)
            original_index = p
            while self.hashmap[p] is not None:
                a = self.hashmap[p]
                if a[0] == key:
                    return a[1]
                p = (p+1) % self.table_size

                if p == original_index:
                    break
            return None
        
        else:
            index = self.get_slot(key)

            
            step = self.hash2(key)
            original_index = index

            while self.hashmap[index] is not None:
                a = self.hashmap[index]
                if a[0] == key:
                    return a[1]
                index = (index + step) % self.table_size

                if index == original_index:
                    break

            return None
    
    def get_slot(self, key):
        a = self.params[0]
        b = self.params[-1]
        hash_code = 0
        for i in range(len(key)):
            if str(key[i]).islower():
                hash_code+= (ord(key[i])-97)*(a**i)
            
            else: # else str(key[i]).isupper():
                hash_code+= (ord(key[i])-39)*(a**i)

            # if isinstance(key[i], int):
            #     hash_code+= key[i]*(a**i)

        
        return hash_code % self.table_size
        


    
    def get_load(self):
        return (self.num_of_ele / self.table_size)
        
    
    def __str__(self):

        if self.collision_type == "Chain":
            s=""
            for i in self.hashmap:
                if i != None:
                    for j in i:
                        p = j[1].__str__()
                        s = s + j[0] +": " + p +"\n"
            return s.strip()
        
        else:
            s=""
            for i in self.hashmap:
                if i!= None:
                    p= i[1].__str__()
                    s = s + i[0] +": " + p +"\n"
            return s.strip()

    def hash2(self,key):
        h2=0
        n = self.params[1]
        p = self.params[2]
        for i in range(len(key)):
            if str(key[i]).islower():
                h2+= (ord(key[i])-97)*(n**i)
            
            else: # if str(key[i]).isupper():
                h2+= (ord(key[i])-39)*(n**i)

            # if isinstance(key[i], int):
            #     h2+= key[i]*(n**i)
        
        return p - (h2 % p)
