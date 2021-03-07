from Abre_Json import Abre_Json 

arquivo = 'C:/Users/thale/Desktop/Aulas Alura/Python 3 Trabalhando com IO/pythonio-projeto-inicial/dados/contatos.json' #Local de onde o arquivo .json está 


objeto = Abre_Json(arquivo) #Transforma o arquivo em um objeto da classe Abre_Json

#print(objeto) #Printa o local da memoria alocada o objeto objeto só pra ver se deu certo mesmo...

#objeto_lista = objeto.apenas_le_json_retorna_lista_python() #Abre o arquivo e lê e retorna em lista do Pyhton, equivalente a um objeto array do Json, portanto se lê o conteudo como lista do Pyhton

#print(objeto_lista) #Printa o Conteudo do arquivo Json como uma lista do Python

#objeto_string = objeto.le_json_retorna_string_de_json(3) #Abre o arquivo, lê e retorna como string de Json, deve se colocar a identação!

#print(objeto_string) #Imprime o conteudo como uma String de Python, tambem sendo uma string de Json, pelo menos eu acho.... 
