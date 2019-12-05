import math

INPUT = [
114739,
132732,
123925,
146385,
72590,
51932,
64164,
72919,
97336,
101791,
101477,
95677,
89907,
76998,
60782,
109021,
138070,
113374,
68672,
133830,
134079,
89079,
72321,
142643,
102734,
103743,
77864,
111363,
72140,
64483,
139567,
141318,
132736,
87824,
81937,
123404,
56730,
54447,
63602,
84561,
145159,
93598,
137770,
52943,
146307,
91674,
143183,
52543,
143052,
107171,
80699,
130825,
141406,
75771,
123497,
87982,
144545,
125153,
147925,
106898,
60193,
111251,
102454,
135886,
141408,
84556,
94143,
97958,
86474,
96848,
126314,
51037,
140379,
142065,
73629,
102432,
123801,
68146,
107720,
51512,
123873,
104308,
59601,
149175,
80400,
76822,
116115,
87990,
90592,
68688,
133868,
78357,
91425,
149328,
123010,
93278,
101150,
120352,
107642,
136050]

def find_total_fuel_requirements(modules):
    total = 0

    for module_mass in modules:
        total += find_module_fuel(module_mass)

    print(total)
    
def find_module_fuel(module_mass):
    module_fuel = math.floor(module_mass / 3) - 2

    if module_fuel < 0:
        return 0
    
    return find_fuel_for_module_fuel(module_fuel)

def find_fuel_for_module_fuel(fuel_mass):
    fuel_for_module_fuel = math.floor(fuel_mass / 3) - 2

    if fuel_for_module_fuel < 0:
        return fuel_mass

    return fuel_mass + find_fuel_for_module_fuel(fuel_for_module_fuel)

if __name__ == "__main__":
    find_total_fuel_requirements(INPUT)