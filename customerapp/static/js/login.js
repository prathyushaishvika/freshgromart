function loginform(){
    username=document.getElementById("name").value ;
    password=document.getElementById("pswd").value ;
    if(username=="" && password==""){
        alert("please enter username and password");
        return false
    }
    else{
        return true
    }

}