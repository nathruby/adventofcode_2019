def get_orbits():
    orbits = []
    indirect_orbits = {}

    with open('input.txt', 'r') as orbit_plan:
        for line in orbit_plan:
            orbits.append(line.strip('\n').split(')'))

    direct_orbits = {orbit: source for source,orbit in orbits}

    #check if the orbit's source directly orbits another body
    indirect_orbits = { orbit: find_indirect_orbits(orbit, direct_orbits) for orbit in direct_orbits.keys()}

    print(sum([len(indirect_orbits[indirect_orbit]) for indirect_orbit in indirect_orbits]))

    find_orbital_transfers_around_you(direct_orbits, indirect_orbits)

def find_indirect_orbits(orbit, orbits):
    
    source = orbits.get(orbit)

    if not source:
        return []

    return [source] + find_indirect_orbits(source, orbits)

def find_orbital_transfers_around_you(orbits, indirect_orbits):
    #find the path to the common parent
    you_path = get_path("YOU", orbits)
    san_path = get_path("SAN", orbits)

    #add up the lengths of each path, removing the intersected values and the direct orbits
    print(len(you_path) + len(san_path) - 2*len(set(you_path) & set(san_path))-2)

def get_path(orbit, orbits):
    if orbits.get(orbit) is not None:
        return [orbit] + get_path(orbits[orbit], orbits)
    else:
        return [orbit]

if __name__ == "__main__":
    get_orbits()