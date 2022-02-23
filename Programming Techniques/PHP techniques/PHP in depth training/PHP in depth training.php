// This document is going to be samples of many common PHP sample commands and techniques
// This document is intended to help us structure proper PHP commands and to perform 
// Actions and Queries on PHP Databasses. 

// The Following are sample code Php structures

// The following are single string commnets in php files or documents

<?php
  // This is a single-line comment
  
  # You can also make single-line comments like this
?>

// The following are some sample commands to print statements in PHP

<?php
ECHO "Hello!<br>";
echo "Welcome to Developer News<br>";
EcHo "Enjoy all of the ad-free articles<br>";
?>

// Following sample code shows how to call variables using PHP

<?php
$name = "Quincy";
echo "Hi! My name is " . $name . "<br>";
echo "Hi! My name is " . $NAME . "<br>";
echo "Hi! My name is " . $NaMe . "<br>";
?>

<?php
// Assign the value "Hello!" to the variable "greeting"
$greeting = "Hello!";
// Assign the value 8 to the variable "month"
$month = 8;
// Assign the value 2019 to the variable "year"
$year = 2019;
?>

// Working with null data types in php 

<?php
// Assign the value "Hello!" to greeting
$greeting = "Hello!";

// Empty the value greeting by setting it to null
$greeting = null;
?>

// Working with Classes and Objects in Php

<?php
class Car {
    function Car() {
        $this->model = "Tesla";
    }
}

// create an object
$Lightning = new Car();

// show object properties
echo $Lightning->model;
?>

// Notice how we structure the PHP code which itself can live within the syntax of other code such as html_entity_decode
// This allows for code to live and perform instructions as it runs within html code files 

// Using PHP resources 

// A resource is a special variable, holding a reference to an external resource. Resources are created and used by special functions.

<?php
// prints: mysql link
$c = mysql_connect();
echo get_resource_type($c) . "\n";

// prints: stream
$fp = fopen("foo", "w");
echo get_resource_type($fp) . "\n";

// prints: domxml document
$doc = new_xmldoc("1.0");
echo get_resource_type($doc->doc) . "\n";

// working with strings inside of PHP 

// Single Quotes Simple strings can be created using single quotes.

$name = 'Joe';

$last_name = 'O\'Brian';

$name = "Joe";

// Finding the Length of a string: 

<?php
echo strlen("Developer News"); // outputs 14
?>

// Finding the number of words in a string 

<?php
echo str_word_count("Developer News"); // outputs 2
?>

// Reverse a string using strrev function

<?php
echo strrev("Developer News"); // outputs sweN repoleveD
?>

// Searching for a text inside of a string 

<?php
echo strpos("Developer News", "News"); // outputs 10
?>

// Replace text within a string: 

<?php
echo str_replace("freeCodeCamp", "Developer", "freeCodeCamp News"); // outputs Developer News
?>

// Using Constants in PHP

// Constants are a type of variable in PHP. The define() function to set a vraible takes three arguments
// They kename they keys value and a boolean which determines whether the key is case sensitive. 

<?php
define("freeCodeCamp", "Learn to code and help nonprofits", false);
echo freeCodeCamp;
>?

// Output: Learn to code and help nonprofits

// Also when creating classes you can declare your own constants: 

class Human {
    const TYPE_MALE = 'm';
    const TYPE_FEMALE = 'f';
    const TYPE_UNKNOWN = 'u'; // When user didn't select his gender
    
    .............
  }

// Note: If you want to use those constants inside the Human class, 
// you can refer them as self::CONSTANT_NAME. If you want to use them outside the class, 
// you need to refer them as Human::CONSTANT_NAME.

// PHP Operators 

// PHP contains all the normal operators one would expect to find in a programming language.

// New to Php 7.0X is the exciting new spaceship operator (<=>) 

<?php

echo 1 <=> 1; // 0
echo 1 <=> 2; // -1
echo 2 <=> 1; // 1

>?

// If statements: 

<?php

  if (condition) {
    statement1;
    statement2;
  }

// Note you can nest as many if statements as you would like. 

<?php

  if (condition) {
    statement1;
    statement2;
  } else {
    statement3;
    statement4;
  }

// elseif Statement: 

    <?php

    if (condition1) {
      statement1;
      statement2;
    } elseif (condition2) {
      statement3;
      statement4;
    } else {
      statement5;
    }

// Nested If/else Statement

<?php

  if (condition1) {
      if (condition2) {
        statement1;
        statement2;
      } else {
        statement3;
        statement4;
      }
  } else {
      if (condition3) {
        statement5;
        statement6;
      } else {
        statement7;
        statement8;
      }
  }




