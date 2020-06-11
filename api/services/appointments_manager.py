from api.dal.providers_dal import ProvidersDal
from api.utils.date_utils import check_date_in_ranges_list


class AppointmentManager(object):
    def set_appointment(self, name, date):
        return self.validate_appointment(name, date)

    def validate_appointment(self, name, date):
        providers_dal = ProvidersDal()
        providers = providers_dal.get_all()
        selected_provider = [provider for provider in providers if provider['name'] == name]

        if len(selected_provider) > 0:
            selected_provider = selected_provider[0]
        else:
            return False

        is_available = check_date_in_ranges_list(selected_provider['availableDates'], date)
        return is_available
