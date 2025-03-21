h, m, s = map(int, input().split())
angle = h * 30 + m * 0.5 + s / 120
print(f"{angle:.1f}")
