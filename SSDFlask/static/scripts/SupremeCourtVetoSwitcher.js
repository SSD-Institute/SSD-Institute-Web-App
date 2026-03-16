let iframe = document.getElementById ("SupremeCourtVetoVisualization");

document.getElementsByName("visualization_selection_button").forEach(element => {
    element.onclick = function () {
        iframe.src = "/static/visualizations/scv/" + element.getAttribute("data-vizsrc");
    }
})

