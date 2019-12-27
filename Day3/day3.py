

def parse_input():
    with open("input.txt") as f:
        input = f.read().split("\n")
    wires = []
    for wire in input:
        wires.append(wire.split(','))
    return wires

def define_lines(wire):
    cur_pos = (0,0)
    positions = []
    positions.append(cur_pos)
    for delta_pos in wire:
        direction = delta_pos[0]
        distance = int(delta_pos[1:])
        if direction == "R":
            new_pos = (cur_pos[0] + distance, cur_pos[1])
        elif direction == "L":
            new_pos = (cur_pos[0] - distance, cur_pos[1])
        elif direction == "U":
            new_pos = (cur_pos[0], cur_pos[1] + distance)
        elif direction == "D":
            new_pos = (cur_pos[0], cur_pos[1] - distance)
        positions.append(new_pos)
        cur_pos = new_pos
    return positions

def find_slope(pt1, pt2):
    if pt1[0] == pt2[0]:
        return None
    else:
        return 0

def find_intercept(slope, pt):
    if slope is None:
        return None
    else:
        return pt[1]

def between(bound1, testpt, bound2):
    return ((bound1 <= testpt <= bound2) or (bound1 >= testpt >= bound2))


def find_intersections(wire_line1, wire_line2):
    intersections = []
    for i in range(1, len(wire_line1)):
        for j in range(1, len(wire_line2)):
            if find_slope(wire_line1[i-1], wire_line1[i]) == 0:
                if (between(wire_line1[i-1][0], wire_line2[j][0], wire_line1[i][0])):
                    if(between(wire_line2[j-1][1], wire_line1[i][1], wire_line2[j][1])):
                        intersections.append((wire_line2[j][0], wire_line1[i][1]))
            else:
                if (between(wire_line1[i-1][1], wire_line2[j][1], wire_line1[i][1])):
                    if(between(wire_line2[j-1][0], wire_line1[i][0], wire_line2[j][0])):
                        intersections.append((wire_line1[i][0], wire_line2[j][1]))
            
    if (0,0) in intersections:
        intersections.remove((0,0))

    return(intersections)


def find_closest(intersections):
    closest = 9999999999
    for intersection in intersections:
        distance = abs(intersection[0]) + abs(intersection[1])
        if(distance < closest):
            closest = distance
            point = intersection
    print(f"The closest intersection to the origin is {closest}, at point {point}")


def dist_between(pt1, pt2):
    if pt1[0] == pt2[0]:
        return abs(pt2[1] - pt1[1])
    elif pt1[1] == pt2[1]:
        return abs(pt2[0] - pt1[0])


def dist_to_intersection(wire_line, intersection_pts):
    distances = []
    for intersection in intersection_pts:
        dist = 0
        for i in range(1, len(wire_line)):
            if wire_line[i-1][1] == wire_line[i][1]:
                dist += dist_between(wire_line[i-1], wire_line[i])
                if intersection[1] == wire_line[i][1] and between(wire_line[i-1][0], intersection[0], wire_line[i][0]):
                    dist -= dist_between(wire_line[i-1], wire_line[i])
                    dist += dist_between(wire_line[i-1], intersection)
                    distances.append(dist)
                    dist += dist_between(wire_line[i-1], wire_line[i])
                    dist -= dist_between(wire_line[i-1], intersection)
                    break
            else:
                dist += dist_between(wire_line[i-1], wire_line[i])
                if intersection[0] == wire_line[i][0] and between(wire_line[i-1][1], intersection[1], wire_line[i][1]):
                    dist -= dist_between(wire_line[i-1], wire_line[i])
                    dist += dist_between(wire_line[i-1], intersection)
                    distances.append(dist)
                    dist += dist_between(wire_line[i-1], wire_line[i])
                    dist -= dist_between(wire_line[i-1], intersection)
                    break
    return distances
                    
        



def main():
    wires = parse_input()
    wire_lines = []
    for wire in wires:
        wire_lines.append(define_lines(wire))
    intersections = find_intersections(wire_lines[0], wire_lines[1])
    print(intersections)
    distances1 = dist_to_intersection(wire_lines[0], intersections)
    distances2 = dist_to_intersection(wire_lines[1], intersections)
    shortest = 99999999999
    for i in range(len(distances1)):
        sum = distances1[i] + distances2[i]
        if sum < shortest:
            shortest = sum
            print(shortest)
    

if __name__ == "__main__":
    main()