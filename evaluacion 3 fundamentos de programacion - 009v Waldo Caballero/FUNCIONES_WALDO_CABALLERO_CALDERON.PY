def uno(arr,variable_costo_dia):
    paciente = {};
        
    nombre = input("Ingrese nombre del paciente");
    paciente["Nombre"] = nombre;
        
    apellido = input("Ingrese apellido del paciente");
    paciente["Apellido"] = apellido;
        
    direccion = input("Ingrese direccion del paciente");
    paciente["Direccion"] = direccion;
        
    total_ch = int(input("Ingrese dias hospitalizado"));
    total_ch = total_ch*variable_costo_dia;
    paciente["por_ch"] = total_ch;
        
    total_im = int(input("Ingrese total por insumos"));
    paciente["por_im"] = total_im;

    total_bono = int(input("Ingrese porcentaje de bonificacion del sistema de salud"));
    paciente["Bonificacion"] = (total_ch+total_im)*(total_bono/100);
        
    paciente["total_pg"] = (total_ch+total_im) - total_bono;
        
    arr.append(paciente);
    
def dos(arr):
    print("Paciente\t\tDireccion\tHospitalizacion\t\tInsumos\t\tBonificacion\t\tTotal")
    for i in range(len(arr)):
        print(f"{arr[i]["Nombre"]} {arr[i]["Apellido"]}\t\t{arr[i]["Direccion"]}\t\t{arr[i]["por_ch"]}\t\t\t{arr[i]["por_im"]}\t\t{arr[i]["Bonificacion"]}\t\t{arr[i]["total_pg"]}");