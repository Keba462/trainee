from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar

trainee = Navbar(name='trainee')

trainee.append_item(
    NavbarItem(
        name='eligible_subject',
        label='subject screening',
        title='Subject Screening',
        fa_icon='fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES.get('screening_listboard_url')
    ))

trainee.append_item(
    NavbarItem(
        name='trainee_subject',
        label='subjects',
        title='Subjects',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES.get('subject_listboard_url')
    ))

trainee.append_item(
    NavbarItem(name='reports',
               label='Reports',
               fa_icon='fa-cogs',
               url_name='trainee_reports:home_url'))

trainee.append_item(
    NavbarItem(name='export_data',
               label=None,
               fa_icon='fa fa-database',
               url_name='trainee_export:home_url'))

trainee.append_item(
    NavbarItem(
        name='calendar',
        label='Calendar',
        fa_icon='fa fa-calendar',
        url_name='trainee_calendar:calendar'))

site_navbars.register(trainee)
