<html>
<body>
<?php
SESSION_START();
echo 'Login name: '.$_SESSION['un'].'<br>';
echo 'Password: '.$_SESSION['pwd'];
SESSION_DESTROY();
?>
</body>
</html>                         