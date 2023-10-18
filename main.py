import folium

# Membuat peta dengan lokasi awal yang ditentukan
m = folium.Map(location=[-7.773262, 110.384808], zoom_start=16)  # Latitude dan Longitude London, UK

# Menambahkan marker untuk kantor Google di London
folium.Marker([-7.773262, 110.384808], tooltip='universitas gadjah mada').add_to(m)

# Menyimpan peta ke dalam file HTML
m.save('mymap.html')
