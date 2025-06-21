def recuperar_matricula(registro:list[dict]):
    matriculas_mapeadas = map(lambda d: d['Número de matrícula'], registro)
    return list(matriculas_mapeadas)

def recuperar_votos(registro:list[dict]):
    matriculas_mapeadas = map(lambda d: d['Voto'], registro)
    return list(matriculas_mapeadas)

def recuperar_turno(registro:list[dict]):
    matriculas_mapeadas = map(lambda d: d['Turno'], registro)
    return list(matriculas_mapeadas)

def recuperar_turma(registro:list[dict]):
    matriculas_mapeadas = map(lambda d: d['Turma'], registro)
    return list(matriculas_mapeadas)

def recuperar_registro(registro:list[dict]):
    matriculas_mapeadas = map(lambda d: d['Carimbo de data/hora'], registro)
    return list(matriculas_mapeadas)