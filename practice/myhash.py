# hash_distribution
from collections import Counter


def distribute(items, num_containers, hash_function=hash):
    return Counter([hash_function(item) % num_containers for item in items])


def plot(histogram):
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")


histogram = [5, 6, 6, 3, 9]
plot(histogram)
