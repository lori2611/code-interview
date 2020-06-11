def get_provider_score(provider):
    return provider['score']


def check_provider_specialty(provider_specialties, necessary_specialty):
    for specialty in provider_specialties:
        if necessary_specialty == specialty.lower():
            return True

    return False
