"""
decorate any function with @trace to display arguments
and results in terminology at each call.
you can also use "data_tycat" to display variables.
"""
from tempfile import NamedTemporaryFile
from os import system
from time import sleep
# TODO: we need to escape special strings for dot.
# TODO: we cannot trace constructor since __str__ will often not work
# before for end of initialization of self

def _dot_ref(variable):
    """
    should given var be dereferenced for dot display ?
    (strings, numbers and None should not)
    """
    if isinstance(variable, (int, float, str)) or variable is None:
        return False

    return True


def _dot_value(variable):
    """
    dot strings for displaying data.
    return address if a reference or string from __str__ else.
    """
    if _dot_ref(variable):
        return str(hex(id(variable)))

    return str(variable)


def _variable_content(variable):
    """
    return list of content of variable for dot display.
    each element in the returned list is a tuple
    (field_name, field_label (in dot), field_value).
    """
    if not _dot_ref(variable):
        return [(str(variable), str(variable), variable)]

    if isinstance(variable, (list, tuple)):
        return [("e"+str(index), _dot_value(value), value)
                for index, value in enumerate(variable)]

    if isinstance(variable, dict):
        return [("k"+str(key), str(key)+":"+_dot_value(value), value)
                for key, value in variable.items()]

    return [(name,
             name + ":" + _dot_value(getattr(variable, name)),
             getattr(variable, name))
            for name in vars(variable)]

def _save_variable_dot(dot_file, remaining_variables, variable):
    """
    save dot code for displaying given variable.
    variables referenced in given var will be added to remaining
    variables.
    """
    print("n{} [label=\"".format(hex(id(variable))), end="", file=dot_file)
    edges = []
    node_content = []

    for field_name, field_label, field_value in _variable_content(variable):
        node_content.append("<" + field_name + ">" + " " + field_label)

        if _dot_ref(field_value):
            edges.append("\"n{}\":{} -> n{};".format(
                hex(id(variable)),
                field_name,
                hex(id(field_value))
            ))
            remaining_variables.append(field_value)

    print(" | ".join(node_content), end="", file=dot_file)
    print("\"];", file=dot_file)

    print("\n".join(edges), file=dot_file)


def _save_dot(dot_file, variables):
    """
    save graph of accessible memory in dot file.
    """
    print("digraph {", file=dot_file)
    print("node [shape=record];", file=dot_file)
    seen_variables = set()

    remaining_variables = list(variables)
    while remaining_variables:
        variable = remaining_variables.pop()
        if id(variable) in seen_variables:
            continue
        seen_variables.add(id(variable))
        _save_variable_dot(dot_file, remaining_variables, variable)

    print("}", file=dot_file)


def data_tycat(*variables):
    """
    draw graph of accessible memory from given array of variables
    in terminology using tycat.
    """
    dot_file = NamedTemporaryFile(mode="w", delete=False)
    _save_dot(dot_file, variables)
    dot_file.close()
    dot_name = dot_file.name
    png_name = dot_name + ".png"
    system("dot -Tpng {} -o {}".format(dot_name, png_name))
    system("tycat {}".format(png_name))
    sleep(1)


def trace(function):
    """
    activate terminal display (tycat) of function arguments and results.
    """
    def tracer(*arguments):
        """
        trace and call original function.
        """
        print("-----------------------------------")
        print(function.__name__ + "(" + ",".join([str(a) for a in arguments])
              + ")")

        data_tycat(*arguments)

        result = function(*arguments)
        if result is not None:
            print("---->" + str(result))
            data_tycat(result)

        return result

    return tracer
