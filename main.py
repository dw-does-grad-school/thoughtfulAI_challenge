def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Dispatch a package to the correct stack based on its dimensions and mass.

    - Bulky if volume >= 1,000,000 cm³ or any dimension >= 150 cm.
    - Heavy if mass >= 20 kg.
    - Rejected if both bulky and heavy.
    - Special if bulky or heavy (but not both).
    - Standard otherwise.

    Returns one of: "STANDARD", "SPECIAL", "REJECTED".
    """
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or any(d >= 150 for d in (width, height, length))
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"
