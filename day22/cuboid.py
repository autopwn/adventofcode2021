class Cuboid():

    def __init__(self, min_x, max_x, min_y, max_y, min_z, max_z):

        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.min_z = min_z
        self.max_z = max_z
        self.volume = (self.max_x - self.min_x + 1) * \
                (self.max_y - self.min_y + 1) * \
                (self.max_z - self.min_z + 1)

    def __repr__(self):
        return f"<{self.min_x},{self.max_x},{self.min_y},{self.max_y}," \
            f"{self.min_z},{self.max_z}/{self.volume}>"

    def is_enclosing(self, cuboid):
        return self.get_intersection(cuboid).volume == cuboid.volume

    def is_intersected(self, cuboid):

        if cuboid.min_x > self.max_x or cuboid.max_x < self.min_x \
            or cuboid.min_y > self.max_y or cuboid.max_y < self.min_y \
            or cuboid.min_z > self.max_z or cuboid.max_z < self.min_z:
            return False
        return True

    def get_intersection(self, cuboid):

        if self.min_x < cuboid.min_x: new_min_x = cuboid.min_x
        else: new_min_x = self.min_x

        if self.max_x > cuboid.max_x: new_max_x = cuboid.max_x
        else: new_max_x = self.max_x

        if self.min_y < cuboid.min_y: new_min_y = cuboid.min_y
        else: new_min_y = self.min_y

        if self.max_y > cuboid.max_y: new_max_y = cuboid.max_y
        else: new_max_y = self.max_y

        if self.min_z < cuboid.min_z: new_min_z = cuboid.min_z
        else: new_min_z = self.min_z

        if self.max_z > cuboid.max_z: new_max_z = cuboid.max_z
        else: new_max_z = self.max_z

        return Cuboid(new_min_x, new_max_x, new_min_y, new_max_y, new_min_z, new_max_z)

    def substract(self, cuboid):

        # left sub cube
        s1 = Cuboid(self.min_x, max(self.min_x, cuboid.min_x) - 1, \
                max(self.min_y, cuboid.min_y), min(self.max_y, cuboid.max_y), \
                max(self.min_z, cuboid.min_z), min(self.max_z, cuboid.max_z))

        # top sub Cuboid // no exclusions
        s2 = Cuboid(self.min_x, self.max_x, min(self.max_y, cuboid.max_y) + 1, \
                self.max_y, self.min_z, self.max_z)

        # right sub Cuboid
        s3 = Cuboid(min(self.max_x, cuboid.max_x) + 1, self.max_x, \
                max(self.min_y, cuboid.min_y), min(self.max_y, cuboid.max_y), \
                max(self.min_z, cuboid.min_z), min(self.max_z, cuboid.max_z))

        # bottom sub Cuboid // no exclusions
        s4 = Cuboid(self.min_x, self.max_x, self.min_y, \
                max(self.min_y, cuboid.min_y) - 1, self.min_z, self.max_z)

        # front sub Cuboid // exclude top and bottom
        s5 = Cuboid(self.min_x, self.max_x, max(self.min_y, cuboid.min_y), \
                min(self.max_y, cuboid.max_y), self.min_z, max(self.min_z, cuboid.min_z) - 1)

        # back sub Cuboid // exclude top and bottom
        s6 = Cuboid(self.min_x, self.max_x, max(self.min_y, cuboid.min_y), \
                min(self.max_y, cuboid.max_y), min(self.max_z, cuboid.max_z) + 1, self.max_z)

        return [x for x in [s1, s2, s3, s4, s5, s6] if x.volume > 0]

