def pre_mutation(context):
    line = context.current_source_line.strip()
    if line.startswith('NOME_') or line.startswith('EMAIL_'):
        context.skip = True
