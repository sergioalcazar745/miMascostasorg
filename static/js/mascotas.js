lista = "";

$(document).ready(function () {
  listadoMascotas();
});

document.addEventListener('click', function handleClickOutsideBox(event) {
  const box = document.getElementById('sugerencias');

  if (!box.contains(event.target)) {
    box.style.display = 'none';
  }
});

function listadoMascotas() {
  $.ajax({
    type: "GET",
    url:
      "/mascotas/" +
      $("#tipo-mascota .titulo-detalle .container h1")
        .html()
        .toLowerCase()
        .trim(),
    success: function (response) {
      lista = JSON.parse(response["lista"]);
      lista_razas = razas();

      document.getElementById("select").innerHTML = "";
      codigo = "<option value='todos' selected>todos</option>";
      for (const ite of lista_razas) {
        codigo += `<option value="${ite}">${ite}</option>`;
      }

      document.getElementById("select").innerHTML = codigo;
      document.getElementById("tipo").innerHTML = String(document.getElementById("select").value).toUpperCase();
      pintarMascotas();
    },
    error: function (error) {
      console.log("ERROR: " + +JSON.stringify(error));
    },
  });
}

function onclickLetter(item) {
  codigo = "";
  if (item.value.toLowerCase() != "") {
    for (const ite of lista) {
      if (ite.nombre.toLowerCase().startsWith(item.value.toLowerCase())) {
        codigo += `<li onclick='clickItem(this)'>${ite.nombre.toLowerCase()}</li>`;
      }
    }
    if (codigo != "") {
      document.getElementById("listaSugerencias").innerHTML = "";
      document
        .getElementById("sugerencias")
        .setAttribute("style", "display: block !important");
      document.getElementById("listaSugerencias").innerHTML = codigo;
    } else {
      document.getElementById("sugerencias").removeAttribute("style");
    }
  } else {
    document.getElementById("sugerencias").removeAttribute("style");
  }
}

function changeRaza() {
  item = document.getElementById("select").value;
  console.log(item)
  document.getElementById("tipo").innerHTML = "";
  document.getElementById("tipo").innerHTML = String(item).toUpperCase();
  if (item == "todos") {
    pintarMascotas();
  } else {
    let codigo = "";
    for (const ite of lista) {
      if (ite.tipo == item) {
        codigo += `
          <div class="col-12 col-md-6 col-lg-4 col-xl-3">
              <div class="card card-custom my-5">
                  <div class="card-head card-head-custom">
                      <div class="animal-detail">
                          <h2>${ite.nombre}</h2>
                          <img src="/media/${
                            ite.imagen
                          }" alt="" class="animal-img">
                          <p>${ite.caracter.toUpperCase()}</p>
                      </div>
                  </div>
                  <div class="card-body card-body-custom">
                      <div class="animal-info">
                          <ul>
                              <li><span class="labels">TIPO:</span> ${
                                ite.tipo
                              }</li>
                              <li><span class="labels">SALUD:</span> ${
                                ite.salud
                              }</li>
                              <li><span class="labels">ALTURA:</span> ${
                                ite.altura
                              }</li>
                              <li><span class="labels">PESO:</span> ${
                                ite.peso
                              }</li>
                          </ul>
                      </div>
                      <div class="animal-discription">
                          <h4 class="labels">OBSERVACIONES</h4>
                          <p>${ite.observaciones}</p>
                      </div>
                  </div>
              </div>
          </div>`;
      }
    }
    if (codigo != "") {
      document.getElementById("contenedorMascotas").innerHTML = codigo;
    } else {
      document.getElementById("contenedorMascotas").innerHTML = codigo;
    }
  }
}

