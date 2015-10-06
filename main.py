from cef_measure import get_CEF
from life_span import get_life_span
from algorithm_competitors import majority_voting
from raw_value_preparation import cook_raw_value
from datetime import timedelta


def get_truth_overlap(truth, result):
    k = 0
    for index, value in enumerate(result):
        if value == truth[index]:
            k += 1

    return 100*k/len(truth)


def cef_initialization(c, e, f_max, observed):
    observed_keys = sorted(observed.keys())
    cef_measures = {}
    f_init = {}
    first_observation = observed.get(observed_keys[0])[0][0]
    last_observation = observed.get(observed_keys[0])[0][-1]
    observation_period = last_observation - first_observation
    delta = timedelta(seconds=0)
    while delta <= observation_period:
        if delta >= observation_period/3 and delta < 2*(observation_period/3):
            f = f_max/3.
        elif delta >= 2*(observation_period/3) and delta <= observation_period:
            f = f_max
        else:
            f = 0.
        f_init.update({delta: f})
        delta += timedelta(seconds=1)
    for s in observed_keys:
        cef = [c, e, f_init]
        cef_measures.update({s: cef})

    return cef_measures


if __name__ == '__main__':
    ground_truth = ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']

    observed_cases = cook_raw_value()

    for case_number, observed in enumerate(observed_cases):
        observed_keys = sorted(observed.keys())
        cef_measures = cef_initialization(c=0.5, e=0.5, f_max=0.5, observed=observed)

        iter_quantity = 0
        sources_number = len(observed_keys)
        # life_span = get_life_span(observed=observed, cef_measures=cef_measures)
        #
        # # print initial info
        # print 'CASE NUMBER: {}'.format(case_number)
        # print 'Ground truth: {}'.format(ground_truth)
        # for key in observed_keys:
        #     print '{}: {}'.format(key, observed.get(key))
        # print 'Initial life span: {}'.format(life_span)
        # print '---------------------'
        # life_span_old = []
        #
        # cef_for_each_s_old = [cef for i in range(sources_number)]
        # cef_delta_sum = [1, 1, 1]
        # while max(cef_delta_sum) > 0.01*sources_number:
        #     cef_for_each_s = []
        #     for s in observed_keys:
        #         # print s
        #         cef = get_CEF(life_span, observed.get(s))
        #         cef_measures.update({s: cef})
        #         cef_for_each_s.append(cef)
        #
        #     life_span_old = life_span
        #     life_span = get_life_span(observed=observed, cef_measures=cef_measures)
        #     iter_quantity += 1
        #
        #     cef_delta_sum = [0, 0, 0]
        #     for old, new in zip(cef_for_each_s_old, cef_for_each_s):
        #         diff_for_s = [abs(x-y) for x, y in zip(old, new)]
        #         for i in range(len(cef_delta_sum)):
        #             cef_delta_sum[i] += diff_for_s[i]
        #     cef_for_each_s_old = cef_for_each_s
        #     majority_voting_result = majority_voting(observed)
        #
        #     print 'iter={}'.format(iter_quantity)
        #     print 'cef_delta_sum: {}'.format(cef_delta_sum)
        #     for cef, s in zip(cef_for_each_s, observed_keys):
        #         print s, ': C={}, E={}, F={}'.format(cef[0], cef[1], cef[2])
        #     print "Object's life span: {} {}%" \
        #         .format(life_span, get_truth_overlap(ground_truth, life_span))
        #     print 'Majority voting results: {} {}%' \
        #         .format(majority_voting_result, get_truth_overlap(ground_truth, majority_voting_result))
        #     print '---------------------'
        #
        # print 'iter_quantity={}'.format(iter_quantity)
        # print "*********************************************************"
