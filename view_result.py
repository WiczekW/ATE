from ABS_analyzer import mass_to_dict
from global_data import abs_to_analyze, result_update


def view_result():
    global abs_to_analyze, result_update
    print(abs_to_analyze)
    print(result_update)
    for i in abs_to_analyze:
        result_update.append(mass_to_dict(str(i)))
    print(result_update)
    return result_update