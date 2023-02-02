<?php
$connection=mysqli_connect('localhost','root','');

mysqli_select_db($connection,'cat16');

$query='select * from emp';
$result=mysqli_query($connection,$query);

if(mysqli_num_rows($result)>0)
{
echo'<table width=100 cellpadding=10 cellspacing=0 border=1>';
echo'<tr><td>ID</td><td>Name</td></tr>';
while($row=mysqli_fetch_row($result))
{
echo'<tr>';
echo'<td>'.$row[0],'</td>';
echo'<td>'.$row[1],'</td>';
echo'</tr>';
}
echo '</table>';
}
else
{
echo"No rows found";
}
