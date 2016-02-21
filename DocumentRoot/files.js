var host_url = 'http://localhost';

$(document).ready(function()
{
   $("#export").click(function(){
      $.ajax({
           url: host_url+"/cgi-bin/exportcsv.py",
           type: "GET",
           success: function(response){
                   alert(JSON.stringify(response));
               }
      });
   });
   $("#purge").click(function(){
      $.ajax({
           url: host_url+"/cgi-bin/purgedb.py",
           type: "POST",
           success: function(response){
               alert(JSON.stringify(response));
               location.reload(true);
           }
      });
   });
   $('.delete').click(function(){
      var tr = $(this).closest('tr');
      var row_id = tr.attr("id");
      $.ajax({
           url: host_url+"/cgi-bin/delete_db_entry.py",
           type: "POST",
           data: {'id': row_id},
           success: function(response){
                  alert(JSON.stringify(response));
                  tr.css("background-color","#FF3700");
                  tr.fadeOut(400, function(){
                      tr.remove();
                  });
                  return false;
               }
      });
   });
   $.ajax({
        url: host_url+"/cgi-bin/disk_space.py",
        type: "POST",
        success: function(response){
            alert(JSON.stringify(response));
            $("#sysmem").html(response['percentage']);
        }
   });
});