function pintarMascotas() {
  let codigo = "";
  for (const ite of lista) {
    codigo += `
    <div class="col-12 col-md-6 col-lg-4 col-xl-3">
        <div class="card card-custom my-5">
            <div class="card-head card-head-custom">
                <div class="animal-detail">
                    <h2>${ite.nombre.toUpperCase()}</h2>
                    <img src="/media/${ite.imagen}" alt="" class="animal-img">
                    <p>${ite.caracter.toUpperCase()}</p>
                </div>
            </div>
            <div class="card-body card-body-custom">
                <div class="animal-info">
                    <ul>
                        <li><span class="labels">TIPO:</span> ${ite.tipo.toUpperCase()}</li>
                        <li><span class="labels">SALUD:</span> ${ite.salud.toUpperCase()}</li>
                        <li><span class="labels">ALTURA:</span> ${
                          ite.altura.toUpperCase()
                        }</li>
                        <li><span class="labels">PESO:</span> ${ite.peso.toUpperCase()}</li>
                    </ul>
                </div>
                <div class="animal-discription">
                    <h4 class="labels">OBSERVACIONES</h4>
                    <p>${ite.observaciones}</p>
                </div>
            </div>
        </div>
    </div>`;
  }
  document.getElementById("contenedorMascotas").innerHTML = codigo;
}

function clickItem(item) {
  let codigo = "";
  document.getElementById("sugerencias").setAttribute("style", "display: none !important");
  document.getElementById("buscar").value = item.innerHTML;
  document.getElementById("tipo").innerHTML = "";
  document.getElementById("tipo").innerHTML = 'Búsqueda "'+item.innerHTML+'"';
  for (const ite of lista) {
    if (ite.nombre.toLowerCase() == item.innerHTML) {
      codigo += `
      <div class="col-12 col-md-6 col-lg-4 col-xl-3">
          <div class="card card-custom my-5">
              <div class="card-head card-head-custom">
                  <div class="animal-detail">
                      <h2>${ite.nombre}</h2>
                      <img src="/media/${ite.imagen}" alt="" class="animal-img">
                      <p>${ite.caracter.toUpperCase()}</p>
                  </div>
              </div>
              <div class="card-body card-body-custom">
                  <div class="animal-info">
                      <ul>
                          <li><span class="labels">TIPO:</span> ${ite.tipo}</li>
                          <li><span class="labels">SALUD:</span> ${ite.salud}</li>
                          <li><span class="labels">ALTURA:</span> ${
                            ite.altura
                          }</li>
                          <li><span class="labels">PESO:</span> ${ite.peso}</li>
                      </ul>
                  </div>
                  <div class="animal-discription">
                      <h4 class="labels">OBSERVACIONES</h4>
                      <p>${ite.observaciones}</p>
                  </div>
              </div>
          </div>
      </div>`;
    }
  }
  document.getElementById("contenedorMascotas").innerHTML = "";
  document.getElementById("contenedorMascotas").innerHTML = codigo;
}

function razas() {
  let lista_razas = [];
  for (const ite of lista) {
    if (lista_razas.indexOf(ite.tipo) == -1) {
      lista_razas.push(ite.tipo);
    }
  }
  return lista_razas;
}

// function onclickLetter(item, tipo, csrf) {
//   $.ajax({
//     type: "POST",
//     url: "/mascotas/" + tipo,
//     data: { letter: item.value, csrfmiddlewaretoken: csrf },
//     headers: {
//       "X-Requested-With": "XMLHttpRequest",
//       "X-CSRFToken": getCookie("csrftoken"), // don't forget to include the 'getCookie' function
//     },
//     dataType: "json",
//     success: function (response) {
//       console.log("RESPUESTA: " + JSON.stringify(response));
//       codigo = "";
//       document.getElementById("datalistOptions").innerHTML = "";
//       response["lista"].forEach((element) => {
//         codigo += "<option value=" + element + ">";
//       });
//       document.getElementById("datalistOptions").innerHTML = codigo;
//     },
//     error: function (error) {
//       console.log("ERROR: " + +JSON.stringify(error));
//     },
//   });
// }

// function getCookie(name) {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== "") {
//     const cookies = document.cookie.split(";");
//     for (let i = 0; i < cookies.length; i++) {
//       const cookie = cookies[i].trim();
//       // Does this cookie string begin with the name we want?
//       if (cookie.substring(0, name.length + 1) === name + "=") {
//         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//         break;
//       }
//     }
//   }
//   return cookieValue;
// }
