<?php
$logFile = 'log.txt';

$ip = $_SERVER['REMOTE_ADDR'];
$time = date('Y-m-d H:i:s');
$logEntry = "IP: $ip, Время: $time\n";
file_put_contents($logFile, $logEntry, FILE_APPEND);
?>