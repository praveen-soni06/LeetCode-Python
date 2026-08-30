class TimeMap:

    def __init__(self):
        self.store = {}   # key : list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        s, e = 0, len(values)-1

        while(s <= e):
            m = (s+e)//2

            if values[m][1] <= timestamp:
                res = values[m][0]
                s = m + 1
            else:
                e = m - 1

        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)