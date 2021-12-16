function [result] = simulate(hits, rank, initialCritRate)
    stackValue = 0.08 + 0.02*(rank - 1);
    critRate = initialCritRate;
    result = 0;
    stacks = 0;
    for i = 1:hits
        if(chance(critRate) == true)
            result = result + 1;
            critRate = initialCritRate;
            stacks = 0;
        else
            if stacks < 5
                stacks = stacks + 1;
                critRate = critRate + stackValue;
            end
        end
    end
end