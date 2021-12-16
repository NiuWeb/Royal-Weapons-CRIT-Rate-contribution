increase = readmatrix("data/increase.csv");
total = readmatrix("data/total.csv");
range = -1:0.001:1;

figure;
xline(0, ':k');
hold;
text = "";
%% POLYFIT FOR INCREASE DATA
for rank = 1:5
   % POLYFIT FOR NEGATIVE NUMBERS
   y = increase(rank, range < 0);
   index = find(y > 0);
   x = range(index);
   y = increase(rank, index);
   plot(x, y);
   p1 = polyfit(x, y, 6);
   plot(x, polyval(p1, x), '--b');
   % POLYFIT FOR RANGE 0-X
   v = 1 - (0.08 + 0.02*(rank - 1));
   p = range >= 0 & range < v;
   y = increase(rank, p);
   x = range(p);
   plot(x, y);
   xline(v, ':k');
   p2 = polyfit(x, y, 3);
   plot(x, polyval(p2, x), '--k');
   % POLYFIT FOR RANGE X-1
   p = range >= v;
   y = increase(rank, p);
   x = range(p);
   plot(x, y);
   p3 = polyfit(x, y, 2);
   plot(x, polyval(p3, x), '--k');
   
   text = text + "[";
   text = text + "[" + num2str(reshape(p1, 1, [])) + "], ";
   text = text + "[" + num2str(reshape(p2, 1, [])) + "], ";
   text = text + "[" + num2str(reshape(p3, 1, [])) + "]";
   text = text + "],";
end
diary poly/coefficients.txt;
disp(text);
diary off;

set(gcf, "PaperUnits", "inches");
set(gcf, "PaperPosition", [0 0 16 9]);
print(gcf, "poly/poly.png", "-dpng", "-r300");