def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    count = 0

    for p in permanence_period:
        try:
            if p[0] <= target_time <= p[1]:
                count += 1
        except TypeError:
            return None

    return count
