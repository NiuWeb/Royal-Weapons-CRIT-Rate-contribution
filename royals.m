range = -1:0.001:1;
increase = zeros(size(range));
total = zeros(size(range));
i = 1;

hits = 1e6;
for critRate = range
    for rank = 1:5
        crits = simulate(hits, rank, critRate);
        rate = crits/hits;
        increase(rank, i) = rate - max(0, critRate);
        total(rank, i) = rate;
    end
    i = i + 1;
end

writematrix(increase, "data/increase.csv");
writematrix(total, "data/total.csv");