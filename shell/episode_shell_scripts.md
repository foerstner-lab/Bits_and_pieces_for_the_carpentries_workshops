---
Title: "Writing scripts in the shell".
Teaching: 15
Exercises: 
Questions:
- "How can I write scripts from the command line with a text editor?
- "How can I run the scripts from the shell?"
Targets:
- "Work with Nano from the command line".
- "Run sh-files from the command line"
- "Comment out lines".

Key points:
- "The shell can be used to create scripts to automate and reproduce processes".
---
## Writing a shell script in nano

Now we get to know a possibility for reproducibility. Once again, with little effort we can 
work with plain text files.
The shell script is also nothing else but such a plain text file, in which we can define commands 
and then have them executed.

For this we need a text editor. You may also know editors like Notepad or 
Notepad ++. If you work a lot with such things, you should get a powerful
Select text editor. We also have a list of text editors in our Pad.

We will now use "nano", a relatively small editor, but good enough for what we want to do now 
and also with all of us in the Bash.

~~~
$ nano my_bash_script.sh
~~~

We take the term "nano" and provide it with an argument that defines my new file. With Enter 
we then call up this file in the nano text editor. With the extension **sh** we define that it is 
is a shell script.

In Nano we can now write commands

~~~
echo "hello world"
~~~

To save the change press <kbd>Ctrl</kbd> + <kbd>o</kbd>. Nano asks us if we want to keep the file name and 
we confirm with <kbd>Enter</kbd>.

We can now leave the editor again with <kbd>Ctrl</kbd> <kbd>x</kbd>.  

Now we can execute our script.

~~~
$ bash my_bash_script.sh
~~~
{: .bash}

As output our echo command is shown in the bottom line.

~~~
$ hello world
~~~
{: .output}

Congratulations. We have programmed the first time!

Here's what we do. Let's go back to our file. We can get the command back by pressing the up arrow key.

~~~
$ nano my_bash_script.sh
~~~

## Using comments

Ideally, we describe our scripts so well that we can still understand them at a later date. Or even another person, 
who's seeing the orders for the first time. To do this we can add comments to our code with a prefix <kbd>#</kbd>.  

~~~
# This is my script to greet the world
echo "hello world"
~~~

The hashtag tells the shell to ignore this line during code execution. Otherwise we would get an error message, 
because the Bash will say, "I don't understand this order."

## For Loops in shell scripts

Again, we can include our for-loop.

~~~
# This is my script to greet the world
echo "hello world"

for FILE in *txt
do
    echo $FILE
    head -n 2 $FILE
    tail -n 2 $FILE
done
~~~

We save our file again. If we execute it now, the first and last two lines 
of all txt files in our shell-lesson folder.

~~~
hello world
829-0.txt
The Project Gutenberg eBook, Gulliver's Travels, by Jonathan Swift

Archive Foundation, how to help produce our new eBooks, and how to
subscribe to our email newsletter to hear about new eBooks.

33504-0.txt
The Project Gutenberg EBook of Opticks, by Isaac Newton

Archive Foundation, how to help produce our new eBooks, and how to
subscribe to our email newsletter to hear about new eBooks.

pg514.txt
The Project Gutenberg EBook of Little Women, by Louisa May Alcott

Archive Foundation, how to help produce our new eBooks, and how to
subscribe to our email newsletter to hear about new eBooks.
~~~

With this we wrote our shell script. With this we can store processes sustainably and reproducibly.
This could be, for example, the downloading of statistics or the conversion of files. In addition, we also have the 
Possibility to share our processes easily with others.

