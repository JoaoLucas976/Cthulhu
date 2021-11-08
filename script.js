function openProfileMenu(){
	var doc = document.getElementById("dropdown");
	var style = window.getComputedStyle(doc);
	var display = style.getPropertyValue('display');

	if (display == "none"){
		document.getElementById('dropdown').style.display = "inline-block"; 		
	} else {
		document.getElementById('dropdown').style.display = "none"; 	
	}
}

function recoverPass(){
	window.alert("Senha Recuperada");
	window.alert("Confia no pai");
}

function newWork(){
	window.alert("Insira aqui a criação de um upload");
}

window.onclick = function(event){}