let iframe = document.getElementById ("ApprovalVotingVisualization");

document.getElementsByName("visualization_selection_button").forEach(element => {
    element.onclick = function () {
        iframe.src = "/static/visualizations/mcv/" + element.getAttribute("data-vizsrc");
    }
})

