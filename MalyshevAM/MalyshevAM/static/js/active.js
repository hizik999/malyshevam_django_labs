document.addEventListener('DOMContentLoaded', function() {
    const menu = document.querySelector('.menu');
    if (menu) {
        menu.querySelectorAll('a').forEach((item) => {
            item.addEventListener('click', (evt) => {
                const activeButton = menu.querySelector('.active');
                if (activeButton) {
                    activeButton.classList.remove('active');
                }
                evt.target.parentElement.classList.add('active');
            });
        });
    }

    // jQuery для работы с Isotope и фильтрацией
    $(document).ready(function () {
        var $grid = $('.grid').isotope({
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
});
