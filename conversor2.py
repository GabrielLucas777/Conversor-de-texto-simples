import pyttsx3

msg = pyttsx3.init()

msg_usuario = input('Digite o que deseja que seja convertido: ')
msg.say(msg_usuario)
msg.runAndWait()