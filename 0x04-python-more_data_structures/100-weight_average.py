#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or not my_list:
        return 0

    total_score = 0
    total_weight = 0

    for tup in my_list:
        score, weight = tup
        total_score += score * weight
        total_weight += weight
    return total_score / total_weight
