var host_url = 'http://169.254.0.2:8080';

$(document).ready(function()
{
   $("#saveScan").click(function(){
      var dpi = $('#scanresolution option:selected').text().split(' ')[0];
      var userNotes = $('#memo').val();
      $.ajax({
           url: host_url+"/cgi-bin/new_scan.py",
           type: "POST",
           data: {'resolution': dpi, 'userNotes': userNotes},
           success: function(response){
		   $("#lastScan").attr("src", host_url+"/scans/lastScan.jpg");
                   alert(JSON.stringify(response));
               }
      });
   });
});
