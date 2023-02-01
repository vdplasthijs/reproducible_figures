##############################
## Module with function specific for reproducible figure tutorial
## Author: Thijs van der Plas (github.com/vdplasthijs)
##############################

import numpy as np
import matplotlib.pyplot as plt
import copy
import scipy.stats

def plot_sin_one_period(ax=None, n_tp=500, phase=0, alpha=1, colour='k'):
    '''Create sine over 1 period with offset phase'''
    if ax is None:
        ax = plt.subplot(111)

    t_array = np.linspace(0, 2 * np.pi, n_tp)
    sin_array = np.sin(t_array + phase)

    ax.plot(t_array, sin_array, linewidth=3, alpha=alpha, c=colour)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Activation (a.u.)')
    ax.set_title('Some simple graphs', y=1.05, fontdict={'weight': 'bold'})


def plot_normal_distr(ax=None, n_tp=500, mean_distr=0, std_distr=1, alpha=1, colour='k'):
    '''Create sine over 1 period with offset phase'''
    if ax is None:
        ax = plt.subplot(111)

    t_array = np.linspace(-3, 3, n_tp)
    norm_array = scipy.stats.norm.pdf(t_array, loc=mean_distr, scale=std_distr)

    ax.plot(t_array, norm_array, linewidth=3, alpha=alpha, c=colour)
    ax.set_xlabel('Some variable')
    ax.set_ylabel('PDF')

def plot_brown_proc(ax_trace=None, ax_hist=None, var=1, n_steps=500,
                    plot_ylabel=True, colour='k'):
    '''Sample brownian motion & plot trace and histogram'''
    gauss_samples = np.random.randn(n_steps) * np.sqrt(var)
    brown_motion = np.cumsum(gauss_samples)
    time_array = np.arange(n_steps)

    if ax_trace is None or ax_hist is None:
        fig, ax = plt.subplots(1, 2)
        ax_trace, ax_hist = ax

    ax_trace.plot(time_array, brown_motion, linewidth=2, c=colour)
    ax_trace.set_xlabel('Iteration')
    if plot_ylabel:
        ax_trace.set_ylabel('Activity')

    ax_hist.hist(brown_motion, bins=np.linspace(-100, 100, 30),
                 facecolor=colour, edgecolor='k', linewidth=1)
    ax_hist.set_xlabel('Activity')
    if plot_ylabel:
        ax_hist.set_ylabel('Frequency')