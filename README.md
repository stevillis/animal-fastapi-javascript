# API de cadastro de animais domésticos. Made with: FastAPI and JavaScript

### Descrição

Uma API para operações de cadastro de animais com os seguintes atributos

```text
id: gerado randomicamente
nome: (texto)
idade: (inteiro)
sexo: (macho\femea)
cor: (texto)
```

### Rotas

- `get`
    - **/animais** — retorna todos os animais cadastrados
    - **/animais/{id}** — retorna o animal com o id especificado
- `post`
    - **/animais** — cria um animal com todos os dados enviados, exceto o id, que é gerado automaticamente
- `put`
    - **/animais/{id}** — atualiza os dados do animal com o id especificado
- `delete`
    - **/animais/{id}** — apaga o animal com o id especificado
