def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    ht = {}
    result = []
    for item in a:
        if item not in ht:
            ht[item] = item

    for key in ht:
       if (key * -1) in ht and key > 0:
           result.append(key)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
