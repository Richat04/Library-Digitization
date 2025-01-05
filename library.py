import hash_table as ht

def merge(left,right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i=i+1
        else:
            sorted_arr.append(right[j])
            j=j+1
    
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

def merge2(left,right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            sorted_arr.append(left[i])
            i=i+1
        else:
            sorted_arr.append(right[j])
            j=j+1
    
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr


def msort(a):
    # p = []
    # for i in a:
    #     p.append(i)
    if len(a)<=1:
        return a[:]
    
    mid = len(a)//2
    left = msort(a[:mid])
    right = msort(a[mid:])
    return merge(left,right)
    # else:
    #     l=p[:len(p)//2]
    #     r=p[len(p)//2:]
    #     msort(l)
    #     msort(r)
    #     i=0
    #     j=0
    #     k=0
    #     while i<len(l) and j<len(r):
    #         if l[i]<r[j]:
    #             p[k]=l[i]
    #             i=i+1
    #             k=k+1
    #         else:
    #             p[k]=r[j]
    #             j=j+1
    #             k=k+1
    #     while i<len(l):
    #         p[k]=l[i]
    #         k=k+1
    #         i=i+1
    #     while j<len(r):
    #         p[k]=r[j]
    #         k=k+1
    #         j=j+1
    #     return p

def msort2(a):

    if len(a)<=1:
        return a[:]
    
    mid = len(a)//2
    left = msort(a[:mid])
    right = msort(a[mid:])
    return merge2(left,right)
       
def bin_search_1(a,key):
        
    l=0
    h=len(a)-1
    while h>=l:
        mid =(h+l)//2
        if a[mid][0]==key:
            return mid
        elif a[mid][0]>key:
            h=mid-1
        else:
            l=mid+1
    return None

def bin_search_0(a,key):  
    # print(a) 
    l=0
    h=len(a)-1
    while h>=l:
        mid =(h+l)//2
        if a[mid]==key:
            return mid
        elif a[mid]>key:
            h=mid-1
        else:
            l=mid+1
    return None

def rem_dupli(arr):
    l=[arr[0]]
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            l.append(arr[i])
    return l

    

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):                        #add return statements to all of these instead of print statement
        whole = []
        for i in range(len(book_titles)):
            whole.append((book_titles[i], texts[i]))
        whole = msort2(whole)
        self.book = []
        self.text = []
        for i in whole:
            self.book.append(i[0])
            self.text.append(i[1])
        
        # print(whole)
        # dupli_book = []
        # dupli_texts = []
        # for i in book_titles:
        #     dupli_book.append(i)
        # for i in texts:
        #     dupli_texts.append(i)
        # self.musk_list = []
        # print(dupli_texts)
        # print(dupli_book)
        for i in range(len(self.text)):
            self.text[i] = msort(self.text[i])
            self.text[i] = rem_dupli(self.text[i])
        #     l= msort(texts[i])
        #     p=[]
        #     p.append(l[0])
        #     for j in range(1,len(l)):
        #         if l[j]!=l[j-1]:
        #             p.append(l[j])
        #     pair=(book_titles[i],p)
        #     self.musk_list.append(pair)

        # self.musk_list = msort2(self.musk_list)
        # print(self.musk_list)
        # print(self.book)
        # print(self.text)
        

    def distinct_words(self, book_title):
        p = bin_search_0(self.book,book_title)
        if p == None:
            print("Book not found")
        else:
            return self.text[p]

    def count_distinct_words(self, book_title):
        p = bin_search_0(self.book,book_title)
        # print(p)
        if p is None:
            print("Book not found")
        else:
            # print(len(self.musk_list[p][1]))
            return len(self.text[p])
        
    def search_keyword(self, keyword):
        p=[]
        for i in range(len(self.text)):
            s = bin_search_0(self.text[i], keyword)
            if s!= None:

                p.append(self.book[i])
                
        
        return p
    
    def print_books(self):
        for i in range(len(self.book)):
            s= " | ".join(self.text[i])
            
            print(self.book[i],": ",s, sep="")
        

        
        


class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):

        if name == "Jobs":
            self.lib = ht.HashMap("Chain",params)
            self.collision = "Chain"
            self.param = params

        elif name == "Gates":
            self.lib = ht.HashMap("Linear",params)
            self.collision = "Linear"
            self.param = params

        else:
            self.lib = ht.HashMap("Double",params)
            self.collision = "Double"
            self.param =params
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        
    
    def add_book(self, book_title, text):
        texts = ht.HashSet(self.collision,self.param)
        for i in text:
            texts.insert(i)
        
        x = (book_title,texts)
        self.lib.insert(x)
        
    
    def distinct_words(self, book_title):
        
        p = self.lib.find(book_title)
        l = p.diff_words()
        return l

        
    
    def count_distinct_words(self, book_title):
        t = self.lib.find(book_title)
        if t != None:
            return t.ele
    
    def search_keyword(self, keyword):       #write function for other probing as well
        if self.collision == "Chain":
            l=[]
            # print(type(self.lib))
            for i in self.lib.hashmap:
                
                if i is not None:
                    for j in i:
                        # print(j)
                        t = j[1].find(keyword)   #find function of hash set is being called
                        if t :
                            l.append(j[0])
            return l

        else:
            l=[]
            for i in self.lib.hashmap:
                if i is not None:
                    # print(i[1])
                    t = i[1].find(keyword)
                    # print(type(i[1]))
                    if t:
                        l.append(i[0])

            # print(l)
            return l
    
    def print_books(self):         #improve this. giving jumbled results in chain hashing
        print(self.lib)


if __name__=="__main__":
    book_titles = ["book1", "Book2"]
    texts = [["The", "name", "of", "this", "book", "contains", "a", "number"],
             ["You", "can", "name", "this", "book", "anything", "anything", "anything"]]
    
    musk_lib = MuskLibrary(book_titles, texts)
    musk_lib.print_books()
    print(musk_lib.count_distinct_words("Book2"))
    print(musk_lib.distinct_words("Book2"))
    print(musk_lib.search_keyword("book"))