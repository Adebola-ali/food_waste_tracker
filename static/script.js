// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const foodTypeInput = document.getElementById("food_type");
  const quantityInput = document.getElementById("quantity");
  const conditionInput = document.getElementById("conditions");

  form.addEventListener("submit", function (event) {
    let valid = true;

    // Validate Food Type
    if (foodTypeInput.value.trim() === "") {
      alert("Food type is required!");
      valid = false;
    }

    // Validate Quantity
    if (quantityInput.value <= 0) {
      alert("Quantity must be greater than zero!");
      valid = false;
    }

    // Validate Condition
    if (conditionInput.value.trim() === "") {
      alert("Condition is required!");
      valid = false;
    }

    // Stop form submission if validation fails
    if (!valid) {
      event.preventDefault();
    }
  });
});
