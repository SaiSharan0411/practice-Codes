<html>
<body>
<pre>
<?php
$connect=mysqli_connect('localhost','root','') or die("Unable to connect");
mysqli_select_db($connect,'cat16') or die("Unable to select database");
$query='select*from emp';
$result=mysqli_query($connect,$query) or die('error in query:$query'.mysqli_error());
echo "</pre>";
if(mysqli_num_rows($result)>0)
{
echo "<table width=30% cellpadding=6 celspacing=0 border=2>";
echo "<tr>
      <td><b>Name</b></td>
      <td><b>Id</b></td>
      <td><b>Doj</b></td>
      </tr>";
while($row=mysqli_fetch_row($result))
{
echo "<tr>";
echo "<td>$row[0]</td>";
echo "<td>$row[1]</td>";
echo "<td>$row[2]</td>";
echo "</tr>";
}
echo "</table>";
}
else
{ 
echo "No rows found";
}
mysqli_free_result($result);
mysqli_close($connectION);
?>
</body>
</html>
