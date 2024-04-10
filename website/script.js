const field = document.getElementById("field");
const recursionDeptSelector = document.getElementById("depth");
const submit = document.getElementById("submit");

submit.addEventListener("click", () => {
    const profileRegex = /^https:\/\/open\.spotify\.com\/user\/[a-zA-Z0-9]+(\?si=[a-zA-Z0-9]+)?$/;
    if (!profileRegex.test(field.value)) {
        document.getElementById("status").textContent = "Please enter a valid profile URL";
        console.warn("failed");
    } else {
        const url = field.value;
        const depth = recursionDeptSelector.value;
        console.log(url);
        console.log(depth);
    }
});
