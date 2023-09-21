# Generalization of functions (or algorithms)
# is the process of modifying a function/algorithm that
# solves a specific problem so that it can solve a wider range of problems, or a larger number of
# instances of the same problem

# How can we generalize each function for reusability?
# (a) This function computes the most number of cards in a 52 card deck that can be dealt equally amongst
# four people

def cards_per_player(number_of_cards, number_of_people ):
    return number_of_cards // number_of_people


# (b) This function computes the number of hours required to watch a 26 episode television show consisting
# of 22 minute episodes

def total_watch_time(n_episodes, min_per_episode):
    mins_per_hour = 60  # constant
    return n_episodes * min_per_episode / mins_per_hour


def paper_thickness_folded(paper_thickness_mm, n_fold):
    total_thickness = paper_thickness_mm * 2**n_fold / 1000 /1000
    return total_thickness

print( paper_thickness_folded(0.1, 42) )  #384,000 km



