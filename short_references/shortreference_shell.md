# Shell - short reference

## Syntax
```$ program [-options] [arguments]```

**options:**

* options change the behaviour of programs
* start with a minus (-)

**arguments:**

* provide information to the program that can be further processed by it

## Commands
| command                        | action                                           |
|--------------------------------|--------------------------------------------------|
| ```pwd```                          | shows the path of the current directory      |
| ```ls```                           | lists all files and folders of a give path   |
| ```cd <directory>```               | go to target directory                       |
| ```touch <filename>```             | creates or updates a file                    |
| ```head <filename>```              | shows the first ten lines of a file          |
| ```tail <filename>```              | shows the last ten last files of a file      |
| ```mv <file1> <file2>```           | moves file1 and saves it as file2            |
| ```cp <file1> <file2>```           | copies files                                 |
| ```rm <filename>```                | removes files                                |
| ```echo "Text"```                  | displays a line of text                      |
| ```wc <filename>```                | counts lines, words, and characters of files |
| ```mkdir <foldername>```           | creates a folder                             |
| ```cat <filename>```               | displays the content of files                |

### Help and manuals

| command            | action                 |
|-------------------|------------------------|
| ```<command> --help``` | shows help of command |
| ```<command> -h```     | shows help of command |
|  ```man <command>```   | shows manual of command  |

## Program redirection

The output of programs does not always have to be displayed in the Shell, but can be redirected to another program

| operator | action                                        | example       |
|----------|-----------------------------------------------|----------------|
| ```>```  | redirect the output to a file            | ```ls > file.txt``` |
| <code>&#124;</code>| redirect the output to another program | <code> wc -l *.tsv &#124; sort -n </code>|

## Shortcuts
| shortcut            | action                                   |
|-------------------|:-----------------------------------------|
| TAB               | autocompletion                    |
| arrow up   | gets to the previous command            |
| ctrl + a          | cursor jumps to start of line          |
| ctrl + e          | cursor jumps to end of line          |
| ctrl + l          | clears the shell window      |
| ctrl + c          | cancels input or running process         |
| ctrl + k          | deletes the input after the cursor       |
| ctrl + u          | deletes the input in front of the cursor        |
| ctrl + y          | pastes the clipboard                  |

## for-loops

```
$ for NAME in "Jo" "Meg" "Beth" "Amy"
> do
>    echo $NAME
> done
```


([CC-BY](https://creativecommons.org/licenses/by/3.0/de/) Felix Langer und Konrad Förstner)

(Translated by Till Sauerwein)