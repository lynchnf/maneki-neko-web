from django.utils import timezone
from staff.models import ContactUsLog, Department
from django.core.mail import send_mail
from website import settings
import logging
from django.http.response import HttpResponse, HttpResponseServerError

logger = logging.getLogger(__name__)

def contact_us(request):
    contactUsLog = ContactUsLog()
    contactUsLog.from_email = request.POST.get('from_email')
    to_department_id = request.POST.get('to_department')
    to_department = Department.objects.get(pk=to_department_id)
    
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

    recipient_list = [contactUsLog.to_email]
    
    try:
        send_mail(subject, contactUsLog.message, contactUsLog.from_email, recipient_list)
        contactUsLog.save()
        return HttpResponse()
    except:
        contactUsLog.sent_successfully = False
        contactUsLog.save()
        logger.exception("Error sending email. from_email=" + str(contactUsLog.from_email) + ", to_department=" + str(contactUsLog.to_department) + ", subject=" + str(contactUsLog.subject))
        return HttpResponseServerError()