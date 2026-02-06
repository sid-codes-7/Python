import random
import time

# Initial traffic light time and queues
traffic_light_time = 5
queue_north = random.randint(3, 10)
queue_south = random.randint(3, 10)
queue_east = random.randint(3, 10)
queue_west = random.randint(3, 10)

# Weather options
weather = ["Sunny", "Rainy", "Foggy", "Slippery", "Normal"]
random_weather = random.choice(weather)


# Set traffic light time and reduction range based on weather
if random_weather == "Sunny": #Sunny
    traffic_light_time = 3
    reduction_min = 0
    reduction_max = 1
    print("\nWEATHER: Sunny --> More cars getting out less due to the relaxation of drivers.\n")

elif random_weather == "Rainy": #Rainy
    traffic_light_time = 5
    reduction_min = 0
    reduction_max = 1
    print("\nWEATHER: Rainy --> More cars getting out more due to heavy rain and wanting to get home faster.\n")

elif random_weather == "Foggy": #Foggy
    traffic_light_time = 5
    reduction_min = 0
    reduction_max = 1
    print("\nWEATHER: Foggy --> More cars getting out less due to heavy fog and not being able to see much.\n")

elif random_weather == "Slippery": #Slippery
    traffic_light_time = 7
    reduction_min = 0
    reduction_max = 1
    print("\nWEATHER: Slippery --> Fewer cars getting out due to slippery roads and fear of accidents.\n")

else:  # Normal
    traffic_light_time = 7
    reduction_min = 1
    reduction_max = 3
    print("\nWEATHER: Normal --> Conditions are fine; more cars are exiting.\n")

# Run the simulation loop
while queue_north > 0 or queue_south > 0 or queue_east > 0 or queue_west > 0:
    print(f"\n--- Traffic Cycle (Time Left: {traffic_light_time}) ---")

    if queue_north > 0:
        reduced = random.randint(reduction_min, min(reduction_max, queue_north))
        queue_north -= reduced
        print(f"North queue reduced by {reduced}. Remaining: {queue_north}")

    if queue_south > 0:
        reduced = random.randint(reduction_min, min(reduction_max, queue_south))
        queue_south -= reduced
        print(f"South queue reduced by {reduced}. Remaining: {queue_south}")

    if queue_east > 0:
        reduced = random.randint(reduction_min, min(reduction_max, queue_east))
        queue_east -= reduced
        print(f"East queue reduced by {reduced}. Remaining: {queue_east}")

    if queue_west > 0:
        reduced = random.randint(reduction_min, min(reduction_max, queue_west))
        queue_west -= reduced
        print(f"West queue reduced by {reduced}. Remaining: {queue_west}")

    print("\nCurrent Queues:")
    print("North:", queue_north)
    print("South:", queue_south)
    print("East:", queue_east)
    print("West:", queue_west)

    traffic_light_time -= 1

    if traffic_light_time <= 0:
        print("Traffic light time finished.")
        break

    time.sleep(1)

print("\nSimulation Finished.")
