/*This Javascript file maps all the buttons to cgi-scripts.
It also makes an initial call for disk space usage*/

$(document).ready(function()
{
   Alert.init("#alert");
   $("#saveScan").click(function(){
      var dpi = $('#scanresolution option:selected').text().split(' ')[0];
      var userNotes = $('#memo').val();
      var prefix = $('#prefix').val();
      $.ajax({
           url: "cgi-bin/new_scan.py",
           type: "POST",
           data: {'resolution': dpi, 'userNotes': userNotes, 'prefix':prefix, 'time':$.now()},
           success: function(response){
              Alert.show(response);
              $("#lastScan").attr("src", "/scans/lastScan.jpg");
           }
      });
   });
   $("#preview").click(function(){
      $.ajax({
           url: "/cgi-bin/acquire_preview.py",
           type: "POST",
           data: {'type': 'preview'},
           success: function(response){
   		       $("#lastScan").attr("src", "/scans/lastScan.jpg");
                Alert.show(response);
            }
            
         });
   });
   $("#acquire").click(function(){
      $.ajax({
           url: "/cgi-bin/acquire_preview.py",
           type: "POST",
           data: {'type': 'acquire'},
           success: function(response){
   		          $("#lastScan").attr("src", "/scans/lastScan.jpg");
                Alert.show(response);
            }
         });
   });
   $("#start").click(function(){
      $.ajax({
           url: "/cgi-bin/motion.py",
           type: "POST",
           data: {'action': 'start'},
           success: function(response){
                Alert.show(response);
            }
         });
   });
   $("#stop").click(function(){
      $.ajax({
           url: "/cgi-bin/motion.py",
           type: "POST",
           data: {'action': 'stop'},
           success: function(response){
                Alert.show(response);
            }
         });
   });
   $("#capture").click(function(){
      $.ajax({
           url: "/cgi-bin/motion.py",
           type: "POST",
           data: {'action': 'screenshot'},
           success: function(response){
                Alert.show(response);
            }
         });
   });
   $("#lasers").click(function(){
     $.ajax({
          url: location.protocol + "//" + location.host+":9999",
          //contentType: 'text/plain',
          type: "POST",
          data: {'callString': 'lazers_toggle'},
          success: function(response){
             Alert.show(response);
         }
      });
   });
   $("#LEDBright").change(function(){
      var brightness = this.value.split('%')[0];
      if(brightness === 'Off'){
          brightness = '0';
      }
      $.ajax({
           url: location.protocol + "//" + location.host+":9999",
           //contentType: 'text/plain',
           type: "POST",
           data: {'callString': 'pwmLED '+brightness},
           success: function(response){
              Alert.show(response);
          }
       });
   });
   $("#pump1").click(function(){
     $.ajax({
          url: location.protocol + "//" + location.host+":9999",
          //contentType: 'text/plain',
          type: "POST",
          data: {'callString': 'pump1_toggle'},
          success: function(response){
             Alert.show(response);
         }
      });
   });
   $("#pump2").click(function(){
     $.ajax({
          url: location.protocol + "//" + location.host+":9999",
          //contentType: 'text/plain',
          type: "POST",
          data: {'callString': 'pump2_toggle'},
          success: function(response){
             Alert.show(response);
         }
      });
   });
   // changes on startup
   $("#webcamfeed").attr('src',location.protocol + "//" + location.host+":8081");
   $.ajax({
        url: "/cgi-bin/disk_space.py",
        type: "POST",
        success: function(response){
            //Alert.show(response);
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
