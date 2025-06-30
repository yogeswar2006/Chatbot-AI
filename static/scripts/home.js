let down_btn = document.getElementById("down-arrow");
let down_img=document.getElementById("down-arrow-btn");

 let login_btn=null;
 let logout_btn=null;



let toggled=false;
down_btn.addEventListener("click", () => {
    if(toggled){
        down_img.setAttribute('href',"/static/images/down-btn.svg");
        document.body.removeChild(login_btn);
        document.body.removeChild(logout_btn);
       
    }else{
      down_img.setAttribute('href',"/static/images/up-arrow.svg");
      if(isLoggedIn==="false"){
            login_btn = document.createElement("div");
        

            login_btn.innerHTML = '<a href="/login"  color: inherit;">login</a>';
            login_btn.style.position = "absolute";
            login_btn.style.top = "60px";
            login_btn.style.right = "30px";
            login_btn.style.background = "aqua";
            login_btn.style.color = "black";
            login_btn.style.padding = "8px 16px";
            login_btn.style.borderRadius = "5px";
            login_btn.style.zIndex = "1000";
            document.body.appendChild(login_btn);
       
      }
      else{
            logout_btn = document.createElement("div");
            logout_btn.innerHTML = '<a href="/logout"  color: inherit;">logout</a>';
            logout_btn.style.position = "absolute";
            logout_btn.style.top = "60px";
            logout_btn.style.right = "30px";
            logout_btn.style.background = "aqua";
            logout_btn.style.color = "black";
            logout_btn.style.padding = "8px 16px";
            logout_btn.style.borderRadius = "5px";
            logout_btn.style.zIndex = "1000";

            document.body.appendChild(logout_btn);
            
      }
       
    }
    toggled=!toggled;
});


 document.getElementById("plus-btn").addEventListener("click", function () {
        const form = document.getElementById("room-form");
        form.style.display = form.style.display === "none" ? "block" : "none";
    });
 document.getElementById("plus-btn2").addEventListener("click", function () {
        const form = document.getElementById("room-form2");
        form.style.display = form.style.display === "none" ? "block" : "none";
    });