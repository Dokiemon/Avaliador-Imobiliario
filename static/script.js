async function send(){
    console.log("Função send sendo chamada")
    area = document.querySelector(".area").value
    rooms = document.querySelector(".rooms").value
    bathrooms = document.querySelector(".bathrooms").value
    parking_spaces = document.querySelector(".parking_spaces").value
    floor = document.querySelector(".floor").value
    animal = document.querySelector(".animal").value
    furniture = document.querySelector(".furniture").value
    features_ = [area, rooms, bathrooms, parking_spaces, floor, animal, furniture]
    console.log(features_)

    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({features: features_}),
    })
}