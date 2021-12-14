$(document).ready(function () {
    $.ajax({
        url: '/api/v1/events',
        method: 'GET',
        success: function (response) {
            for (let event of response) {
                let el = " <li class='list-group-item'>" + event.name + "</li>";
                $('#events').append(el);
            }
        }
    })
});
