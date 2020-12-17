scheme = 'cc-vivid';
hexcode = '#E58606,#5D69B1,#52BCA3,#99C945,#CC61B0,#24796C,#DAA51B,#2F8AC4,#764E9F,#ED645A,#CC3A8E,#A5AA99';

hexcode_arr = split(hexcode, ',');
scheme_rgb = zeros(length(hexcode_arr), 3);

for kk=1:length(hexcode_arr)
    hexstr = hexcode_arr{kk};
    scheme_rgb(kk, 1) = 1/256*hex2dec(hexstr(2:3));
    scheme_rgb(kk, 2) = 1/256*hex2dec(hexstr(4:5));
    scheme_rgb(kk, 3) = 1/256*hex2dec(hexstr(6:7));
end

save([scheme, '.txt'], '-ascii', 'scheme_rgb')