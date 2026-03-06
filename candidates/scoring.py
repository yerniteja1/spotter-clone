from django.utils import timezone

REQUIRED_SKILLS = {"react", "django", "python"}
BONUS_SKILLS    = {"docker", "redis", "typescript", "postgresql", "aws", "kubernetes"}

WEIGHTS = {
    "experience": 30,
    "required_skills": 40,
    "bonus_skills": 20,
    "recency": 10,
}

def calculate_score(candidate):
    score = 0.0

    # 1. Experience — max 30 points
    exp = min(candidate.years_experience, 10)
    score += (exp / 10) * WEIGHTS["experience"]

    # 2. Required skills — max 40 points
    candidate_skills = set(s.lower() for s in candidate.skills)
    matched_required = candidate_skills & REQUIRED_SKILLS
    score += (len(matched_required) / len(REQUIRED_SKILLS)) * WEIGHTS["required_skills"]

    # 3. Bonus skills — max 20 points
    matched_bonus = candidate_skills & BONUS_SKILLS
    bonus = len(matched_bonus) * 5
    score += min(bonus, WEIGHTS["bonus_skills"])

    # 4. Recency — max 10 points
    # applied_at is None before first save — handle that edge case
    if candidate.applied_at:
        days_ago = (timezone.now() - candidate.applied_at).days
        if days_ago <= 7:
            score += WEIGHTS["recency"]
        elif days_ago <= 30:
            score += WEIGHTS["recency"] * 0.5

    return round(score, 2)