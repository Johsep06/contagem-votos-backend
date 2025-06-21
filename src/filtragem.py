from collections import Counter

from . import leitura

def remover_duplicatas(registros:list[dict]):
    matriculas = leitura.recuperar_matricula(registros)
    
    contagem_matriculas = Counter(matriculas)
    matriculas_com_uma_ocorrencia = []

    for registro in registros:
        matricula = registro['Número de matrícula']
        
        if contagem_matriculas[matricula]  == 1:
            matriculas_com_uma_ocorrencia.append(registro)
            
    return matriculas_com_uma_ocorrencia

def remover_calouros(registros:list[dict]):
    lista_sem_calouro = []

    for registro in registros:
        ano_matricula = registro['Número de matrícula'][:4]
        if ano_matricula < '2025':
            lista_sem_calouro.append(registro)
    
    return lista_sem_calouro

def remover_menbros_ca(registros:list[dict]):
    matriculas_menbros_ca = [
        '202133840007',
        '202133840011',
        '202133840036',
        '202133840028',
        '202133840033',
        '202133840035',
        '202133840021',
        '202133840005',
    ]
    
    registros_sem_menbros_do_ca = []
    for registro in registros:
        matricula = registro['Número de matrícula']
        if matricula not in matriculas_menbros_ca:
            registros_sem_menbros_do_ca.append(registro)
            
    return registros_sem_menbros_do_ca

def remover_registros_fora_de_hora(registros:list[dict]):
    registros_validos = []

    for registro in registros:
        hora = registro['Carimbo de data/hora']
        if '23/06/2025 07:59' < hora < "23/06/2025 18:00":
            registros_validos.append(registro)

    return registros_validos

def recuperar_votos_filtrados(votos:list[dict]):
    votos_sem_duplicatas = remover_duplicatas(votos)
    votos_sem_calouros = remover_calouros(votos_sem_duplicatas)
    votos_sem_menbros_ca = remover_menbros_ca(votos_sem_calouros)
    votos_validos = remover_registros_fora_de_hora(votos_sem_menbros_ca)
    
    return votos_validos