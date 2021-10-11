# !/bin/bash/

### syntax rules
1. when defining a variable whitespaces must be eliminated
2. include the shell in all the scripts at the beginning of the file (#!/bin/bash)

3. $var is used to print the value of the variable
4.  $(command) is used to execute a command
5.  $((expression)) this format is used to perform math operations and it returns the value at the end
6.  ((expression)) performs math operation but doesn't return the value

<br>

```bash
# echo 
read -p "Enter your name " name
echo "hello world $name"
read -p "Enter your first and last name " first_name last_name
echo "Grettings to $first_name $last_name"
# -sp flag is used to hide user input
read -sp "Enter secret code " code
echo $code
echo "this text will be in a file" > file1

# array
  Fruits=('Apple' 'Banana' 'Oranges')

  Fruits[0]="Apple"
  Fruits[1]="Banana"
  Fruits[2]="Oranges"

  # array operations
  Fruits=("${Fruits[@]}" "Watermelon")    # Push
  Fruits+=('Watermelon')                  # Also Push
  unset Fruits[2]                         # Remove one item
  Fruits=("${Fruits[@]}")                 # Duplicate
  Fruits=("${Fruits[@]}" "${Veggies[@]}") # Concatenate
  lines=(`cat "logfile"`)                 # Read from file

  # working with arryas
  echo ${Fruits[0]}           # Element #0
  echo ${Fruits[-1]}          # Last element
  echo ${Fruits[@]}           # All elements, space-separated
  echo ${#Fruits[@]}          # Number of elements
  echo ${#Fruits}             # String length of the 1st element
  echo ${#Fruits[3]}          # String length of the Nth element
  echo ${Fruits[@]:3:2}       # Range (from position 3, length 2)
  echo ${!Fruits[@]}          # Keys of all elements, space-separated

  # iteration
  for i in "${arrayName[@]}"; do
    echo $i
  done

# dictionary
  # Declares sound as a Dictionary object (aka associative array).
  declare -A sounds

  sounds[dog]="bark"
  sounds[cow]="moo"
  sounds[bird]="tweet"
  sounds[wolf]="howl"

  # working with dictionaries
  echo ${sounds[dog]} # Dog's sound
  echo ${sounds[@]}   # All values
  echo ${!sounds[@]}  # All keys
  echo ${#sounds[@]}  # Number of elements
  unset sounds[dog]   # Delete dog

  # iteration over values
  for val in "${sounds[@]}"; do
    echo $val
  done

  # iteration over keys
  for key in "${!sounds[@]}"; do
    echo $key
  done

# math
num1=1
num2=1
sum=$((num1 + num2))
echo $sum
sum=$(python3 -c "print($num1+$num2)")
echo "sum is $sum"

# let keyword
rand=5
let rand+=1
echo $rand

# if statements
if (( num1 < num2 || num1 == num2 ))
then
    echo "$num1 is greater"
else
    echo "$num2 is greater"
fi

# other method of if (ge - >= , le - <= , gt - > , lt - < , eq - == , ne - !=)
age=18
if [ $age -ge 18 ]
then
    echo "you can drive"
elif [ $age -lt 18 ] 
then
    echo "you cant drive"
fi

# one more method of the above
age=18
if [ $age -ge 18 ]; then
    echo "you can drive"
elif [ $age -lt 18 ]; then
    echo "you cant drive"
fi


# nested execution
echo $(( myvar = 7 + $(( vartwo = 4 + 4 )) ))

# print multiple lines ('END' word can be replaced with anything)
cat<< END
this is a big paragraph
and it can be in multiple 
lines like this
END

# functions 
myfunction() {
    echo "hello $1 $2"
}

myfunction "John" "maclarne"

# return values
# echo in functions doesn't print the value but acts like 'return' similar to other progamming language 
myfunc() {
    local myresult='some value'
    echo $myresult              
}
result="$(myfunc)"

# when a function is called within a variable var=$(funcation_name) , then all the multiple echo statements made inside the function would accumulate in "var"
function1(){
    echo "Start of the func"
    local num1=$1
    local num2=$2
    local sum=$(( num1 + num2 ))
    echo "Sum total inside func $sum"
    echo "end of the func"
}

echo "Before the func "
var=$(function1 10 11)
echo "after the func"
echo "Variable 'var' being called where output of function1 resides"
echo "$var"

# function being called without using any varible to store the output
function2(){
    echo "Start of the func"
    local num1=$1
    local num2=$2
    local sum=$(( num1 + num2 ))
    echo "Sum total inside func $sum"
    echo "end of the func"
}

echo "Before the func "
function2 10 11
echo "after the func"

#global and local variables
var_change () {
    local var1='local 1'
    echo Inside function: var1 is $var1 : var2 is $var2
    var1='changed again'
    var2='2 changed again'
    
}
var1='global 1'
var2='global 2'
echo Before function call: var1 is $var1 : var2 is $var2
var_change
echo After function call: var1 is $var1 : var2 is $var2

# string 
str1=""

if [ "$str1"  ]; then
    echo "string is not null"
else
    echo "string is null"
fi

# the -z flag checks whether the string is null
if [ -z $str1  ]; then
    echo "String is null"
else
    echo "String is not null"
fi

# -e flag checks whether a file exists or not
# -f checks whether it is a normal file
# -r checks if it is readable
# -w checks if it is writable
# -x checks if it is executable
# -d checks if it is a directory
# -L is it a symbolic link
# -G is it owned by the group
# -O is it owned by the usedid
file="./file2"

if [ -e $file  ]; then
    echo "$file exists"
else
    echo "$file doesn't exist"
fi

#case 
read -p "Enter your age " age

case $age in
    [0-4])
        echo "to young for school"
        ;;
    [5])
        echo "go to kindergarten"
        ;;
    [6-9]|1[0-8])                         #checks from 6 to 18
        grade=$((age-5))
        echo "go to grade $grade"
        ;;                                #default statment
    *)           
        echo "too old for school"
esac

# example function with switch case
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.tar.xz)    tar xJf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}


# while loop
while true; do
  echo "this is an infinite loop"
done

# reading lines 
cat file.txt | while read line; do
  echo $line
done

# C-like for loop
for ((i = 0 ; i < 100 ; i++)); do
  echo $i
done

# for loop using range
for i in {1..5}; do
  echo "Welcome $i"
done

```

<br>
