from django.core.management.base import BaseCommand
from pytz import timezone

from dojo.models import Finding
from dojo.utils import update_issue, get_system_setting, add_issue

locale = timezone(get_system_setting('time_zone'))

"""
Author: Matti HEIKKILA
This script will create jira tickets for all active/verified issues in defect dojo:
"""


class Command(BaseCommand):
    help = 'No input commands for Jira bulk update.'

    def handle(self, *args, **options):

        findings = Finding.objects.exclude(jira_issue__isnull=False)
        findings = findings.filter(verified=True, active=True)

        for finding in findings:
            add_issue(finding, True)
            print "Checking issue:" + str(finding.id)
            #update_issue(finding, finding.status(), True)
            print "########\n"
~                                                                                                                                 
~                                                
