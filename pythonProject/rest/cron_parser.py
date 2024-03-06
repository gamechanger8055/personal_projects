from sys import argv
import unittest


def define_string(string, datatype):
    """
    INPUT: string = Value of parameter, datatype = Type of the parameter.
    OUTPUT: String indicating the matching time period for that parameter
    (e.g. which minutes the command will run).
    """
    # ranges for the different parameter values
    values = {
        'week': [i for i in range(1, 8)],
        'month': [i for i in range(1, 13)],
        'hour': [i for i in range(0, 24)],
        'day': [i for i in range(1, 32)],
        'minute': [i for i in range(0, 60)]
    }

    # word conversions for months of the year
    months = [
        'JAN', 'FEB', 'MAR',
        'APR', 'MAY', 'JUN',
        'JUL', 'AUG', 'SEP',
        'OCT', 'NOV', 'DEC'
    ]

    # word conversions for days of the week
    days = [
        'SUN', 'MON', 'TUE',
        'WED', 'THU', 'FRI',
        'SAT'
    ]

    # return all values in range if * selector is used
    if string == "*":
        return ' '.join(map(str, values[datatype]))

    if string == "?":
        return 'Not Specified'

    # handle ranges
    if "-" in string:
        values = days if datatype == "week" else months
        return handle_range(string, values, datatype)

    # handle intervals
    if "/" in string:
        return handle_intervals(string, values[datatype], datatype)

    # handle lists
    if "," in string:
        if datatype == 'month' or datatype == 'week':
            sub = days if datatype == "week" else months
            return handle_lists(string, values[datatype], datatype, sub)
        else:
            return handle_lists(string, values[datatype], datatype)

    # handle last operator
    if "L" in string:
        return handle_last(string, datatype, days)

    # handle weekday operator
    if "W" in string:
        return handle_weekday(string, datatype)

    return string


def handle_range(string, values, datatype):
    """
    INPUT: string = Value of parameter, values = Array of possible values for
    parameter, datatype = Type of the parameter.
    OUTPUT: String of all values in the range given. If word form was used
    (e.g. JAN instead of 1), it returns a word-formatted range.
    """
    start, end = string.split('-')
    try:
        start, end = int(start), int(end)
    except ValueError:
        try:

            start, end = values.index(start.upper()), values.index(end.upper())
            return ' '.join(values[start:end + 1])
        except ValueError:
            raise Exception('{} input combination is not valid. Please use either string or number syntax.'.format(datatype))

    return ' '.join(map(str, [i for i in range(start, end + 1)]))


def handle_intervals(string, values, datatype):
    """
    INPUT: string = Value of parameter, values = Array of possible value for
    parameter.
    OUTPUT: String of all the values matching the specified interval in the
    possible range.
    """
    first, second = string.split("/")

    if first == "*":
        return ' '.join(
            map(str, [i for i in values
                if i % int(second) == 0])
            )

    if type(first) != int or type(second) != int:
        raise Exception('Invalid input for {}'.format(datatype))
    else:
        return ' '.join(
            map(str, [i for i in range(int(first), values[:-1])
                if i % int(second) == 0])
            )


def handle_lists(string, values, datatype, sub=None):
    """
    INPUT: string = Value of parameter, values = Array of possible value for
    parameter, datatype = Type of the parameter, sub = An optional parameter
    used when there are 2 possible input formats (e.g. JAN vs 1). We also
    verify that formats (i.e. JAN vs 1) are not mixed.
    OUTPUT: String of all the values listed in the input, if they are part
    of the range of possible values for that parameter.
    """
    inputs = string.split(',')
    type_value = None
    v = None
    for i in inputs:
        try:
            v = int(i)
        except ValueError:
            v = i

        if type_value is None:
            type_value = type(v)
        elif type_value != type(v):
            raise Exception('{} input combination is not valid. Please use either string or number syntax.'.format(datatype))

        if type(v) == str and v.upper() not in sub:
            raise Exception('Invalid {} data provided'.format(datatype))
        if type(v) == int:
            if v not in values:
                raise Exception('Invalid {} data provided'.format(datatype))


    return string.replace(",", " ")

def handle_last(string, datatype, days):
    """
    INPUT: string = Value of parameter, datatype = Type of the parameter.
    OUTPUT: String indicating the day of the week/month the command will run.
    """
    if datatype == 'week':
        if len(string) > 1:
            num, _ = string.split('L')
            return "Last {} of the Month".format(days[int(num) - 1])
        return days[-1]
    elif datatype == 'day':
        if string == "LW":
            return 'Last week day of the Month'
        elif "-" in string:
            _, day = string.split("-")
            return "{} days from the end of the month".format(day)
        return 'Last day of the Month'
    else:
        raise ValueError('L is not a valid {} input value'.format(datatype))


def handle_weekday(string, datatype):
    """
    INPUT: string = Value of parameter, datatype = Type of the parameter.
    OUTPUT: String indicating the nearest weekday to which day of the month the
    command will run.
    """
    if datatype == 'day':
        date = string.split('W')[0]
        return 'Nearest weekday to day {} of the month'.format(date)


def describe_cron(cron_str):
    """
    INPUT: cron_str = The input string containing the entire cron string from
    the user.
    OUTPUT: A formatted string containing the minute, hour, day, month,
    weekday and command that will run.
    """
    try:
        minute, hour, day, month, week, cmd = cron_str.split(" ")
    except ValueError:
        raise Exception('Not enough parameters passed.')

    return '\n'.join([
        "minute: {}".format(define_string(minute, 'minute')),
        "hour: {}".format(define_string(hour, 'hour')),
        "day of month: {}".format(define_string(day, 'day')),
        "month: {}".format(define_string(month, 'month')),
        "day of Week: {}".format(define_string(week, 'week')),
        "command: {}".format(cmd)
    ])


def main():
    print(describe_cron(argv[1]))


if __name__ == '__main__':
    main()