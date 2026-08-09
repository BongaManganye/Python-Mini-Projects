#Dictionary Merger
# Write a function that merges two dictionaries. If a key exists in both, sum their integer values; otherwise
# include the key-value pair

def merge_dicts(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        results[k] = result.get(k, 0) + v
    return result
