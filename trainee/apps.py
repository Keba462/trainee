from datetime import datetime
from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_appointment.appointment_config import AppointmentConfig
from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
from dateutil.tz import gettz
from edc_data_manager.apps import AppConfig as BaseEdcDataManagerAppConfig
from edc_sms.apps import AppConfig as BaseEdcSmsAppConfig
from edc_senaite_interface.apps import AppConfig as BaseEdcSenaiteInterfaceAppConfig
from edc_device.constants import CENTRAL_SERVER

from trainee_dashboard.patterns import subject_identifier

class AppConfig(DjangoAppConfig):
    name ='trainee'
    verbose_name ='trainee base App'
    include_in_administration_section=True


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'trainee'
    institution = 'BHP'

class EdcDeviceAppConfig(BaseEdcDeviceAppConfig):
    use_settings = True
    device_id = settings.DEVICE_ID
    device_role = settings.DEVICE_ROLE


class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
    country = 'botswana'
    definitions = {
        '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                             slots=[100, 100, 100, 100, 100, 100, 100]),
        '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                             slots=[100, 100, 100, 100, 100])
        }

class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
    send_sms_reminders = True
    apply_community_filter = True
    configurations = [
        AppointmentConfig(
            model='edc_appointment.appointment',
            related_visit_model='trainee_subject.subjectvisit',
            appt_type='clinic')]


class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
    visit_models = {
        'trainee_subject': ('subject_visit', 'trainee_subject.subjectvisit')
        }


class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    protocol = 'BHP703'
    protocol_name = 'Trainee Project'
    protocol_number = '703'
    protocol_title = ''
    study_open_datetime = datetime(
        2023, 5, 3, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(
        2025, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))

class EdcIdentifierAppConfig(BaseEdcIdentifierAppConfig):
    identifier_prefix = '703'

class EdcDataManagerAppConfig(BaseEdcDataManagerAppConfig):
    identifier_pattern = subject_identifier


class EdcSmsAppConfig(BaseEdcSmsAppConfig):
    locator_model = 'trainee_subject.subjectlocator'
    consent_model = 'trainee_subject.subjectconsent'
    sms_model = 'trainee_subject.sms'


class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
        reason_field = {'trainee_subject.subjectvisit': 'reason'}
        other_visit_reasons = ['off study', 'deferred', 'death']
        other_create_visit_reasons = [
            'initial_visit/contact', 'fu_visit/contact',
            'missed_visit', 'unscheduled_visit/contact']
        create_on_reasons = [SCHEDULED, UNSCHEDULED] + other_create_visit_reasons
        delete_on_reasons = [LOST_VISIT] + other_visit_reasons



class EdcSenaiteInterfaceAppConfig(BaseEdcSenaiteInterfaceAppConfig):
    host ="https://bhplims-dev.bhp.org.bw"
    client = "Trainee"
    courier = ""
    result_models ={'trainee_subject':['subjectrequisitionresult','subjectresultvalue']}
    sample_type_match = {'viral_load': 'Whole Blood EDTA'}
    container_type_match = {'viral_load': 'EDTA tube'}
    template_match = {'viral_load': 'HIV RNA PCR'}
    
