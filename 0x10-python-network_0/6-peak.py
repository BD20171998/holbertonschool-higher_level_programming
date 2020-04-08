#!/usr/bin/python3


def find_peak(list_of_integers):

    if list_of_integers == [] or list_of_integers is None:
        return None

    def binarySearch(arr, l, r):

        if l == r:
            return l

        mid = (r + l) / 2
        mid = int(mid)

        if arr[mid] > arr[mid + 1]:
            return binarySearch(arr, l, mid)

        return binarySearch(arr, mid + 1, r)

    return list_of_integers[binarySearch(list_of_integers, 0,
                                         len(list_of_integers) - 1)]
