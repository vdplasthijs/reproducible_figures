
## ToC v2:

### 0. Introduction & overview:
- Show screenshots (but NOT code) of example. (Fundamental break-down)

### Step 1: preparing your individual panels
- Assuming you've got your data plot as a single panel 
- Write up as function that takes `ax` arg
- Write test function that tests such a function? 

### Step 2: composing axes for a multi-panel figure
- Gridspec as basic functionality to use (explain all args) 
- color bar axis
- Extra: shortcuts: mosaic, subplots, subplot 

### Step 3: Filling axes with content

### Step 4: tidying up (ie removing unnecessary elements)
- despine, naked
- tick (multiplier)
- ... 

### Step 5: adding clarification elements 
- labels
- Text, annotate, 
- Arrows, .. 
- clip_on, zorder 
- Formatting numbers (scientific notation), p values, text .. 
- Colour, font size etc. 

### Step 6: exporting your finished figure
- PDF + other formats. 
- Vectorising + specifying DPI of images. 
- Embedding in text editors. 

## Bonus 1: (importing) images and schematics:
- Some guidelines for creating schematics
- Importing external vector files (white background?)
- File formats (tiff, jpg, png .. ?)
- `imshow` without interpolation 
_- Could probably go in another chapter?_

### Bonus 2: bringing it all together:


### Bonus 3: geospatial figures
- Vector and raster overlays.

### Bonus 4: interactive figures
- Sliders etc. 
- `qt` but not in juptyer

### Appendix 1: links to tutorials:
- Lines: `plt.plot()`
- Scatter: `plt.plot()`, `plt.scatter()`
- Histogram & bar plots
- Heatmaps: `plt.imshow()` and `sns.heatmap()` 
- Radial plots

### Appendix 2: gallery