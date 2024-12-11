import h3
import plotly.express as px

def create_simple_map():
    
    locations = [
        {"name": "Cristo Redentor", "latitude": -22.9519, "longitude": -43.2105},
        {"name": "MACHU PICCHU", "latitude": -13.1631, "longitude": -72.5450},
        {"name": "CHICHÉN ITZÁ", "latitude": 20.6829, "longitude": -88.5697},
        {"name": "COLISEU", "latitude": 41.8902, "longitude": 12.4922},
        {"name": "TAJ MAHAL", "latitude": 27.1751, "longitude": 78.0421},
        {"name": "PETRA", "latitude": 30.3285, "longitude": 35.4444},
        {"name": "MURALHA DA CHINA", "latitude": 40.4319, "longitude": 116.5704},
    ]

    
    treasure_name = "MACHU PICCHU"

    
    user_choice = "MACHU PICCHU"

    
    h3_resolution = 2

    
    geojson_features = []
    for loc in locations:
        h3_index = h3.latlng_to_cell(loc["latitude"], loc["longitude"], h3_resolution)
        hexagon_boundary = [[lon, lat] for lat, lon in h3.cell_to_boundary(h3_index)]

       
        color = "green" if loc["name"] == user_choice else "blue"

        
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [hexagon_boundary],
            },
            "properties": {"name": loc["name"], "color": color},
        }
        geojson_features.append(feature)

    geojson = {"type": "FeatureCollection", "features": geojson_features}

   
    center_lat = sum([loc["latitude"] for loc in locations]) / len(locations)
    center_lon = sum([loc["longitude"] for loc in locations]) / len(locations)

    
    fig = px.choropleth_mapbox(
        geojson=geojson,
        featureidkey="properties.name",
        locations=[loc["name"] for loc in locations],  # Nome dos locais
        color=[feature["properties"]["color"] for feature in geojson_features],
        mapbox_style="carto-positron",
        center={"lat": center_lat, "lon": center_lon},
        zoom=1,
        opacity=0.5,
    )

    fig.show()


create_simple_map()