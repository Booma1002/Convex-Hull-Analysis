import matplotlib.pyplot as plt
import numpy as np
import math
import time


def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def solve_graham(points):
    pts = list(points)
    n = len(pts)
    if n < 3: return pts

    start = min(pts, key=lambda p: (p[1], p[0]))

    # sort by polar angle
    sorted_points = sorted(pts, key=lambda p: (
        math.atan2(p[1] - start[1], p[0] - start[0]),
        (p[0] - start[0]) ** 2 + (p[1] - start[1]) ** 2
    ))

    # build hull using stack
    hull = [start]
    for p in sorted_points[1:]:
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    # add start to end to close the loop for plotting
    return hull + [start]


if __name__ == "__main__":
    np.random.seed(1)
    pts = np.random.randint(0, 100, size=(100, 2))

    start_time = time.time()
    hull_vertices = solve_graham(pts)
    print(f"done in {time.time() - start_time:.4f}s. hull has {len(hull_vertices) - 1} vertices.")

    plt.figure(figsize=(8, 6))
    plt.title("Algorithm 2: Graham Scan (Result)")

    xs, ys = zip(*pts)
    plt.scatter(xs, ys, color='blue')

    # plot hull
    hx, hy = zip(*hull_vertices)
    plt.scatter(hx, hy, color='orange', zorder=5)
    plt.plot(hx, hy, 'g-', linewidth=2, label='Convex Hull')

    plt.legend()
    plt.grid(True)
    plt.show()