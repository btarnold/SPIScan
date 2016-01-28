var host_url = 'http://localhost';

$(document).ready(function()
{
   $("#saveScan").click(function(){
      var dpi = $('#scanresolution option:selected').text().split(' ')[1];
      var userNotes = $('#memo').val();
      $.ajax({
           url: host_url+"/cgi-bin/new_scan.py",
           type: "POST",
           data: {'resolution': dpi, 'userNotes': userNotes},
           success: function(response){
                   alert(JSON.stringify(response));
               }
      });
   });
});
