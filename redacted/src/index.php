<?php error_reporting(0); ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sunway Confession</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
<nav class="navbar navbar-expand-sm navbar-dark">
    <a class="navbar-brand ml-2 font-weight-bold" href="#">Sunway Confession</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor02"
            aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="end">
        <div class="collapse navbar-collapse" id="navbarColor02">
            <ul class="navbar-nav">
                <li class="nav-item"><a class="nav-link" href="admin.php">Admin</a></li>
            </ul>
        </div>
    </div>
</nav>

<section>
    <div class="container">
        <div class="row">
            <div class="col-sm-5 col-md-6 col-12 py-4">
                <h1>Comments</h1>
                <?php
                require_once "db.php";
                global $conn;
                date_default_timezone_set('Asia/Kuala_Lumpur');

                $result = $conn->query("SELECT v FROM settings WHERE k = 'match' OR k = 'replace' ORDER BY k");
                $match = $result->fetch_assoc()['v'];
                $replace = $result->fetch_assoc()['v'];

                $result1 = $conn->query("SELECT * FROM messages ORDER BY timestamp DESC");
                while ($post = $result1->fetch_assoc()) {
                    ?>
                    <div class="post text-justify darker mt-4 float-right">
                        <h4><?php echo htmlspecialchars(preg_replace($match, $replace, $post["name"])) ?></h4>
                        <span> - <?php echo htmlspecialchars(date('j F Y, H:i:s', $post["timestamp"])) ?></span>
                        <br>
                        <p class="pt-1"><?php echo htmlspecialchars(preg_replace($match, $replace, $post["message"])) ?></p>
                    </div>
                <?php } ?>
            </div>
            <div class="col-lg-4 col-md-5 col-sm-4 offset-md-1 offset-sm-1 col-12 mt-4">
                <form method="POST" action="message.php">
                    <div class="form-group">
                        <h4>Leave your message</h4>

                        <label for="name" class="pt-3">Name</label>
                        <input type="text" name="name" id="name" class="form-control">

                        <label for="message" class="pt-3">Message</label>
                        <textarea name="message" id="message" cols="30" rows="5" class="form-control"></textarea>

                        <div class="d-flex justify-content-center pt-4">
                            <button type="submit" id="post" class="btn px-3">POST COMMENT</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</section>
</body>

<style>
    .navbar-nav {
        width: 100%;
    }

    @media (min-width: 568px) {
        .end {
            margin-left: auto;
        }
    }

    @media (max-width: 768px) {
        #post {
            width: 100%;
        }
    }

    #post {
        margin: 10px;
        padding: 2px 6px;
        text-align: center;
        background-color: #ecb21f;
        border-color: #a88734 #9c7e31 #846a29;
        color: black;
        border-width: 1px;
        border-style: solid;
        border-radius: 13px;
        width: 50%;
    }

    body {
        background-color: black;
    }

    #nav-items li a {
        text-decoration: none;
        color: rgb(224, 219, 219);
        background-color: black;
    }

    .darker {
        border: 1px solid #ecb21f;
        background-color: black;
        float: right;
        border-radius: 5px;
        padding-left: 40px;
        padding-right: 30px;
        padding-top: 10px;
    }

    .comment h4, .comment span, .darker h4, .darker span {
        display: inline;
    }

    .comment p, .comment span, .darker p, .darker span {
        color: rgb(184, 183, 183);
    }

    .post {
        width: 100%;
    }

    h1, h4 {
        color: white;
        font-weight: bold;
    }

    label {
        color: rgb(212, 208, 208);
    }

    .form-group input, .form-group textarea {
        background-color: black;
        border: 1px solid rgba(16, 46, 46, 1);
        border-radius: 12px;
    }

    form {
        border: 1px solid rgba(16, 46, 46, 1);
        background-color: rgba(16, 46, 46, 0.973);
        border-radius: 5px;
        padding: 20px;
    }
</style>
</html>