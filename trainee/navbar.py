from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar

trainee = Navbar(name='trainee')

trainee.append_item(
    NavbarItem(
        name='eligible_subject',
        label='Subject Screening',
        fa_icon='fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES.get('screening_listboard_url')))

trainee.append_item(
    NavbarItem(
        name='trainee_subject',
        label='Subjects',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES.get('subject_listboard_url')))



site_navbars.register(trainee)