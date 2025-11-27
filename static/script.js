async function send(){
    console.log("Função send sendo chamada")
    area = document.querySelector(".area").value
    rooms = document.querySelector(".rooms").value
    bathrooms = document.querySelector(".bathrooms").value
    parking_spaces = document.querySelector(".parking_spaces").value
    floor = document.querySelector(".floor").value
    animal = document.querySelector('input[name="animal"]:checked').value
    furniture = document.querySelector('input[name="furniture"]:checked').value
    features_ = [area, rooms, bathrooms, parking_spaces, floor, animal, furniture]
    console.log(features_)

    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({features: features_}),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        let predictedRent = data.predicted_rent;
        let formattedRent = new Intl.NumberFormat('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 }).format(predictedRent);
        document.querySelector(".result").innerHTML = `Predicted Rent: ${formattedRent}`;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}