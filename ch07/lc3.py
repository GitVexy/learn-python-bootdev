def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
    
    distance = distance_one_way * 2

    return energy_available >= distance / meters_per_energy
