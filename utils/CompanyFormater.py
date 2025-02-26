def formatCompanyCode(code):
    """Formata a inscrição estadual no formato XX.XXX.XXX-X"""
    return f"{code[:2]}.{code[2:5]}.{code[5:8]}-{code[8]}"
