# Interaktive-Karte-der-Nachhaltigkeit
Dies ist eine interaktive Karte, die die Nachhaltigkeit der Länder der Welt im Vergleich darstellt. <br>
Dazu berechnet eine selbst entwickelte Formel einen Wert, der mit einem Click auf das Land eingesehen werden kann. Die Datengrundlage stammt in diesem Falle von Our World in Data und dessen Quellen, die Informationen zu verschiedenen Dimensionen als csv-Dateien anbieten. Ein Python-Script berechnet einzelne und Gesammtwerte, die den Färbunger der Karte und der JSON-Datenbank zur Beretstellung der Begründung als Basis dienen. 
<br><br>
# Hinweis
Dieses Projekt verwendet in einzelnen Dokumenten vorschläge von GitHub Copilot. Dadurch sind Ähnlichkeiten mit bestehenden Open Source Projekten nicht unmöglich. Sollten diese Ähnlichkeiten auffallen, freue ich mich über einen kurzen Hinweis!
<br><br>
# Setup zur Reproduktion
1. <a href="data\licenses\DATA_SOURCES.md">csv-Dateien von Our World in Data und Quellen</a> unter Beachtung der rechtlichen Vorraussetzungen laden<br>
2. Geladene Dateien in /data/raw speichern<br>
3. <a href="requirements.txt">Requirements</a> installieren<br>
4. <a href="tools\processed_data.py">processed_data.py</a>, <a href="tools\export_data.py">export_data.py</a> und <a href="tools\fetch_data.py">fetch_data.py</a> ausführen<br>
5. Daten aus data\processed\sustainability_index.csv oder direkt csvs aus public\data nutzen, um Karten zu erstellen<br>
6. html-Dateien für Präsentation in public\webpage erstellen und Karten einbinden<br>
7. Aus <a href="tools\fetch_data.py">fetch_data.py</a> entstehende calculations.json für die Erklärung verwenden (sie sollte in data\calculations.json gefunden werden)
<br><br>
# Zielsetzung
Ein Projekt zur Visualisierung der globalen Nachhaltigkeitsleistungen anhand ausgewählter SDG-Indikatoren. 
<br>
Diese interaktive Weltkarte zeigt die Nachhaltigkeitsleistung von Ländern in den drei Dimensionen Soziales, Ökonomisches und Ökologisches. Die Auswahl der Indikatoren orientiert sich an den SDGs (Sustainable Development Goals), die die Vereinten Nationen in ihrer Agenda 2030 festgelegt haben. <br>
Ausgewählt werden die jeweiligen Werte in ihren Dimensionen nach Dringlichkeit, in Kombination zu ihrer Relevanz im Sinne der Bedürfnisspyramiede nach Maslow. 
# Berechnung und Begründung
1. Soziales <br>
<h3>Indikator</h3>
- Lebenserwartung bei der Geburt <br>
- Gesundheitsausgaben <br>
<h4>Begründung</h4>
Die Lebenserwartung bei der Geburt stellt vergleichbare Werte zur allgemeinen Gesundheit und Lebensqualität der Person und Generation her, die Ausgaben für Gesundheit darüber hinaus Sicherheit und Zukunfsfähigkeit aktueller Daten. <br><br>
2. Ökologisches
<h3>Indikator</h3>
- CO_2 Emissionen pro Kopf<br>
- Andere Emissionen<br>
<h4>Begründung</h4>
CO_2 stellt einen der Treiber der globalen Erderwärmung da und weitere Emissionen in besonderem Maße die Sicherheit der eigenen Bevölkerung, da sie oft auf nicht-sachgemäße Müllentsorgung zurückzuführen ist, die statistisch kaum erfasst wird. <br><br>
3. Ökonimisches
<h3>Indikator</h3>
- BIP pro Kopf<br>
- Arbeitslosigkeit in % <br>
<h4>Begründung</h4>
Das BIP pro Kopf zeigt die wirtschaftliche Leistungsfähigkeit, wärend die Arbeitslosigkeit indikator für Effizienz und Zukunftsfähigekit ist. <br><br>
Somit ist für jede der drei Dimensionen der Nachhaltigkeit ein aktueller (eindeutiger) und ein zukunftsperspektivischer Blick gegeben. <br><br>
<br>Jeder dieser Werte wird auf einer Skala von 1 (nidriege Ausprägung) bis 100 (stark ausgeprägt) eingeordnet. Alle drei Dimensionen (Ökologisches, Ökonimisches, Soziales) werden gleich stark gewichtet. <br>
Der gesammte Nachhaltigkeitsindex setzt sich folgendermaßen zusammen:<br>
Nachhaltigkeitsindex = (Sozialer Wert + Ökologischer Wert + Ökonomischer Wert) / 3 <br>
Einzelne Werte = (Wert A + Wert B)/ 2
<br><br>
Der jeweils größte und kleinste Wert jeder Einheit wird vom Python-Script automatisch erkannt. Aus den Daten aller Jahre der Länder wird aktuellste gewählt. <br>
Je nach Thema wird die Einteilung zwischen 100 (optimal) und 1 (ungünstig) vorgenommen. Das bedeutet, dass Werte wie der CO_2-Ausstoß möglichst klein und Werte wie das BIP groß sein sollten, um einen hohen Wert zu erhalten. Das Script erkennt am Dateinamen dessen Klassifizierung und dreht die Berechnung automatisch um. <br> Alle dazwischen liegenden Werte werden damit ins Verhältnis gesetzt, die Ausgabe der gesammten Berechnung wird nach /data/processed verschoben, die Zwischenschritte können im log der Console verfolgt werden. 
<br><br><br>
<h2>ErgebnissE</h2>
Bei korrekter Anwendung könnte der Überblick auf der Website wie folgt aussehen: <br>
<img width="1856" height="1006" alt="Screenshot 2025-12-11 at 14-29-52 Interaktive-Karte-der-Nachhaltigkeit" src="https://github.com/user-attachments/assets/34dad48a-35f8-4797-9ae4-0c5e67e59aa7" />
Der Wert des angeclickten Lades wird neben diesem und im Vergleich zu den anderen Ländern in der Legende angezeigt. <br>
Im Suchfeld eingegebene bzw. diesen sehr ähnelnde Ländernamen werden mit passenden Daten zur Berechnung dargestellt:
<img width="1856" height="1006" alt="Screenshot 2025-12-11 at 14-30-41 Interaktive-Karte-der-Nachhaltigkeit" src="https://github.com/user-attachments/assets/8b47ff54-8018-4e16-a20a-b4657f681ef2" />
Oben hinter einem Button sind die einzelnen Dimensionen (ökologisches, ökonimisches, soziales) verborgen und können zum Vergleich angezeigt werden: <br>
<img width="1856" height="1006" alt="Screenshot 2025-12-11 at 14-33-01 Interaktive-Karte-der-Nachhaltigkeit" src="https://github.com/user-attachments/assets/e8a8a7cb-18e8-455e-9185-d291fc791932" />
<br><br>
Beispielcode, wie eine solche Seite aufgebaut sein könnte, kann auch in meinem Repository <a href="https://github.com/Helji314/sources?tab=readme-ov-file">sources</a> gefunden werden. 
