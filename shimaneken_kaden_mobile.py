import folium

m = folium.Map(location=[34.9401461,132.6594752],zoom_start=9)
m

folium.Marker(location=[35.3661093,132.7438121],popup='エディオン 出雲店　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.9015974,132.0851039],popup='エディオン 浜田店　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[34.689726,131.8206514],popup='エディオン 益田店　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[35.4687108,133.0620435],popup='エディオン 松江店　　　　　　　　',icon=folium.Icon(color="blue")).add_to(m)
m

folium.Marker(location=[35.4347434,133.1230941],popup='家電住まいる館YAMADA松江店　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[35.1988172,132.4915515],popup='ヤマダデンキ テックランド大田店　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.9021568,132.0709828],popup='ヤマダデンキ テックランド浜田港町店　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.688883,131.8241433],popup='ヤマダデンキ テックランド益田店　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[35.4740129,133.0688681],popup='ヤマダデンキ テックランド松江学園南店　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[35.3779321,132.7520227],popup='ヤマダデンキ テックランドNew出雲店　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[34.988585,132.1877644],popup='ヤマダデンキ ヤマダアウトレット江津店　　　　　　　　　　　　　　　　　　',icon=folium.Icon(color="red")).add_to(m)
m

folium.Marker(location=[35.3691069,132.7415492],popup='ケーズデンキ 出雲店　　　　　　　　　',icon=folium.Icon(color="orange")).add_to(m)
m

folium.Marker(location=[35.4639884,133.0693533],popup='イオンモバイル 松江店　　　　　　　　　　',icon=folium.Icon(color="purple")).add_to(m)
m

folium.Marker(location=[35.3729096,132.7368258],popup='100満ボルト 出雲店　　　　　　　　',icon=folium.Icon(color="lightgreen")).add_to(m)
m

folium.Marker(location=[35.4363334,133.0495786],popup='100満ボルト 松江本店　　　　　　　　　',icon=folium.Icon(color="lightgreen")).add_to(m)
m

folium.Marker(location=[35.4787324,133.0686114],popup='パソコン工房 松江店　　　　　　　　　',icon=folium.Icon(color="green")).add_to(m)
m

folium.Marker(location=[35.4227735,133.3328964],popup='マーキュリー 米子　　　　　　　　',icon=folium.Icon(color="white")).add_to(m)
m

m.save('shimaneken_kaden_mobile.html')
