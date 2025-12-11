import eel

eel.init('web')

@eel.expose
def sayhello(x):
    print("hello"+x)

sayhello('my')
eel.sayhellojs('myjs')

eel.start('index.html')