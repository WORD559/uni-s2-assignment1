# -*- coding: utf-8 -*-
# pylint: disable=E0012, invalid-name, no-member, C0301, C0411, C1801, W0622, W0511, W0611


''' Term 2, Assignment 1

Assignment Tasks: 2

Restrictions:
    Do not change anything outside TODO blocks.
    Do not use import.
    Do not add pylint directives.
    Do not use random numbers, i.e. don't draw samples of birthdays.

Author of template:
    Wolfgang Theis
    School of Physics and Astronomy
    University of Birmingham
'''

import numpy as np

# TODO: Assignment Task 1: write any utility functions you might find useful
def month_probability(months):
    """Calculates your probability of being born in any given month knowing
    the number of days in each month.

    Parameters
    ----------
    months : dictionary {name_of_month: days_in_the_month}

    Returns
    -------
    probabilities : dictionary {name_of_month: probability}
        This is the normalised probability of being born in the given month

    """

    total_days = sum(months.values())
    probabilities = months.copy()
    for key, val in months.items():
        probabilities[key] = val/total_days

    return probabilities

def student_chance_of_matching(name, probabilities=None):
    """Calculates your probability of the first letter of an individual student's
    name matching the first letter of their birth month.

    Parameters
    ----------
    name : name of student
    months : dictionary {name_of_month: days_in_the_month}

    Returns
    -------
    probability : float

    """

    probability = 0.0
    for key, val in probabilities.items():
        if key[0].lower() == name[0].lower():
            probability += val

    return probability

def inverse_probabilities(probabilities):
    """Inverts all probabilities in a probability dictionary as inverse = (1-p)

    Parameters
    ----------
    probabilities : dictionary {key: probability}

    Returns
    -------
    inv_probabilities: dictionary {key: inverse_probability}

    """
    inv_probabilities = {}
    for key, val in probabilities.items():
        inv_probabilities[key] = 1-val

    return inv_probabilities

# End of Task 1; proceed to Task 2

def matching(months, names):
    ''' Calculate the average number of matches between first letter in name
    and month of birth for months and list of names as provided.
    Further calculate the probability that no letters match.
    It is assumed that there are no seasonal preferences for certain names.

    Parameters
    ----------
    months : dictionary {name_of_month: days_in_the_month}
        does not have to be the latin calendar but can be an arbitrary number
        of months with an arbitrary number of days to facilitate reliable
        testing of the function.
    names : list of unicode strings
        list of names

    Returns
    -------
    (avg_matches, prob_no_match) : tuple of numbers
        avg_matches is the average number of matches of name's initial
        with birth month's initial.
        prob_no_match is the probability that no match occurs.

    '''
    # TODO: Assignment Task 2: write function body
    probabilities = month_probability(months)
    student_matches = {}
    for name in names:
        student_matches[name] = student_chance_of_matching(name, probabilities=probabilities)
    avg_matches = sum(student_matches.values())
    inv_student_matches = inverse_probabilities(student_matches)
    prob_no_match = np.product(list(inv_student_matches.values()))

    return (avg_matches, prob_no_match)


    # End of Task 2; no further tasks

if __name__ == '__main__':

    import unittest

    class Tests(unittest.TestCase):
        ''' tests for average_matches_and_no_match_probability(months, names) '''

        def test_single_month_no_match_one_name(self):
            ''' matching({'January': 31}, ['Tim']) should yield 0, 1'''
            self.assertEqual(matching({'January': 31}, ['Tim']), (0, 1))

        def test_single_month_no_match_multi_name(self):
            ''' matching({'January': 31}, ['Tim', 'Tina']) should yield 0, 1'''
            self.assertEqual(matching({'January': 31}, ['Tim', 'Tina']), (0, 1))

        def test_single_month_match_one_name(self):
            ''' matching({'January': 31}, ['Jim']) should yield 1, 0'''
            self.assertEqual(matching({'January': 31}, ['Jim']), (1, 0))

        def test_single_month_match_multi_name(self):
            ''' matching({'January': 31}, ['Jim', 'Jill']) should yield 2, 0'''
            self.assertEqual(matching({'January': 31}, ['Jim', 'Jill']), (2, 0))

        def test_two_months_match_all_names(self):
            ''' matching({'January': 31, 'June': 30}, ['Jim', 'Jill']) should yield 2, 0'''
            self.assertEqual(matching({'January': 31, 'June': 30}, ['Jim', 'Jill']), (2, 0))

        def test_two_months_two_names_one_month_matching_one_name(self):
            ''' matching({'January': 15, 'April': 5}, ['Anna', 'Rob']) should yield 0.25, 0.75'''
            self.assertEqual(matching({'January': 15, 'April': 5}, ['Anna', 'Rob']), (0.25, 0.75))

        def test_two_months_two_names_pairwise_matching(self):
            ''' matching({'January': 15, 'April': 5}, ['Anna', 'James']) should yield 1.0, 0.1875'''
            self.assertEqual(matching({'January': 15, 'April': 5}, ['Anna', 'James']), (1.0, 0.1875))

    unittest.main(exit=False)
