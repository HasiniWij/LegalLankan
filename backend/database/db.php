<?php
$dbhost = 'localhost';
$dbuser = 'root';
$dbpass = '';
$dbname = 'sdgp';

$conn = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname);

if (!$conn)
{
 die('Could not connect: ' . mysqli_error($conn));
}

mysqli_select_db($conn, $dbname);
?>