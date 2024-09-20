<?php
error_reporting(0);
require_once 'db.php';
global $conn;

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['match']) && isset($_POST['replace'])) {
        $match = $_POST['match'];
        $replace = $_POST['replace'];

        if (strlen($match) > 50 || strlen($replace) > 50) {
            echo "<script>alert('Value(s) too long');</script>";
            return;
        }

        if (@preg_match($match, null) === false) { // Check if the regex is properly delimited
            $match = '/' . preg_quote($match, '/') . '/';
        }

        $stmt = $conn->prepare("INSERT INTO settings (k, v) VALUES (?, ?) ON DUPLICATE KEY UPDATE v = ?");
        $k1 = 'match';
        $stmt->bind_param("sss", $k1, $match, $match);
        $stmt->execute();
        $k2 = 'replace';
        $stmt->bind_param("sss", $k2, $replace, $replace);
        $stmt->execute();
    } else {
        echo "<script>alert('Missing parameters');</script>";
    }
} else {
    echo "<script>alert('Method not allowed');</script>";
}
echo "<script>window.location.href = 'admin.php';</script>";