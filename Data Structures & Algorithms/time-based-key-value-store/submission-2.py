class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append([value, timestamp])
        else:
            self.time_map[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        key_list = self.time_map[key]

        res = ""
        l, r = 0, len(key_list) - 1

        while l <= r:
            mid = (l + r) // 2
            mid_val, mid_stamp = key_list[mid][0], key_list[mid][1]
            if mid_stamp == timestamp: return mid_val
            elif mid_stamp > timestamp:
                r = mid - 1
            else:
                res = mid_val
                l = mid + 1
        
        return res
        
