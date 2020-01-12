"""
This module is for your final visualization code.
One visualization per hypothesis question is required.
A framework for each type of visualization is provided.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

sns.set_style('darkgrid')


def overlapping_density(group1, group2, label1, label2, title):
    """
    Set the characteristics of your overlapping density plot
    All arguments are set to None purely as a filler right now

    Function takes package name, input variables(categories), and target variable as input.
    Returns a figure

    Should be able to call this function in later visualization code.

    PARAMETERS

    :param group1: first group for comparison
    :param group2: second group for comparison
    :param label1: label for first group
    :param label2: label for second group 
    :return: returns figure
    """

    # Set size of figure
    fig = plt.figure(figsize=(10, 7), dpi=80)

    sns.distplot(group1, hist=False, kde_kws={"shade": True}, color = '#5bd46b', label=label1)
    sns.distplot(group2, hist=False, kde_kws={"shade": True}, color = '#ff7a70', label=label2)
    plt.legend()
    plt.title(title)



def boxplot_plot(package=None, input_vars=None, target_vars=None):
    """
    Same specifications and requirements as overlapping density plot

    Function takes package name, input variables(categories), and target variable as input.
    Returns a figure

    PARAMETERS

    :param package:        should only take sns or matplotlib as inputs, any other value should throw and error
    :param input_vars:     should take the x variables/categories you want to plot
    :param target_vars:    the y variable of your plot, what you are comparing
    :return:               fig to be enhanced in subsequent visualization functions
    """
    plt.figure(figsize=(16, 10), dpi=80)

    pass


def visualization_one(target_var = None, input_vars= None, output_image_name=None):
    """
    The visualization functions are what is used to create each individual image.
    The function should be repeatable if not generalizable
    The function will call either the boxplot or density plot functions you wrote above

    :param target_var:
    :param input_vars:
    :param output_image_name: the desired name for the image saved
    :return: outputs a saved png file and returns a fig object for testing
    """
    ###
    # Main chunk of code here
    ###

    # Starter code for labeling the image
    plt.xlabel(None, figure = fig)
    plt.ylabel(None, figure = fig)
    plt.title(None, figure= fig)
    plt.legend()

    # exporting the image to the img folder
    plt.savefig(f'img/{output_image_name}.png', transparent = True, figure = fig)
    return fig


# please fully flesh out this function to meet same specifications of visualization one

def visualization_two(output_image_name):
    pass

def visualization_three(output_image_name):
    pass

def visualization_four(output_image_name):
    pass