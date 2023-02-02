<html>
<head>
<title> File Handling </title>
</head>
<body>
<?php
echo "<center><h1><b>File Handling</b></h1>";
$a=$_POST["txt1"];
$b=$_POST["txt2"];
$fp=fopen("file1.txt","w")or die("unable to create file");
fwrite($fp,$a);
fclose($fp);
$fp=fopen("file1.txt","r")or die("unable to open file");
$c=filesize("file1.txt");
echo $c;
$d=fread($fp,$c);
echo $d;
fclose($fp);
$fq=fopen("file2.txt","w")or die("unable to create file");
fwrite($fq,$b);
fclose($fq);
$fq=fopen("file2.txt","r")or die("unable to open file");
$f=filesize("file2.txt");
echo $f;
$e=fread($fq,$f);
echo $e;
fclose($fq);
?>
</body>
</html>
