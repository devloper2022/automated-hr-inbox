def rate_candidate(candidate):
    exp = candidate["Experience"]
    if exp <= 1:
        return "Beginner (1⭐)"
    elif exp <= 4:
        return "Intermediate (2⭐)"
    else:
        return "Experienced (3⭐)"
