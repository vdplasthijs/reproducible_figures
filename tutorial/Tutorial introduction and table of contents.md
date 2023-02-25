## Introduction

This folder contains tutorials to create reproducible figures in Python. (See `reproducible_figures/slides reproducible figs - Thijs van der Plas - 15 June 2022.pdf` for a conceptual introduction on reproducible figures). The purpose of these tutorials is to explain how to create fully reproducible, multi-panel figures at publication level using standard plotting library `matplotlib` (and others?), as well as the new functions in this package `rep_fig_vis`. 

The tutorial is split up in different Jupyter notebooks by topic, and can be done in sequence or separately. Good luck and have fun!


## Principles:
See slides.

## Table of contents:

### 1. Basics
- Fundamental set-up of a reproducible figure in `matplotlib` showcased by one example figure. 

### 2. Customised colour bars 
- Placement using colour axis (`cax`)
- Creating colour schemas (making `cmap`, choosing colours, basic principles of colours in data visualisation)

### 3. Text placement
- `plt.annotate()`, `plt.text` and (tick)labels + titles
- How to align neatly in figure 
- Formatting numbers (scientific notation), p values, text .. 
- Colour, font size etc. 

### 4. Heatmaps
- `plt.imshow()` and `sns.heatmap()` 

### 5. Schematics and illustrations 
- Some guidelines for creating schematics
- Importing external vector files (white background?)

### 6. Including images 
- File formats (tiff, jpg, png .. ?)
- `imshow` without interpolation 

### 7. Exporting your finished figure
- PDF + other formats. 
- Vectorising + specifying DPI of images. 
- Embedding in text editors. 

### 8. Geospatial figures
- Vector and raster overlays.

### 9. Interactive figures
- Sliders etc. 
- `qt` but not in juptyer



