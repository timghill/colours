function plot_all_colourschemes()
% Function plot_all_colourmaps plots all colourmaps available in the
% directory using the default number of colour levels

p=mfilename('fullpath');
path=fileparts(p);
% path_parts=split(path,'/');
% path=join(path_parts(1:end-1),'/');
path=[path '/data/categorical'];

cmap_files=dir([path,'/*.txt']);
cmap_files={cmap_files.name};

cmap_names=cell(size(cmap_files));

N_maps=length(cmap_names);

for ii=1:N_maps
%     cmap_file=[path,'/',cmap_files{ii}];
    cmap_file=cmap_files{ii};
    cmap_names{ii}=cmap_file(1:end-4);
end

% cmap_names
N_levels=12;
xdata=linspace(0,1,N_levels);
y=linspace(0,1,10);

[xx,yy]=meshgrid(xdata,y);
cdata=xdata'*ones(size(y));
cdata=cdata';

figure('Position', [500, 48, 720, 500])
t = tiledlayout(ceil(N_maps/4), 4);
% setappdata(gcf, 'SubplotDefaultAxesLocation', [0, 0, 1, 1]);
for jj=1:N_maps
%     subplot(ceil(N_maps/3),3,jj)
    nexttile
    hold on
    colormap(gca,get_colourscheme(cmap_names{jj}))
    pcolor(xx,yy,cdata)
    shading interp
    xlim([0,1])
    ylim([0,1])
    caxis([0,1])
    set(gca,'Visible','off')
    text(0.5,0.5,cmap_names{jj},'HorizontalAlignment','center','VerticalAlignment','middle','interpreter','none')
end

t.TileSpacing = 'none';
t.Padding = 'none';
