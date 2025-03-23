import geopandas as gpd
import folium


supermarkt_gpkg = "D:/ZZ_Michael/_Diverses/geodata/supermarkt_15min.gpkg"
isochronen_shp = "D:/ZZ_Michael/_Diverses/geodata/emskirchen_isochrones_auto.shp"

# supermarkt
supermarkt_gdf = gpd.read_file(supermarkt_gpkg).to_crs(epsg=4326)

# Kartenmittelpunkt
mean_lat = supermarkt_gdf.geometry.y.mean()
mean_lon = supermarkt_gdf.geometry.x.mean()

m = folium.Map(location=[mean_lat, mean_lon], zoom_start=12)

# Isochronen
isochrone_colors = {5: "#1b9e77", 10: "#d95f02", 15: "#7570b3"}

isochronen_gdf = gpd.read_file(isochronen_shp).to_crs(epsg=4326)
isochronen_gdf = isochronen_gdf[isochronen_gdf['interval'].isin([5, 10, 15])]

isochrone_layer = folium.FeatureGroup(name="Fahrzeit-Polygone", show=True).add_to(m)
for _, iso_feature in isochronen_gdf.iterrows():
    interval = iso_feature['interval']
    color = isochrone_colors.get(interval, "gray")
    folium.GeoJson(
        iso_feature['geometry'],
        name=f"{interval} Minuten",
        style_function=lambda x, col=color: {
            'fillColor': col, 'color': col, 'weight': 2, 'fillOpacity': 0.4
        }
    ).add_to(isochrone_layer)

# Supermärkte
supermarkt_layer = folium.FeatureGroup(name="Supermärkte", show=True).add_to(m)
for _, row in supermarkt_gdf.iterrows():
    lat, lon = row.geometry.y, row.geometry.x
    name = row.get('name', 'Unbekannt')
    if "ALDI Süd" in name:
        name = "ALDI"

    folium.CircleMarker(
        location=[lat, lon],
        radius=7,
        color="black",
        weight=1.5,
        fill=True,
        fill_color="red",
        fill_opacity=1,
    ).add_to(supermarkt_layer)

    folium.Marker(
        location=[lat, lon],
        icon=folium.DivIcon(html=f"""
            <div style="
                font-size: 14px;
                font-weight: bold;
                font-family: Arial, sans-serif;
                color: black;
                text-shadow: -2px -2px 1px rgba(255,255,255,0.75), 
                             2px -2px 1px rgba(255,255,255,0.75), 
                            -2px 2px 1px rgba(255,255,255,0.75), 
                             2px 2px 1px rgba(255,255,255,0.75);
                transform: translate(10px, -10px);
                ">
                {name}
            </div>
        """)
    ).add_to(supermarkt_layer)

# Legende
legend_html = f"""
<div style="position: fixed; bottom: 50px; left: 50px; width: 220px; height: auto;
            background-color: white; z-index:9999; padding: 10px; border-radius: 5px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.4); font-size: 14px;">
    <b>Legende</b><br>
    <i style="background:{isochrone_colors[5]}; width: 12px; height: 12px; display: inline-block;"></i> 5 Minuten Fahrzeit<br>
    <i style="background:{isochrone_colors[10]}; width: 12px; height: 12px; display: inline-block;"></i> 10 Minuten Fahrzeit<br>
    <i style="background:{isochrone_colors[15]}; width: 12px; height: 12px; display: inline-block;"></i> 15 Minuten Fahrzeit<br>
    <i style="background:red; border: 2px solid black; width: 12px; height: 12px; display: inline-block; border-radius: 50%;"></i> Supermarkt / Discounter<br>
</div>
"""
m.get_root().html.add_child(folium.Element(legend_html))

# Quelle
source_html = """
<div style="position: fixed; bottom: 10px; right: 50px; width: 300px; height: auto;
            background-color: white; z-index:9999; padding: 5px; border-radius: 5px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.4); font-size: 12px; text-align: right;">
    <b>Datenquellen</b><br>
    Supermarkt-Daten: OpenStreetMap (OSM) - openstreetmap.org<br>
    Fahrzeit-Polygone: OpenRouteService (ORS) - openrouteservice.org<br>
</div>
"""
m.get_root().html.add_child(folium.Element(source_html))

# **Layer-Control**
folium.LayerControl().add_to(m)

# html
m.save("supermarkt_karte_mit_routing.html")

