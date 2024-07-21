distance_from_sun = {
  # for planets in  distance_from_sun
    "mercury": {
        "moons": 0,
        "atmosphere": False
         #print(distance_from_sun["mercury"]["moons"])
    },
    "venus": {
        "moons": 1,
        "atmosphere": False
        #print(distance_from_sun["venus"]["moons"])

    },
}
print(distance_from_sun["venus"]["moons"])

total_moons = 0
for x in distance_from_sun:
    print(x + " " + str(distance_from_sun[x]["moons"]))
    total_moons = total_moons + distance_from_sun[x]["moons"]

print("total amt of moons " +str(total_moons))    
