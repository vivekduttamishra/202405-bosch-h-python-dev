def plot_histogram(frequency):
    design='=== '
    for value,frequency in frequency.items():
        print(f'{value}|{design*frequency} {frequency}')