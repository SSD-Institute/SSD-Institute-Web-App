let iframe = document.getElementById ("CollaborativeVetoVisualization");

document.getElementsByName("visualization_selection_button").forEach(element => {
    element.onclick = function () {
        iframe.src = "/static/visualizations/cv/" + element.getAttribute("data-vizsrc");
    }
})

