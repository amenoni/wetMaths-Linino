from firebase import firebase

firebase = firebase.FirebaseApplication('https://resplendent-torch-6152.firebaseio.com', None)

def sendMessage(message):
    #use example, we are calling this method in game post_save
    result = firebase.post('/mensaje',message)