---
Titel: "Sharing your work"
Unterricht: 30
Übungen: 0
Fragen:
- "Wie kann ich Git und GitHub benutzen, um meine Arbeit zu teilen?"
- "Wie kann ich ein lokales Git-Repository mit GitHub verlinken?"
- "Wie verschiebe ich Änderungen zwischen einem lokalen Git-Repository und einem GitHub-Repository?"
- "Wie kann ich die Unterschiede zwischen meiner aktuellen Datei und meiner letzten Übertragung sehen?"
Ziele:
- "Ein entferntes Repository auf GitHub erstellen"
- "ein lokales Git-Repository mit einem entfernten GitHub-Repository zu verknüpfen"
- "Änderungen zwischen dem lokalen und entfernten Repository mit `push` und `pull` verschieben".
- "Untersuche den Unterschied zwischen einer bearbeiteten Datei und der zuletzt übertragenen Version der Datei"
Schlüsselpunkte:
- "Remote-Repositories auf GitHub helfen Ihnen bei der Zusammenarbeit und der gemeinsamen Arbeit"
- `push` ist ein Git-Verb für das Senden von Änderungen aus dem lokalen Repository in ein entferntes Repository.
- "pull" ist ein Git-Verb, um Änderungen aus einem entfernten Repository in das lokale Repository zu bringen.
- "`diff` ist ein Git-Verb, um den Unterschied zwischen einer bearbeiteten Datei und der letzten Übertragung der Datei zu sehen".
---

## Erstellen Sie ein Repository auf GitHub

Wenn wir uns bei GitHub eingeloggt haben, können wir ein neues Repository erstellen, indem wir auf das **+** Symbol in der oberen rechten Ecke von
eine beliebige Seite und wählen Sie dann **Neues Repository**. Lass uns das jetzt machen.

* Neues Projektarchiv erstellen
* Gib ihm den Namen `Halo-World`

GitHub fragt Sie, ob Sie eine README.md, eine Lizenz oder eine `.gitignore` Datei hinzufügen möchten. Machen Sie vorerst nichts davon.

> ## Eine Lizenz auswählen
> Die Wahl einer Lizenz ist ein wichtiger Teil der offenen Weitergabe Ihrer kreativen Arbeit im Internet. Für Hilfe beim Waten durch die
> viele Arten von Open-Source-Lizenzen, besuchen Sie bitte <https://choosealicense.com/>.
{: .callout}

## Verbinden Ihres lokalen Repositorys mit dem GitHub-Repository

In der vorherigen Episode haben wir ein lokales Repository auf unserem eigenen Computer erstellt.
Jetzt haben wir auch ein entferntes Repository auf GitHub erstellt.
Aber zu diesem Zeitpunkt sind die beiden komplett voneinander isoliert.
Wir wollen sie miteinander verbinden, um sie zu synchronisieren und unser Projekt mit der Welt zu teilen.

Dazu brauchen wir die GitHub-Repository-URL, die ungefähr so aussehen sollte
(mit "some-librarian" ersetzt durch Ihren Benutzernamen):

![Die Repository-URL auf GitHub](../fig/repository-url.png)

Wenn die URL mit `git@` statt `https://` beginnt, klicken Sie bitte auf den "HTTPS"-Button, um sie zu ändern.

