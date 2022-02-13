async function fetchAnimals() {
  const response = await axios.get("http://localhost:8000/animais");
  const animals = response.data;

  const animalTableBody = document.querySelector("#animalTableBody");
  animals.forEach((animal) => {
    const tr = document.createElement("tr");

    tr.innerHTML = `
    <td>${animal.id}</td>
    <td>${animal.name}</td>
    <td>${animal.age}</td>
    <td>${animal.sex}</td>
    <td>${animal.color}</td>
    `;
    animalTableBody.appendChild(tr);
  });
}

function app() {
  fetchAnimals();
}

app();
