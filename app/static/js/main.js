const getTitleMessageFromCategory = category => {
    const titles = {
        'success': 'Bien Hecho',
        'warning': 'Atencion',
        'info': 'Atencion',
        'error': 'Oops...!',

    }
    return titles[category]
}

function showMessageAlert(category, message) {
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
    })

    Toast.fire({
        icon: category,
        title: getTitleMessageFromCategory(category),
        text: message
    })
}


const $btnTomarFotoServidor = document.querySelector("#btnTomarFotoServidor"),
    $btnIniciarGrabacion = document.querySelector("#btnIniciarGrabacion"),
    $btnDetenerGrabacion = document.querySelector("#btnDetenerGrabacion"),
    $btnEscuchar = document.querySelector("#btnEscuchar"),
    $btnAlertLadron = document.querySelector("#btnAlertLadron"),
    $estado = document.querySelector("#estado");

const obtenerEstadoDeGrabacionYRefrescarVista = async () => {
    const respuestaRaw = await fetch("./estado_grabacion");
    const grabando = await respuestaRaw.json();
    if (grabando) {
        $btnIniciarGrabacion.style.display = "none";
        $btnDetenerGrabacion.style.display = "inline";
    } else {
        $btnIniciarGrabacion.style.display = "inline";
        $btnDetenerGrabacion.style.display = "none";
    }
};
obtenerEstadoDeGrabacionYRefrescarVista();
/*
En el clic del botón hacemos una petición a ./tomar_foto_guardar 
*/
$btnTomarFotoServidor.onclick = async () => {
    $estado.textContent = "Tomando foto...";
    const respuestaRaw = await fetch("./tomar_foto_guardar");
    const respuesta = await respuestaRaw.json();
    let mensaje = "";
    if (respuesta.ok) {
        mensaje = `Foto guardada como ${respuesta.nombre_foto}`;
    } else {
        mensaje = `Error tomando foto`;
    }
    $estado.textContent = mensaje;
};
/*
Iniciar grabación
*/
$btnIniciarGrabacion.onclick = async () => {
    $estado.textContent = "Iniciando grabación...";
    const respuestaRaw = await fetch("./comenzar_grabacion");
    const respuesta = await respuestaRaw.json();
    if (respuesta) {
        $estado.textContent = "Grabación iniciada";
        obtenerEstadoDeGrabacionYRefrescarVista();
    } else {
        $estado.textContent = "Error iniciando grabación";
        obtenerEstadoDeGrabacionYRefrescarVista();
    }
};

$btnDetenerGrabacion.onclick = async () => {
    $estado.textContent = "Deteniendo grabación...";
    const respuestaRaw = await fetch("./detener_grabacion");
    const respuesta = await respuestaRaw.json();
    if (respuesta) {
        $estado.textContent = "Grabación detenida";
        obtenerEstadoDeGrabacionYRefrescarVista();
    } else {
        $estado.textContent = "Error deteniendo grabación";
        obtenerEstadoDeGrabacionYRefrescarVista();
    }
};
/*
En el clic del botón hacemos una voz de alert de ladron 
*/
$btnEscuchar.onclick = async () => {
    console.log('boton escuchar')
    const respuestaRaw = await fetch("./voice");
    const respuesta = await respuestaRaw.json();
    let mensaje = "";
    if (respuesta) {
        mensaje = `voz`;
    } else {
        mensaje = `Error de voz`;
    }
    
   /*const respuestaRaw = await fetch("./voice");
    const respuestaRaw = await fetch("./voice");
    const respuesta = await respuestaRaw.json();
    let mensaje = "";
    if (respuesta) {
        mensaje = `voz`;
    } else {
        mensaje = `Error de voz`;
    }
    */
};