<?php
//To get the count of pieces of legeslations in a folder that contain all legeslationsof a catagary 
include("db.php");

$path='C:/Users/User/Desktop/Rights';
//C:/Users/User/Desktop/Crime
//C:/Users/User/Desktop/Rights
//C:/Users/User/Desktop/Family
//C:/Users/User/Desktop/Employment

$folder_names = scandir($path);

$legpaths = array();
for ($x = 2; $x < sizeof($folder_names); $x++) {
	$legpath=$path.'/'.$folder_names[$x];
	array_push($legpaths,$legpath);	
}

$count=0;
foreach ($legpaths as $leg){
	$file_names = scandir($leg);
	unset($file_names[0]);
	unset($file_names[1]);
		foreach ($file_names as $file_name){
			$count++;	
		}	
}
echo "Number of pieces in ".$path." : ".$count;



?>
	