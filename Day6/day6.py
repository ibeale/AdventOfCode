class space_object:
    def __init__(self, name=None, orbits=None):
        self.name = name
        self.orbits = orbits
        self.orbiter = []
    
    def add_orbiter(self, space_object_name):
        self.orbiter.append(space_object_name)

    def __eq__(self, other):
        return self.name == other.name

    def __name__(self):
        return self.name

    def __repr__(self):
        return self.name


def main():
    test_input = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN"
    input = get_string_from_file()
    space_objects = string_to_orbit(input)
    sum = 0
    print_space_object_info(space_objects)
    print(len(space_objects))
    for key in space_objects:
        sum += count_parents(space_objects[key], space_objects)
    print(sum)
    paths = shortest_path(space_objects, space_objects["YOU"], space_objects["SAN"])
    print(paths["SAN"] - 2)
    

def count_parents(space_obj, space_objects):
    if space_obj.orbits:
        return 1 + count_parents(space_objects[space_obj.orbits.name], space_objects)
    else:
        return 0

        
                
def get_string_from_file():
    with open("C:/Users/isaac/Documents/MyProjects/AdventOfCode/Day6/input.txt") as f:
        return f.read()

def print_space_object_info(space_objects):
    with open("output.txt", "w+") as f:
        for key in space_objects:
            f.write(f"Name: {space_objects[key].name}\n")
            f.write(f"Orbits: {space_objects[key].orbits}\n")
            f.write(f"These objects orbit around {space_objects[key].name}: {space_objects[key].orbiter}\n")
            f.write("---------------------\n")

def string_to_orbit(input):
    space_objects = {}
    orbit_data = input.split("\n")
    for data in orbit_data:
        names = data.split(")")
        object1 = space_object(name = names[0])
        object2 = space_object(name = names[1], orbits = object1)
        object1.add_orbiter(object2)
        if object1.name not in space_objects:
            space_objects[object1.name] = object1
        else:
            space_objects[object1.name].orbiter.append(object2)
        if object2.name not in space_objects:
            space_objects[object2.name] = object2
        else:
            space_objects[object2.name].orbits = object1
    return space_objects

def shortest_path(space_objects, start_object, end_object):
    unsolved = []
    to_solve = {}
    solved = {}
    for key in space_objects:
        unsolved.append(key)
    unsolved.remove(start_object.name)
    to_solve[start_object.name] = 0
    cur = start_object
    dist_to_cur = 0
    while end_object.name not in solved:
        will_solve = {}
        for planet in to_solve:
            if planet not in solved:
                for orb in space_objects[planet].orbiter:
                    if space_objects[orb.name].name not in to_solve and space_objects[orb.name].name not in solved:
                        will_solve[space_objects[orb.name].name] = dist_to_cur + 1
                if space_objects[planet].orbits and (space_objects[planet].orbits.name not in to_solve) and (space_objects[planet].orbits.name not in solved):
                    will_solve[space_objects[planet].orbits.name] = dist_to_cur + 1
                value = to_solve[planet]
                solved[planet] = value
                if end_object.name in solved:
                    return solved
                
        to_solve = will_solve
        dist_to_cur += 1
        



    

if __name__ == "__main__":
    main()