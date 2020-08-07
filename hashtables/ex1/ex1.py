def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    if length <= 1:
        return None
    ht = {}
    for i in range(length):
        ht[(weights[i])] = i
    for i in range(length):
        diff = limit - weights[i]
        if diff in ht and ht[diff] != i:
            return [ht[diff], i]

    return None