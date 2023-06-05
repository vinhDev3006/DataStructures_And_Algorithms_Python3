requirements_needed = {
    "Web development",
    "Mobile development",
    "Cloud computing",
    "Internet of Things",
    "Blockchain",
    "Virtual reality",
    "Natural language processing",
    "Robotics",
    "Data analytics",
    "Cybersecurity",
    "DevOps",
}

persons = {
    "Nguyễn Ngọc Vĩnh": {
        "Web development",
        "Mobile development",
        "Internet of Things",
        "DevOps",
        "Cloud computing",
    },
    "John Doe": {
        "Natural language processing",
        "DevOps",
        "Data analytics",
    },
    "Mathew Jason": {
        "Cybersecurity",
        "Robotics",
        "Blockchain",
        "Natural language processing",
    },
    "Bruce Wayne": {
        "Blockchain",
        "Virtual reality",
        "Cybersecurity",
    },
    "Luigi Mario": {
        "Virtual reality",
        "Robotics",
    },
    "Franci Bonni": {"Mobile development", "Internet of Things"},
    "Michael Jackson": {"Cybersecurity", "Robotics", "Virtual reality"},
}

final_person = set()


def person_finding(requirements_needed, persons):
    while requirements_needed:
        best_person = None
        requirements_covered = set()
        for person, requirements_for_person in persons.items():
            covered = requirements_needed & requirements_for_person
            if len(covered) > len(requirements_covered):
                best_person = person
                requirements_covered = covered

        if best_person is not None:
            requirements_needed -= requirements_covered
            final_person.add(best_person)
            persons.pop(best_person)
        else:
            return (final_person, requirements_needed)
    return (final_person, {"Nothing"})


person_to_hire, missing_requirement = person_finding(requirements_needed, persons)

print(f'You need to hire: {", ".join(name for name in person_to_hire)}')
print(f'Missing requirements: {", ".join(job for job in missing_requirement)}')
