    def mode(collection):
        count = {val: collection.count(val) for val in collection}
        # find the highest value (the most frequent number)
        max_value = max(count.values())
        # now we need to see at which index the highest value is at
        correct_index = list(count.values()).index(max_value)
        # finally, return the correct key for the correct index (we have to convert cou)
        return list(count.keys())[correct_index]
