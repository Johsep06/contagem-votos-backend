from collections import Counter

from src import filtro

def contar_eleitores_por_turno(eleitores:list[dict]):
    turnos = filtro.recuperar_turno(eleitores)
    return Counter(turnos)

def contar_eleitores_por_turma(eleitores:list[dict]):
    turmas = filtro.recuperar_turma(eleitores)
    return Counter(turmas)

def contar_eleitores_por_registro(eleitores:list[dict]):
    registros = filtro.recuperar_registro(eleitores)
    return Counter(registros)

def contar_votos(eleitores:list[dict]):
    votos = filtro.recuperar_votos(eleitores)
    return Counter(votos)