/*This Javascript file maps all the buttons to cgi-scripts.
It also enables editing of user-notes (by double clicking) and make an
ajax request to the appropriate cgi-script if there is a change made.
It also makes an initial call for disk space usage.*/

//useful function, needed for replacing commas
String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.split(search).join(replacement);
};

$(document).ready(function()
{
   
   //BUTTON MAPPINGS
   $("#export").click(function(){
      $.ajax({
           url: "/cgi-bin/exportcsv.py",
           type: "GET",
           success: function(response){
                   Alert.show(response);
               }
      });
   });
   $("#purge").click(function(){
      bootbox.confirm("This will purge the entire database and delete all scans. Please offload if you have not yet. Are you sure?", function(result) {
        if(result){
          bootbox.confirm("This is your last chance. Are you sure you want to purge?", function(result) {
            if(result){
              $.ajax({
                 url: "/cgi-bin/db.py",
                 type: "POST",
                 data: {'action':'purge'},
                 success: function(response){
                     Alert.show(response);
                     location.reload(true);
                 }
              });
            }
          });
        }
      });
   });
   $('.delete').click(function(){
      var tr = $(this).closest('tr');
      var row_id = tr.attr("id");
      bootbox.confirm("This will delete the entry. Are you sure?", function(result) {
        if(result){
          $.ajax({
               url: "/cgi-bin/db.py",
               type: "POST",
               data: {'id': row_id, 'action':'delete_entry'},
               success: function(response){
                      Alert.show(response);
                      tr.css("background-color","#FF3700");
                      tr.fadeOut(400, function(){
                          tr.remove();
                      });
                      return false;
               }
          });
        }
      }); 
   });
   $(".editable").dblclick(function () {
        var OriginalContent = $(this).text().replaceAll("'","&apos;");
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
                   //newContent.replaceAll("&apos;","'");
                   $.ajax({
                        url: "/cgi-bin/db.py",
                        type: "POST",
                        data: {'id': row_id, 'newContent': newContent, 'action':'update'},
                        success: function(response){
                                Alert.show(response);
                            }
                   });
               }
            }
        });

        $(this).children().first().blur(function(){
            OriginalContent = OriginalContent.replaceAll("&apos;","'");
            $(this).parent().text(OriginalContent);
            $(this).parent().removeClass("cellEditing");
        });
    });
   //PAGE INITIALIZATION
   Alert.init("#alert");
   $.ajax({
        url: "/cgi-bin/disk_space.py",
        type: "POST",
        success: function(response){
            //alert(JSON.stringify(response));
            var percentage = response['percentage'].split('%')[0];
            $("#sysmem").html(
              '<div class="progress"> \
                <div class="bar" style="width:'+percentage+'%;"> \
                  '+percentage+'% Full \
                </div> \
              </div>'
            );
        }
   });
});
