
document.addEventListener('DOMContentLoaded', function() {
    const dateField = document.querySelector('input[type="date"]');

    function disableWeekends(date) {
        /** Checks if a given date falls on a weekend (Saturday or Sunday). 
         * It takes a date as input, 
         * creates a new Date object, 
         * and uses the getUTCDay method to get the day 
         * of the week (0 for Sunday, 6 for Saturday). */
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