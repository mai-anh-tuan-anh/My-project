from math import sqrt
from random import shuffle
def dist(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
def circle_from_two(p1, p2):
    center = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    radius = dist(p1, p2) / 2
    return center, radius
def welzl(points, R=[]):
    if len(points) == 0 or len(R) == 3:
        if len(R) == 0:
            return ((0, 0), 0)
        elif len(R) == 1:
            return (R[0], 0)
        elif len(R) == 2:
            return circle_from_two(R[0], R[1])
        elif len(R) == 3:
            return circle_from_three(R[0], R[1], R[2])
    p = points.pop()
    circle = welzl(points, R)
    if dist(circle[0], p) <= circle[1]:
        points.append(p)
        return circle
    new_circle = welzl(points, R + [p])
    points.append(p)
    return new_circle
def circle_from_three(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    det = (x1 - x2) * (y2 - y3) - (y1 - y2) * (x2 - x3)
    if abs(det) < 1e-9:
        return None
    A = x1**2 + y1**2
    B = x2**2 + y2**2
    C = x3**2 + y3**2
    D = 2 * det
    Ux = ((A - B) * (y2 - y3) - (B - C) * (y1 - y2)) / D
    Uy = ((B - C) * (x1 - x2) - (A - B) * (x2 - x3)) / D
    center = (Ux, Uy)
    radius = dist(center, p1)
    return center, radius
def count_inside(center, radius, points):
    return sum(1 for p in points if dist(center, p) < radius)
def solve(n, k, points):
    shuffle(points)
    center, radius = welzl(points)
    cnt = count_inside(center, radius, points)
    return "YES" if cnt == k else "NO"
if __name__ == "__main__":
    content = []
    while True:
        try:
            content.extend(list(map(int, input().split())))
        except:
            break
    T = content.pop(0)
    for _ in range(T):
        n = content.pop(0)
        k = content.pop(0)
        points = [(content.pop(0), content.pop(0)) for _ in range(n)]
        print(solve(n, k, points))