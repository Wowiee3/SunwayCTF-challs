<?php
$wrong = false;
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $secretcode = $_POST['code'];
    if("361586575" === $secretcode){
        echo "sunctf{rAndom_is_n0t_truly_rand0m}";
        die();
    }
    $wrong = true;

}
?>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flag</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            height: 100vh;
        }
        .container {
            margin-top: 10px;
            max-width: 400px;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        h2 {
            color: #333;
        }
        form {
            max-width: 400px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        label {
            font-weight: bold;
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <form action="./flag.php" method="post">
        <label for="name">Submit Code From codeGen.php</label>
        <br>
        <input type="text" id="code" name="code" required><br><br>
        <input type="submit" value="Submit">
    </form>
    <?php
        if ($wrong){
            echo '<br>';
            echo '<br>';
            echo '<div class="container">';
            echo '<p>Wrong Code! Do not bruteforce, its useless</p>';
            echo '</div>';
        }

    ?>
</body>
</html>
