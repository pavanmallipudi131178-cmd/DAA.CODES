'''#selection sort
a = list(map(int, input("Enter numbers: ").split()))

n = len(a)

for i in range(n):
    min = i

    for j in range(i + 1, n):
        if a[j] < a[min]:
            min = j

    a[i], a[min] = a[min], a[i]

print("Sorted array:", a)'''



'''#binary search
a = list(map(int, input("Enter numbers: ").split()))
tar = int(input("Enter target number: "))

low = 0
high = len(a) - 1

while low <= high:
    mid = (low + high) // 2

    if a[mid] == tar:
        print("Found at index:", mid)
        break

    elif a[mid] < tar:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Target not found")'''



'''#selection sort
a = list(map(int, input("Enter numbers: ").split()))

n = len(a)

for i in range(n):
    min = i

    for j in range(i + 1, n):
        if a[j] < a[min]:
            min = j

    a[i], a[min] = a[min], a[i]

print("Sorted array:", a)'''


'''#insertion sort
a = list(map(int, input("Enter numbers: ").split()))

for i in range(1, len(a)):
    key = a[i]
    j = i - 1

    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1

    a[j + 1] = key

print("Sorted array:", a)'''


'''#bubble sort
a = list(map(int, input("Enter numbers: 1,2,3,4").split()))

n = len(a)

for i in range(n):
    for j in range(0, n - i - 1):

        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print("Sorted array:", a)'''

'''def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge the two halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements of left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements of right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = list(map(int, input("Enter numbers: ").split()))

merge_sort(arr)

print("Sorted array:", arr)'''


'''#quick sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


arr = list(map(int, input("Enter numbers: ").split()))

quick_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)'''


'''#heap-mini
def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


def min_heap_sort(arr):
    n = len(arr)


    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    result = []

    for i in range(n):
        result.append(arr[0])

        arr[0], arr[n - i - 1] = arr[n - i - 1], arr[0]

        heapify(arr, n - i - 1, 0)

    return result


arr = list(map(int, input("Enter elements: ").split()))

print("Sorted array:", min_heap_sort(arr))'''



'''#heap-max
def heapify(arr, n, i):
    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def max_heap_sort(arr):
    n = len(arr)


    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        heapify(arr, i, 0)


arr = list(map(int, input("Enter elements: ").split()))

max_heap_sort(arr)

print("Sorted array:", arr)'''



'''fact= int(input("enter a number for factorial"))
factorial=1
for i in range(1,fact+1):
    factorial=factorial*i
print("factorial of",fact,"is",factorial)'''



'''fact=1
def factorial(a):
  global fact
  if a>1:
    fact = fact*a
    factorial(a-1)

  else:
    return
num =int(input("enter a number for factorial"))
factorial(num)
print("factorial of",num,"is",fact)'''



'''#knapsack
def knapsack(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[ i- 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))
capacity = int(input("Enter capacity: "))

print("Maximum value:", knapsack(weights, values, capacity))'''



'''#matrix
def matrix_chain(p, n):
    dp = [[0 for j in range(n)] for i in range(n)]

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = 999999

            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j]
                        + p[i - 1] * p[k] * p[j])

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n - 1]



n = int(input("Enter number of matrices: "))

p = []

print("Enter dimensions:")
for i in range(n + 1):
    x = int(input())
    p.append(x)

ans = matrix_chain(p, n)

print("Minimum number of multiplications:", ans)'''




'''def coin_change(coins, amount):
    n = len(coins)

    dp = [[0] * (amount + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, amount + 1):

            if coins[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    print("\nDP Table:")

    for row in dp:
        print(row)

    return dp[n][amount]


coins = list(map(int, input("Enter coins: ").split()))
amount = int(input("Enter amount: "))

ways = coin_change(coins, amount)

print("Number of ways:", ways)'''



'''#bfs
from collections import deque

def bfs(adj):
    n = len(adj)
    visited = [False] * n
    res = []

    src = 0
    g = deque()

    g.append(src)
    visited[src] = True
    while g:
        u = g.popleft()
        res.append(u)

        for v in adj[u]:
            if not visited[v]:
                g.append(v)
                visited[v] = True

    return res

adj = [
    [1, 2],
    [0, 3],
    [0, 3],
    [1, 2, 4],
    [3]
]

print("BFS Traversal:", bfs(adj))'''




'''#DFS

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for neighbour in graph[node]:
            dfs(neighbour)

print("DFS Traversal:")
dfs('A')'''



'''graph = [
    [0, 2, 3, 0],
    [2, 0, 1, 4],
    [3, 1, 0, 5],
    [0, 4, 5, 0]
]

n = len(graph)
visited = [False] * n
visited[0] = True
cost = 0

for _ in range(n - 1):
    minimum = float('inf')
    x = -1
    y = -1

    for i in range(n):
        if visited[i]:
            for j in range(n):
                if graph[i][j] != 0 and not visited[j]:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(x, "-", y, ":", minimum)
    cost += minimum
    visited[y] = True

print("Minimum cost:", cost)'''



