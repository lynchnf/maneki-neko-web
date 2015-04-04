from django.core.mail.message import EmailMessage
from django.http.response import HttpResponse, HttpResponseServerError
from django.utils import timezone
from staff.models import ContactUsLog, Department
from website import settings
import logging

logger = logging.getLogger(__name__)

def contact_us(request):
    contactUsLog = ContactUsLog()
    contactUsLog.from_email = request.POST.get('from_email')
    contactUsLog.to_department_id = request.POST.get('to_department')
    to_department = Department.objects.get(pk=contactUsLog.to_department_id)
    contactUsLog.to_department = to_department.name
    contactUsLog.to_email = to_department.email
    contactUsLog.subject = request.POST.get('subject')
    contactUsLog.message = request.POST.get('message')
    contactUsLog.timestamp = timezone.now()
    contactUsLog.sent_successfully = True
    
    subject = settings.CONTACT_US_SUBJECT_PREFIX + contactUsLog.subject
    if contactUsLog.message == None or contactUsLog.message == "":
        subject = subject + "<eom>"
        ContactUsLog.message = None

    email_message = EmailMessage()
    email_message.subject = subject
    email_message.body = contactUsLog.message
    email_message.from_email = contactUsLog.from_email
    email_message.to = [contactUsLog.to_email]
    
    if not to_department.chair:
        email_message.cc = []
        cc_departments = Department.objects.filter(chair=True)
        for cc_department in cc_departments:
            email_message.cc.append(cc_department.email)

    try:
        email_message.send()
        contactUsLog.save()
        return HttpResponse()
    except:
        contactUsLog.sent_successfully = False
        contactUsLog.save()
        logger.exception("Error sending email. from_email=" + str(contactUsLog.from_email) + ", to_department=" + str(contactUsLog.to_department) + ", subject=" + str(contactUsLog.subject))
        return HttpResponseServerError()