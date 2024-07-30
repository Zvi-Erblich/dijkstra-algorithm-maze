import heapq
import math
import cv2
import matplotlib.pyplot as plt

# file = 'maze.jpeg'
# file = 'maze5.jpeg'
file = 'maze2.png'


img = cv2.imread(file)  # read an image from a file using
cv2.circle(img, (22, 315), 3, (255, 0, 0), -1)  # add a circle at (5, 220)
cv2.circle(img, (330, 326), 3, (0, 0, 255), -1)  # add a circle at (5,5)
plt.figure(figsize=(7, 7))
plt.imshow(img)  # show the image
img = cv2.imread(file)
plt.show()

print(img.shape)


img = img[:, :, 0] // 200


def graph_to_list(image):
    graph = image.tolist()
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            graph[i][j] = [graph[i][j], (i, j), float("inf"), None]
    return graph


def neighbors(vertex, image=img):
    neighbors = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            x, y = vertex
            x += i
            y += j
            if 0 <= x < image.shape[0] and 0 <= y < image.shape[1] and (x, y) != vertex:
                neighbors.append((x, y))
    return neighbors


def init_dijkstra(heap, graph, source):
    x, y = source
    graph[x][y][2] = 0
    heapq.heappush(heap, [graph[x][y][2], graph[x][y]])
    return heap


def dijkstra(heap, graph, end):
    visited = set((float("inf"), None))
    # progres = tqdm(225 * 225)
    while end not in visited:
        # progres.update()
        # print(len(heap))
        min = heapq.heappop(heap)
        visited.add(min[1][1])
        x_min, y_min = min[1][1]
        for neighbor in neighbors(min[1][1]):
            if neighbor in visited:
                continue
            else:
                x, y = neighbor
                if graph[x][y][0] == 0:
                    continue
                if graph[x][y][0] == 1:
                    if x == x_min or y == y_min:
                        if graph[x][y][2] > min[1][2] + 1:
                            graph[x][y][2] = min[1][2] + 1
                            graph[x][y][3] = min[1][1]
                            heapq.heappush(heap, (graph[x][y][2], graph[x][y]))
                    else:
                        if graph[x][y][2] > min[1][2] + math.sqrt(2):
                            graph[x][y][2] = min[1][2] + math.sqrt(2)
                            graph[x][y][3] = min[1][1]
                            heapq.heappush(heap, (graph[x][y][2], graph[x][y]))
    print(graph)
    return graph


def get_path(graph, source, end):
    path = []
    current = end
    while current != source:
        path.append(current)
        current = graph[current[0]][current[1]][3]
    print(path)
    return path


def draw_path(img, path, thickness=1):
    x0, y0 = path[0]
    for vertex in path[1:]:
        x1, y1 = vertex
        cv2.line(img, (y0, x0), (y1, x1), (255, 0, 0), thickness)
        x0, y0 = vertex


empty_heap = []
graph = graph_to_list(img)
# source = (5, 25)
# source = (330, 326)
source = (155, 18)
heap = init_dijkstra(empty_heap, graph, source)
# end = (220, 5)
# end = (330, 17)
end = (146, 190)
graph_1 = dijkstra(heap, graph, end)
path = get_path(graph_1, source, end)
img = cv2.imread(file)
draw_path(img, path)
plt.figure(figsize=(7, 7))
plt.imshow(img)  # show the image on the screen
plt.show()
