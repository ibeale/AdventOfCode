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
    test_input = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L"
    space_objects = string_to_orbit(test_input)
    print_space_object_info(space_objects)
    num = count_direct_and_indirect(space_objects)
    print(f"Total direct + indirect = {num}")
    

def count_direct_and_indirect(space_objects):
    for space_obj in space_objects:
        
                
def get_string_from_file():
    with open("input.txt") as f:
        return f.read()

def print_space_object_info(space_objects):
    for space_obj in space_objects:
        print(f"Name: {space_obj.name}")
        print(f"Orbits: {space_obj.orbits}")
        print(f"These objects oribt around {space_obj.name}: {space_obj.orbiter}")
        print("---------------------")

def string_to_orbit(input):
    space_objects = []
    orbit_data = input.split("\n")
    for data in orbit_data:
        names = data.split(")")
        object1 = space_object(name = names[0])
        object1.add_orbiter(names[1])
        object2 = space_object(name = names[1], orbits = names[0])
        if object1 not in space_objects:
            space_objects.append(object1)
        else:
            space_objects[space_objects.index(object1)].orbiter += (object1.orbiter)
        if object2 not in space_objects:
            space_objects.append(object2)
    return space_objects
    

if __name__ == "__main__":
    main()