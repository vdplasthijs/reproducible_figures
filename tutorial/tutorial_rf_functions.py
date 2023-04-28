##############################
## Module with function specific for reproducible figure tutorial
## Author: Thijs van der Plas (github.com/vdplasthijs)
##############################

import numpy as np
import matplotlib.pyplot as plt
import copy
import scipy.stats
import seaborn as sns
import sys
sys.path.append('../scripts/')
import rep_fig_vis as rfv

def plot_scatter_data_distr(ax=None, data=None, name_data=None,
                            x_label='', y_label='', 
                            title=None, plot_legend=False):
    if ax is None:
        ax = plt.subplot(111)

    if data is None:
        data = np.random.randn(100, 2)

    assert type(data) == np.ndarray, 'Data must be a numpy array'
    assert data.shape[1] == 2, 'Data must have 2 columns'

    ax.scatter(data[:, 0], data[:, 1], label=name_data)
    if plot_legend:
        ax.legend()
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    if title is not None:
        ax.set_title(title)
    
    return ax

def plot_scatter_along_line(ax=None, n=100, slope=1, limit_data=10, 
                            noise=1):
    
    if ax is None:
        ax = plt.subplot(111)

    x = np.linspace(0, limit_data, n)
    y = slope * x + np.random.randn(n) * noise

    ax.scatter(x, y)
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')

    return ax

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

def plot_gaussian_profile(ax=None, cax=None, fig=None, remove_spines=True,
                          title='2D Gaussian profile'):
    m, n = 100, 100
    lims = (-3, 3) # support of the PDF
    xx, yy = np.meshgrid(np.linspace(*lims, m), np.linspace(*lims, n))
    points = np.stack((xx, yy), axis=-1)
    mean = (1, 2) # Whatever your (i, j) is
    covariance = 15.0
    pdf = scipy.stats.multivariate_normal.pdf(points, mean, covariance)
    pdf = pdf / np.max(pdf)

    hm = ax.imshow(pdf)
    if fig is not None:
        if cax is None:
            fig.colorbar(hm, ax=ax)
        else:
            fig.colorbar(hm, cax=cax)
        
    if remove_spines:
        rfv.naked(ax)  # get rid of the axis labels and ticks 

    ax.set_title(title)
    return (ax, cax)

def plot_distr(ax=None, distr_name='uniform', color_line='k', histtype='bar'):
    n_samples = 10000
    assert distr_name in ['uniform', 'gaussian', 'poisson', 'exp'], f'Distribution {distr_name} not supported'

    if ax is None:
        ax = plt.subplot(111)

    if distr_name == 'uniform':
        distr = np.random.uniform(size=n_samples)
        full_name = 'Uniform distribution'
    elif distr_name == 'gaussian':
        distr = np.random.normal(size=n_samples)
        full_name = 'Gaussian distribution'
    elif distr_name == 'poisson':
        distr = np.random.poisson(size=n_samples)
        full_name = 'Poisson distribution'
    elif distr_name == 'exp':
        distr = np.random.exponential(size=n_samples)
        full_name = 'Exponential distribution'

    tmp = ax.hist(distr, bins=20, density=True, histtype=histtype,
            linewidth=2, color=color_line, label=full_name.split(' ')[0])
    pdf_points = np.concatenate((np.array([0]), tmp[0]))#, np.array([0])))

    ax.set_title(full_name)
    ax.set_xlabel('Sample')
    ax.set_ylabel('PDF')
    return ax, pdf_points

def plot_cdf(ax=None, pdf=None, color_line='k'):
    if ax is None:
        ax = plt.subplot(111)

    # pdf = np.sort(pdf)

    cdf = np.cumsum(pdf) / np.sum(pdf)
    ax.plot(cdf, color=color_line, linewidth=2)
    ax.set_title('Cumulative distribution function')
    ax.set_xlabel('Normalised sample')
    ax.set_ylabel('CDF')

    return ax