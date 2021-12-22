from cuboid import Cuboid
from itertools import combinations

def solve(data):

    cuboids = []
    discounts = []
    total_active_cubes = 0

    for line in data:
        action, cuboid = [x for x in line.split(' ')]
        cuboids.append((Cuboid(*[item for sublist in [[int(y) \
            for y in x.split('=')[1].split('..')] \
            for x in cuboid.split(',')] for item in sublist]), action == 'on'))
    
    for idx in range(len(cuboids) - 1, -1, -1):

        if cuboids[idx][1]:
            active_cubes = cuboids[idx][0].volume
            for discount in discounts:
                if cuboids[idx][0].is_intersected(discount):
                    active_cubes -= cuboids[idx][0].get_intersection(discount).volume
            total_active_cubes += active_cubes

        local_discounts = [cuboids[idx][0]]
        for discount in discounts:
            new_local_discounts = []
            local_discounts_to_drop = []
            for local_discount in local_discounts:
                if local_discount.is_intersected(discount):
                    new_local_discounts += local_discount.substract(discount)
                    local_discounts_to_drop.append(local_discount)
            for i in local_discounts_to_drop:
                local_discounts.remove(i)
            local_discounts += new_local_discounts
        discounts += local_discounts

    return total_active_cubes

if __name__ == "__main__":

    example = 0

    with open('example.txt' if example else 'input.txt', 'r') as f:
        data = f.read().strip().splitlines()
        print(f"Part 1: {solve(data[0:20])}")
        print(f"Part 2: {solve(data)}")
