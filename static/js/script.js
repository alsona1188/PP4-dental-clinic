
document.addEventListener('DOMContentLoaded', function() {
    const dateField = document.querySelector('input[type="date"]');

    function disableWeekends(date) {
        const day = new Date(date).getUTCDay();
        return day === 0 || day === 6; // 0 = Sunday, 6 = Saturday
    }

    dateField.addEventListener('change', function() {
        const inputDate = this.value;
        if (disableWeekends(inputDate)) {
            alert('Weekends are not allowed. Please select a weekday.');
            this.value = '';
        }
    });
});