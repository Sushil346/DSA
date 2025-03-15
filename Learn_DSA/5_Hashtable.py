class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        return None  # Explicitly return None for clarity
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][index] = [key, val]  # Consistent list
                found = True
                break     
        if not found:
            self.arr[h].append([key, val])

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h].pop(index)
                return

if __name__ == '__main__':
    t = HashTable()
    t['march 6'] = 21
    t['march 7'] = 2
    t['march 8'] = 1
    t['march 17'] = 22

    print(t)
    print(t['march 8'])
    del t['march 8']
    print(t['march 8'])
    print(t)