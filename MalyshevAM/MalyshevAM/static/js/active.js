$(document).ready(function () {
//    $('.my-slider').unslider({
//        animation: 'vertical',
//        autoplay: true,
//        infinite: true
//    });
//
//
//    $('.our-client-carousal').owlCarousel({
//        items: 1,
//        loop: true,
//        autoplay: true,
//        autoplayTimeout: 5000,
//        margin: 10,
//        nav: true,
//        navText: [
//        "<i class=\"fa fa-angle-left\" aria-hidden=\"true\"></i>",
//        "<i class=\"fa fa-angle-right\" aria-hidden=\"true\"></i>"],
//    });
     var $grid = $('.grid').isotope({
//        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
    });
    var filterFns = {
        numberGreaterThan50: function () {
            var number = $(this).find('.number').text();
            return parseInt(number, 10) > 50;
        },
        ium: function () {
            var name = $(this).find('.name').text();
            return name.match(/ium$/);
        }
    };
    $('.filters-button-group').on('click', 'button', function () {
        var filterValue = $(this).attr('data-filter');
        filterValue = filterFns[filterValue] || filterValue;
        $grid.isotope({
            filter: filterValue
        });
    });
    $('.button-group').each(function (i, buttonGroup) {
        var $buttonGroup = $(buttonGroup);
        $buttonGroup.on('click', 'button', function () {
            $buttonGroup.find('.is-checked').removeClass('is-checked');
            $(this).addClass('is-checked');
        });
    });
});