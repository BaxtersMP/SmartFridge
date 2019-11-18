from random import *


def generate_weight(size):
    return size + random()


def use_item(item, amount):
    return (1 - amount) * item


def calculate_weight(items):
    return sum(items)

