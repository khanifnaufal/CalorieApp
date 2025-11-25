# calculator.py

def get_activity_factor(level: str) -> float:
    """Mengembalikan faktor pengali aktivitas."""
    factors = {
        'sedentari': 1.2,
        'ringan': 1.375,
        'sedang': 1.55,
        'berat': 1.725,
        'sangat_berat': 1.9
    }
    return factors.get(level.lower().replace(" ", "_"), 1.2)


def calculate_bmr(gender: str, age: int, weight_kg: float, height_cm: float) -> float:
    """Menghitung BMR (Mifflin-St Jeor)."""
    # Rumus Dasar: (10 * berat) + (6.25 * tinggi) - (5 * usia)
    bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age)
    
    # Tambahkan offset berdasarkan jenis kelamin
    if gender.lower() == 'pria':
        bmr += 5  # Pria: +5
    else: # Wanita
        bmr -= 161 # Wanita: -161
        
    return round(bmr, 0)


def calculate_tdee(bmr: float, activity_level: str) -> float:
    """Menghitung TDEE."""
    factor = get_activity_factor(activity_level)
    tdee = bmr * factor
    return round(tdee, 0)

# --- Akhir calculator.py ---