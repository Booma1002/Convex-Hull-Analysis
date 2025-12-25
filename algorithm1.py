import matplotlib.pyplot as plt
import numpy as np
import time


def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def solve_naive(points):
    points = np.array(points)
    n = len(points)
    hull_edges = []

    for i in range(n):
        for j in range(n):
            if i == j: continue
            is_valid = True
            for k in range(n):
                if k == i or k == j: continue
                if cross_product(points[i], points[j], points[k]) < 0:
                    is_valid = False
                    break

            if is_valid:
                hull_edges.append((points[i], points[j]))

    return hull_edges


if __name__ == "__main__":
    np.random.seed(42)
    pts = np.random.randint(0, 100, size=(100, 2))

    start_time = time.time()
    edges = solve_naive(pts)
    print(f"done in {time.time() - start_time:.4f}s. found {len(edges)} hull edges.")

    plt.figure(figsize=(8, 6))
    plt.title("Algorithm 1: Naive Approach (Result)")
    plt.scatter(pts[:, 0], pts[:, 1], color='blue')

    for p1, p2 in edges:
        plt.scatter([p1[0],p2[0]], [p1[1],p2[1]], color='orange',zorder=5)
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'r-', linewidth=2)

    plt.grid(True)
    plt.show()