% Read in a colourmap
% cmap_data = load('data/scm-tofino.txt');

z = peaks(200);
% z(z<0) = 0;
pcolor(z)
shading flat
colormap(get_colourmap('mc-cube1'))
set(gca, 'Visible', 'off')
colorbar
