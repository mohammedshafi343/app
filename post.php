<!-- form_handler.php -->
<!DOCTYPE html>
<html>
<body>

<form method="POST" action="<?php echo $_SERVER['PHP_SELF']; ?>">
  Name: <input type="text" name="name"><br>
  Email: <input type="text" name="email"><br>
  <input type="submit" value="Submit">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    
    if (!empty($name) && !empty($email)) {
        echo "Hello, $name. Your email is $email.";
    } else {
        echo "Please fill out both fields.";
    }
}
?>

</body>
</html>
