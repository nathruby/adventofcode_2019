def get_orbits():
    orbits = []

    with open('input.txt', 'r') as orbit_plan:
        for line in orbit_plan:
            orbits.append(line.strip('\n').split(')'))

    direct_orbits = {orbit: source for source,orbit in orbits}

    #check if the orbit's source directly orbits another body
    orbit_paths = { orbit: find_parent_orbits(orbit, direct_orbits) for orbit in direct_orbits.keys()}
    
    print(sum([len(orbit_paths[orbit_path]) for orbit_path in orbit_paths.keys()]))

    find_orbital_transfers_around_you(direct_orbits, orbit_paths)

def find_parent_orbits(orbit, orbits):
    
    source = orbits.get(orbit)

    if not source:
        return []

    return [source] + find_parent_orbits(source, orbits)

def find_orbital_transfers_around_you(orbits, indirect_orbits):

    #find the path to the common parent
    you_path = find_parent_orbits("YOU", orbits)
    san_path = find_parent_orbits("SAN", orbits)
    
    #add up the lengths of each path, removing the intersected values 
    #as they go past the shortest path needed to reach destination
    print(len(you_path) + len(san_path) - 2*len(set(you_path) & set(san_path)))

if __name__ == "__main__":
    get_orbits()