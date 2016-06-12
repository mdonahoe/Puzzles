terrain = [5, 8, 4, 4, 4, 6, 4, 3, 2, 4, 4, 6, 1, 3, 3, 2, 2, 1, 4, 3]
stack = []
total_water = 0

class Grid(dict):
    "Helper for visualizing the terrain and water level"
    def add_water(self, x, y):
        assert (x, y) not in self
        self[(x, y)] = 'o'

    def add_terrain(self, x, y):
        assert (x, y) not in self
        self[(x, y)] = '|'

    def draw(self):
        out = []
        for y in reversed(range(max(terrain))):
            for x in range(len(terrain)):
                out.append(self.get((x, y), ' '))
            out.append('\n')
        print ''.join(out)

grid = Grid()

for i, h in enumerate(terrain):
    # Add the terrain pixels to the map.
    for y in range(h):
        grid.add_terrain(i, y)

    while True:
        if not stack or terrain[stack[-1]] > h:
            stack.append(i)
            break
        if h > terrain[stack[-1]]:
            low_h = terrain[stack.pop()]
            # Fill in some water
            if not stack:
                # There is no left wall to hold the water, ignore.
                continue
            wall_h = min(h, terrain[stack[-1]])
            left_x = stack[-1] + 1
            water_block = (wall_h - low_h) * (i - left_x)
            total_water += water_block

            # Add the watered pixels to the map and draw it.
            for y in range(low_h, wall_h):
                for x in range(left_x, i):
                    grid.add_water(x, y)
            grid.draw()
        else:
            # This section is flat. Update the stack to take the right-most section.
            stack[-1] = i
            break

print 'water', total_water
print 'stack', stack
grid.draw()
