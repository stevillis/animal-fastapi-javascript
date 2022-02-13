const GET_AND_POST_ENDPOINT = "http://localhost:8000/animais";

async function removeElementChildren(element) {
  let child = element.lastElementChild;

  while (child) {
    element.removeChild(child);
    child = element.lastElementChild;
  }
}

async function fetchAnimals() {
  const response = await axios.get(GET_AND_POST_ENDPOINT);
  const animals = response.data;
  const animalTableBody = document.querySelector("#animalTableBody");

  await removeElementChildren(animalTableBody);
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

async function createAnimal(name, age, sex, color) {
  await axios.post(GET_AND_POST_ENDPOINT, {
    name: name,
    age: age,
    sex: sex,
    color: color
  });
  fetchAnimals();
}

function formSubmit() {
  const formAnimal = document.querySelector("#formAnimal");
  const nameInput = document.querySelector("#name");
  const ageInput = document.querySelector("#age");
  const sexInput = document.querySelector("#sex");
  const colorInput = document.querySelector("#color");

  formAnimal.onsubmit = event => {
    event.preventDefault();

    const name = nameInput.value;
    const age = parseInt(ageInput.value);
    const sex = sexInput.value;
    const color = colorInput.value;

    createAnimal(name, age, sex, color);
  }
}

function app() {
  formSubmit();

  // API 
  fetchAnimals();
}

app();
