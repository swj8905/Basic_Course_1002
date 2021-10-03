import folium

map = folium.Map(location=[37.497831910190435, 127.02768230567065],
           zoom_start=17)
map.save("./map.html")