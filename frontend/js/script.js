const signup_switchingButtton=document.getElementById('signup-switchingButtton');
const signin_switchingButtton=document.getElementById('signin-switchingButtton');
const signup_form=document.getElementById('signup-form');
const signin_form=document.getElementById('signin-form');
const alternate_signup=document.getElementById('alternate-signup');
const password = document.getElementById("signin-password");
const toggleBtn = document.getElementById("toggle-btn");
const eyeIcon = document.getElementById("eye-icon");
const signup_eyeIcon = document.getElementById("signup-eye-icon");
const signup_password = document.getElementById("signup-password");
const signup_toggleBtn = document.getElementById("signup-toggle-btn");
const confirm_password = document.getElementById("confirm-password");


// on click of sign UP switching button event
signup_switchingButtton.addEventListener("click",()=>{
    signup_form.style.display="flex";
    signin_form.style.display="none";

});

// on click of sign IN switching button event
signin_switchingButtton.addEventListener("click",()=>{
    signup_form.style.display="none";
    signin_form.style.display="flex";
});

// on click of botton signup alternative event
alternate_signup.addEventListener("click",function(event){
    event.preventDefault();
    signup_form.style.display="flex";
    signin_form.style.display="none";
});

// password toggle button handling on signin page
toggleBtn.addEventListener("click", function(){

   if(password.type === "password"){

      password.type = "text";
      eyeIcon.classList.remove("fa-eye");
      eyeIcon.classList.add("fa-eye-slash");

   }
   else{

      password.type = "password";
      eyeIcon.classList.remove("fa-eye-slash");
      eyeIcon.classList.add("fa-eye");

   }

});

//password toggling buttton on signup page
signup_toggleBtn.addEventListener("click", function(){

   if(signup_password.type === "password" && confirm_password.type === "password"){

      signup_password.type = "text";
      confirm_password.type = "text";
      signup_eyeIcon.classList.remove("fa-eye");
      signup_eyeIcon.classList.add("fa-eye-slash");

   }
   else{

      signup_password.type = "password";
      confirm_password.type = "password";
      signup_eyeIcon.classList.remove("fa-eye-slash");
      signup_eyeIcon.classList.add("fa-eye");

   }

});

// signup page backend connection
const signupForm = document.querySelector("#signup-form form");

signupForm.addEventListener("submit", async function(event){
    event.preventDefault();
    const username = document.querySelector("#username").value;
    const email = document.querySelector("#signup-email").value;
    const password = document.querySelector("#signup-password").value;

    const userData={
        username:username,
        email:email,
        password:password
    }
    console.log(userData)

    const response = await fetch("http://127.0.0.1:8000/auth/signup", {

        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(userData)
    });
    const data = await response.json();
    console.log(data);
    if(response.ok) {
        alert("Signup successful! Please sign in.");
    }
    else{
        console.error(data.detal);
    }


})

// signin page backend connection
const signinForm = document.querySelector("#signin-form form");
signinForm.addEventListener("submit", async function(event){
    event.preventDefault();
    const email = document.querySelector("#signin-email").value;
    const password = document.querySelector("#signin-password").value;
    const credentials = {
        email:email,
        password:password
    }
    const formData = new URLSearchParams();
    formData.append("username", email);
    formData.append("password", password);
    console.log(credentials);
    const response=await fetch("http://127.0.0.1:8000/auth/login",{
        method:"POST",
        headers:{
            "Content-Type":"application/x-www-form-urlencoded"
        },
        body:formData
    });
    const data=await response.json();
    console.log(data);
    if(response.ok){
        alert("Login successful!");
    }
    else{
        console.error(data.detail);
    }

})