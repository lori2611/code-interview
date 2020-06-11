def get_available_dates(available_dates):
    available_dates_list = []

    for dates_range in available_dates:
        for available_date in range(dates_range['from'], dates_range['to'], 50):
            available_dates_list.append(available_date)

    return available_dates_list


def check_date_in_ranges_list(available_dates, date):
    for dates_range in available_dates:
        if dates_range['from'] <= date <= dates_range['to']:
            return True

    return False
