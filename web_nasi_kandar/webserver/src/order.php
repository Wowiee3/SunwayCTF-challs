<?php
error_reporting(0);
session_start(); 

if (!isset($_SESSION['logged'])) {
    header("Location: index.php");
    exit();
}
?>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sunway Nasi Kandar</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            width: 300px;
            text-align: center;
        }

        h1 {
            color: #333;
        }

        form {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .form-group {
            margin: 8px 0;
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .form-group label {
            flex: 1;
            text-align: left;
        }

        .form-group input {
            width: 50px;
            padding: 5px;
            border-radius: 5px;
            border: 1px solid #ccc;
            text-align: center;
        }

        .form-group input[type="text"] {
            width: calc(100% - 60px);
        }

        button {
            width: 100%;
            padding: 10px;
            margin: 20px 0;
            border-radius: 5px;
            border: none;
            background-color: #007bff;
            color: #fff;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        .disclaimer {
            font-size: 0.8em;
            color: #666;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Online Order Sunway's Nasi Kandar</h1>
        <form action="price.php" method="POST">
            <div class="form-group">
                <label for="sotong">Sotong: </label>
                <input type="number" id="sotong" name="sotong" min="0" value="0">
            </div>
            <div class="form-group">
                <label for="ayam_goreng">Ayam Goreng: </label>
                <input type="number" id="ayam_goreng" name="ayam_goreng" min="0" value="0">
            </div>
            <div class="form-group">
                <label for="kobis">Kobis: </label>
                <input type="number" id="kobis" name="kobis" min="0" value="0">
            </div>
            <div class="form-group">
                <label for="ikan">Ikan: </label>
                <input type="number" id="ikan" name="ikan" min="0" value="0">
            </div>
            <div class="form-group">
                <label for="telur_masin">Telur Masin:</label>
                <input type="number" id="telur_masin" name="telur_masin" min="0" value="0">
            </div>
            <div class="form-group">
                <label for="price">Price:</label>
                <input type="text" id="price" name="price">
            </div>
            <button type="submit">Submit</button>
        </form>
        <div class="disclaimer">
            * If you guess the price correctly, you get a flag!
        </div>
    </div>
</body>
</html>
