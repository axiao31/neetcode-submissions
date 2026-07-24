class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        index = self.map[val]  # get index of the element to remove
        last  = self.nums[-1]  # get the last element in the list
        self.nums[index] = last  # overwrite the element at idx with the last element
        self.map[last] = index  # update the map: the last element now lives at idx
        self.nums.pop()  # remove the duplicate last element (O(1))
        del self.map[val]  # delete the removed value from map
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
        
    #time: O(1)
    #space: O(n)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()