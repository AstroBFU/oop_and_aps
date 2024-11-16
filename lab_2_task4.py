

class Planet:
    def __init__(self):
        self.radius = 12.3

        self._mask = 2

    @classmethod
    def get_radius(self, cls):
        return cls.radius


    @property
    def mask(self):
        return self._mask


    @staticmethod
    def _print_info(self):
        print(f"Planet radius: {self.radius}")
        print(f"Planet mask: {self._mask}")
    


r = Planet()
print(r.get_radius(cls=r))
print(r.mask)
print(r._print_info(r))
