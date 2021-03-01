<?php

include("db.php");

$path='C:/Users/User/Desktop/Family';
//C:/Users/User/Desktop/Crime
//C:/Users/User/Desktop/Rights
//x =4 in family
//C:/Users/User/Desktop/Family
//C:/Users/User/Desktop/Employment

$folder_names = scandir($path);

$legpaths = array();
$count=0;
for ($x = 2; $x < sizeof($folder_names); $x++) {
	$leg_path=$path.'/'.$folder_names[$x];
	$file_names = scandir($leg_path);
	unset($file_names[0]);
	unset($file_names[1]);
		foreach ($file_names as $file_name){
			
			$count++;
			
			//removing the .txt file extention to get the file name 
			$title=substr($file_name,0,-4);
			
			//read content from file 
			$file_path=$leg_path."/".$file_name;
			$myfile = fopen($file_path, "r") or die("Unable to open file!");
			$content= fgets($myfile);
			
			//getting the legislationIndex of a given piece
			$Leg_SQL="SELECT legislationIndex FROM legislation WHERE legislationName = '$folder_names[$x]'";
			$exe_leg_SQL=mysqli_query($conn, $Leg_SQL) or die (mysqli_error($conn));
			$array_leg=mysqli_fetch_array($exe_leg_SQL);
			$legIndex=$array_leg['legislationIndex'];
			
			
			//if the content contains both " and ' echos the deatils of the piece 
			if( preg_match('/[\"]/',  $content)&& preg_match('/[\']/',  $content)){
				echo "<br>";
				echo $title;
				echo "<br>";
				echo $folder_names[$x];
				echo "<br>";
				
				continue;
			}
			
			//if the content contains " the mysql statment string should be enclosed with '
			elseif( preg_match('/[\"]/',  $content)){
				$SQL="INSERT INTO piece(pieceTitle, content,legislationIndex) VALUES ('".$title."','".$content."','".(int)$legIndex."');";
				$exeSQL=mysqli_query($conn, $SQL) or die (mysqli_error($conn));	
				continue;
			}
			//insert content
			
			$SQL='INSERT INTO piece(pieceTitle, content,legislationIndex) VALUES ("'.$title.'","'.$content.'","'.(int)$legIndex.'");'; 
			$exeSQL=mysqli_query($conn, $SQL) or die (mysqli_error($conn));		
		}
}
echo "<br>";
echo $count;
			
?>
	