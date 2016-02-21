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
                   if(response['success']){
                      alert("scan added");
                   }
                   else {
                      alert("Please Export and Purge DB\n System Memory is too full");
                   }
               }
      });
   });
   $("#preview").click(function(){
      $.ajax({
           url: host_url+"/cgi-bin/acquire_preview.py",
           type: "POST",
           data: {'type': 'preview'},
           success: function(response){
   		       $("#lastScan").attr("src", host_url+"/scans/lastScan.jpeg");
                alert(JSON.stringify(response));
            }
         });
   });
   $("#acquire").click(function(){
      $.ajax({
           url: host_url+"/cgi-bin/acquire_preview.py",
           type: "POST",
           data: {'type': 'acquire'},
           success: function(response){
   		       $("#lastScan").attr("src", host_url+"/scans/lastScan.jpeg");
                alert(JSON.stringify(response));
            }
         });
   });
});
