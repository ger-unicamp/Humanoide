import b0RemoteApi
from math import pi as PI
import time

with b0RemoteApi.RemoteApiClient('b0RemoteApi_pythonClient','b0RemoteApi',60) as client:
   
    client.simxAddStatusbarMessage('Hello',client.simxDefaultPublisher()) # mensagem que aparece no coppelia ao rodar o código

    client.simxStartSimulation(client.simxDefaultPublisher()) # comando para iniciar a simulação
    
    degree = 90
    while True:
        # Looping principal

        print("Estou rodando!")
        ombro_direito = client.simxGetObjectHandle("r_shoulder_joint", client.simxServiceCall()) # modelo para pegar handle na cena
        
        client.simxSetJointTargetPosition(ombro_direito[1], ((degree*PI)/180), client.simxServiceCall()) # mexe o braço do Darwin
        
        # angualacao de rotacao do braço do darwin
        if degree < 180:
            degree += 30
        else:
            degree -= 100
        
        # delay pra não rodar muitas vezes por segundo
        time.sleep(0.5)

        # parar código quando a cena parar
        if((client.simxGetSimulationState(client.simxServiceCall())[1] == 0)):
            break