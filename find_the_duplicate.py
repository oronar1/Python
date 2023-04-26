    def find_the_duplicate(arr):
        counter = {}
        for val in arr:
            if val in counter:
                counter[val] += 1
            else:
                counter[val] = 1
        for key in counter.keys():
            if counter[key] > 1:
                return int(key)
        return none
