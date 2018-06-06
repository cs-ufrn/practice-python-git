# This file provides a simple command-line calculator, 
# with implementations of important mathematical functionalities.
#
# The implementors must fill the empty functions (all of them!)
# with the right code. Also, there are some functions specified only in comments, 
# without their declarations, so one should declare 
# and implement them.
#
# All functions must be properly documented.
#
# CS UFRN 2018
###################################################################################

def display_calculator():
    ''' Interact with the user, showing a command-line menu and
        receiving input for operations and operands. '''
    pass

def mean(values):
    pass

def median(values):
    pass

# mode 
#
# Takes a list and computes the mode value.

# standard_deviation  
#
# Takes a list and computes the standard deviation of its values.

# n_max_numbers
#
# Takes an integer N and a list L, and computes the N maximum numbers in L.

# n_min_numbers
#
# Takes an integer N and a list L, and computes the N minimum numbers in L.

# sum_n_max_numbers
#
# Takes an integer N and a list L, and computes the sum of the N maximum numbers in L.

# sum_n_min_numbers
#
# Takes an integer N and a list L, and computes the sum of the N minimum numbers in L.

def validate_matrix(lists):
    try:
        columns = len(lists[0])

        for row in lists[1:]:
            if len(row) != columns:
                return False
        return True
    except (TypeError, LookupError):
        err = "lists argument is not 2-dimensional list"
        raise TypeError(err)

def add_matrices(matrix1, matrix2):
    if not validate_matrix(matrix1) or not validate_matrix(matrix2):
        raise TypeError("argument is not a valid matrix")
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("matrices do not have the same shape")

    result = []
    for m1_row, m2_row in zip(matrix1, matrix2):
        result_row = [t1+t2 for t1,t2 in zip(m1_row, m2_row)]
        result.append(result_row)
    return result

def multiply_matrices(matrix1, matrix2):
    if not validate_matrix(matrix1) or not validate_matrix(matrix2):
        raise TypeError("argument is not a valid matrix")
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("matrices shapes do not align")

    result = []
    for m1_row in matrix1:
        result_row = []
        for m2_col in zip(*matrix2):
            r_term = sum([a*b for a,b in zip(m1_row, m2_col)])
            result_row.append(r_term)
        result.append(result_row)
    return result

# exp_approx
#
# Takes a value X and a float E, and computes an approximation for e^X with maximum error E.

# sin_approx
#
# Takes a value X and a float E, and computes an approximation for sin(X) with maximum error E.

# cos_approx
#
# Takes a value X and a float E, and computes an approximation for cos(X) with maximum error E.

