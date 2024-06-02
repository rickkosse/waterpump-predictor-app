from flask import Flask, render_template, request, jsonify
import folium
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Load the saved model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the dataset
df = pd.read_csv('data/train_data.csv')

# Columns to drop from the dataset
cols_to_drop = [
    'scheme_name', 'id', 'date_recorded', 'region', 'funder', 'recorded_by',
    'wpt_name', 'subvillage', 'ward', 'lga', 'basin', 'quality_group',
    'quantity_group', 'installer', 'source_type', 'source_class',
    'waterpoint_type_group', 'extraction_type_group',
    'extraction_type_class', 'management_group', 'payment_type'
]
df = df.drop(cols_to_drop, axis=1)

# Haversine formula to calculate the distance
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the earth in kilometers
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    
    distance = R * c
    return distance

def predict_functionality(lat, lon):
    # Calculate distances from the given point to all points in the dataset
    df['distance'] = haversine(df['latitude'], df['longitude'], lat, lon)
    
    # Find the closest point
    closest_row = df.loc[df['distance'].idxmin()]
    closest_row_df = closest_row.to_frame().T.reset_index(drop=True)

    # Use the loaded model to make predictions
    probability = model.predict_proba(closest_row_df)[:, 1][0]
    return float(probability)

@app.route('/')
def index():
    start_coords = [-6.369028, 34.888822]
    folium_map = folium.Map(location=start_coords, zoom_start=6)

    # Add the GeoJSON data for Tanzania and make the borders red
    folium.GeoJson(
        'tanzania.geojson',
        name='geojson',
        style_function=lambda feature: {
            'color': 'red',
            'weight': 2,
            'fillOpacity': 0
        }
    ).add_to(folium_map)

    folium_map.save('templates/map.html')
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    lat = data['lat']
    lon = data['lon']
    probability = predict_functionality(lat, lon)
    return jsonify({'probability': probability})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
