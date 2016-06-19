import folium
import pandas
import json

state_data_path = 'changes_in_state_pvi_2000_2012.csv'
state_geojson_path = 'us_state_boundaries_5m_edited.json'
state_data = pandas.read_csv(state_data_path).set_index('State')
state_geojson = json.load(open(state_geojson_path))
map_location = [50.99,-112.02]
map_zoom_start = 4

def pvi_comparison_geojson(begin_year, end_year):
    # begin_year and end_year must be column titles
    return folium.GeoJson(
        state_geojson,
        style_function=lambda feature: {
            'fillColor': pvi_color(
                feature['properties']['NAME'], begin_year, end_year),
            'fillOpacity': 0.9,
            'weight': 1,
            'color': 'black'
            }
        )

def pvi_color(state_name, begin_year, end_year):
    pvi_colormap = folium.colormap.LinearColormap(
        ['#ca0020', '#f7f7f7', '#0571b0'], index=[-13, 0, 13], vmin=-13, vmax=13
    )
    initial_pvi = state_data.loc[state_name][begin_year]
    final_pvi = state_data.loc[state_name][end_year]
    pvi_change = final_pvi - initial_pvi
    return pvi_colormap(pvi_change)

def pvi_map(begin_year, end_year):
    map = folium.Map(location=map_location, zoom_start=map_zoom_start)
    pvi_comparison_geojson(begin_year=begin_year, end_year=end_year).add_to(map)
    return map

pvi_map('PVI 2000', 'PVI 2008').save('pvi_map_2000_2008.html')
pvi_map('PVI 2000', 'PVI 2004').save('pvi_map_2000_2004.html')
pvi_map('PVI 2004', 'PVI 2008').save('pvi_map_2004_2008.html')
pvi_map('PVI 2000', 'PVI 2012').save('pvi_map_2000_2012.html')
pvi_map('PVI 2008', 'PVI 2012').save('pvi_map_2008_2012.html')
