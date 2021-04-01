window.addEventListener("load", function() {

    const inRef = document.getElementById("ref");
    const outRank = document.getElementById("rank");
    const inCrit = document.getElementById("basecrit");
    const outContrib = document.getElementById("contrib");

    listen(inRef);
    listen(inCrit);
    update();
    
    function listen(input) {
        input.addEventListener("change", update);
    }
    function val(input) {
        return parseFloat(input.value);
    }
    function update(){
        outRank.innerText = (8 + 2*(val(inRef)-1)).toString();
        outContrib.value = truncate(calculate(val(inRef), val(inCrit)/100)*100, 4);
    }


    function calculate(r, x) {
        var ref = Array(5);
        ref[0] = function(x) { return -0.10158034117292747*Math.pow(x, 3)+0.31101509708848735*Math.pow(x, 2)+-0.4000198511105707*Math.pow(x, 1)+0.18932855038352558}
        ref[1] = function(x) { return -0.10114100798963055*Math.pow(x, 3)+0.31549951098707774*Math.pow(x, 2)+-0.42777398106120645*Math.pow(x, 1)+0.21160958631034335}
        ref[2] = function(x) { return -0.0973317320403049*Math.pow(x, 3)+0.3109264569837878*Math.pow(x, 2)+-0.4462218801782434*Math.pow(x, 1)+0.23015547899566594}
        ref[3] = function(x) { return -0.09305456817824306*Math.pow(x, 3)+0.30332830972277874*Math.pow(x, 2)+-0.45976802242978737*Math.pow(x, 1)+0.24621017771906156}
        ref[4] = function(x) { return -0.08877667311982003*Math.pow(x, 3)+0.29461590134457105*Math.pow(x, 2)+-0.47051978617321616*Math.pow(x, 1)+0.26049964486333793}
        return Math.max(ref[r-1](x), 0);
    }

    function truncate(x, n) {
        return (Math.floor(x*Math.pow(10, n))/Math.pow(10, n)).toString();
    }
});