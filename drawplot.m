increase = readmatrix("data/increase.csv");
total = readmatrix("data/total.csv");

%% ROYAL WEAPONS CRIT RATE INCREASE
F1= figure;
title("Royal Weapons CRIT Rate increase");

xlabel("Initial CRIT Rate");
ylabel("CRIT Rate increase");

xticks(-1:0.05:1);
yticks(0:0.01:1);

grid;
hold;
for rank = 1:5
    plot(range, increase(rank,:));
end
xline(0, ":k");

legend("R1", "R2", "R3", "R4", "R5");
set(gcf, "PaperUnits", "inches");
set(gcf, "PaperPosition", [0 0 16 9]);
print(gcf, "plots/increase.png", "-dpng", "-r300");
%% ROYAL WEAPONS EFFECTIVE CRIT RATE
figure;
title("Royal Weapons Effective CRIT Rate");

xlabel("Initial CRIT Rate");
ylabel("Effective CRIT Rate");

xticks(-1:0.05:1);
yticks(0:0.05:1);

grid;
hold;
for rank = 1:5
    plot(range, total(rank,:));
end
xline(0, ":k");

legend("R1", "R2", "R3", "R4", "R5");

set(gcf, "PaperUnits", "inches");
set(gcf, "PaperPosition", [0 0 16 9]);
print(gcf, "plots/total.png", "-dpng", "-r300");