> ## HTTPS vs. SSH
>
> Wir verwenden hier HTTPS, weil es keine zusätzliche Konfiguration erfordert, die unterschiedlich ist
> von Betriebssystem zu Betriebssystem. Wenn Du Git regelmäßig benutzt, würdest Du
> wie das Einrichten eines SSH-Zugangs, der etwas sicherer und bequemer ist, indem
> nach einem der großartigen Tutorials von
> [GitHub](https://help.github.com/articles/generating-ssh-keys),
> [Atlassian/BitBucket](https://confluence.atlassian.com/bitbucket/set-up-an-ssh-key-728138079.html)
> und [GitLab](https://about.gitlab.com/2014/03/04/add-ssh-key-screencast/)
> (dieser hat einen Screencast).
{: .callout}

Beachten Sie, dass GitHub tatsächlich hilfreich genug ist, um Anweisungen für uns zu geben
damit wir uns nicht an diese Befehle erinnern müssen:

![GitHub-Anweisungen](../fig/github-instructions.png)

Sie können diese daher kopieren und in die Befehlszeile einfügen.
Oder Sie können sie auch austippen, um sie in Ihre Finger zu bekommen.
Das werde ich tun. Also beginnen wir mit dem Befehl, unser lokales Repository zu verlinken
zum GitHub-Repository:

~~~
$ git remote add origin https://github.com/some-librarian/hello-world.git
~~~
{: .bash)

wobei `some-librarian` durch Ihren eigenen Benutzernamen ersetzt werden sollte.

> >#Warum `ursprünglich`?
> `ursprünglich` in der `git remote add` Zeile ist nur ein kurzer Name oder ein Alias, den wir dieser großen langen Repository-URL geben.
> Es könnte fast jede beliebige Zeichenkette sein, die wir wollen, aber in git wird sie normalerweise `ursprünglich` genannt, was bedeutet, dass
> der Repo entstanden ist.
{: .callout}

Mit dem Befehl können wir überprüfen, ob es richtig eingestellt ist:

~~~
$ git remote -v
~~~
{: .bash)
~~~
Herkunft https://github.com/<Ihr_github_Benutzername>/hello-world (fetch)
Herkunft https://github.com/<Ihr_github_Benutzername>/hello-world (drücken)
~~~
{: .output}

~ Pushing changes ~

Jetzt haben wir eine Verbindung zwischen den beiden Repositories hergestellt, aber wir haben noch nicht
ihren Inhalt synchronisiert, so dass das entfernte Repository noch leer ist. Um das zu beheben, haben wir
müssen unsere lokalen Änderungen in das GitHub-Repository "pushen". Wir tun dies mit der
"Git-Push"-Befehl:

~~~
$ git push -u Ursprung Meister
~~~
{: .bash)
~~~
Zählen von Objekten: 3, fertig.
Objekte schreiben: 100% (3/3), 226 Bytes | 0 Bytes/s, fertig.
Gesamt 3 (Delta 0), wiederverwendet 0 (Delta 0)
Zu https://github.com/<Ihr_Github_Benutzername /hello-world
 * [neue Niederlassung] Master -> Master
Zweigmaster eingerichtet, um den entfernten Zweigmaster vom Ursprung aus zu verfolgen.
~~~
{: .output}

Der Spitzname unseres entfernten Repositorys ist "origin" und der Standardname des lokalen Zweigs ist "master".
Das `-u` Flag sagt git, dass es sich die Parameter merken soll, so dass wir beim nächsten Mal einfach `git push` ausführen können.
und Git wird wissen, was zu tun ist.

Sie werden möglicherweise aufgefordert, Ihren GitHub-Benutzernamen und Ihr Passwort einzugeben, um den Befehl abzuschließen.



Wenn wir einen `Git-Push` machen, werden wir sehen, wie Git 'pusht' sich stromaufwärts zu GitHub ändert. Da unsere Datei sehr klein ist, ist diese 
wird nicht lange dauern, aber wenn wir eine Menge Änderungen gemacht haben oder ein sehr großes Repository hinzufügen, müssen wir vielleicht ein 
etwas länger. Wir können mit dem "Git-Status" überprüfen, wo wir sind.

~~~
$ Git-Status
~~~
{: .bash)
~~~
Auf Filialmeister
Ihre Filiale ist mit 'Herkunft/Stamm' auf dem neuesten Stand.
nichts zu übergeben, Arbeitsbaum sauber
~~~
{: .output}

Dieser Ausgang lässt uns wissen, wo wir arbeiten (der Master-Zweig). Wir können auch sehen, dass wir keine Änderungen zu übergeben haben 
und alles ist in Ordnung.

Wir können das `git diff` Kommando benutzen, um Änderungen zu sehen, die wir gemacht haben, bevor wir einen Commit machen. Öffnen Sie index.md mit einem beliebigen Text 
Editor und geben Sie einen Text in eine neue Zeile ein, zum Beispiel "Eine neue Zeile" oder etwas anderes.
Wir werden dann `git diff` benutzen, um die Änderungen zu sehen, die wir gemacht haben:

~~~
$ git diff
~~~
{: .bash)
~~~
diff --git a/index.md b/index.md
index aed0629..989787e 100644
--- a/index.md
+++ b/index.md
@@ -1 +1,2 @@
-# Hallo, Welt!
\ Kein Zeilenumbruch am Ende der Datei
+# Hallo, Welt!
+Eine neue Linie
~~~
{: .output}

Der Befehl produziert eine Menge Informationen und kann anfangs etwas überwältigend sein,
aber lass uns hier ein paar Schlüsselinformationen durchgehen:

1. Die erste Zeile sagt uns, dass Git eine Ausgabe ähnlich dem Unix-Befehl `diff` produziert, wobei die alte und die neue verglichen wird 
Versionen der Datei.
2. Die zweite Zeile sagt genau, welche Versionen der Datei Git vergleicht; `aed0629` und `989787e` sind eindeutig 
computergenerierte Identifikatoren für diese Versionen.
3. In der dritten und vierten Zeile wird noch einmal der Name der zu ändernden Datei angezeigt.
4. Die restlichen Zeilen sind die interessantesten; sie zeigen uns die tatsächlichen Unterschiede und die Zeilen, auf denen sie auftreten. 
Insbesondere die +-Markierungen in der ersten Spalte zeigen uns, wo wir Zeilen hinzugefügt haben.

Wir können diese Änderungen nun übertragen:

~~~
$ git add index.md
$ git commit -m 'Weitere Zeile hinzufügen'.
~~~
{: .bash)

Wenn wir sehr vergesslich sind und bereits vergessen haben, was wir verändert haben, erlaubt uns `git log` einen Blick auf das, was 
die wir mit unserem Git-Repository gemacht haben (in umgekehrter chronologischer Reihenfolge, mit den allerneuesten Änderungen zuerst).


~~~
$ git log
~~~
{: .bash)
~~~
8e2eb9920eaa0bf18a4adfa12474ad58b765fd06
Autorin: Ihr Name <Ihr_E-Mail>
Ein Date:   Mon Jun 5 12:41:45 2017 +0100

    Weitere Zeile hinzufügen

e9e8fd3f12b64fc3cbe8533e321ef2cdb1f4ed39
Autorin: Ihr Name <Ihr_E-Mail>
Ein Date:   Fr 2. Juni 18:15:43 2017 +0100

    Index.md hinzufügen
~~~
{: .output}

Dies zeigt uns die beiden Commits, die wir gemacht haben und zeigt die Nachrichten, die wir geschrieben haben. Es ist wichtig zu versuchen, sinnvolle 
Commit-Meldungen, wenn wir Änderungen vornehmen. Das ist besonders wichtig, wenn wir mit anderen Leuten zusammenarbeiten, die vielleicht nicht 
so leicht erraten können, was unsere kurzen kryptischen Nachrichten bedeuten könnten. Beachten Sie, dass es am besten ist, immer zu schreiben 
Commit-Meldungen im Imperativ (z.B. 'Add index.md', statt 'Add index.md').

## Änderungen (erneut) verschieben

Schauen wir uns jetzt noch einmal das Repository bei GitHub an
(d.h. `https://github.com/some-librarian/hello-world` mit `some-librarian` ersetzt durch Ihren Benutzernamen).
Wir sehen, dass die Datei `index.md` vorhanden ist, aber es gibt nur einen Commit:

![Nur ein Commit auf GitHub](../fig/github-one-commit.png)

Und wenn du auf `index.md` klickst, siehst du, dass sie die "Hallo, Welt!"-Überschrift enthält,
aber nicht die neue Linie, die wir gerade hinzugefügt haben.

Das liegt daran, dass wir unsere lokalen Änderungen noch nicht in das entfernte Repository verschoben haben.
Das mag wie ein Fehler im Design aussehen, aber es ist 
oft nützlich, um eine Menge Commits für kleine Änderungen zu machen, damit Sie später sorgfältige Revisionen vornehmen können und nicht 
wollen notwendigerweise all diese Veränderungen nacheinander vorantreiben.

Ein weiterer Vorteil dieses Designs ist, dass Sie Commits machen können, ohne mit dem Internet verbunden zu sein.

Aber lass uns unsere Änderungen jetzt mit dem `git push` Befehl pushen:

~~~
$ Git Push
~~~
{: .bash)
~~~
Zählen von Objekten: 3, fertig.
Objekte schreiben: 100% (3/3), 272 Bytes | 0 Bytes/s, fertig.
Gesamt 3 (Delta 0), wiederverwendet 0 (Delta 0)
Zu https://github.com/<Ihr_github_Benutzername>/hello-world
   e9e8fd3..8e2eb99 Master -> Master
~~~
{: .output}

Und lasst uns bei GitHub nachsehen, dass wir dort jetzt 2 Commits haben.

~ Pulling changes ~

Wenn wir mit anderen zusammenarbeiten oder wenn wir unsere eigenen Änderungen an verschiedenen Maschinen vornehmen, brauchen wir eine Möglichkeit, diese
Remote Änderungen zurück in unsere lokale Kopie. Vorerst können wir sehen, wie das funktioniert, indem wir eine Änderung auf der GitHub-Website vornehmen und 
und dann diese Änderung zurück zu unserem Computer "ziehen".

Lass uns zu unserem Repository in GitHub gehen und eine Änderung vornehmen. Unterhalb unserer index.md Datei sehen Sie eine 
Taste auf 'README hinzufügen'. Tun Sie dies jetzt, geben Sie ein, was Sie wollen, scrollen Sie nach unten und klicken Sie auf 'Commit new'. 
Datei' (Die Standard-Commit-Meldung wird 'Create README.md' sein, was für unsere Zwecke in Ordnung ist).



> ## Die README-Datei
> Es ist eine gute Praxis, jedem Projekt eine README-Datei hinzuzufügen, um einen kurzen Überblick über das Projekt zu geben. Wenn Sie 
> legen Sie Ihre README-Datei in das Hauptverzeichnis Ihres Repositorys, GitHub wird Ihre README-Datei erkennen und automatisch an die Oberfläche bringen 
> an die Besucher des Repositoriums
{: .callout}

Unser lokales Repository ist nun nicht mehr synchron mit unserem entfernten Repository, also lasst uns das beheben, indem wir die entfernten Änderungen in
unser lokales Repository mit dem `git pull` Befehl.

~~~
$ Git Pull
~~~
{: .bash)
~~~
entfernt: Zählen von Objekten: 3, fertig.
Fernbedienung: Objekte komprimieren: 100% (2/2), erledigt.
Fernbedienung: Gesamt 3 (Delta 0), wiederverwendet 0 (Delta 0), wiederverwendet 0
Auspacken von Gegenständen: 100% (3/3), fertig.
Von https://github.com/<Ihr_github_Benutzername>/hello-world
   8e2eb99..0f5a7b0 Master -> Ursprung / Master
Aktualisierung 8e2eb99..0f5a7b0
Schnellvorlauf
 README.md | 1 +
 1 Datei geändert, 1 Einfügung(+)
 Modus erstellen 100644 README.md
~~~
{: .output}
Die obige Ausgabe zeigt, dass wir unser lokales Repository im Schnelldurchlauf um die Datei README.md erweitert haben. Wir konnten bestätigen
dies durch die Eingabe des `ls` Befehls.

Wenn wir anfangen, an komplexeren Projekten zusammenzuarbeiten, müssen wir vielleicht mehr Aspekte der Git-Funktionalität berücksichtigen, aber 
das sollte ein guter Anfang sein. Im nächsten Abschnitt können wir uns die Zusammenarbeit und die Nutzung der GitHub-Seiten genauer ansehen, um
eine Website für unser Projekt erstellen.
