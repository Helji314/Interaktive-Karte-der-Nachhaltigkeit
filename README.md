# Interaktive-Karte-der-Nachhaltigkeit
Dies wird eine interaktive Karte der Welt, an der man die Nachhaltigkeit gezeigter Länder ablesen kann. Eine Datenbank verwendet Werte (hauptsächlich Our World In Data), die Berechnung der selbst entwickelten Formel findet live statt, so können aktuelle Werte leicht ergänzt werden. Mit einem Click auf das Land kann die Berechnung eingesehen werden.
<br><br>
# Hinweis
Dieses Projekt nutzt GitHub Copilot. Einige Code-Ausschnitte der Datei <a href="public/webpage/index.html">index.html<a> könnten Ähnlichkeiten mit bestehenden Open-Source-Projekten aufweisen. Die entsprechenden Matches sind in <a href="Code Citations.md">Code Citations.md<a> dokumentiert.
<br><br>
# Setup
1. Requirements installieren<br>
2. In /data genannte Dateien unter beachtung der rechtlichen Voraussetzungen des Urhebers runterladen und in /data/raw speichern
<br><br>
# Zielsetzung
Ein Projekt zur Visualisierung der globalen Nachhaltigkeitsleistungen anhand ausgewählter SDG-Indikatoren. 
<br>
Diese interaktive Weltkarte zeigt die Nachhaltigkeitsleistung von Ländern in den drei Dimensionen Soziales, Ökonomisches und Ökologisches. Die Auswahl der Indikatoren orientiert sich an den SDGs (Sustainable Development Goals), die die Vereinten Nationen in ihrer Agenda 2030 festgelegt haben. <br>
Ausgewählt werden die jeweiligen Werte in ihren Dimensionen nach Dringlichkeit, in Kombination zu ihrer Relevanz im Sinne von Maslows darstellung der Bedürfnisse. 
# Berechnung und Datenquellen
1. Soziales <br>
<h3>Indikator</h3>
- Lebenserwartung bei der Geburt <br>
- Ausgaben für die Gesundheit <br>
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
Das BIP pro Kopf zeigt die wirtschaftliche Leistungsfähigkeit, wärend die Arbeitslosigkeit Effizienz und Zukunftsfähigekit (und damit Indikatoren der Nachhaltigkeit) transferiert. <br><br>
Somit ist für jede der drei Dimensionen der Nachhaltigkeit ein aktueller, damit sicherer Wert und einen, der weiter in die Zukunft blickt und damit für die Bestimmung der Nachhaltigkeit insbesondere relevant ist, bestimmt. <br><br>
<br>Jeder dieser Werte wird auf einer Skala von 1 (nidriege Ausprägung) bis 100 (stark ausgeprägt) eingeordnet. Alle drei Dimensionen (Ökologisches, Ökonimisches, Soziales) werden gleich stark gewichtet. <br>
Der gesammte Nachhaltigkeitsindex setzt sich folgendermaßen zusammen:<br>
Nachhaltigkeitsindex = (Sozialer Wert + Ökologischer Wert + Ökonomischer Wert) / 3 <br>
Einzelne Werte = (Wert A + Wert B)/ 2
<br><br>
Der jeweils größte und kleinste Wert werden vom Script automatisch erkannt. Aus den Daten aller Jahre der Länder wird die größte Zahl, als das aktuellste Jahr gewählt. <br>
Je nach Thema werden den größten bzw. kleinsten Werten Zahlen zwischen 1 ("schlecht") und 100 ("gut") zugeordnet, alle dazwischen liegenden Werte werden damit ins Verhältnis gesetzt, die Ausgabe der gesammten Berechnung wird nach /data/processed verschoben. 
<br><br><br>
<h2>Technische Umsetung</h2>
- Daten: Automatisierte Abfrage mithilfe einer Datenbank <br>
- Visualisierung: Erstellung der Karte mithilfe von Datawrapper, diese als Farben dargestellten Klassifizierungen lassen sich nicht live updaten. <br>
- Interaktiv-Machen: Arbeit mit dem Image Map Generator<br>
- Hostig: Mithilfe von GitHub Pages<br><br><br>
<h2>Nächste Schritte</h2>
- Datenquellen Sammeln, Daten vergleichbar machen<br>
- Skript zur Verarbeitung und Berechnung der Werte<br>
- Visualisieren und Interaktivieren der Karte<br>
- Hosting und gesammte rechtl. Regelungen<br>
