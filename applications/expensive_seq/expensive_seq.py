# Your code here
cache = {}

def exps(x, y, z):
    if x <= 0:
        return y + z
    if x > 0:
        return exps(x-1,y+1,z*1) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)
    

def expensive_seq(x, y, z):
    # Your code here
    if x <= 0:
        return y + z

    if x > 0:
        x_cache, y_cache, z_cache = 0,0,0
        if (x-1, y+1,z*1) not in cache:
            cache[(x-1,y+1,z*1)] = expensive_seq(x-1,y+1,z*1)

        if (x-2,y+2,z*2) not in cache:
            cache[(x-2,y+2,z*2)] = expensive_seq(x-2,y+2,z*2)

        if (x-3,y+3,z*3) not in cache:
            cache[(x-3,y+3,z*3)] = expensive_seq(x-3,y+3,z*3)
        
        return cache[(x-1,y+1,z*1)] + cache[(x-2,y+2,z*2)] + cache[(x-3,y+3,z*3)]

if __name__ == '__main__':
    for r in range(10):
        x = exps(r*2, r*3, r*4)
        print(f'{r*2} {r*3} {r*4} = {x}')

    print('\n')

    for r in range(10):
        x = expensive_seq(r*2, r*3, r*4)
        print(f'{r*2} {r*3} {r*4} = {x}')




if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
