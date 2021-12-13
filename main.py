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
        ombro_esquerdo = client.simxGetObjectHandle("l_shoulder_joint", client.simxServiceCall())
        joelho_direito = client.simxGetObjectHandle("r_knee_joint", client.simxServiceCall())
        joelho_esquerdo = client.simxGetObjectHandle("l_knee_joint", client.simxServiceCall())
        quadril_direito = client.simxGetObjectHandle("r_hip_joint", client.simxServiceCall())
        quadril_esquerdo = client.simxGetObjectHandle("l_hip_joint", client.simxServiceCall())
        coxa_direita = client.simxGetObjectHandle("r_thigh_joint", client.simxServiceCall())
        coxa_esquerda = client.simxGetObjectHandle("l_thigh_joint", client.simxServiceCall())
        pescoco = client.simxGetObjectHandle("neck_joint", client.simxServiceCall())
        tornozelo_direito = client.simxGetObjectHandle("r_ankle_joint", client.simxServiceCall())
        tornozelo_esquerdo = client.simxGetObjectHandle("l_ankle_joint", client.simxServiceCall())
        pe_direito = client.simxGetObjectHandle("r_foot_joint", client.simxServiceCall())
        pe_esquerdo = client.simxGetObjectHandle("l_foot_joint", client.simxServiceCall())
        biceps_direito = client.simxGetObjectHandle("r_biceps_joint", client.simxServiceCall())
        biceps_esquerdo = client.simxGetObjectHandle("l_biceps_joint", client.simxServiceCall())
        cotovelo_direito = client.simxGetObjectHandle("r_elbow_joint", client.simxServiceCall())
        cotovelo_esquerdo = client.simxGetObjectHandle("l_elbow_joint", client.simxServiceCall())
        client.simxSetJointTargetPosition(ombro_direito[1], ((degree*PI)/180), client.simxServiceCall()) # mexe o braço do Darwin
        #client.simxSetJointTargetPosition(coxa_direita[1], ((10*PI)/180), client.simxServiceCall())
        #client.simxSetJointTargetPosition(tornozelo_esquerdo[1], ((-10*PI)/180), client.simxServiceCall())
        #client.simxSetJointTargetPosition(quadril_direito[1], ((10*PI)/180), client.simxServiceCall())
        client.simxSetJointTargetPosition(quadril_esquerdo[1], ((30*PI)/180), client.simxServiceCall())
        time.sleep(0.5)
        client.simxSetJointTargetPosition(quadril_esquerdo[1], ((0*PI)/180), client.simxServiceCall())
        client.simxSetJointTargetPosition(ombro_esquerdo[1], ((-degree*PI)/180), client.simxServiceCall()) # mexe o braço do Darwin
        # angulacao de rotacao do braço do darwin
        if degree < 30:
            degree += 30
        else:
            degree -= 30
        
        # delay pra não rodar muitas vezes por segundo
        time.sleep(0.5)

        # parar código quando a cena parar
        if((client.simxGetSimulationState(client.simxServiceCall())[1] == 0)):
            break