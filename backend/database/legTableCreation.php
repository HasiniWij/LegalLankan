<?php

//Insertion of records into the legislation table of the database, which includes the legislationIndex, legisaltionName and category.

include("db.php");

$path='C:\Users\User\Desktop\Family';
//C:\Users\User\Desktop\Crime
//C:\Users\User\Desktop\Rights
//C:\Users\User\Desktop\Family
//C:\Users\User\Desktop\Employment
$a = scandir($path);
for ($x = 4; $x < sizeof($a); $x++) {
	$temp=$a[$x];
	echo $temp;
	$SQL="INSERT INTO legislation(legislationName, categoryIndex) VALUES ('$temp','FA')";
	$exeSQL=mysqli_query($conn, $SQL) or die (mysqli_error($conn));
	//echo $a[$x];
	echo "<br>";
}


?>
