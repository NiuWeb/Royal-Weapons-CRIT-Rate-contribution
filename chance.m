function [result] = chance(probability) 
    p = rand;
    if(p <= probability)
        result = true;
    else
        result = false;
    end
end