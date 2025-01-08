def reduce(hp, damage, times):
    while times > 0:
        hp -= damage
        times -= 1
        print(hp)

reduce(1000, 100, 4)