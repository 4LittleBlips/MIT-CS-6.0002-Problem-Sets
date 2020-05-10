###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows_info = {}

    with open(filename, 'r') as cow_data:
        for line in cow_data:
            cow = line.split(',')
            cows_info[cow[0]] = int(cow[1])

    return cows_info


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cows_info = sorted(cows.items(), key = lambda cow: cow[1], reverse = True)
    all_trips = []

    while len(cows_info) != 0:
        trip = []
        total_weight = 0

        for index, cow in enumerate(cows_info):
            if cow[1] + total_weight <= limit:
                trip.append(cow[0])
                total_weight += cow[1]
                del cows_info[index]

        all_trips.append(trip)

    return all_trips





# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    total_weight = 0
    total_partitions = []
    cows_names = list(cows.keys())

    for partition in get_partitions(cows_names):
        total_partitions.append(partition)

    total_partitions = sorted(total_partitions, key = lambda x: len(x))

    for i in range(len(total_partitions)):
        all_trips = total_partitions[i]
        counter = 0
        for trip in all_trips:
            if sum(cows[name] for name in trip) < limit:
                counter += 1
            if counter == len(all_trips):
                return all_trips



        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start1 = time.time()
    greedy = greedy_cow_transport(cows)
    end1 = time.time()
    print('The greed algorithm took {0} seconds and found {1}'.format(end1-start1, greedy))

    start2 = time.time()
    brute = brute_force_cow_transport(cows)
    end2 = time.time()
    print('The Brute Force algorithm took {0} seconds and found {1}'.format(end2-start2, brute))


cows = load_cows('ps1_cow_data.txt')
cows_from_pdf = {"Jesse":6, "Maybel": 3, "Callie": 2, "Maggie": 5}