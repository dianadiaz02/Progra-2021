#!/usr/bin/env python
# coding: utf-8




#Universidad del Valle de Guatemala                   Diana Díaz 21066
#Algoritmos y programación                            Sección: 90





#Dar la bienvenida al programa





import turtle
print("Bienvenido/a al sistema de vacunación Guatemala")





nombre=input(str("Ingrese sus nombres y apellidos:"))





#Hacerle recordatorio que hay que responder con honestidad





print("Recuerde que vamos en Fase I, por favor responder con honestidad")





print("Ingrese su CUI")
dpi=input()





#Hacer la lista con las preguntas





def preguntas():
    resultado = []
    print("Por favor no incluir tildes")

    print("¿Es usted es trabajador de establecimientos de salud assitencial que atiende pacientes con COVID-19?")
    res1=input()
    resultado.append(res1.lower().strip())
    print("¿Es usted trabajador de establecimientos de saludasistencial no incluidos en sub-fase 1 y comunitariosde apoyo?")
    res2=input()
    resultado.append(res2.lower().strip())
    print("¿Es usted parte de algún establecimiento de salud?")
    res3=input()
    resultado.append(res3.lower().strip())
    print("¿Es usted estudiante de medicina y practicante?")
    res4=input()
    resultado.append(res4.lower().strip())
    print("¿Es usted parte de trabajos funerarios?")
    res5=input()
    resultado.append(res5.lower().strip())
    print("¿Es usted trabajor de alguna institución de adultos mayores?")
    res6=input()
    resultado.append(res6.lower().strip())
    print("¿Usted se encuentra en algún hogar/institución de adultos mayores?")
    res7=input()
    resultado.append(res7.lower().strip())
    print("¿Es usted mayor de 70 años?")
    res8=input()
    resultado.append(res8.lower().strip())

    print("¿Usted padece de alguna de estas condiciones: Hipertensión arterial que requiere medicamento, diabetes mellitus, \n enfermedad pulmonar crónica, enfermedad renal crónica, enfermedades cardiovasculares y cerebrovasculares,\n inmunosupresión (VIH,cáncer, uso de inmunosupresores) u obesidad?")
    res9=input()
    resultado.append(res9.lower().strip())

    return resultado




#Crear una definición para cuando no esté en el grupo para la vacunación





def no_lista ():
    import turtle
       
    t=turtle.Pen()
    t.color("red")
    t.penup()
    t.goto(-175,250)
    t.pendown
    t.begin_fill()
    for i in range (8):
        t.forward(200)
        t.right(45)
    t.end_fill()
    t.penup()
    t.goto(25,-25)
    t.left(90)

    t.color("black")
    t.goto(-70,80)
    t.write("No pertenece", font=("Impact", "40"), align="center")

    t.penup()
    t.goto(-70,15)
    t.pendown()
    t.write("al grupo actual", font=("Impact", "40"), align="center")

    t.penup()
    t.goto(-70,-60)
    t.pendown()
    t.write("de vacunacion", font=("Impact", "40"), align="center")
    





#Crear una definicón para cuando le toque turno para la vacuna





def lista(turno):
    import turtle
    t=turtle
    t.color("green")
    t.penup()
    t.goto(-250, 250)
    t.pendown()
    t.begin_fill()
    for i in range (2):
        t.forward(500)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()


    t.color("black")
    t.penup()
    t.goto(0, 200)
    t.pendown()
    t.write("El turno asignado es: ", font=("Cosmic Sans", "30"), align="center")

    t.penup()
    t.goto(0,100)
    t.pendown()
    t.write(str(turno), font=("Cosmic Sans", "30"), align="center")
   




#Descartar si está en el grupo o no





def res_final(respuestas, turno):
    if "si" in respuestas:
        return lista(turno)
    return no_lista()





#hacer el conteo para los turno y verificar si quiere salir del programa





def main():
    cola = 1
    salir_programa = False
    while salir_programa == False:
        resultado = preguntas()
        res_final(resultado, cola)
        salir = input("Desesa salir del programa ? (s/n)")
        if (salir == "s"):
            salir_programa = True
        cola += 1
        turtle.Screen().reset()





main()





#cuando salga del programa, hacerle unos avisos





print("No olvide presentar su papelería al centro de vacunación")
print("Gracias por su honestidad")







