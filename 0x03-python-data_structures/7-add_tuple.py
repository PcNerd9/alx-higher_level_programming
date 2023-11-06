#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    t_a_0 = tuple_a[0] if len(tuple_a) > 0  else 0
    t_a_1 = tuple_a[1] if len(tuple_a) > 1 else 0 

    t_b_0 = tuple_b[0] if len(tuple_b) > 0 else 0
    t_b_1 = tuple_b[1] if len(tuple_b) > 1 else 0
    return(t_a_0 + t_b_0, t_a_1 + t_b_1)
