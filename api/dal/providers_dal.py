import json

from api.utils.date_utils import check_date_in_ranges_list
from api.utils.provider_utils import get_provider_score, check_provider_specialty


class ProvidersDal(object):
    def __init__(self):
        data = ''
        with open('providers/providers.json') as json_file:
            data = json.load(json_file)

        self.providers = data

    def get_all(self):
        return self.providers

    def get_available_providers(self, specialty, date, min_score):
        available_providers = []

        for provider in self.providers:
            is_available = check_date_in_ranges_list(provider['availableDates'], date)
            has_specialty = check_provider_specialty(provider['specialties'], specialty)

            if is_available and has_specialty and provider['score'] >= min_score:
                available_providers.append(provider)

        available_providers.sort(key=get_provider_score, reverse=True)
        provider_names = [provider['name'] for provider in available_providers]
        return provider_names
