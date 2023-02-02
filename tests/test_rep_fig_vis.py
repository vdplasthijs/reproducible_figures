
def test_make_fig_layout(figure_layout1_fixture):
    dpi = 300
    from reproducible_figures.rep_fig_vis import make_fig_layout
    fig, axes, grid = make_fig_layout(layout=figure_layout1_fixture, dpi=dpi)

def test_show_test_figure_layout(figure_layout1_fixture):
    from reproducible_figures.rep_fig_vis import make_fig_layout
    from reproducible_figures.rep_fig_vis import show_test_figure_layout

    fig, axes, grid = make_fig_layout(layout=figure_layout1_fixture, dpi=300)
    show_test_figure_layout(fig, axes, show=True)
