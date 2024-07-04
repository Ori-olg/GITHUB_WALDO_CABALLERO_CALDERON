import FUNCIONES_WALDO_CABALLERO_CALDERON as funy;
import random as rd;

op = 0; monto_hospi_diario = 90000;
l_pacientes = [];
sectores = ["Centro","Norte","Sur"];

print(f"Su numero de la suerte hoy es: {rd.randint(1,100)}! :D")

while (op != 4):

    op = int(input("""1. Registrar cobro
2. Listar cobros registrados
3. Definir sector de despacho
4. Salir"""));

    if (op == 1):
        funy.uno(l_pacientes,monto_hospi_diario);
    elif(op == 2):
        funy.dos(l_pacientes);
    elif(op == 3):
        pass;
print("Programa cerrado\nQue tenga buen dia/tarde/noche.");