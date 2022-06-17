from typing import Union

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import copy


##############################
###   GENERAL PLOTTING FUNCTIONS
##############################

def despine(ax):
    '''Remove top and right spines'''
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


def naked(ax):
    '''Remove all spines, ticks and labels'''
    for ax_name in ['top', 'bottom', 'right', 'left']:
        ax.spines[ax_name].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel('')
    ax.set_ylabel('')


def set_fontsize(font_size=12):
    '''Set font size for all text elements'''
    plt.rcParams['font.size'] = font_size
    plt.rcParams['axes.autolimit_mode'] = 'data'  # default: 'data'
    params = {'legend.fontsize': font_size,  # set for all kinds of text elements
              'axes.labelsize': font_size,
              'axes.titlesize': font_size,
              'xtick.labelsize': font_size,
              'ytick.labelsize': font_size}
    plt.rcParams.update(params)
    print(f'Font size is set to {font_size}')


def equal_xy_lims(ax, start_zero=False):
    '''Set xlim equal to ylim (by their max)'''
    xlims = ax.get_xlim()
    ylims = ax.get_ylim()
    max_outer_lim = np.maximum(xlims[1], ylims[1])
    min_inner_lim = np.minimum(xlims[0], ylims[0])

    if start_zero:
        ax.set_xlim([0, max_outer_lim])
        ax.set_ylim([0, max_outer_lim])
    else:
        ax.set_xlim([min_inner_lim, max_outer_lim])
        ax.set_ylim([min_inner_lim, max_outer_lim])


def equal_lims_two_axs(ax1, ax2):
    '''Set xlim equal to ylim across two axes'''
    xlim_1 = ax1.get_xlim()
    xlim_2 = ax2.get_xlim()
    ylim_1 = ax1.get_ylim()
    ylim_2 = ax2.get_ylim()

    new_x_min = np.minimum(xlim_1[0], xlim_2[0])
    new_x_max = np.maximum(xlim_1[1], xlim_2[1])
    new_y_min = np.minimum(ylim_1[0], ylim_2[0])
    new_y_max = np.maximum(ylim_1[1], ylim_2[1])

    ax1.set_xlim([new_x_min, new_x_max])
    ax2.set_xlim([new_x_min, new_x_max])
    ax1.set_ylim([new_y_min, new_y_max])
    ax2.set_ylim([new_y_min, new_y_max])


def equal_lims_n_axs(ax_list):
    '''Set ax lims equal across list of ax, but xlim and ylim are seperate here'''
    for i_ax, ax in enumerate(ax_list):
        x_min, x_max = ax.get_xlim()
        y_min, y_max = ax.get_ylim()

        if i_ax == 0:
            x_min_min = copy.deepcopy(x_min)
            x_max_max = copy.deepcopy(x_max)
            y_min_min = copy.deepcopy(y_min)
            y_max_max = copy.deepcopy(y_max)

        else:
            if x_min < x_min_min:
                x_min_min = copy.deepcopy(x_min)
            if x_max > x_max_max:
                x_max_max = copy.deepcopy(x_max)
            if y_min < y_min_min:
                y_min_min = copy.deepcopy(y_min)
            if y_max > y_max_max:
                y_max_max = copy.deepcopy(y_max)

    for ax in ax_list:
        ax.set_xlim([x_min_min, x_max_max])
        ax.set_ylim([y_min_min, y_max_max])


def remove_xticklabels(ax):
    '''remove x ticklabels but keep ticks'''
    ax.set_xticklabels(['' for x in ax.get_xticklabels()])


def remove_yticklabels(ax):
    '''remove y ticklabels but keep ticks'''
    ax.set_yticklabels(['' for x in ax.get_yticklabels()])


def remove_both_ticklabels(ax):
    '''both x and y'''
    remove_xticklabels(ax)
    remove_yticklabels(ax)


##############################
###   SPECIFIC FUNCTIONS FOR THIS TUTORIAL
##############################

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


# %% FUNCTIONS DEFINED BY PRAJAY

