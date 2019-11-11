# Installationsanleitungen

## Bash

Die Bash ist eine Unix Shell, mit der Sie Befehl aufrufen können und
einfach verschiedene Schritte automatisieren können.

### Windows

- Öffnen Sie
  [https://git-for-windows.github.io/](https://git-for-windows.github.io/)
  in einem Webbrowser.
- Klicken Sie auf Download und wählen die aktuellste Version **Git for
  Windows** aus um diesen herunterzuladen.
- Führen Sie den Installer aus.
- Drücken viermal *Next* ohne etwas zu ändern.
- Wählen Sie *Use the nano editor by default* aus und klicken Sie
  *Next*.
- Behalten Sie die Auswahl *Use Git and optional Unix tools from the
  Command Prompt* und klicken Sie *Next* (dies ist wichtig; sollte Sie
  es vergessen haben wiederholen Sie bitte die Installation).
- Klicken Sie *Next*.
- Behalten Sie die Auswahl *Checkout Windows-style, commit Unix-style
  line endings* und klicken Sie *Next*.
- Behalten Sie die Auswahl *Use Windows' default console window* und
  klicken Sie *Next*.
- Drücken Sie *Install*.
- Drücken Sie *Finish*.

Wenn Ihre Umgebungsvariable "HOME" nicht konfiguriert sind oder Sie
nicht wissen was dies ist:
- Öffnen Sie den Command-Prompt: Dazu öffnen Sie das Start-Menü,
  geben Sie `cmd` ein und drücken Sie *Enter*.
- Geben Sie `setx HOME "%USERPROFILE%"`.
- Drücken Sie *Enter*; Sie sollten `SUCCESS: Specified value was
  saved.` sehen.
- Schließen Sie die Command-Prompt indem Sie `exit` ein und drücken
  Sie *Enter*.

Hiermit wird Bash und Git gemeinsam installiert.

Ein (englisches) Video-Tutorial ist
**[hier](https://www.youtube.com/watch?v=339AEqk9c-8)** zu finden.

### macOS

Bash ist die Standard-Shell von macOS - es ist somit nicht nötig etwas
zu installieren. Sollten Sie eine andere Standard-Shell konfiguiert,
können Sie Bash durch Eingabe von `bash` und Drücken der *Enter*-Taste
aufrufen.

Tipp: Vielleicht möchten Sie das Terminal in ihrem Dock beibehalten um
diese schneller aufrufen können.

### Linux

Bash ist die Standard-Shell der meisten Linux-Distributionen - es ist
somit nicht nötig etwas zu installieren. Sollten Sie eine andere
Standard-Shell konfiguiert haben, können Sie Bash durch Eingabe von
`bash` und Drücken der *Enter*-Taste aufrufen.

## Anaconda (Python + Jupyter Notebook)

Wir werden die Programmiersprache *[Python](https://www.python.org/)*
kennen lernen und nutzen. Diese werden wir unter anderem in *[Jupyter
Notebook](https://jupyter.org/)* machen. Mit
*[Anaconda](https://anaconda.org/)* installieren Sie einerseits
Python, aber auch zahlreichen Werkzeuge u.a. Jupyter Notebook. Jupyter
Notebooks werden im Browser angezeigt. Stellen Sie sicher, dass ihr
Browser damit kompatibel ist
([Link](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html#browser-compatibility)).

### Windows

- Öffnen Sie [https://www.anaconda.com/download/#windows](https://www.anaconda.com/download/#windows) in einem
  Webbrowser.
- Laden den *Anaconda 2019.10 for Windows Installer* für Python
  **3.7** herunter.
- Installieren Sie Anaconda mit allen Standardeinstellungen mit
  Ausnahme der Auswahl die Option *Add Anaconda to my PATH environment
  variable* ausgewählt zu haben.

Ein (englisches) Video-Tutorial ist
**[hier](https://www.youtube.com/watch?v=xxQ0mzZ8UvA)** zu finden.

### macOS

- Öffnen Sie
  [https://www.anaconda.com/download/#macos](https://www.anaconda.com/download/#macos)
  in einem Webbrowser.
- Laden den *Anaconda 2019.10 for macOS Installer* für Python **3.7** herunter.
- Installieren Sie Anaconda mit allen Standardeinstellungen.

Ein (englisches) Video-Tutorial ist
**[hier](https://www.youtube.com/watch?v=TcSAln46u9U)** zu finden.

### Linux

- Öffnen Sie
  [https://www.anaconda.com/download/#linux](https://www.anaconda.com/download/#linux)
  in einem Webbrowser.
- Laden den *Anaconda 2019.10 for Linux Installer* für Python **3.7**
  herunter.
- Öffnen Sie ein Terminal.
- Geben Sie `bash Anaconda3` ein und drücken Sie die *Tab*-Taste um
  den Namen der Datei zu vervollständigen. Der Name der
  heruntergeladenen Datei sollte erscheinen. Sollte das nicht der Fall
  sein, gehen Sie in den Ordner in dem die Datei heruntergeladen
  wurden (z.b. durch `cd Downloads`) und versuchen Sie es noch
  einmal. Drücken Sie die Enter-Taste.
- Sie werden verschieden Fragen gefragt: Geben Sie `yes` ein und
  drücken Sie die *Enter*-Taste um die Lizenz zu bestätigen. Drücken
  Sie dann *Enter* um den Standard-Ort für die Installation von
  Dateien zu bestätigen. Geben Sie `yes` ein und drücken Sie die
  *Enter*-Taste um Anaconda-Tools zu ihre `PATH` hinzuzufügen.
- Schließen Sie das Terminal.

### Git und GitHub

[Git](https://git-scm.com/) ist ein Versions-Verwaltungsprogramm mit
dem man die Veränderung von Dateien nachvoll-ziehen kann. Durch die
Plattform [GitHub](https://github.com/join) kann man sehr einfach
kollaborativ mit git arbeiten. Sollte Sie noch keinen GitHub-Account
haben, richten Sie sich diesen bitter hier ein:
[https://github.com/join](https://github.com/join)

### Windows

Git sollte durch die Installation von *Git for Windows* (s.o)
installiert sein.

### macOS

- Öffnen Sie [http://sourceforge.net/projects/git-osx-installer/files/](http://sourceforge.net/projects/git-osx-installer/files/)
  in einem Webbrowser.
- Für macOS 10.9 und höher laden Sie die aktuellste
  *mavericks*-Version herunter.
- Für ältere Versionen 10.5-10.8 laden Sie die aktuellste
  *snow-leopard*-Version herunter.
- Rufen Sie den Installer auf.

Nach der Installation sollte sich Git durch Eingabe von `git` im
Terminal aufrufen lassen.

Ein (englisches) Video-Tutorial ist
**[hier](https://www.youtube.com/watch?v=9LQhwETCdwY)** zu finden.

### Linux

Sollte Git noch nicht installiert sein, kann es mittel des
Packagemanagers der Distribution installiert werden. Für Debian,
Ubuntu und andere Distributionen geht diese mit `sudo apt-get install
git`. Unter Feudora mit `sudo dnf install git`.
