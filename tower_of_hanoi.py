def towerOfHanoi (n, a,b,c):
    if n==1:
        print(f"move 1st disk from {a} to {c}")
        return
    towerOfHanoi(n-1, a,c,b)
    print(f"move {n}th disk from {a} to {c}")
    towerOfHanoi(n-1, b,a,c)

towerOfHanoi(3, "a","b","c")