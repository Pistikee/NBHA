import math

def nbha_hash(input_value: int, multiplier: int, chaos: int) -> int:
    """
    NBHA Hashing Algorithm by Pisti
    - input_value: The number to hash (used as the 'seed' or primary input)
    - multiplier: Influences the math complexity (formerly 'bits')
    - chaos: A scaling factor that affects final range/output (formerly 'bytes')
    """

    # 1. SALT Calculation (acts as a dynamic modifier based on input_value)
    try:
        salt_log = math.log(multiplier, input_value)
    except ValueError:
        salt_log = 0
    salt = (((salt_log * (chaos * multiplier)) * input_value) % (2 ** chaos))

    # 2. HASH Calculation
    try:
        log_term = math.log(multiplier, (input_value * 65536))
    except ValueError:
        log_term = 0

    combo = ((log_term + (input_value * (input_value / multiplier))) % (2 ** chaos))
    
    try:
        inner = (combo + ((salt ** 2) / multiplier))
        sine = math.sin(inner)
    except:
        sine = 0

    final_hash = round(sine * salt)
    return final_hash