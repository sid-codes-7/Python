import random
import time


traffic_light_time = 5 

queue_north = random.randint(3,10)
queue_south = random.randint(3,10)
queue_east = random.randint(3,10)
queue_west = random.randint(3,10)
traffic_directions = ["North", "South", "East", "West"]
weather = ["Sunny", "Rainy", "Foggy", "Slippery"]
random_weather = random.choice(weather)

print("\nWeather: ", random_weather)

def run_simulation():
    
    global traffic_light_time, queue_north, queue_south, queue_west, queue_east
    

    while queue_north > 0 or queue_south > 0 or queue_east > 0 or queue_west > 0:
        print(f"\n--- Traffic Cycle (Time: {traffic_light_time}) ---")
        
       
        if queue_north > 0:
            reduced = random.randint(1, min(3, queue_north))
            queue_north -= reduced
            print(f"North queue reduced by {reduced}. Remaining: {max(0, queue_north)}")
        
        if queue_south > 0:
            reduced = random.randint(1, min(3, queue_south))
            queue_south -= reduced
            print(f"South queue reduced by {reduced}. Remaining: {max(0, queue_south)}")

        if queue_east > 0:
            reduced = random.randint(1, min(3, queue_east))
            queue_east -= reduced
            print(f"East queue reduced by {reduced}. Remaining: {max(0, queue_east)}")

        if queue_west > 0:
            reduced = random.randint(1, min(3, queue_west))
            queue_west -= reduced
            print(f"West queue reduced by {reduced}. Remaining: {max(0, queue_west)}")


        print("Current Queues - " \
              "\nN:", max(0, queue_north), 
              "\nS:", max(0, queue_south), 
              "\nE:", max(0, queue_east), 
              "\nW:", max(0, queue_west))
        

        traffic_light_time -= 1
  
        if traffic_light_time <= 0:
            print("Traffic light time finished.")
            break
            
        time.sleep(1) 

    print("\nSimulation Finished.")


run_simulation()
