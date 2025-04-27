prior_skills = {
    "typescript": "javascript",
    "react": "html",
    "tailwind": "css",
    "next": "react"
}

class InvalidSkill(Exception):
    pass

def check_skill(skill):
    prior_skill = prior_skills[skill]
    if prior_skills[skill]:
        raise InvalidSkill(f"You must know {prior_skill} prior learning {skill}.")
    return True

try:
    check_skill("typescript")
    # check_skill("tailwind")
    # check_skill("react")
    # check_skill("next")
    
except InvalidSkill as e:
    print(e)