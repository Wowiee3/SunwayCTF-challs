<?php
error_reporting(0);

require_once "db.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST['username']) && isset($_POST['password'])) {

        $username = $_POST['username'];
        $password = $_POST['password'];

        if ($username === "admin"){
            echo "Admin log in is disabled!";
            die();
        }

        $sql = "SELECT id, username, password FROM users WHERE username = ? AND password = ?";
        
        if ($stmt = mysqli_prepare($db_connection, $sql)) {

            mysqli_stmt_bind_param($stmt, "ss", $username, $password);

            mysqli_stmt_execute($stmt);

            mysqli_stmt_store_result($stmt);

            if (mysqli_stmt_num_rows($stmt) === 1) {
                session_start();
                $_SESSION['logged'] = True;
                header("Location: order.php");
                exit();
            } else {
                echo "Invalid credentials";
                exit();
            }

            mysqli_stmt_free_result($stmt);
            mysqli_stmt_close($stmt);
        } else {
            echo "Error preparing statement: " . mysqli_error($db_connection);
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Login</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f0f0f0;
        }

        .container {
            max-width: 300px;
            width: 100%;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        }

        label {
            display: block;
            margin-bottom: 10px;
            font-weight: bold;
        }

        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 3px;
            box-sizing: border-box;
        }

        input[type="submit"] {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 3px;
            background-color: #007bff;
            color: #fff;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>

</head>
<body>
    <form action="index.php" method="POST">
        <h1>Admin Login</h1>
        <label for="username">Username:</label>
        <input type="text" id="username" name="username">
        <label for="password">Password:</label>
        <input type="password" id="password" name="password">
        <input type="submit" value="Login">
    </form> 
</body>
</html>