def normalize_arguments(values):
    sequences = ("list","tuple")
    if len(values)==1 and type(values[0]).__name__ in sequences:
        values = values[0]   

    return values