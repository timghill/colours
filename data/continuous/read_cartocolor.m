% Script to play with https://carto.com/carto-colors/ colours

%% Colourmaps
cmap_name = 'ccFall';
cmap = '#3d5941,#778868,#b5b991,#f6edbd,#edbb8a,#de8a5a,#ca562c';
cmap_cells = split(cmap, ',');
cmap_rgb = zeros(length(cmap_cells),3);
for ii=1:length(cmap_cells)
    hexstr = cmap_cells{ii};
    cmap_rgb(ii,1) = 1/256*hex2dec(hexstr(2:3));
    cmap_rgb(ii,2) = 1/256*hex2dec(hexstr(4:5));
    cmap_rgb(ii,3) = 1/256*hex2dec(hexstr(6:7));
end
% cmap_rgb = [1, 1, 1; cmap_rgb];


x = linspace(0, 1, size(cmap_rgb, 1));
xq = linspace(0, 1, 256);
cmap_rgb_interp = zeros(256, 3);
for kk = 1:3
    cmap_rgb_interp(:, kk) = interp1(x, cmap_rgb(:, kk), xq);
end

save([cmap_name, '.txt'], '-ascii', '-tabs', 'cmap_rgb_interp')