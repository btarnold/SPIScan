var host_url = "http://localhost";

$(document).ready(function () {
    $(".editable").dblclick(function () {
        var OriginalContent = $(this).text();
        var row_id = $(this).parents("tr").attr("id");
        $(this).addClass("cellEditing");
        $(this).html("<input type='text' value='" + OriginalContent + "' />");
        $(this).children().first().focus();

        $(this).children().first().keypress(function (e) {
            if (e.which == 13) { //enter key
                var newContent = $(this).val();
                $(this).parent().text(newContent);
                $(this).parent().removeClass("cellEditing");
                if(newContent !== OriginalContent){
                   $.ajax({
                        url: host_url+"/cgi-bin/updatedb.py",
                        type: "POST",
                        data: {'id': row_id, 'newContent': newContent},
                        success: function(response){
                                alert(JSON.stringify(response));
                            }
                   });
               }
            }
        });

    $(this).children().first().blur(function(){
        $(this).parent().text(OriginalContent);
        $(this).parent().removeClass("cellEditing");
    });
    });
});
