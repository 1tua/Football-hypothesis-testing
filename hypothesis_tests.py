"""
This module is for your final hypothesis tests.
Each hypothesis test should tie to a specific analysis question.

Each test should print out the results in a legible sentence
return either "Reject the null hypothesis" or "Fail to reject the null hypothesis" depending on the specified alpha
"""

import pandas as pd
import numpy as np
from scipy import stats
import math
import matplotlib.pyplot as plt

def sampling(data, n, column, seed):
    sample=data.sample(n, random_state=seed)
    sampled_value=sample[column]
    return sampled_value

def make_t_dist(t, t_critical, dof, title, direction='right'):
    """
    makes a visualisation of a t-distribution, with lines for t-statistic and critical t-value
    :param t: t-statistic
    :param t_critical: the critical t value 
    :param dof: the welch's degress of freedom
    :param direction: left or right, depending on which end of the t-distribution we're testing
    :title: the desired title of the graph
    """
    
    x= np.linspace(-5, 5, 200)
    
    y = stats.t.pdf(x, dof, 0, 1)
    
    fig = plt.figure(figsize=(8,5))
    
    ax = fig.gca()
    
    ax.plot(x, y, linewidth=3, color='#4a4a5e')
    
    if direction == 'right':
        # plot a vertical line for our measured difference in rates t-statistic
        ax.axvline(t, color = '#5bd46b', linestyle=':', lw=4,label=f't-statistic: {round(t, 3)}')
        ax.axvline(t_critical, color = '#ff7a70', linestyle='--', lw=4, label=f'critical t-value{round(t_critical,3)}')
        ax.fill_betweenx(y, x, t_critical, where = x>t_critical)
        ax.legend()
        plt.title(title)
        plt.show()
    else:
         # plot a vertical line for our measured difference in rates t-statistic
        ax.axvline(t, color = '#5bd46b', linestyle=':', lw=4,label=f't-statistic: {round(t, 3)}')
        ax.axvline(t_critical, color = '#ff7a70', linestyle='--', lw=4, label=f'critical t-value{round(t_critical,3)}')
        ax.fill_betweenx(y, x, t_critical, where = x<t_critical)
        ax.legend()
        plt.title(title)
        plt.show()

def welch_dof(a, b):
    """
    This module is for calculating the degrees of freedom that go into a welch's t-test
    :param a: first sample to compare
    :param b: second sample to compare
    """
    s1 = a.var(ddof=1)
    s2 = b.var(ddof=1)
    n1 = len(a)
    n2 = len(b)
    numerator = (s1/n1 + s2/n2)**2
    denominator = (s1/ n1)**2/(n1 - 1) + (s2/ n2)**2/(n2 - 1)
    return numerator/denominator

def cohen_d(group1, group2):

    diff = group1.mean() - group2.mean()

    n1, n2 = len(group1), len(group2)
    var1 = group1.var()
    var2 = group2.var()
    
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)

    d = diff / np.sqrt(pooled_var)
    
    return d

# def create_sample_dists(cleaned_data, y_var=None, categories=[]):
#     """
#     Each hypothesis test will require you to create a sample distribution from your data
#     Best make a repeatable function

#     :param cleaned_data:
#     :param y_var: The numeric variable you are comparing
#     :param categories: the categories whose means you are comparing
#     :return: a list of sample distributions to be used in subsequent t-tests

#     """
#     htest_dfs = []

#     # Main chunk of code using t-tests or z-tests
#     return htest_dfs

# def compare_pval_alpha(p_val, alpha):
#     status = ''
#     if p_val > alpha:
#         status = "Fail to reject"
#     else:
#         status = 'Reject'
#     return status


# def hypothesis_test_one(alpha = None, cleaned_data):
#     """
#     Describe the purpose of your hypothesis test in the docstring
#     These functions should be able to test different levels of alpha for the hypothesis test.
#     If a value of alpha is entered that is outside of the acceptable range, an error should be raised.

#     :param alpha: the critical value of choice
#     :param cleaned_data: 
#     :return:
#     """
#     # Get data for tests
#     comparison_groups = create_sample_dists(cleaned_data=None, y_var=None, categories=[])
#     ###
#     # Main chunk of code using t-tests or z-tests, effect size, power, etc
#     ###
    
    
#     # starter code for return statement and printed results
#     status = compare_pval_alpha(p_val, alpha)
#     assertion = ''
#     if status == 'Fail to reject':
#         assertion = 'cannot'
#     else:
#         assertion = "can"
#         # calculations for effect size, power, etc here as well

#     print(f'Based on the p value of {p_val} and our aplha of {alpha} we {status.lower()}  the null hypothesis.'
#           f'\n Due to these results, we  {assertion} state that there is a difference between NONE')

#     if assertion == 'can':
#         print(f"with an effect size, cohen's d, of {str(coh_d)} and power of {power}.")
#     else:
#         print(".")

#     return status

# def hypothesis_test_two():
#         """
#     Describe the purpose of your hypothesis test in the docstring
#     These functions should be able to test different levels of alpha for the hypothesis test.
#     If a value of alpha is entered that is outside of the acceptable range, an error should be raised.

#     :param alpha: the critical value of choice
#     :param cleaned_data: 
#     :return:
#     """
#     # Get data for tests
#     comparison_groups = create_sample_dists(cleaned_data=None, y_var=None, categories=[])
#     ###
#     # Main chunk of code using t-tests or z-tests, effect size, power, etc
#     ###

#     # starter code for return statement and printed results
#     status = compare_pval_alpha(p_val, alpha)
#     assertion = ''
#     if status == 'Fail to reject':
#         assertion = 'cannot'
#     else:
#         assertion = "can"
#         # calculations for effect size, power, etc here as well

#     print(f'Based on the p value of {p_val} and our aplha of {alpha} we {status.lower()}  the null hypothesis.'
#           f'\n Due to these results, we  {assertion} state that there is a difference between NONE')

#     if assertion == 'can':
#         print(f"with an effect size, cohen's d, of {str(coh_d)} and power of {power}.")
#     else:
#         print(".")

#     return status


# def hypothesis_test_three(alpha=None, group1, group2):
#         """
#     Testing to see whether the 

#     :param alpha: the critical value of choice
#     :param cleaned_data: 
#     :return:
#     """
    
#     ###
#     # Main chunk of code using t-tests or z-tests, effect size, power, etc
#     ###
    
#     tt_results = stats.ttest_ind(group1, group2, equal_var = False)
#     t_stat = tt_results[0]
#     p_val = tt_results[1]
    

#     # starter code for return statement and printed results
#     status = compare_pval_alpha(p_val, alpha)
#     assertion = ''
#     if status == 'Fail to reject':
#         assertion = 'cannot'
#     else:
#         assertion = "can"
#         # calculations for effect size, power, etc here as well

#     print(f'Based on the p value of {p_val} and our aplha of {alpha} we {status.lower()}  the null hypothesis.'
#           f'\n Due to these results, we  {assertion} state that there is a difference between games with a red card and those without')

#     if assertion == 'can':
#         print(f"with an effect size, cohen's d, of {str(coh_d)} and power of {power}.")
#     else:
#         print(".")

#     return status


# def hypothesis_test_four():
#     pass
