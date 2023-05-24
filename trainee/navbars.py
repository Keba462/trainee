from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar

trainee = Navbar(name='trainee')

trainee.append_item(
    NavbarItem(
        name='eligible_subject',
        label='subject_screening',
        title='Subject Screening',
        fa_icon='fa-user-plus',
        url_name= settings.DASHBOARD_URL_NAMES.get('screening_listboard_url')
        ))

trainee.append_item(
     NavbarItem(
       name='trainee_subject',
         label='subjects',
         title= 'Subjects',
         fa_icon='far fa-user-circle',
         url_name= settings.DASHBOARD_URL_NAMES.get('subject_listboard_url')
         ))

trainee.append_item(
    NavbarItem(name='reports',
               label='Reports',
               fa_icon='fa-cogs',
               url_name='trainee_reports:home_url'))


site_navbars.register(trainee)