import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
#name = list(data["NAME"])

#html = """<h4>Volcano information:</h4>
#Height: %s m
#"""
#html = """
#Volcano name:<br>
#<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
#Height: %s m
#"""

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

#Featuregroups used to keep code orgnised and allow layers
fgv = folium.FeatureGroup(name="volcanoes")
fgp = folium.FeatureGroup(name="Population")

#for coordinates in[[38.2,-99.1],[38.9,-99.6]]
#for lt, ln, el, name in zip(lat, lon, elev, name):
for lt, ln, el in zip(lat, lon, elev):
    #popup only accepts strings
    #iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    #iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    #fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='green')))
    #fg.add_child(folium.Marker(location=coordinates, popup=str(el)+" m", icon=folium.Icon(color='green')))
    fgv.add_child(folium.CircleMarker(location=[lt, ln],radius=6, popup=str(el)+" m", fill_color=color_producer(el), color="grey", fill_opacity=0.7 ))

#adds polygon layer, this allows changing the polygon colours by arguments
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))



#Adding a marker, markers must have arguments
#map.add_child(folium.Marker(location=[38.2,-99.1], popup="Hi I am a Marker", icon=folium.Icon(colour='green')))
map.add_child(fgv)
map.add_child(fgp)

#add layer control, if using featuregroups, this will see all layers as one in the fg
map.add_child(folium.LayerControl())


#All changes must be added before saving
#map.save("Map_html_popup_advanced.html")
#map.save("Map_html_popup_simple.html")
map.save("Map1.html")
