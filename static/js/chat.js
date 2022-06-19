$(document).ready(function(){
    $('#action_menu_btn').click(function(){
        $('.action_menu').toggle();
        // $('.action_menu').hide()
    });
});


document.querySelector('#room-name-input').focus();
document.querySelector('#room-name-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#room-name-submit').click();
        console.log("clicked");
    }
};

document.querySelector('#room-name-submit').onclick = function(e) {
    var roomName = document.querySelector('#room-name-input').value;
    window.location.pathname = '/chat/' + roomName + '/';
    console.log("clicked1");
};