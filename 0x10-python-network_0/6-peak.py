#!/usr/bin/python3
""" A module that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """A function that finds peak list of unsorted array integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    base_var = 0
    top_var = len(list_of_integers)
    centre_pnt = ((top_var - base_var) // 2) + base_var
    centre_pnt = int(centre_pnt)
    if top_var == 1:
        return list_of_integers[0]
    if top_var == 2:
        return max(list_of_integers)
    if list_of_integers[centre_pnt] >= list_of_integers[centre_pnt - 1] and\
            list_of_integers[centre_pnt] >= list_of_integers[centre_pnt + 1]:
        return list_of_integers[centre_pnt]
    if centre_pnt > 0 and list_of_integers[centre_pnt] < list_of_integers[centre_pnt + 1]:
        return find_peak(list_of_integers[centre_pnt:])
    if centre_pnt > 0 and list_of_integers[centre_pnt] < list_of_integers[centre_pnt - 1]:
        return find_peak(list_of_integers[:centre_pnt])
