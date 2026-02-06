from collections import OrderedDict

def LRUCache(strArr):
    cache_size = 5
    cache = OrderedDict()

    for char in strArr:
        if char in cache:
            cache.move_to_end(char)  # Move accessed item to the most recent position
        else:
            if len(cache) >= cache_size:
                cache.popitem(last=False)  # Remove the least recently used item
            cache[char] = True  # Insert new item

    return "-".join(cache.keys())  # Convert cache order to required output format

# Example Test Cases
print(LRUCache(["A", "B", "A", "C", "A", "B"]))  # Output: C-A-B
print(LRUCache(["A", "B", "C", "D", "E", "D", "Q", "Z", "C"]))  # Output: E-D-Q-Z-C
print(LRUCache(["A", "B", "C", "D", "A", "E", "D", "Z"]))  # Output: C-A-E-D-Z
