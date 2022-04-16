

# while(True):
#     correo=input("introduzca la direccion de correo:")
#     contador=0
#     #si hay arroba en correo
#     if "@" in correo:
#         #las cuenta
#         for i in correo:
#             if i=="@":
#                 contador+=1
#         if contador>1:
#                 print("mas de un @")
#                 continue          
#         if correo[0]!="@":

#             if not correo.endswith("@"):
#                 print("re bien")
#                 break
#             else:
#                 print("Termina con @")
#                 continue
#         else:
#             print("empieza con @")
#             continue
#     else:
#         print("no tiene @")
#         continue

# o tambien se puede así

correo=input("introduzca la direccion de correo:")  

cuantasArrobas=correo.count("@")
#print(cuantasArrobas)
#rfind da la posicion del caracter mas pegado al final(si solo hay uno pues da igual)
print(correo.rfind("@"))

if (cuantasArrobas!=1 or correo.find("@")==0 or correo.find("@")==len(correo)-1):
    print("correo mal")
else:
    print("buen correo")    
    
