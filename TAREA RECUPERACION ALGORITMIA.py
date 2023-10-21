























apuesta=int(input("ingrese el valor de dinero que desea apostar:"))
valor=int(apuesta/2*2)
validad=1000
if valor >= validad:
  print("bienvenido jugador")
  dado1=int(input("cuanto salio en  el primer dado:"))
  dado2=int(input("cuanto salio en el segundo dado:"))
  dado3=int(input("cuanto salio en el tercer dado:"))
  dados =(dado1 + dado2 + dado3)

  if dado1==dado2 and dado1==dado3:
    print("Ohhh que bien tu apuesta ha sido multiplicada de", apuesta, "a", apuesta *10)
  elif dado1 == dado2 or dado1 == dado3:
    print("Tremendo, HAS MULTIPLICADO TU APUESTA ", apuesta, "a", apuesta *5)
  elif dados >= 13:
    print("Has recuperado tu apuesta, genial")
  elif dados >12:
    print("Has perdido la mitad de tu apuesta, que mala suerte :", apuesta/2)
  elif dados> 7  and dados<13:
    print("Has perdido la apuesta, intenta de nuevo")
else:
  print("Cantidad Denegada ")




print("Hola somos Sigma7, ingresa los detalles del envío:")
zona = int(input("Zona del envío (1 a 5): "))   
peso = float(input("Peso del envío en Kg: "))

# Validar que el peso sea <= 50Kg
print("Validacion del peso...")
if peso > 50:
    print("El peso supera el limite establecido")
else:
    print("Peso Recibido!")

    # Calcular el costo según la zona 
    print("Procesando Costo Por la Zona...")        
    if zona == 1:
       costo = peso * 97
       print("Zona Norte américa ")                
    elif zona == 2:           
       costo = peso * 70
       print("Zona Centroamérica ")                 
    elif zona == 3:
       costo = peso * 50  
       print("Zona Sur américa ")                  
    elif zona == 4:
       costo = peso * 100
       print("Zona Europa ")                      
    elif zona == 5:
       costo = peso * 120
       print("Zona Asia ")

    # Convertir a pesos colombianos al cambio de 4.750                 
    print("Conversion a COP...")       
    cobro = costo * 4750

    # Imprimir el cobro
    print("El cobro total en COP es: $", cobro)