<?php
error_reporting(0);
require_once 'db.php';
global $conn;

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (!empty($_POST['name']) && !empty($_POST['message'])) {
        $name = $_POST['name'];
        $message = $_POST['message'];

        if (strlen($name) > 500 || strlen($message) > 50) {
            echo json_encode(['status' => 400, 'msg' => 'Content too long']);
            return;
        }

        $stmt = $conn->prepare("INSERT INTO messages (timestamp, name, message) VALUES (?, ?, ?)");
        $timestamp = time();
        $stmt->bind_param("iss", $timestamp, $name, $message);
        $stmt->execute();
    } else {
        echo "<script>alert('Missing parameters');</script>";
    }
} else {
    echo "<script>alert('Method not allowed');</script>";
}
echo "<script>window.location.href = 'index.php';</script>";