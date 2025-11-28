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
        document.querySelector(".result").innerHTML = `${formattedRent}`;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const numberInputs = document.querySelectorAll('input[type="number"]');
    
    numberInputs.forEach(input => {
        input.addEventListener('input', function() {
            const min = parseFloat(this.getAttribute('min')) || 0;
            if (parseFloat(this.value) < min) {
                this.value = min;
            }
        });
        
        input.addEventListener('blur', function() {
            const min = parseFloat(this.getAttribute('min')) || 0;
            if (this.value === '' || parseFloat(this.value) < min) {
                this.value = min;
            }
        });
    });
});
