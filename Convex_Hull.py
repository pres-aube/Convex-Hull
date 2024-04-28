import matplotlib.pyplot as plt

def convex_hull(points):

    # Sort points by x-coordinate
    sorted_points = sorted(points)

    def turn_direction_right(p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        
        return (y2 - y1) * (x3 - x2) - (x2 - x1) * (y3 - y2) > 0

    def build_hull(sorted_points):
        hull = []
        for p in sorted_points:
            while len(hull) >= 2 and not turn_direction_right(hull[-2], hull[-1], p):
                hull = hull[:-1]
            hull += [p]
        return hull

    # Get input from user
    num_points = int(input("Enter the number of points: "))
    points = [tuple(map(int, input(f"Enter point {i + 1} (x y): ").split())) for i in range(num_points)]

    # Build upper and lower hulls simultaneously
    convex_hull_points = build_hull(sorted(points)) + build_hull(sorted(points, reverse=True))[1:-1]

    x, y = zip(*convex_hull_points + [convex_hull_points[0]]) 
    plt.scatter(*zip(*points), color='blue')
    plt.plot(x, y, color='red', marker='o', linestyle='-', linewidth=2)
    plt.title('Convex Hull Visualization')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

result = convex_hull([])