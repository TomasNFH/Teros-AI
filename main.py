tarea = 'descarga de camiones a ibc'
sustancia = 'soda cáustica'
condiciones_entorno = 'Es un lugar cerrado, el lugar tiene ventilación, zona de descarga claramente señalizada, hay duchas de emergencia y lava ojos accesibles y funcionando cerca del área de trabajo, recipientes y equipos etiquetados y en buen estado.'
operario = 'Juan'

def funcion_de_riesgo(tarea, sustancia, condiciones_entorno, operario):

  Prompt1 = 'Quiero que me brindes un checklist como una lista de strings de condiciones que tiene que cumplir el operario (ejemplo usar casco, guantes, mascarilla, lentes, etc. ), de realizar la tarea de'+tarea+'de'+sustancia+'en una fabrica de BASF. Quiero que utilices el documento de hoja de seguridad BASF que te adjunto como referencia y la hoja de datos de seguridad de '+sustancia+' para que verifique qué tiene que cumplir el operario (ej> si es GHS05 - corrosiva, que use guantes, mascarilla si es GHS08 Sensibilizante respiratorio , etc.). No quiero que incluyas posibles procedimientos en caso de emergencia, solo que conciderar.'
  print(Prompt1)

  
  riesgo_opeerador = 0
  riesgo_hambiental = 0
  return [riesgo_opeerador, riesgo_hambiental]
