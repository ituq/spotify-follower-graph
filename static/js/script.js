const field = document.getElementById("field");
const recursionDepthSelector = document.getElementById("depth");
const submit = document.getElementById("submit");
const statusElement = document.getElementById("status");

submit.addEventListener("click", () => {
    const profileRegex = /^https:\/\/open\.spotify\.com\/user\/[a-zA-Z0-9]+(\?si=[a-zA-Z0-9]+)?$/;
    if (!profileRegex.test(field.value)) {
        statusElement.textContent = "Please enter a valid profile URL";
        console.warn("failed");
    } else {
        // Prepare data for submission
        const formData = new FormData();
        formData.append('url', field.value);
        formData.append('depth', recursionDepthSelector.value);
        submit.innerHTML='<div class="loader""></div>'
        // Fetch API to send form data to the server
        fetch('/process', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Assuming the server responds with a JSON object containing the redirect URL
            if(data.redirectURL) {
                window.location.href = data.redirectURL; // Redirect the user
            } else {
                statusElement.textContent = "Server did not provide a redirect URL";
            }
        })
        .catch(error => {
            console.error('Error:', error);
            statusElement.textContent = "An error occurred while submitting the form";
        });
    }
});
