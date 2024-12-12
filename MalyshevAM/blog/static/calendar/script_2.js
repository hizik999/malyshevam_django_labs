document.addEventListener('DOMContentLoaded', function () {
    let today = new Date();
    let currentMonth = today.getMonth();
    let currentYear = today.getFullYear();
    let selectedDay = today.getDate();

    showCalendar(currentMonth, currentYear);

    document.querySelector('#previous').addEventListener('click', () => {
        currentMonth--;
        if (currentMonth < 0) {
            currentMonth = 11;
            currentYear--;
        }
        showCalendar(currentMonth, currentYear);
    });

    document.querySelector('#next').addEventListener('click', () => {
        currentMonth++;
        if (currentMonth > 11) {
            currentMonth = 0;
            currentYear++;
        }
        showCalendar(currentMonth, currentYear);
    });

    function showCalendar(month, year) {
        let firstDay = new Date(year, month, 1).getDay() - 1; // Смещаем первый день на воскресенье
        if (firstDay < 0) firstDay = 6;

        let lastDateOfMonth = new Date(year, month + 1, 0).getDate();

        let calendarBody = document.getElementById("calendar-body");
        calendarBody.innerHTML = '';

        // Создаем строку для первой недели
        let row = document.createElement("tr");

        // Заполняем пустые ячейки до первого дня месяца
        for (let i = 0; i < firstDay; i++) {
            let cell = document.createElement("td");
            cell.textContent = '';
            row.appendChild(cell);
        }

        // Заполняем ячейки числами месяца
        for (let i = 1; i <= lastDateOfMonth; i++) {
            let cell = document.createElement("td");
            cell.textContent = i;

            if (i === selectedDay) {
                cell.classList.add("active");
            }

            cell.onclick = function () {
                selectedDay = parseInt(this.innerText);
                showCalendar(month, year);

                const dateFormat = `${year}-${month + 1}-${i}`;
                document.getElementById("dateDisplay").textContent = dateFormat;
            };

            row.appendChild(cell);

            // Если дошли до конца недели, начинаем новую строку
            if ((firstDay + i) % 7 === 0 || i === lastDateOfMonth) {
                calendarBody.appendChild(row);
                row = document.createElement("tr");
            }
        }

        // Добавляем пустые ячейки после последнего дня месяца
        while (row.children.length < 7) {
            let cell = document.createElement("td");
            cell.textContent = '';
            row.appendChild(cell);
        }

        // Добавляем последнюю строку, если она неполная
        if (row.children.length > 0) {
            calendarBody.appendChild(row);
        }

        document.getElementById("monthAndYear").innerText = getMonthName(month) + ', ' + year;
    }

    function getMonthName(monthIndex) {
        const months = [
            'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
            'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
        ];
        return months[monthIndex];
    }
});