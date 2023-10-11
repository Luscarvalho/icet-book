function searchFilm() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function back() {
    window.history.back();
}

$(document).ready(function () {
    $('#myTable').DataTable({
        paging: false,
        info: false,
        searching: false,
        responsive: true,
        "language": {
          "emptyTable": "Não há livros disponíveis."
        }
    });
});