seg = int(input('Número de segundos a ser convertido '))

dias = seg // 86400
Seg_Restantes_Após_Dias = seg % 86400
horas = Seg_Restantes_Após_Dias // 3600
Seg_Restantes_Apos_Hora = seg % 3600
minutos = Seg_Restantes_Apos_Hora // 60         #
Seg_Restantes_Apos_Minutos = seg % 60

print(dias,'dias',horas,'horas',minutos,'minutos','e',Seg_Restantes_Apos_Minutos,'segundos')