# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    ht = {}
    for q in queries:
        if q not in ht:
            ht[q] = []
    for f in files:
        g = f.split("/", -1)[-1]
        if g in ht:
            result.append(f)
  
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
