function validarCantidad(input){

let stock = parseInt(input.dataset.stock)

if(input.value > stock){

alert("No hay suficiente stock")
input.value = stock

}

}

function confirmarPedido(){

return confirm("¿Confirmar pedido?")

}