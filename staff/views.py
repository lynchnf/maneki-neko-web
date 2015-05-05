from django.core.mail.message import EmailMessage
from django.http.response import HttpResponse, HttpResponseServerError, HttpResponseForbidden, HttpResponseNotFound
from django.utils import timezone
from staff.models import Department, EmailLog, Position
from website import settings
import json
import logging

logger = logging.getLogger(__name__)

def contact_us(request):
    emailLog = EmailLog()
    emailLog.subject = request.POST.get('subject')
    emailLog.body = request.POST.get('message')
    emailLog.from_email = request.POST.get('from_email')
    to_department_id = request.POST.get('to_department')
    to_department = Department.objects.get(pk=to_department_id)
    emailLog.to = to_department.email
    cc = []
    emailLog.cc = None
    cc_departments = Department.objects.filter(chair=True).exclude(id=to_department_id)
    for cc_department in cc_departments:
        cc.append(cc_department.email)
        if emailLog.cc == None:
            emailLog.cc = cc_department.email
        else:
            emailLog = emailLog + "," + cc_department.email
            
    emailLog.department = to_department     
    emailLog.timestamp = timezone.now()
    emailLog.sent_successfully = True

    email_message = EmailMessage()
    subject = settings.CONTACT_US_SUBJECT_PREFIX + emailLog.subject
    if emailLog.body == None or emailLog.body == "":
        subject = subject + "<eom>"
        emailLog.message = None
    email_message.subject = subject
    email_message.body = emailLog.body
    email_message.from_email = emailLog.from_email
    email_message.to = [emailLog.to]
    if cc:
        email_message.cc = cc

    try:
        email_message.send()
        emailLog.save()
        return HttpResponse()
    except:
        emailLog.sent_successfully = False
        emailLog.save()
        logger.exception("Error sending email. from_email=" + str(emailLog.from_email) + ", to_department=" + str(emailLog.department) + ", subject=" + str(emailLog.subject))
        return HttpResponseServerError()

def email_instance(request):
    # If the current user is not logged in, access is denied.
    if not request.user.is_authenticated() or not request.user.is_active:
        return HttpResponseForbidden()
    
    # Does this email actually exist?
    emailId = request.GET.get("emailId")
    emailLog = None
    try:
        emailLog = EmailLog.objects.get(pk=emailId)
    except EmailLog.DoesNotExist:
        return HttpResponseNotFound()
    
    # Is the current user con-chair (or vice-chair)? Try to find a position record.
    position = Position.objects.filter(user__id=request.user.id,title__in=[1,2],department__chair=True)
    # If the user is a super-user or a con-chair, then he can see the email.
    # Otherwise, ...
    if not request.user.is_superuser and not position.exists():
        # ... the email must be for a department that the current user is head or second of.
        position = Position.objects.filter(user__id=request.user.id,title__in=[1,2],department__id=emailLog.department.id)
        if not position.exists():
            return HttpResponseForbidden()
        
    email = {}
    email["from_email"] = emailLog.from_email
    email["to"] = emailLog.to
    email["cc"] = emailLog.cc
    email["subject"] = emailLog.subject
    email["body"] = emailLog.body
    email["timestamp"] = emailLog.timestamp.strftime("%Y-%m-%d %I:%M %p")
    email["sent_successfully"] = emailLog.sent_successfully
        
    context = {}
    context["email"] = email

    try:
        content = json.dumps(context)
        return HttpResponse(content, content_type='application/json')
    except:
        logger.exception("Error serializing email with id=" + str(emailId))
        return HttpResponseServerError()

def email_list(request):
    # If the current user is not logged in, access is denied.
    if not request.user.is_authenticated() or not request.user.is_active:
        return HttpResponseForbidden()
    
    email_log = []
            
    # Is the current user con-chair (or vice-chair)? Try to find a position record.
    position = Position.objects.filter(user__id=request.user.id,title__in=[1,2],department__chair=True)
    # If the user is a super-user or a con-chair, show all the emails.
    if request.user.is_superuser or position.exists():
        email_log = EmailLog.objects.order_by("-timestamp")
    else:
        # Otherwise, show just the emails for the departments that the current user is head or second of.
        departmentIds = Position.objects.filter(user__id=request.user.id,title__in=[1,2]).values('department')
        email_log = EmailLog.objects.filter(department__id__in=departmentIds).order_by("-timestamp")

    emails = []
    for log_entry in email_log:
        email = {}
        email["id"] = log_entry.id
        email["from_email"] = log_entry.from_email
        email["to"] = log_entry.to
        email["subject"] = log_entry.subject
        email["timestamp"] = log_entry.timestamp.strftime("%Y-%m-%d %I:%M %p")
        email["sent_successfully"] = log_entry.sent_successfully
        emails.append(email);

    context = {}
    context["emails"] = emails

    try:
        content = json.dumps(context)
        return HttpResponse(content, content_type='application/json')
    except:
        logger.exception("Error serializing email list.")
        return HttpResponseServerError()