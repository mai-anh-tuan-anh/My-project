import sys
n = int(sys.stdin.readline())
max_score = -1
silver_score = -1
for _ in range(n):
    score = int(sys.stdin.readline().strip())
    if score > max_score:
        silver_score = max_score
        max_score = score
    elif score > silver_score and score < max_score:
        silver_score = score
print(f"Silver = {silver_score}")