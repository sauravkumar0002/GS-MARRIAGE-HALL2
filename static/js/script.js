// Future JS like date-picker, modal, alert fade etc.
document.addEventListener('DOMContentLoaded', () => {
  const flashMessages = document.querySelectorAll('.flash');
  flashMessages.forEach(msg => {
    setTimeout(() => {
      msg.style.display = 'none';
    }, 4000); // auto hide in 4 sec
  });
});
