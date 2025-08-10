// Calendar availability highlighting
document.addEventListener('DOMContentLoaded', function () {
  const bookedDates = window.bookedDates || [];
  // Highlight booked dates in calendar
  bookedDates.forEach(function (dateStr) {
    const dateCell = document.querySelector(`[data-date="${dateStr}"]`);
    if (dateCell) {
      dateCell.classList.add('booked');
      dateCell.innerText += ' (Booked)';
    }
  });
  // Mark today
  const today = new Date().toISOString().substr(0, 10);
  const todayCell = document.querySelector(`[data-date="${today}"]`);
  if (todayCell) {
    todayCell.classList.add('today');
  }
  // Click available date to select
  document.querySelectorAll('.calendar-table td.available').forEach(function (cell) {
    cell.onclick = function () {
      alert('You selected: ' + cell.getAttribute('data-date'));
      // You can redirect to booking form or trigger your logic here
    };
  });
});
