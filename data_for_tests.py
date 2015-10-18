import datetime

observed_cases = [
    # # case 0 from article
    # {
    #     'S1': [['2011-10-19 00:00:00', '2011-10-19 00:00:07'],
    #            ['UW', 'Google']],
    #     'S2': [['2011-10-19 00:00:00', '2011-10-19 00:00:02', '2011-10-19 00:00:05'],
    #            ['Wisc', 'UW', 'Google']],
    #     'S3': [['2011-10-19 00:00:01', '2011-10-19 00:00:06'],
    #            ['Wisc', 'UW']],
    #     'S4': [['2011-10-19 00:00:05'],
    #            ['UW']],
    #     'S5': [['2011-10-19 00:00:03', '2011-10-19 00:00:05', '2011-10-19 00:00:07'],
    #            ['Wisc', 'Google', 'UW']],
    # },
    # case 2
    {
        'S0': [['2011-10-19 15:20:00', '2011-10-19 15:20:5'],
               ['Wisc', 'MSR']],
        'S1': [['2011-10-19 15:20:02', '2011-10-19 15:20:6'],
               ['Wisc', 'MSR']],
        'S2': [['2011-10-19 15:20:3', '2011-10-19 15:20:08'],
               ['Wisc', 'MSR']],
    },
    ]


def get_observed_cases():
    observed_cases_new = []
    for case in observed_cases:
        case_new = {}
        for s in case:
            t_new = []
            for t in case.get(s)[0]:
                t_new.append(datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S'))
            case_new.update({s: [t_new, case.get(s)[1]]})
        observed_cases_new.append(case_new)

    return observed_cases_new