#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    ht = {}
    route = []
    for ticket in tickets:
        ht[ticket.source] = ticket.destination
    print(ht)
    route.append(ht['NONE'])
    n = ht['NONE']
    while ht[n] != 'NONE':
        route.append(ht[n])
        n = ht[n]
    route.append('NONE')
    print(route)
    return route
