function signupform(){
    username=document.getElementById("name").value;
    email=document.getElementById("email").value ;
    number=document.getElementById("number").value ;
    password=document.getElementById("pswd1").value ;
    confirmpassword=document.getElementById("pswd2").value ;

    if (fullname==""||number==""||email==""||pswd1==""||pswd2=="")
    {
     document.getElementById('error').innerHTML="all field must be filled out"
     return false
    
    }
    else if( pswd1!=pswd2)
    {
      alert("password not matched")
    }
    else{
      alert("password matched")  
 
      }
      
  }
   
 

