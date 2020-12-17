function RGB = get_colourscheme(varargin)
% get_colourscheme returns an N x 3 RGB array representing a colour set.
%
% palettes plots all available colourmaps
%
% cmap = palettes(cmap) returns a 256 x 3 RGB array representing the
% colourmap 'cmap.

if isempty(varargin)
    plot_all_colourschemes
    return
else
    name=char(varargin{1});
end

p=mfilename('fullpath');
path=fileparts(p);
% path_parts=split(path,'/');
% path=join(path_parts(1:end-1),'/');
path=[path '/data/categorical'];
% Assumes files exist in this directory with the given name + '.xml'
flip=false;
if strcmp(name(1),'-')
    flip=true;
    name=name(2:end);
end
file_name=[path,'/',name,'.txt'];

if ~isfile(file_name)
    error('Colourmap "%s" does not exist',name)
end
    
RGB = load(file_name);

if flip
    RGB=flipud(RGB);
end