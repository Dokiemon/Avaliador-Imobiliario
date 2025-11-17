def predict_rent(user_features, model_):
    print("Função predict_rent sendo chamada")
    predicted_rent = model_.predict(user_features)
    print(predicted_rent)
    return predicted_rent