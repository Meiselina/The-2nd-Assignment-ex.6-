In [1]: x = "There are %d types of people." % 10

In [2]: x=

  File "<stdin>", line 1
    x=
     ^
SyntaxError: invalid syntax


In [3]: binary = "binary"
... do_not = "don't"
... y = "Those who know %s and those who %s." % (binary, do_not)

In [4]: print (x)
There are 10 types of people.

In [5]: print (y)
Those who know binary and those who don't.

In [6]: print ("I said: %r. " % x)
I said: 'There are 10 types of people.'. 

In [7]: print ("I also said: '%s'." % y")

  File "<stdin>", line 1
    print ("I also said: '%s'." % y")
                                    ^
SyntaxError: EOL while scanning string literal


In [8]: In [7]: print ("I also said: '%s'." % y"))

  File "<stdin>", line 1
    print ("I also said: '%s'." % y"))
                                     ^
SyntaxError: EOL while scanning string literal


In [9]: In [7]: print ("I also said: '%s'." % y)
I also said: 'Those who know binary and those who don't.'.

In [10]: hilarious = False
... joke_evaluation = "Isn't that joke so funny?! %r"

In [11]: print joke_evaluation % hilarious
... 
... w = "This is the left side of..."
... e = "a string with a right side."
... 
... print (w + e)

  File "<stdin>", line 1
    print joke_evaluation % hilarious
                        ^
SyntaxError: Missing parentheses in call to 'print'


In [12]: print ("w + e")
w + e

In [13]: hilarious = False
... joke_evaluation = "Isn't that joke so funny?! %r"
... 
... print (w + e)

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    print (w + e)
NameError: name 'w' is not defined


In [14]: hilarious = False

In [15]: joke_evaluation = "Isn't that joke so funny?! %r"

In [16]: print (w + e)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print (w + e)
NameError: name 'w' is not defined


In [17]: print (joke_evaluation % hilarious)
Isn't that joke so funny?! False

In [18]: w = "This is the left side of..."

In [19]: e = "a string with a right side."

In [20]: print (w + e)
This is the left side of...a string with a right side.