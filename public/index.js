function fetchAnimals() {
  axios.get('http://localhost:8000/animais').then(response => {
    console.log(response.data);
  })
}

function app() {
  fetchAnimals();
}

app();