import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt



def welch_dof(a, b):
    s1 = a.var(ddof=1)
    s2 = b.var(ddof=1)
    n1 = a.size
    n2 = b.size
    numerator = (s1/n1 + s2/n2)**2
    denominator = (s1/ n1)**2/(n1 - 1) + (s2/ n2)**2/(n2 - 1)
    return numerator/denominator

def make_t_dist(t, t_critical, dof, title):
    """
    makes a visualisation of a t-distribution, with lines for t-statistic and critical t-value
    :param t: t-statistic
    :param t_critical: the critical t value 
    :param dof: the welch's degress of freedom
    :title: the desired title of the graph
    """
    
    x= np.linspace(-5, 5, 200)
    
    y = stats.t.pdf(x, dof, 0, 1)
    
    fig = plt.figure(figsize=(8,5))
    
    ax = fig.gca()
    
    ax.plot(x, y, linewidth=3, color='darkblue')
    
    # plot a vertical line for our measured difference in rates t-statistic
    ax.axvline(t, color='yellow', linestyle='--', lw=2,label='t-statistic')
    ax.axvline(t_critical, color='purple', linestyle='--', lw=2, label='critical t-value')
    ax.fill_betweenx(y, x, t_critical, where = x>t_critical)
    ax.legend()
    plt.title(title)
    plt.show()
    
    
def Cohen_d(group1, group2):

    # Compute Cohen's d.

    diff = group1.mean() - group2.mean()

    n1, n2 = len(group1), len(group2)
    var1 = group1.var()
    var2 = group2.var()

    # Calculate the pooled threshold as shown earlier
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    
    # Calculate Cohen's d statistic
    d = diff / np.sqrt(pooled_var)
    
    return d