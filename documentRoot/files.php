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

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

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

    <div class="container">
      <?php
         class MyDB extends SQLite3
         {
            function __construct()
            {
               $this->open('../db/test.db');
            }
         }
         $db = new MyDB();
         if(!$db){
            echo $db->lastErrorMsg();
         } else {
            echo "Opened database successfully<br/>";
         }

         $sql = "SELECT * from COMPANY";
         $ret = $db->query($sql);
         echo "<table class = 'table'>";
         echo "<thead><tr>";
         echo "<th align='left'>ID</th>";
         echo "<th align='left'>NAME</th>";
         echo "<th align='left'>ADDRESS</th>";
         echo "<th align='left'>SALARY</th>";
         echo "<th>EDIT</th>";
         echo "<th>DELETE</th>";
         echo "</tr></thead>";
         while($row = $ret->fetchArray(SQLITE3_ASSOC) ){
            echo "<tr id = '".$row['ID']."'>";
            echo "<td>". $row['ID'] . "</td>";
            echo "<td><a href = 'images/". $row['NAME'] .".jpg'";
            echo "download = '".$row['NAME'].".jpg'>";
            echo $row['NAME'] ."</a></td>";
            echo "<td>". $row['ADDRESS'] ."</td>";
            echo "<td>".$row['SALARY'] ."</td>";
            echo "<td><button>EDIT</td></button></td>";
            echo "<td><button>DELETE</td></button></td>";
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
