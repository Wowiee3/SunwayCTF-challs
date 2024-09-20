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
    <a class="navbar-brand ml-2 font-weight-bold" href="index.php">Sunway Confession</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor02"
            aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="end">
        <div class="collapse navbar-collapse" id="navbarColor02">
            <ul class="navbar-nav">
                <li class="nav-item"><a class="nav-link" href="index.php">Home</a></li>
            </ul>
        </div>
    </div>
</nav>

<section>
    <div class="container">
        <div class="row">
            <div class="col-12 py-4">
                <form method="POST" action="filter.php">
                    <div class="form-group">
                        <h4>Comment Filter Rules</h4>

                        <?php
                        require_once "db.php";
                        global $conn;

                        $result = $conn->query("SELECT v FROM settings WHERE k = 'match' OR k = 'replace' ORDER BY k");
                        $match = $result->fetch_assoc()['v'];
                        $replace = $result->fetch_assoc()['v'];
                        ?>

                        <label for="match" class="pt-3">Match:</label>
                        <input type="text" name="match" id="match" class="form-control"
                               value="<?php echo htmlspecialchars($match) ?>">
                        <p><small>RegEx is supported.</small></p>

                        <label for="replace" class="pt-3">and replace:</label>
                        <input type="text" name="replace" id="replace" class="form-control"
                               value="<?php echo htmlspecialchars($replace) ?>">

                        <div class="d-flex justify-content-center pt-4">
                            <button type="submit" id="post" class="btn px-1">APPLY</button>
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

    #nav-items li a, small {
        text-decoration: none;
        color: rgb(224, 219, 219);
        background-color: black;
    }

    .comment h4, .comment span, .darker h4, .darker span {
        display: inline;
    }

    .comment p, .comment span, .darker p, .darker span {
        color: rgb(184, 183, 183);
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