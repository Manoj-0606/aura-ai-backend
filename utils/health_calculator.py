def calculate_bmi(weight, height_cm):

    height_m = float(height_cm) / 100

    bmi = float(weight) / (height_m * height_m)

    return round(bmi, 2)


def fat_loss_calories(weight):

    maintenance = float(weight) * 30

    fat_loss = maintenance - 500

    return int(maintenance), int(fat_loss)


def protein_requirement(weight):

    protein = float(weight) * 1.8

    return int(protein)