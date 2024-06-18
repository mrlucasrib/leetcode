class TimeMap:

    def __init__(self):
        self.hm = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        val = self.hm.get(key, None)
        if val is not None:
            val.append((timestamp, value))
        else:
            self.hm[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        val = self.hm.get(key, None)
        if val is None:
            return ""
        ans = ""
        l, r = 0, len(val) -1
        while l <= r:
            mid = int((l+r)/2)
            if val[mid][0] <= timestamp:
                ans = val[mid][1]
                l = mid+1
            else:
                r = mid-1
        return ans
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)