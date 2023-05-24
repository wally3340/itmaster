"""Escribir un programa para un negocio de venta de granos que desea controlar las ventas
realizadas. De cada venta ingresa el importe total y un código que indica la forma de pago.
Los códigos puede ser:
C: cheque, 20% de recargo.
E: efectivo, 10% de descuento.
T: con tarjeta, 12% de recargo.
Se debe ingresar una F para finalizar el día de venta y arrojar los siguientes totales.
| Forma de Pago | Total |
| ---------------- | --------- | | Efectivo en Caja |  xxxx.xx||Tarjeta/Crédito|  xxxx.xx |
| Cheques |  xxxx.xx||TotaldeVenta|  xxxx.xx | """

importe = int(input("Ingrese el importe: "))
codigo = input("Ingrese el tipo de venta: ")

cheques = importe + (importe * 20 / 100)
efectivo = importe - (importe * 10 / 100 )
tarjeta = importe + (importe * 12 / 100)

importe = 0
codigo = input("<<<Codigo C,E,T,F (Fin)>>>: ").upper()
while codigo != f:
    importe = float(input("ingrese importe: "))
    if codigo = "C"
           
    














print (f"""**************************
       Forma de Pago      Total
       Cheques            xxxx.xx
       Efectivo en caja   xxxx.xx
       Tarjeta/Credito    xxxx.xx
       ******************************
       Total de Ventas    xxxx.xx""")
        