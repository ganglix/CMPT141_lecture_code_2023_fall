def cost_phone_call(call_duration):
    """
    computes the cost of a phone call
    call_duration: length of phone call in minutes
    return: total cost of phone call after all fees applied
    """

    # base cost of call
    cost = 0.35

    # compute cost of call in first ten minutes
    cost = cost + min(call_duration, 10.0) * 0.50
    remaining_duration = max(call_duration - 10.0, 0.0) #;print("remaining_duration",remaining_duration)

    # compute cost of call after first ten minutes
    # (only counts full minutes)
    cost = cost + remaining_duration / 1 * 0.25 #; print("addition cost after 10 mins", remaining_duration / 1 * 0.25)

    # discount from plan deducts 10% from total cost
    cost = cost * 0.9
    return cost

"""
line    cost    call_duration   remaining_duration
9       0.35    11.15
12      5.35    11.15
13      5.35    11.15           1.15
17

"""

# should be 5.04
inputs = 11.15
expected_outputs = 5.04
bill = cost_phone_call(11.15)

print(bill)
# if bill != expected_outputs:
#     print("fault found!",
#           "inputs", inputs,
#           "expected", expected_outputs,
#           "returned", bill)
