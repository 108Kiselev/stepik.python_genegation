def merge(values):
    d = {k: {values[i].get(k) for i in range(len(values)) if values[i].get(k) != None} for i in range(len(values)) for k in values[i].keys()}
    return d
print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))