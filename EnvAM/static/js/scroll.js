$(document).ready(function(){
    var offset = 100;

    $("#navbar a").on('click', function(event) {
        if (this.hash !== "") {
            event.preventDefault();

             $($(this).attr('href'))[0].scrollIntoView();
                scrollBy(0, -offset);
        }
    });

    var scrollLocation = document.getElementById("scroll_location").textContent;
    $("div" + scrollLocation)[0].scrollIntoView();

});