'''def prim(graph, n):
    visited = [False] * n
    visited[0] = True

    edges = []
    total_cost = 0

    for _ in range(n - 1):
        min_cost = float('inf')
        u = -1
        v = -1

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and graph[i][j] != 0:
                        if graph[i][j] < min_cost:
                            min_cost = graph[i][j]
                            u = i
                            v = j

        if u == -1:
            print("Graph is not connected!")
            return

        edges.append((u, v, min_cost))
        total_cost += min_cost
        visited[v] = True
            print("\nMinimum Spanning Tree:")
    for u, v, cost in edges:
        print(u, "-", v, ":", cost)

    print("Total Minimum Cost:", total_cost)



n = int(input("Enter number of vertices: "))
graph = [[0] * n for _ in range(n)]

e = int(input("Enter number of edges: "))

print("Enter edges as: source destination weight")
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w

prim(graph, n)'''




'''def kruskal(vertex,edge)
edge sort[key=lambda  edge:edge[2]]
graph=[[v] for v in vertex]
mst=[(a,c,1)]
cost=0||1
for i,j,weight in edge:
  grp-i=None
  grp-j=None
  for g in graph:
    if i in g:
      grp-i=g
    if j in g:
      grp-j=g
      if grp-i!=grp-j:
        mst.append((i,j,weight))
        cost+=weight
        graph.remove(grp-i)
        graph.remove(grp-j)'''




'''def kruskal(vertex, edge):
    edge.sort(key=lambda edge: edge[2])

    graph = [[v] for v in vertex]
    mst = []
    cost = 0

    for i, j, weight in edge:
        grp_i = None
        grp_j = None

        for g in graph:
            if i in g:
                grp_i = g
            if j in g:
                grp_j = g

        if grp_i != grp_j:
            mst.append((i, j, weight))
            cost += weight

            new_group = grp_i + grp_j
            graph.remove(grp_i)
            graph.remove(grp_j)
            graph.append(new_group)

        if len(mst) == len(vertex) - 1:
            break

    if len(mst) != len(vertex) - 1:
        print("Graph is not connected!")
        return

    print("Minimum Spanning Tree:")
    for i, j, weight in mst:
        print(i, "-", j, ":", weight)

    print("Total Minimum Cost:", cost)# User input
vertex = list(map(int, input("Enter vertices: ").split()))
e = int(input("Enter number of edges: "))

edge = []
print("Enter edges as: source destination weight")

for _ in range(e):
    i, j, weight = map(int, input().split())
    edge.append((i, j, weight))

kruskal(vertex, edge)'''




'''def kruskal(vertex, edge):
    edge.sort(key=lambda edge: edge[2])

    graph = [[v] for v in vertex]
    mst = []
    cost = 0

    for i, j, weight in edge:
        grp_i = None
        grp_j = None

        for g in graph:
            if i in g:
                grp_i = g
            if j in g:
                grp_j = g

        if grp_i != grp_j:
            mst.append((i, j, weight))
            cost += weight

            new_group = grp_i + grp_j
            graph.remove(grp_i)
            graph.remove(grp_j)
            graph.append(new_group)

        if len(mst) == len(vertex) - 1:
            break

    if len(mst) != len(vertex) - 1:
        print("Graph is not connected!")
        return

    print("Minimum Spanning Tree:")
    for i, j, weight in mst:
        print(i, "-", j, ":", weight)

    print("Total Minimum Cost:", cost)# User input
vertex = list(map(int, input("Enter vertices: ").split()))
e = int(input("Enter number of edges: "))

edge = []
print("Enter edges as: source destination weight")

for _ in range(e):
    i, j, weight = map(int, input().split())
    edge.append((i, j, weight))

kruskal(vertex, edge)'''




'''INF = 99999

def floyd_warshall(graph):
    n = len(graph)

    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    print("Shortest Distance Matrix:")
    for row in dist:
        for value in row:
            if value == INF:
                print("INF", end=" ")
            else:
                print(value, end=" ")
        print()


graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

floyd_warshall(graph)'''





'''def tsp(graph, start):
    n = len(graph)
    visited = [False] * n
    visited[start] = True

    min_cost = float('inf')

    def find_path(city, count, cost):
        nonlocal min_cost

        if count == n:
            total_cost = cost + graph[city][start]
            min_cost = min(min_cost, total_cost)
            return

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                find_path(i, count + 1, cost + graph[city][i])
                visited[i] = False

    find_path(start, 1, 0)
    return min_cost


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start = 0
result = tsp(graph, start)

print("Minimum travelling cost:", result)'''






