from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin
from django.apps import apps as django_apps


class HomeView(EdcBaseViewMixin, NavbarViewMixin, TemplateView):
    template_name = 'trainee/home.html'
    navbar_name = 'trainee'
    navbar_selected_item = 'home'

    subject_screening_model = 'trainee_subject.subjectscreening'
    subject_consent_model = 'trainee_subject.subjectconsent'

    @property
    def subject_screening_cls(self):
        return django_apps.get_model(self.subject_screening_model)

    @property
    def subject_consent_cls(self):
        return django_apps.get_model(self.subject_consent_model)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject_screenig = self.subject_screening_cls.objects.all()
        subject_consent = self.subject_consent_cls.objects.all()

        screened_subjects = subject_screenig.count()
        consented_subjects = subject_consent.count()

        context.update(
            consented_subjects=consented_subjects,
            screened_subjects=screened_subjects)

        return context
