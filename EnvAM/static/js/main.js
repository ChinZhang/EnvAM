$(document).ready();

    function checkForm(form) {
        var scode1 = form.scode1.value
        var scode2 = form.scode2.value

        if(scode1 == scode2) {
            alert("Error: Data 1 can not be equal to Data 2.");
            form.scode1.focus();
            return false;
        }

        if(scode1 == "Select Variable" || scode2 == "Select Variable") {
            alert("Error: Select a variable for both Data 1 and Data 2");
            form.scode1.focus();
            return false;
        }

        return true;
    }

        function addressToggle(dataInsight) {
        $(dataInsight).slideToggle('slow');
    }