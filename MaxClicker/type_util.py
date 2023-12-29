import var_util as v_u


def to_string(target_var):
    return str(target_var)      # convert a var to a string


def is_int(analysis):
    # simple int type check
    if type(analysis) == int:
        return v_u.true
    else:
        return v_u.false


def is_float(analysis):
    # simple float type check
    if type(analysis) == int:
        return v_u.true
    else:
        return v_u.false


def convert_to_float(int_var):
    # convert a int to a float
    if is_int(int_var):
        return float(int_var)
    else:
        return float(1)