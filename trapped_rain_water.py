def trapped_rain_water(elevation_map):
    n = len(elevation_map)

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = elevation_map[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], elevation_map[i])

    right_max[n-1] = elevation_map[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], elevation_map[i])

    trapped_water = 0
    for i in range(1, n-1):
        water = min(left_max[i], right_max[i]) - elevation_map[i]
        if water > 0:
            trapped_water += water

    return trapped_water

if __name__ == "__main__":
    elevation_map = [0,1,0,2,1,0,1,3,2,1,2,1]
    max_water = trapped_rain_water(elevation_map)
    print(max_water)
    #output = 6
