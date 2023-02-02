<html>
<body>
<?php
$current=getdate();
$current_time=$current['hours'].':'.$current['minutes'].':'.$current['seconds'];
$current_date=$current['mday'].':'.$current['mon'].':'.$current['year'];
echo "$current_time<br><br>";
echo "$current_date<br><br>";
$d=mktime(6,25,0,7,18,2008);
echo"today is".date("y/m/d")."<br><br>";
echo"today id".date("y.m.d")."<br><br>";
echo"today id".date("y-m-d")."<br><br>";
echo"today is".date("1")."<br><br>";
echo"today is".date("h:i:sa")."<br><br>";
?>
</body>
</html>