console.log('incident review script loaded');

eventid = $("#details-container").attr("data-event-id");

console.log(eventid);

$('body').append('<div style="position:absolute; right:5px; top:45px;"><a href="incidentstatus/0">Incident</a></div>')
$('body').append('<div style="position:absolute; right:5px; top:55px;"><a href="incidentstatusisevent/0">Event</a></div>')
