import time
def printOut(m):
    l = list(m)
    for i in range(0, len(l)):
        print(l[i], end='', flush=True)
        time.sleep(0.02)
    print()