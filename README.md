# Reproducible figures tutorial
## Why &amp; how to make reproducible figures in Python

### Introduction

Welcome to this tutorial for creating _reproducible figures_ in Python. The tutorial consists of 5 steps, which can be done in sequence or in parts. But first, this page covers a conceptual overview of what reproducible figures are, why they are preferred over "manually compiled figures", and what the basic (conceptual) principles are for creating them. After that, the 5 steps are covered in [5 separate Jupyter notebooks](https://github.com/vdplasthijs/reproducible_figures/blob/main/tutorial/Step%201%3A%20Preparing%20individual%20panels.ipynb), in Python. This tutorial will focus on how to design, implement and export reproducible figures, and assumes basic knowledge of Python/`numpy`/`matplotlib`. For brevity, this tutorial will not cover plotting functionality that is independent of creating reproducible figures per se (such as a customising bar plots or heatmaps), but links to other tutorials are sometimes provided instead. 

The purpose of these tutorials is to explain how to create fully reproducible, multi-panel figures at scientific publication level using standard plotting library `matplotlib`, as well as the new functions in this package `rep_fig_vis`. Other fantastic plotting libraries for Python exist (`seaborn`, `plotly`, `bokeh`, ..), but for simplicity we will use just `matplotlib`, which can covers almost all use-cases (and is compatible with `seaborn`). 

Importantly, this tutorial is by no means an exhaustive resource to all possible functionalities. Instead it's brief, and sticks to the core functionalities needed to create reproducible figures, with some common customisation options highlighted. Other (more exhaustive) resources are linked at the bottom of each tutorial page. This tutorial is divided into 5 steps that cover the fundamental workflow to create reproducible figures. Furthermore, there also is a collection of appendices that provide some additional tips. 

### What are reproducible figures? 

We define __reproducible figures (RFs)__ as _"A (multi-panel) figure that is produced __completely__ and __finally__ by code, and can therefore be reproduced (by anyone)"_. A common alternative is to use plotting libraries to create individual panels, but afterwards using graphics software such as Illustrator or Inkscape to compile and polish them manually. 

### What benefits do RFs offer?
- For now, please see my slides in this repository (`reproducible_figures/slides reproducible figs - Thijs van der Plas - 15 June 2022.pdf`) for a conceptual introduction on the benefits of reproducible figures. 

### RF principles
These are the key principles that underlie this tutorial:

:key: **Separate panel _content_ from panel _lay-out_.**
This is the key principle for creatings RFs, and will be covered in Steps 1-3. By separating content and lay-out, panels can be flexibly (re-)organised, reused and adjusted/updated. 

:clinking_glasses: **Separate data analysis (functions) from plotting (functions)**

:bulb: **Take inspiration from other reproducible figures!**
If (published) figures are reproducible and the code is public, it should be easy to look up the code that generated particular bits that you might want to replicate. For example, the figures of [this paper](https://proceedings.mlr.press/v199/plas22a/plas22a.pdf) (by me) can be found [at its repository](https://github.com/vdplasthijs/eavesdropping/blob/master/Figure%20generation%20notebook.ipynb) (as also linked in the paper). Arguably, data visualisation code is some of the easiest code to share and reuse, as others can directly see the output! Check out our [gallery](https://github.com/vdplasthijs/reproducible_figures/blob/main/tutorial/Tutorial%20appendix%20D%3A%20Gallery.md) of reproducible figures!


### Installation:
This tutorial was written in Jupyter notebooks, and can therefore either be read in browser, or git-cloned and run locally. If doing so, dependences are minimal, listed in `rf_env.yml`. (Install directly with conda by typing in terminal: `conda env create -f rf_env.yml` ). Note; for appendix A (import svg files) you also need to `pip install svgutils`, as documented in `rf_env_detailed.yml`. 


### Other resources:
For tutorial on plotting (in `matplotlib`) in general, see:
- https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html


### Conclusion:
Good luck and have fun!

[Start tutorial](https://github.com/vdplasthijs/reproducible_figures/blob/main/tutorial/Step%201%3A%20Preparing%20individual%20panels.ipynb)