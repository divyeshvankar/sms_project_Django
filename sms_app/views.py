from django.shortcuts import render
from .forms import FormEntryForm
from django.conf import settings
import requests

def form_entry(request):
    if request.method == 'POST':
        form = FormEntryForm(request.POST)
        if form.is_valid():
            form.save()

            # Send SMS notification
            send_sms_notification(form.cleaned_data)

            return render(request, 'success.html')
    else:
        form = FormEntryForm()
    
    return render(request, 'form.html', {'form': form})

# def send_sms_notification(data):
#     contacts = ['+917573853920']  # Add the phone numbers you want to send the SMS to

    # message = f"New form submission:\nName: {data['name']}\nPhone: {data['phone_number']}\nPickup: {data['pickup_location']}\nDrop: {data['drop_location']}\nCab Type: {data['cab_type']}\nTrip Type: {data['trip_type']}"
# # https://username:password@api.twilio.com/2010-04-01/your_desired_path
#     for contact in contacts:
#         requests.post(
#             f"https://api.twilio.com/2010-04-01/Accounts/{settings.TWILIO_ACCOUNT_SID}/Messages.json",
#             # f"https://api.twilio.com/2010-04-01/Accounts/{settings.TWILIO_ACCOUNT_SID}/Messages.json",
#             auth=(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN),
#             data={
#                 "From": settings.TWILIO_PHONE_NUMBER,
#                 "To": contact,
#                 "Body": message,
#             },
#         )

# message, recipient
def send_sms_notification(data):
    recipient='+917573853920'
    message = f"New form submission:\nName: {data['name']}\nPhone: {data['phone_number']}\nPickup: {data['pickup_location']}\nDrop: {data['drop_location']}\nCab Type: {data['cab_type']}\nTrip Type: {data['trip_type']}"
#             f"https://api.twilio.com/2010-04-01/Accounts/{settings.TWILIO_ACCOUNT_SID}/Messages.json",
   
    url = 'https://api.twilio.com/2010-04-01/Accounts/{settings.TWILIO_ACCOUNT_SID}/Messages.json'
    headers = {
        'Authorization': 'Bearer {settings.TWILIO_AUTH_TOKEN}',
    }
    data = {
        'To': recipient,
        'From': settings.TWILIO_PHONE_NUMBER,
        'Body': message,
    }
    response = requests.post(url, headers=headers, data=data)
    return response.status_code

#  url = 'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages.json'
#     headers = {
#         'Authorization': 'Bearer YOUR_TWILIO_AUTH_TOKEN',
#     }
#     data = {
#         'To': recipient,
#         'From': 'YOUR_TWILIO_NUMBER',
#         'Body': message,
#     }
#     response = requests.post(url, headers=headers, data=data)
#     return response.status_code