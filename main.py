tarea = 'descarga de camiones a ibc'
sustancia = 'soda cáustica'

def funcion_de_riesgo(tarea, sustancia, condiciones_entorno):

  Prompt1 = 'Quiero que me brindes un checklist como un archivo .txt de condiciones que tiene que cumplir el operario (ejemplo usar casco, guantes, mascarilla, lentes, etc. ), de realizar la tarea de'+tarea+'de'+sustancia+'en una fabrica de BASF. Quiero que utilices el documento de hoja de seguridad BASF que te adjunto como referencia y la hoja de datos de seguridad de '+sustancia+' para que verifique qué tiene que cumplir el operario (ej> si es GHS05 - corrosiva, que use guantes, mascarilla si es GHS08 Sensibilizante respiratorio , etc.). No quiero que incluyas posibles procedimientos en caso de emergencia, solo que conciderar.'
  print(Prompt1)

