from flask import Blueprint, request, jsonify
import joblib
from flaskr.services.data_preparation import prepare_data
import os

genre_blueprint = Blueprint('genre', __name__)

# Construct the absolute path
base_dir = os.path.abspath(os.path.dirname(__file__))
# base file path for machine learning models
base_path = os.path.join(base_dir, '../../../machine_learning/models/')

# Load models and encoders
model = joblib.load(base_path + 'genre_model_based_number_of_rating.pkl')
age_encoder = joblib.load(base_path + 'age_ohe.pkl')
occupation_encoder = joblib.load(base_path + 'occupation_ohe.pkl')
genre_columns = joblib.load(base_path + 'genre_columns.pkl')
age_map = joblib.load(base_path + 'age_map.pkl')


def predict_genre(gender, age, occupation):

    input_features = prepare_data(age, occupation, gender, age_encoder, occupation_encoder, age_map)
    predictions = model.predict(input_features)
    predicted_genre_labels = [genre for genre, flag in zip(genre_columns, predictions[0]) if flag == 1]

    # return jsonify({'predicted_genres': predicted_genre_labels})
    return predicted_genre_labels
