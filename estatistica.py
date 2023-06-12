import math as mt

# criando estastitica e probabilidade 

class Estatistica:
    
    # def __init__(self):
    #     pass
    
    def hipergeometrica(self, **valor):
        
        if 'N' in valor and 'n' in valor and 'x' in valor and 'r' in valor:
            probabilidade = (mt.comb(valor['r'],valor['x']) * mt.comb(valor['N']-valor['r'],valor['n']-valor['x'])) / mt.comb(valor['N'],valor['n'])
            variavel = lambda x: f'{x * 100:.2f}%'  
            result = variavel(probabilidade)
        else:           
            lista_argumentos = ['N','n','x','r']         
            result = [print(f'esqueceu de {arg}') for arg in lista_argumentos if arg not in valor]
                                 
        return result
    
    def binominal(self,**valor):
        
        if 'n' in valor and 'p' in valor and 'k' in valor:
            probabilidade = mt.comb(valor['n'],valor['k']) * mt.pow(valor['p'],valor['k']) * mt.pow(1-valor['p'],valor['n']-valor['k'])
            
            variavel = lambda x:f'{x * 100:.2f}%'
            result = variavel(probabilidade)   
        else:    
            lista_argumentos = ['n','p','k']
            result = [print(f'esqueceu de {arg}') for arg in lista_argumentos if arg not in valor]
            
        return result
    
    def teorema_bayes(self,**valor):
        
        if 'a' in valor and 'b' in valor and 'ba' in valor:
            variavel = (valor['ba'] * valor['a']) / valor['b']
                     
        if 'a' in valor and 'b' in valor and 'ab' in valor:
            variavel = (valor['ab'] * valor['b']) / valor['a']
            
        result = variavel  
        result = f'{result * 100:.2f}%' 
           
        return result
    
    def geometrica(self,**valor):
        
        if 'p' in valor and 'k' in valor:
            x = valor['p'] * (mt.pow(1 - valor['p'],valor['k'] - 1))
            result = f'{x * 100:.2f}%'
        else:           
            lista_argumentos = ['p','k']         
            result = [print(f'esqueceu de {arg}') for arg in lista_argumentos if arg not in valor]  
        
        return result
    
    def poisson(self,**valor):
        
        if 'q' in valor and 'x' in valor:
            p = mt.exp(-valor['q']) * (mt.pow(valor['q'],valor['x']) / mt.factorial(valor['x']))
            result =f'{p *100:.2f}%'
        else:           
            lista_argumentos = ['q','x']         
            result = [print(f'esqueceu de {arg}') for arg in lista_argumentos if arg not in valor]      
            
        return result
    
    
    
    
    

