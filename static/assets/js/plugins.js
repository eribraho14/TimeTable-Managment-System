// Check for elements with the specified attributes
var toastElements = document.querySelectorAll("[toast-list]");
var choicesElements = document.querySelectorAll("[data-choices]");
var providerElements = document.querySelectorAll("[data-provider]");

// Check if any of the elements are present
if (toastElements.length > 0 || choicesElements.length > 0 || providerElements.length > 0) {
    // Load Toastify script
    document.writeln("<script type='text/javascript' src='https://cdn.jsdelivr.net/npm/toastify-js'></script>");

    // Load Choices script
    document.writeln("<script type='text/javascript' src='{% static '/assets/libs/choices.js/public/assets/scripts/choices.min.js' %}'></script>");

    // Load Flatpickr script
    document.writeln("<script type='text/javascript' src='{% static '/assets/libs/flatpickr/flatpickr.min.js' %}'></script>");
}
