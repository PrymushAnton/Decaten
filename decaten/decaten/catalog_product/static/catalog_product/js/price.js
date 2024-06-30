
let priceGap = 0;
function updateProgress() {
    let minVal = parseInt($(".range-input input:eq(0)").val()),
        maxVal = parseInt($(".range-input input:eq(1)").val());
    let minRange = parseInt($("#min-price-slider").attr("min")),
        maxRange = parseInt($("#max-price-slider").attr("max"));
    let leftValue = ((minVal - minRange) / (maxRange - minRange)) * 100 + "%";
    let rightValue = ((maxRange - maxVal) / (maxRange - minRange)) * 100 + "%";
    $(".progress").css({
        "left": leftValue,
        "right": rightValue
    });
    $('.input-min').val(minVal);
    $('.input-max').val(maxVal);
}
updateProgress();
$(".price-input input").each(function (index, input) {
    $(input).on("input", function (e) {
        let minPrice = parseInt($(".price-input input:eq(0)").val()),
            maxPrice = parseInt($(".price-input input:eq(1)").val());

        if ((maxPrice - minPrice >= priceGap) && maxPrice <= $("#max-price-slider").attr("max")) {
            if ($(this).hasClass("input-min")) {
                $("#min-price-slider").val(minPrice);
                updateProgress();
            } else {
                $("#max-price-slider").val(maxPrice);
                updateProgress();
            }
        }
    });
});
$(".range-input input").each(function (index, input) {
    $(input).on("input", function (e) {
        let minVal = parseInt($(".range-input input:eq(0)").val()),
            maxVal = parseInt($(".range-input input:eq(1)").val());
        if ((maxVal - minVal) < priceGap) {
            if ($(this).hasClass("range-min")) {
                $(".range-input input:eq(0)").val(maxVal - priceGap);
                updateProgress();
            } else {
                $(".range-input input:eq(1)").val(minVal + priceGap);
                updateProgress();
            }
        } else {
            updateProgress();
        }
    });
});






function updateProgressPhone() {
    let minVal = parseInt($(".range-input-phone input:eq(0)").val()),
        maxVal = parseInt($(".range-input-phone input:eq(1)").val());
    let minRange = parseInt($("#min-price-slider-phone").attr("min")),
        maxRange = parseInt($("#max-price-slider-phone").attr("max"));
    let leftValue = ((minVal - minRange) / (maxRange - minRange)) * 100 + "%";
    let rightValue = ((maxRange - maxVal) / (maxRange - minRange)) * 100 + "%";
    $(".progress-phone").css({
        "left": leftValue,
        "right": rightValue
    });
    $('.input-min-phone').val(minVal);
    $('.input-max-phone').val(maxVal);
}
updateProgressPhone();
$(".price-input-phone input").each(function (index, input) {
    $(input).on("input", function (e) {
        let minPrice = parseInt($(".price-input-phone input:eq(0)").val()),
            maxPrice = parseInt($(".price-input-phone input:eq(1)").val());

        if ((maxPrice - minPrice >= priceGap) && maxPrice <= $("#max-price-slider-phone").attr("max")) {
            if ($(this).hasClass("input-min-phone")) {
                $("#min-price-slider-phone").val(minPrice);
                updateProgress();
            } else {
                $("#max-price-slider-phone").val(maxPrice);
                updateProgress();
            }
        }
    });
});
$(".range-input-phone input").each(function (index, input) {
    $(input).on("input", function (e) {
        let minVal = parseInt($(".range-input-phone input:eq(0)").val()),
            maxVal = parseInt($(".range-input-phone input:eq(1)").val());
        if ((maxVal - minVal) < priceGap) {
            if ($(this).hasClass("range-min")) {
                $(".range-input-phone input:eq(0)").val(maxVal - priceGap);
                updateProgressPhone();
            } else {
                $(".range-input-phone input:eq(1)").val(minVal + priceGap);
                updateProgressPhone();
            }
        } else {
            updateProgressPhone();
        }
    });
});
