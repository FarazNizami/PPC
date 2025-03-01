document.addEventListener("DOMContentLoaded", function() {
    var sidebar = document.getElementById("sidebar");
    var toggleBtn = document.getElementById("toggle-btn");

    toggleBtn.addEventListener("click", function() {
        sidebar.classList.toggle("collapsed");

        // Store sidebar state in localStorage so it remembers the last position
        if (sidebar.classList.contains("collapsed")) {
            localStorage.setItem("sidebarState", "collapsed");
        } else {
            localStorage.setItem("sidebarState", "expanded");
        }
    });

    // Check localStorage and set sidebar state on page load
    if (localStorage.getItem("sidebarState") === "collapsed") {
        sidebar.classList.add("collapsed");
    }
});
