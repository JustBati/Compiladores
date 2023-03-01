"""Variables globales a utilizar"""


estados_lista=[]
estadosF_lista=[]
estadoI_lista=[]
alfabeto_lista=[]
#creacion de la lista de transiciones
inicio=[]
caracter=[]
fin=[]   
resul=[]

"""
Funcion para leer el archivo txt y almacenar en variables globales la estructura del automata
"""

def leer():
    memo = open("p.txt", "r")
    i=memo.readline()
    estados_lista=i.split(",")

    i=memo.readline()
    estadosF_lista=i.split(",")

    i=memo.readline()
    estadoI_lista=i

    i=memo.readline()
    alfabeto_lista=i.split(",")
    
    
    for i in memo:
        
        j= i.split(",")
        for n in range(3):
            if n==0:
                inicio.append(j[n])
                
            elif n==1:
                caracter.append(j[n])
                

            else:
                fin.append(j[n])
                



    memo.close()
        
def automata(estado_act, cadena_eval, id, mov_real):
    num=0 
    for n in range(len(inicio)):
        if id<len(cadena_eval):
            if(estado_act==inicio[n] and cadena_eval[id]==caracter[n]):
                
                mov_real.append(f"{estado_act}({cadena_eval[id]}) -> {fin[n]} ")
                automata(fin[n],cadena_eval,id+1,mov_real)
    
    

if __name__ == '__main__':   
        
    asd=["a","b"] #aqui pones la cadena a evaluar
    mov_real=[]#aqui se guardan las transiciones
    leer()
    automata("0",asd,0,mov_real)
    resul.append(mov_real)
    
    print(resul)
        