def add_scale_bar(ax, loc: tuple, length: tuple, bartype: str = "L", text: Union[str, tuple, list] = 'scalebar',
                  **kwargs):
    """
    Add a scale bar of the specified type to the ax object provided.

    :param ax:
    :param loc:
    :param length: length of scalebar line if L type: index 0 is the y scalebar and index 1 is the x scalebar.
    :param bartype:
    :param text: textlabel for scale bars. if L type: index 0 is the y scalebar and index 1 is the x scalebar.
    :param kwargs:
        text_offset: ratio to offset the text labels for the scalebars
        lw: linewidth of the scalebar
    """

    text_offset = [1] * len(text) if not 'text_offset' in kwargs else kwargs['text_offset']
    # text_offset_2 = [1] * len(text) if not 'text_offset_2' in kwargs else kwargs['text_offset_2']
    lw = 0.75 if not 'lw' in kwargs else kwargs['lw']
    fs = 10 if not 'fs' in kwargs else kwargs['fs']
    if bartype == 'L':
        ax.plot([loc[0]] * 2, [loc[1], loc[1] + length[0]], color='black', clip_on=False, lw=lw,
                solid_capstyle='butt')
        ax.plot((loc[0], loc[0] + length[1]), [loc[1]] * 2, color='black', clip_on=False, lw=lw,
                solid_capstyle='butt')
        # kwargs['fig'].show()
        assert type(text) is not str, 'incorrect type for L scalebar text provided.'
        assert len(text) == 2, 'L scalebar text argument must be of length: 2'

        ax.text(x=loc[0] - 1 * text_offset[0], y=loc[1], s=text[0], fontsize=fs, rotation=90)
        ax.text(x=loc[0], y=loc[1] - 1 * text_offset[1], s=text[1], fontsize=fs, rotation=0)

    else:
        raise ValueError(f'{type} not implemented currently.')


def make_fig_layout(layout: dict = None, **kwargs):
    pass

    """
    main idea is that the grid dictionary contains the necessary relationships for the layout.
    layout arg:
        # panel_shape = ncols x nrows
        # bound = l, t, r, b

    """

    figsize = (8, 10) if 'figsize' not in kwargs else kwargs['figsize']
    dpi = 400 if 'dpi' not in kwargs else kwargs['dpi']
    wspace = 0.1 if 'wspace' not in kwargs else kwargs['wspace']
    hspace = 0.1 if 'hspace' not in kwargs else kwargs['hspace']


    fig = plt.figure(constrained_layout=False,  # False better when customising grids
                     figsize=figsize, dpi=dpi)  # width x height in inches


    # layout = {
    #     'topleft': {
    #         'panel_shape': (1,2),
    #         'bound': (0.05, 0.95, 0.25, 0.8)}
    # }

    axes = {}  # this is the dictionary that will collect *all* axes that are required for this plot, named as per input grid

    for name, _grid in layout.items():
        gs_ = fig.add_gridspec(ncols=_grid['panel_shape'][0], nrows=_grid['panel_shape'][1],
                               left=_grid['bound'][0],
                               top=_grid['bound'][1],
                               right=_grid['bound'][2],
                               bottom=_grid['bound'][3],
                               wspace=0.1, hspace=0.4
                               )  # leave a bit of space between grids (eg left here and right in grid above)

        n_axs: int = _grid['panel_shape'][0] * _grid['panel_shape'][1]
        _axes = {}
        if _grid['panel_shape'][0] > 1 and _grid['panel_shape'][1] > 1:
            for col in range(_grid['panel_shape'][0]):
                for row in range(_grid['panel_shape'][1]):
                    _axes[col, row] = fig.add_subplot(gs_[col, row])  # create ax by indexing grid object

        elif _grid['panel_shape'][0] > 1 or _grid['panel_shape'][1] > 1:
            for i in range(n_axs):
                _axes[i] = fig.add_subplot(gs_[i])  # create ax by indexing grid object

        elif _grid['panel_shape'][0] == 1 or _grid['panel_shape'][1] == 1:
            pass
        else:
            pass

        axes[name] = _axes

    return fig, axes


