import heapq


def heap_sort(data: list[int], descending: bool = False):
    sign = -1 if descending else 1

    h = [sign * el for el in data]
    heapq.heapify(h)

    return [sign * heapq.heappop(h) for _ in range(len(h))]

def get_cost(cable_lengths: list[int]) -> int:
    cost: int = 0
    connected_length: int = 0
    
    for cable_length in cable_lengths:
        connected_length += cable_length
        cost += (connected_length + cable_length)

    return cost


cable_lengths_unsorted: list[int] = [5, 3, 8, 4, 9, 2, 6, 1, 7, 10]
cable_lengths_sorted: list[int] = heap_sort(data=cable_lengths_unsorted)

cost_unsorted: int = get_cost(cable_lengths=cable_lengths_unsorted)
cost_sorted: int =get_cost(cable_lengths=cable_lengths_sorted)

print('To get the minimal cost of solution, the cables must be sorted in ascending order by their length and connected one by one into a single cable.')
print(f'Cost of solution when cables are not heapsorted: {cost_unsorted}')
print(f'Cost of solution when cables are heapsorted: {cost_sorted}')