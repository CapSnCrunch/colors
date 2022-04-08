# Random Colors
This is a repository which combines a couple of my different projects relating to color.

## Color Gradient Paths
The first project I decided to work on can be found in para-color.py. This project was a little UI for selecting points in the <a href='https://en.wikipedia.org/wiki/RGB_color_model'>RGB color model</a> and
creating linear paths between them. Scrolling while hovering of the right most square of the UI moves the current view of the RGB color cube up the
blue-axis and clicking in this square selects a point. You can see the selected points in the square to the right. Once at least two points have been
selected, the program will automatically follow a piecewise linear path between all of the points, changing the background color to match the current
position of the marker following this path.

<p align='center'>
  <img src='imgs/para-color-example.gif' width='400'>
  <h5 align = 'center'>Example of piecewise linear gradient selection</h5>
</p>

Eventually, I hope to add some way to interface with an arduino to control a set of RGB lights using this tool.

## Distinguishable Color Generation
