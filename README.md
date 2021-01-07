# BWICodingChallenge
BWI Coding Challenge - Optimization problem for the distribution of hardware

## Algorithmus
Zunächst wurde der Quotient aus Nutzen und Gewicht bestimmt, um eine Priorisierung der zu beladenen Hardware
vorzunehmen. In Form einer nested dict wurde die Hardware definiert und nach Priorität sortiert. Anschließend erfolgte
die Beladung des ersten Trucks. Dabei wurden zunächst die höchst priorisierte Hardware eingeladen, danach die nächst
höhere priorisierte Hardware. Diese Schritte wurden mit Beachtung der Gewichtsbeschränkung durchgeführt. Für den zweiten
Truck erfolgte dieses Vorgehen analog, wobei die bereits im ersten Truck eingeladene Hardware mitberücksichtigt wurde.
Bei jeder Iteration erfolgte eine Aktualisierung der Last, des Nutzens und der Ladung des jeweiligen Trucks.

## Code
Der Code befindet sich im Ordner [src](../src). Zum Ausführen reicht es den folgenden Befehl 
im Hauptverzeichnis des Repository auszuführen.

```shell script
python main.py
```

## Ergebnis
###Gesamt
Gesamtnutzen beider Trucks aufsummiert: 74640

###**Truck 1**

Gesamtnutzen: 44764

Gesamtgewicht: 1099,276 kg

Gewicht des Fahres: 72,4 kg

Geladene Hardware:


| Hardware      | Units        | Nutzen | Gewicht in kg
| ------------- |-------------  | ----- | ----- 
| Mobiltelefon Outdoor | 157 | 9420 | 155,116
| Mobiltelefon Heavy Duty | 220      |   14300 | 268,400
| Mobiltelefon Büro | 60      |    1800 | 43,020
| Tablet outdoor groß | 283 | 19244 | 560,340


###**Truck 2**

Gesamtnutzen: 29876

Gesamtgewicht: 1099,555 kg

Gewicht des Fahres: 85,7 kg

Geladene Hardware: 


| Hardware      | Units        | Nutzen | Gewicht in kg
| ------------- |-------------  | ----- | ----- 
| Tablet outdoor groß | 87 | 5916 | 172,260
| Tablet Büro klein | 599      |   23960 | 841,595
