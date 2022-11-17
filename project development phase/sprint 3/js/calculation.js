function calculate() {
        if (isNaN(document.forms["myform"]["total_cost"].value) || document.forms["myform"]["total_cost"].value == "") {
            var text1 = 0;
        } else {
            var text1 = parseInt(document.forms["myform"]["total_cost"].value);
        }
        if (isNaN(document.forms["myform"]["Quantity"].value) || document.forms["myform"]["Quantity"].value == "") {
            var text2 = 0;
        } else {
            var text2 = parseFloat(document.forms["myform"]["Quantity"].value);
        }
        document.forms["myform"]["total_Amount"].value = (text1 * text2);
    }  

    