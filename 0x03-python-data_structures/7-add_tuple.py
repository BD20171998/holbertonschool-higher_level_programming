#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        x, y = tuple_a[0:2]
        w, t = tuple_b[0:2]
        return (x + w, y + t)

    elif not tuple_a and not tuple_b:
        return (0, 0)

    elif len(tuple_a) == 1 and len(tuple_b) >= 2:
        x = tuple_a[0]
        w, t = tuple_b[0:2]
        return (x + w, t)

    elif len(tuple_a) >= 2 and len(tuple_b) == 1:
        x, y = tuple_a[0:2]
        w = tuple_b[0]
        return (x + w, y)

    elif not tuple_a and len(tuple_b) == 1:
        w = tuple_b[0]
        return (w, 0)

    elif len(tuple_a) == 1 and not tuple_b:
        x = tuple_a[0]
        return (x, 0)

    elif not tuple_a and len(tuple_b) == 2:
        w, t = tuple_b[0:2]
        return (w, t)

    elif len(tuple_a) == 2 and not tuple_b:
        x, y = tuple_a[0:2]
        return (x, y)

    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        x = tuple_a[0]
        w = tuple_b[0]
        return (x, w)
