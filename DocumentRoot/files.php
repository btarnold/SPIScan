<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>SPI-Scan Surveyor</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="GUI SPI-Scan Surveyor">
    <meta name="author" content="Benthic Science Limited">
	<!-- Version 0.1.0 21 April 2012 D-Space/Benthic Science Limited --!>
	<!-- Open-source under the Apache License Version 2.0, January 2004 http://www.apache.org/licenses/ --!>
	<!-- Based on the Twitter Bootstrap --!>

    <!-- Le styles -->
    <link href="static/docs/assets/css/bootstrap.css" rel="stylesheet">
    <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }
    </style>
    <link href="static/docs/assets/css/bootstrap-responsive.css" rel="stylesheet">
    <link href="table.css" rel="stylesheet">
    <link href="theme.css" rel="stylesheet">

    <!-- Le fav and touch icons -->
    <link rel="shortcut icon" href="static/docs/ico/favicon.ico">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="static/docs/assets/ico/apple-touch-icon-114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="static/docs/assets/ico/apple-touch-icon-72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="static/docs/assets/ico/apple-touch-icon-57-precomposed.png">
  </head>

  <body>

    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
	<a class="brand" href="#">SPI-Scan Surveyor</a>
          <div class="nav-collapse">
            <ul class="nav">
	      <li><a href="/spiscansurveyor.html">deploy</a>
              <li><a href="/setup.html">setup</a></li>
              <li><a href="/io.html">input/output</a></li>
              <li class="active"><a href="#">FILES</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>
    <div align = "center">
       <div id = 'sysmem'></div>
       <a class = 'btn' id = 'export'>Export and Pack</a>
       <a class = 'btn' id = 'dlzip' href = "/db.zip">Download Zip</a>
       <a class = 'btn' id = 'purge'>Purge</a>
    </div>

    <div class="container">
      <?php
         class MyDB extends SQLite3
         {
            function __construct()
            {
               $this->open('db/test.db');
            }
         }
         $db = new MyDB();
         if(!$db){
            echo $db->lastErrorMsg();
         } else {
            echo "Opened database successfully<br/>";
         }

         $sql = "SELECT * from SCANS";
         $ret = $db->query($sql);
         echo "<table class = 'table'>";
         echo "<thead><tr>";
         echo "<th align='left'>ID</th>";
         echo "<th align='left'>FILENAME</th>";
         echo "<th align='left'>DPI</th>";
         echo "<th align='left'>USERNOTES</th>";
         echo "<th align='left'>TIME</th>";
         echo "<th align='left'>LOCATION</th>";
         echo "<th>DOWNLOAD</th>";
         echo "<th>DELETE</th>";
         echo "</tr></thead>";
         while($row = $ret->fetchArray(SQLITE3_ASSOC) ){
            echo "<tr id = '".$row['ID']."'>";
            echo "<td>". $row['ID'] . "</td>";
            echo "<td><a href = 'scans/". $row['FILENAME'] ."'>";
            echo $row['FILENAME'] ."</a></td>";
            echo "<td>". $row['DPI'] ."</td>";
            echo "<td class = 'editable'>".$row['USERNOTES'] ."</td>";
            echo "<td>".$row['TIME'] ."</td>";
            echo "<td>".$row['LOCATION'] ."</td>";
            echo "<td><button><a href = 'scans/".$row['FILENAME'] . "' ";
            echo "download = '".$row['FILENAME']."'>";
	         echo "DOWNLOAD</td></button></td>";
            echo "<td><button class = 'delete'>DELETE</button></td>";
            echo "</tr>";
         }
         echo "</table>";
         #echo "Operation done successfully\n";
         $db->close();
      ?>


    </div> <!-- /container -->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->

    <script src="static/docs/assets/js/jquery.js"></script>
    <script src="table.js"></script>
    <script src="files.js"></script>
    <script src="static/docs/assets/js/bootstrap-transition.js"></script>
    <script src="static/docs/assets/js/bootstrap-alert.js"></script>
    <script src="static/docs/assets/js/bootstrap-modal.js"></script>
    <script src="static/docs/assets/js/bootstrap-dropdown.js"></script>
    <script src="static/docs/assets/js/bootstrap-scrollspy.js"></script>
    <script src="static/docs/assets/js/bootstrap-tab.js"></script>
    <script src="static/docs/assets/js/bootstrap-tooltip.js"></script>
    <script src="static/docs/assets/js/bootstrap-popover.js"></script>
    <script src="static/docs/assets/js/bootstrap-button.js"></script>
    <script src="static/docs/assets/js/bootstrap-collapse.js"></script>
    <script src="static/docs/assets/js/bootstrap-carousel.js"></script>
    <script src="static/docs/assets/js/bootstrap-typeahead.js"></script>

  </body>
</html>
