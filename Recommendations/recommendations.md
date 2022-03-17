# Recommendations around the workshop topics

## Python-Library-Recommendations
Python - Standard Libraries - Third Party Libraries
- [Python Standard Libraries](https://docs.python.org/3/library/)
  * [pathlib](https://docs.python.org/3/library/pathlib.html)
- [Selenium](https://pypi.org/project/selenium/)
- [Seaborn](https://seaborn.pydata.org/)
- [bokeh](https://docs.bokeh.org/en/latest/index.html)
- [black](https://pypi.org/project/black/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [NLTK](https://www.nltk.org/)
- [Django](https://www.djangoproject.com/)
- [flask](https://www.fullstackpython.com/flask.html)
- [Camelot](https://camelot-py.readthedocs.io/en/master/)

## reading/listening/vision recommendations
### reading

- [Automate Boring stuff with Python](https://automatetheboringstuff.com/)
- [Fluent Python](https://www.oreilly.com/library/view/fluent-python/9781491946237/) (advanced)
- [Learning_python](oreilly.com/library/view/learning-python-5th/9781449355722/)
- [PEP-0008](https://www.python.org/dev/peps/pep-0008/)
- [pandas_cheat_sheet](https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf)
- [python_cheat_sheet](https://github.com/ehmatthes/pcc/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc_all.pdf)
- [The 35 Words You Need to Python](https://yawpitchroll.com/posts/the-35-words-you-need-to-python/)
- [Python built-ins worth learning](https://treyhunner.com/2019/05/python-builtins-worth-learning/)
- book [Git from the Bottom Up](https://jwiegley.github.io/git-from-the-bottom-up/)
- book [Pro Git](https://git-scm.com/book/en/v2)
- [GitHub Pages](https://pages.github.com/)
- [Oh Shit, Git?!?](https://ohshitgit.com/de)
- [Definitly not lazy Comic](https://www.commitstrip.com/en/2017/02/28/definitely-not-lazy/)
- Video German 09:09 min [Die Entstehung von Unix](https://www.youtube.com/watch?v=OdJFi8fTsxg)
- Video German 5:39 min [5 Linux Distributionen für Anfänger](https://www.youtube.com/watch?v=5UD3jZefBsk)
- Video Multilingual 01:25:04 min [Revolution OS - 2001](https://www.youtube.com/watch?v=Eluzi70O-P4)
- Video German 51:12 min [Arte Doku: Codename Linux 2001](https://www.youtube.com/watch?v=SzKEi5AHZf4)

### podcasts
- [Command Line Heros](https://www.redhat.com/en/command-line-heroes) (en) - "Command Line Heroes tells the epic true tales of how developers, programmers, hackers, geeks, and open source rebels are revolutionizing the technology landscape." Z. B.
  * [Python's Tale](https://www.redhat.com/en/command-line-heroes/season-3/pythons-tale)
  * [Heroes in a Bash Shell](https://www.redhat.com/en/command-line-heroes/season-3/heroes-in-a-bash-shell)
- [Talk Python to me](https://talkpython.fm/) (en)
- [PythonBytes](https://pythonbytes.fm/) (en)


### Requirements for a Good Editor/IDE
- Save and Reload Source Code 
    - An IDE or editor must save your work and reopen everything later, in the same state it was in when you left, thus saving time for development.
- Execution from Within the Environment
    - It should have a built-in compiler to execute your code. If you are not executing it in the same software, then probably it is a text editor. 
- Debugging Support
    - The debugger in most IDEs provides stepping through your code and applying breakpoints for the code's partial execution. 
- Syntax Highlighting
    - Being able to spot keywords, variables quickly, and symbols in your code make reading and understanding code much easier.
- Automatic Code Formatting
    - This is an interesting feature; the code indents itself as the developer uses loops, functions, or any other block code.

### text editors/IDEs (integrated development environment)
1) [PyCharm](https://www.jetbrains.com/pycharm/)
2) [Spyder](https://www.spyder-ide.org/)
3) [Atom](https://atom.io/)
4) [Emacs](https://www.gnu.org/software/emacs/)
5) [Geany](https://www.geany.org/)
6) [Visual Studio Code](https://code.visualstudio.com/) / [VSCodium](https://github.com/VSCodium/vscodium) (binary releases of VS Code without MS branding/telemetry/licensing )
7) [Notepad ++](https://notepad-plus-plus.org/)
8) ... [viele mehr](https://en.wikipedia.org/wiki/List_of_text_editors)

### videos
- [PyCon](https://www.youtube.com/results?search_query=pycon&search_type=) - Talks, Tutorial und vieles mehr von den PyCon-Konferenzen

## What to do after the LC-workshop
 - Go through the lessons and try to reproduce them alone
  - [Rosalind](http://rosalind.info/problems/locations/)
 - [Intro_to_computer_science](https://www.udacity.com/course/introduction-to-python--ud1110)
 - Find small tasks you solve on a daily bases and try to solve them using the computation skills you have learned
 - [Participate to the hacky-hour](https://hackyhour.github.io/Cologne/)
 
## tips and tricks

- [GitHub Solution for email privacy issue](https://help.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address)

### How to run python in the Git Bash on Windows
```
$ winpty <path-to-python-installation-dir>/python.exe
```

### Workaround if Anaconda doesn't work
Go to https://mybinder.org/. Put the URL
https://github.com/foerstner-lab/Bits_and_pieces_for_the_carpentries_workshops
after "GitHub repository name or URL" and write
"empty_jupyter_notebook_for_binder.ipynb" after "Path to a notebook
file".

Click on "launch" .

