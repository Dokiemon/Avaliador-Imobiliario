def predict_rent(user_features, model_):
    predicted_rent = model_.predict(user_features)
    return predicted_rent