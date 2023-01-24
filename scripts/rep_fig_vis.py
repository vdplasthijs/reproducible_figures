##############################
## GENERAL PLOTTING FUNCTIONS
## Author: Thijs van der Plas (github.com/vdplasthijs)
##############################
 
import numpy as np
import matplotlib.pyplot as plt
import copy

def dummy_example_functions(fig=None, ax=None):
    '''Example of common input arguments'''

    if ax is None:
        if fig is None:
            ## Create both a figure & axis handle
            fig, ax = plt.subplot(111)
        else:
            ## Create single axis on figure 
            ax = fig.add_subplot(111)
    else: 
        ## use provided axis, figure must already exist so don't create new one:
        pass 

    return fig, ax 

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
    plt.rcParams['axes.autolimit_mode'] = 'data' # default: 'data'
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

def add_panel_label(ax, fig, label_letter='A', label_ind=None, uppercase=True, use_fig_bbox=False,
                    x_override=None, y_override=None, x_offset=0, y_offset=0,
                    weight='bold', fontsize=None, verbose=0):
    '''Add a panel label to ax. 
    Either the str given by label_letter or the i-th letter given by label_ind. 
    Panel label is automatically placed at top-left corner. But can be overriden by using x_override and y_override. 
    By default using regular fontsize, but can be overriden by setting fontsize. 
    '''
    if label_letter is None:
        assert type(label_ind) == int, f'label_ind should be an int, but is a {type(label_ind)}'
        letters = 'abcdefghijklmnopqrstuvwxyz'
        label_letter = letters[label_ind]
        if uppercase:
            label_letter = label_letter.upper() 
    else:
        assert type(label_letter) == str, f'label_letter should be a str, but is a {type(label_letter)}'         
        if label_ind is not None:
            print('WARNING: both label_letter and label_ind are not None. Using label_letter.')   

    ## Get left-most x lim of all elements of ax
    ## Get top-most y lim of all elements of ax
    if use_fig_bbox:
        bbox_fig = ax.get_tightbbox(fig.canvas.get_renderer())  # use bounding box of ax object
        xcoord_left = bbox_fig.xmin
        ycoord_top = bbox_fig.ymax
    else:  # use bounding boxes of yaxis and title
        xcoord_left = ax.yaxis.get_tightbbox(fig.canvas.get_renderer()).xmin  # alternatively, get lims from yaxis & title. 
        ycoord_top = ax.title.get_tightbbox(fig.canvas.get_renderer()).ymax

    ## Offset if necessary:
    if x_offset is not None:
        xcoord_left += x_offset
    if y_offset is not None:
        ycoord_top += y_offset

    ## Override if necessary
    if x_override is not None:
        xcoord_left = x_override
    if y_override is not None:
        ycoord_top = y_override

    ## Create label, if verbose print coords.
    if verbose > 0:
        print(f'Coordinates: x {xcoord_left}, y {ycoord_top}')
    if fontsize is None:
        fontsize = plt.rcParams['font.size']
    ax.annotate(s=label_letter, xy=(xcoord_left, ycoord_top), xycoords='figure pixels', 
                ha='left', va='top', weight=weight, fontsize=fontsize)
