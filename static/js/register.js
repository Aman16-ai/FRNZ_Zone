console.clear();

const loginBtn = document.getElementById('login');
const signupBtn = document.getElementById('signup');

loginBtn.addEventListener('click', (e) => {
	let parent = e.target.parentNode.parentNode;
	Array.from(e.target.parentNode.parentNode.classList).find((element) => {
		if(element !== "slide-up") {
			parent.classList.add('slide-up')
		}else{
			signupBtn.parentNode.classList.add('slide-up')
			parent.classList.remove('slide-up')
		}
	});
});

signupBtn.addEventListener('click', (e) => {
	let parent = e.target.parentNode;
	Array.from(e.target.parentNode.classList).find((element) => {
		if(element !== "slide-up") {
			parent.classList.add('slide-up')
		}else{
			loginBtn.parentNode.parentNode.classList.add('slide-up')
			parent.classList.remove('slide-up')
		}
	});
});

function validationHandler() {

	let firstName = document.getElementById('firstNametxt').value;
	let lastName = document.getElementById('lastNametxt').value;
	let userName = document.getElementById('userNametxt').value;
	let password = document.getElementById('passwordtxt').value;


	if((firstName === '' || firstName === ' ') || (lastName === '' || lastName === ' ') || (userName === "" || userName === " ")) {
		alert("please enter valid data")
		return false;
	}
	else if(password.length < 5) {
		alert("password must be greated than 5");
		return false;
	}
	else {
		return true
	}
	
}