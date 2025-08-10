// Razorpay Payment - (demo)
document.addEventListener("DOMContentLoaded", function () {
  const payBtn = document.getElementById('payBtn');
  if (payBtn) {
    payBtn.addEventListener('click', function () {
      var options = {
        key: "<YOUR_RAZORPAY_KEY_ID>",
        amount: "50000", // Amount in paise (₹500)
        currency: "INR",
        name: "Bookwedgo Marriage Hall",
        description: "Booking Payment",
        handler: function (response){
          alert('Payment successful! Payment ID: ' + response.razorpay_payment_id);
          // Proceed to server-side verification here
        },
        prefill: {
          name: "",
          email: "",
          contact: ""
        },
        notes: {
          booking_id: "ID12345"
        },
        theme: {
          color: "#FA5480"
        }
      };
      var rzp1 = new Razorpay(options);
      rzp1.open();
    });
  }
});
