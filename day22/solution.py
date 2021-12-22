from cuboid import Cuboid

def solve(data):
    discounts = []
    total_active_cubes = 0

    for line in reversed(data):
        action, cuboid = [x for x in line.split(' ')]
        cuboid = Cuboid(*[item for sublist in [[int(y) \
            for y in x.split('=')[1].split('..')] \
            for x in cuboid.split(',')] for item in sublist])

        if action == 'on':
            active_cubes = cuboid.volume
            for discount in discounts:
                if cuboid.is_intersected(discount):
                    active_cubes -= cuboid.get_intersection(discount).volume
            total_active_cubes += active_cubes

        local_discounts = [cuboid]
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

with open('input.txt', 'r') as f:
    data = f.read().strip().splitlines()
    print(f"Part 1: {solve(data[0:20])}")
    print(f"Part 2: {solve(data)}")