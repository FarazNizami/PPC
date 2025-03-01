document.getElementById("toggle-btn").addEventListener("click", function() {
    var sidebar = document.getElementById("sidebar");
    sidebar.classList.toggle("minimized");
});

function loadPage(page) {
    fetch(`/pages/${page}`)
    .then(response => response.text())
    .then(data => {
        document.getElementById("content-area").innerHTML = data;
    });
}
