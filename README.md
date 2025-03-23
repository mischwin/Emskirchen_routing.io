# Supermarkt-Analyse Emskirchen

Dieses Repository enthält eine interaktive Karte, die Fahrzeit-Isochronen (5, 10 und 15 Minuten) um Emskirchen sowie die Standorte von Supermärkten darstellt. Ziel der Analyse ist es aufzuzeigen, wie viele Supermärkte innerhalb der definierten Fahrzeiten liegen – ein Befund, der nahelegt, dass kein Neubau eines zusätzlichen Supermarktes in Emskirchen notwendig ist.

## Inhalt

- **Interaktive Karte:**  
  Eine HTML-Datei, die mit Python (Folium, GeoPandas) erstellt wurde.  
  - Fahrzeit-Isochronen (5, 10, 15 Minuten) werden farblich differenziert dargestellt.  
  - Supermärkte werden als rote Punkte mit direkter Beschriftung (mit schrägem Offset) angezeigt.

- **Code:**  
  Python-Skripte, die die Daten aus OpenStreetMap (OSM) und OpenRouteService (ORS) verarbeiten und die interaktive Karte generieren.

## Ziel der Analyse

Die interaktive Karte zeigt, dass eine ausreichende Anzahl von Supermärkten innerhalb kurzer Fahrzeiten (bis 15 Minuten) in Emskirchen vorhanden ist. Damit wird belegt, dass die bestehende Versorgungslage so gut ist, dass der Bau eines neuen Supermarktes nicht erforderlich ist.

## Datenquellen

- **Supermarkt-Daten:**  
  Die Standorte der Supermärkte werden aus [OpenStreetMap (OSM)](https://www.openstreetmap.org) bezogen, welche unter der [Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/) stehen.

- **Fahrzeit-Polygone:**  
  Die Isochronen (Fahrzeit-Polygone) wurden mithilfe von [OpenRouteService (ORS)](https://openrouteservice.org) generiert. ORS bietet leistungsfähige Routing-Dienste, die ebenfalls auf Open-Source-Daten basieren.

## Anforderungen

- Python 3.x  
- [Folium](https://python-visualization.github.io/folium/)  
- [GeoPandas](https://geopandas.org)  
- Weitere Python-Bibliotheken wie `shapely` und `random`

## Nutzung

