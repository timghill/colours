y1 = (1:100) + 10*randn(1,100);
y2 = -25 + 1.5*(1:100) + 10*randn(1, 100);
y3 = -50 + 2*(1:100) + 10*randn(1, 100);
y4 = -75 + 3*(1:100) + 10*randn(1, 100);

% cscheme = get_colourscheme('cc-vivid');
% cscheme = cscheme(6:end, :);

cscheme = get_colourscheme('5set3');

figure
hold on
set(gca, 'ColorOrder', cscheme)
plot(y1, 'LineWidth', 2)
plot(y2, 'LineWidth', 2)
plot(y3, 'LineWidth', 2)
plot(y4, 'LineWidth', 2)
plot(fliplr(y1), 'LineWidth', 2)

legend({'y1', 'y2', 'y3', 'y4', 'y5'}, 'box', 'off', 'Location', 'northwest')