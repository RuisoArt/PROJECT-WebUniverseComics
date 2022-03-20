

function usrpas()
{
	if (document.form1.user.value=="felipe" && document.form1.pass.value=="159951")
		{
            window.location="../my_app/templates/universes/home.html"
		}
	 
	else 
		{
			alert("ERROR \n Ingreso de credenciales falsas \n WORLD COMICS \n Si está intentando acceder sin conocer las credenciales correctas \n Absténgase por su bien de seguir intentando.")
		}
}
document.oncontextmenu=new Function("return false");