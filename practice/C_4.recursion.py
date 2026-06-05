# 코드바 워크샵 
def hanoi_tower(n:int, current:int, new:int, alternative:int):
    if n > 0:
        hanoi_tower(n-1, current, alternative, new)
        print(f"move disc {n} from {current} to {new}")
        hanoi_tower(n-1, alternative, new, current)

hanoi_tower(5, 1, 3, 2)