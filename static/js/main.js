document.addEventListener('DOMContentLoaded', function () {
  // Simple booking form validation
  const bookingForm = document.querySelector('form');
  if (bookingForm) {
    bookingForm.addEventListener('submit', function (e) {
      // Validate name, email, date not empty
      const name = bookingForm.querySelector('input[name="name"]');
      const email = bookingForm.querySelector('input[name="email"]');
      const date = bookingForm.querySelector('input[name="date"]');
      if (!name.value.trim() || !email.value.trim() || !date.value) {
        alert('Please fill all booking fields!');
        e.preventDefault();
        return false;
      }
    });
  }
});
