Calculator = function(opts) {
    $theForm    = opts.$theForm;
    $a          = $theForm.find("input[name=a]");
    $b          = $theForm.find("input[name=b]");
    $op         = $theForm.find("input[name=op]");
    $error      = opts.$error;
    $errorMsg   = $error.find("#msg");
    $answer     = opts.$answer;
    $answerVal  = opts.$answerVal;
    
    $theForm.on("submit", handleFormSubmit);

    function handleFormSubmit(evt) {
        var a = $a.val();
        var b = $b.val();
        var op = $op.filter(":checked").val();
        calculateResult(a, b, op);
        evt.preventDefault();
    }

    function calculateResult(a, b, op) {
        $.ajax({
            url:"/calculate",
            data: {"a":a, "b":b, "op":op},
            success: showResult,
            error: handleError,
            method:"POST"
        });
    }

    function showResult(data) {
        $error.hide();
        $answer.show();
        $answerVal.html(data);
     }

    function handleError(jqxhr, textstatus, errorthrown) {
        $errorMsg.html(jqxhr.responseText);
        $error.show();
    }
};