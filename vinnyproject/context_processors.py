from django.conf import settings

def project_settings(context):
    return {'SETTINGS': settings}
