from clases.models import Clases

c1= Clases(nombre="Sublime Text 2", descripcion="Clase de Sublimte Text 2 donde aprenderemos consejos y trucos de este gran editor", url="_gs_EIPkMVo",thumb="sublime2.png")

c2= Clases(nombre="Motores Render de los Browsers", descripcion="Descripcion de cuales son los motores render que usan actualmente los navegadores y su importancia", url="hfGVnq7to0w",thumb="motores.png")

c3= Clases(nombre="Mide y organiza tus proyectos web como la gente atractiva", descripcion="Aprender a organizar y optimizar tus proyectos de forma correcta", url="hC_blYTGYhY",thumb="organiza.png")

c4= Clases(nombre="La importancia del Responsive Design @LeonidasEsteban", descripcion="Charla de @LeonidasEsteban sobre la importancia del Responsive Design en la web", url="YnphMCRsdXM",thumb="responsive.png")

c1.save()
c2.save()
c3.save()
c4.save()
