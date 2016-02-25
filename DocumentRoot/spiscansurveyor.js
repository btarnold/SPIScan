var host_url = 'http://localhost';

$(document).ready(function()
{
   $("#saveScan").click(function(){
      var dpi = $('#scanresolution option:selected').text().split(' ')[1];
      var userNotes = $('#memo').val();
      var prefix = $('#prefix').val();
      $.ajax({
           url: host_url+"/cgi-bin/new_scan.py",
           type: "POST",
           data: {'resolution': dpi, 'userNotes': userNotes, 'prefix':prefix},
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
   		       $("#lastScan").attr("src", host_url+"/scans/lastScan.jpg");
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
   		          $("#lastScan").attr("src", host_url+"/scans/lastScan.jpg");
                alert(JSON.stringify(response));
            }
         });
   });
   $("#start").click(function(){
      $.ajax({
           url: host_url+"/cgi-bin/motion.py",
           type: "POST",
           data: {'action': 'start'},
           success: function(response){
                alert(JSON.stringify(response));
            }
         });
   });
   $("#stop").click(function(){
      $.ajax({
           url: host_url+"/cgi-bin/motion.py",
           type: "POST",
           data: {'action': 'stop'},
           success: function(response){
                alert(JSON.stringify(response));
            }
         });
   });
   $("#capture").click(function(){
      $.ajax({
           url: host_url+"/cgi-bin/motion.py",
           type: "POST",
           data: {'action': 'screenshot'},
           success: function(response){
                alert(JSON.stringify(response));
            }
         });
   });
   $("#lasers").click(function(){
     $.ajax({
          url: host_url + ":9999",
          //contentType: 'text/plain',
          type: "POST",
          data: {'callString': 'lazers_toggle'},
          success: function(response){
             alert(JSON.stringify(response));
         }
      });
   });
   $("#LEDBright").val('Off');
   $("#LEDBright").change(function(){
      var brightness = this.value.split('%')[0];
      if(brightness === 'Off'){
          brightness = '0';
      }
      $.ajax({
           url: host_url + ":9999",
           //contentType: 'text/plain',
           type: "POST",
           data: {'callString': 'pwmLED '+brightness},
           success: function(response){
              alert(JSON.stringify(response));
          }
       });
   });
   $("#pump1").click(function(){
     $.ajax({
          url: host_url + ":9999",
          //contentType: 'text/plain',
          type: "POST",
          data: {'callString': 'pump1_toggle'},
          success: function(response){
             alert(JSON.stringify(response));
         }
      });
   });
   $("#pump2").click(function(){
     $.ajax({
          url: host_url + ":9999",
          //contentType: 'text/plain',
          type: "POST",
          data: {'callString': 'pump2_toggle'},
          success: function(response){
             alert(JSON.stringify(response));
         }
      });
   });
   $.ajax({
        url: host_url + ":9999",
        //contentType: 'text/plain',
        type: "POST",
        data: {'callString': 'init'},
        success: function(response){
           alert(JSON.stringify(response));
       }
    });

});
