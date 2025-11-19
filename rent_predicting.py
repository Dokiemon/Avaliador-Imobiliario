from array import array

def predict_rent(user_features, model_):
    print("Função predict_rent sendo chamada")
    user_features = [int(feature) for feature in user_features]
    print(user_features)
    #>>array('i', [89, 2, 2, 1, 6, 1, 0])
    print(model_.n_features_in_)
    predicted_rent = model_.predict([user_features])
    print("Predicted rent: ", predicted_rent)
    return predicted_rent