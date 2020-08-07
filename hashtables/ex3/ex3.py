def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    ht = {}
    for array in arrays:
        for elem in array:
            if elem not in ht:
                ht[elem] = elem
            else:
                result.append(ht[elem])
    print(ht)
    print(result)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
