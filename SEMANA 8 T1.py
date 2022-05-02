def signo(dia, mes):  #FUNÇÃO SIGNO DEFINIDA COM OS PARÂMETROS DIA E MES.
  if mes == 3:
    return 'Peixes' if dia < 21 else 'Áries'
  if mes == 4:
    return 'Áries' if dia < 20 else 'Touro'
  if mes == 5:
    return 'Touro' if dia < 21 else 'Gêmeos'
  if mes == 6:
    return 'Gêmeos' if dia < 22 else 'Câncer'
  if mes == 7:
    return 'Câncer' if dia < 23 else 'Leão'
  if mes == 8:
    return 'Leão' if dia < 23 else 'Virgem'
  if mes == 9:
    return 'Virgem' if dia < 23 else 'Libra'
  if mes == 10:
    return 'Libra' if dia < 23 else 'Escorpião'
  if mes == 11:
    return 'Escorpião' if dia < 22 else 'Sagitário'
  if mes == 12:
    return 'Sagitário' if dia < 22 else 'Capricórnio'
  if mes == 1:
    return 'Capricórnio' if dia < 20 else 'Aquário'
  if mes == 2:
    return 'Aquário' if dia < 19 else 'Peixes'



def remover_acentos(texto): #FUNÇÃO remover_acentos DEFINIDA COM UM PARÂMETRO IDENTIFICADO COMO texto.
  from unicodedata import normalize #IMPORTO A FUNÇÃO NORMALIZE DO MÓDULO UNICODEDATA

  return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII') #A FUNÇÃO NORMALIZE RECEBE
  #DOIS PARÂMETROS, ENCODE QUE FAZ A CONVERSÃO DO UNICODE PARA ASCII E IGNORA QUALQUER CARACTERE QUE
  # NAO PUDER SER CONVERTIDO; E O OUTRO PARÂMETRO, A FUNÇÃO DECODE É CHAMADA PARA RECONVERTER A FUNÇÃO
  #ENCONDE EM UMA STRING LITERAL.



def horoscopo(signo_desejado):   #DEFINIDA A FUNÇÃO HORÓSCOPO COM O PARÂMETRO DEFINIDO signo_desejado
  import urllib.request #IMPORTO A FUNÇÃO request DO MÓDULO urllib

  signo_formatado = remover_acentos(signo_desejado).lower() #CHAMO A FUNÇÃO remover_acentos QUE TEM COMO
  #PARÂMETRO, O PRÓPRIO PARÂMETRO DA FUNÇÃO horoscopo(signo_desejado), E CONVERTO TODA A STRING PRA 
  #MINÚSCULA.
  minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado #VARIÁVEL minha_url
  #RECEBE UM ENDEREÇO('https://www.horoscopovirtual.com.br/horoscopo/') + A VARIÁVEL signo_formatado

  requisicao = urllib.request.Request(
      url=minha_url,
      headers={'User-Agent':'Mozila/5.0'} #REQUISIÇÃO PRA PODER ENTRAR NA URL(DA VARIÁVEL minha_url) 
      #IDENTIFICANDO O NAVEGADOR QUE VOU USAR.
  )


  resposta = urllib.request.urlopen(requisicao) #EXECUTO A AÇÃO DE ABRIR O SITE.

  pagina = resposta.read().decode('utf-8') #LER A PÁGINA EXECUTADA E DECODIFICÁ-LA NO SISTEMA DE CARACTERES
  #UTF-8

  marcador_inicio = '<p class="text-pred">' #INÍCIO DA SELEÇÃO
  marcador_final = '</p>' #FINAL DA SELEÇÃO

  inicio = pagina.find(marcador_inicio) + len(marcador_inicio) #PROCURAR ALGO NA PÁGINA A PARTIR DO VALOR
  #DA VARIÁVEL marcador_inicio
  final = pagina.find(marcador_final, inicio)#AQUI ACABA A MINHA PESQUISA NA PÁGINA.

  return signo_desejado + ': ' + pagina[inicio:final] #RETORNAR O SIGNO DESEJADO + O QUE CONTÉM
  #NA PÁGINA NA PARTE QUE EU DEMARQUEI A PROCURA.([inicio:final])


  
def separar_data(dma): #FUNCAO DEFINIDA PRA FORMATAR A DATA, COM VARIÁVEL dma
    a = dma % 10000 # RESTO DE dma%10000
    dma //= 10000  # A DIVISÃO EXATA ENTRE O VALOR DA dma E 1000 RESULTA NO ANO.

    m = dma % 100  # O RESTO DA DIVISÃO ENTRE dma e 100 .
    dma //= 100 # E A DIVISÃO EXATA ENTRE dma e 100 RESULTA NO MÊS.

    d = dma 
    return d, m, a #RETORNO d, m, a




def main(): #FUNÇÃO PRINCIPAL DEFINIDA.
    #ENTRADA DE DADOS
    nascimento = int(input("Digite sua data de nascimento no formato DD/MMAAA: "))

    #PROCESSAMENTO
    dia, mes, _ = separar_data(nascimento) #CHAMO A FUNÇÃO separar_data e uso como PARÂMETRO A VARIÁVEL
    #nascimento
    meu_signo = signo(dia, mes) #CHAMO A FUNÇÃO signo E USO AS VARIÁVEIS dia, mes, _ COMO PARÂMETROS
    horoscopo_de_hoje = horoscopo(meu_signo) #CHAMO A FUNÇÃO horoscopo
    #SAÍDA DE DADOS
    print(horoscopo_de_hoje)




if __name__ == '__main__': #EXECUTO A FUNÇÃO main(), CASO __name__ == '__main__'
  main()  