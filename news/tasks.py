from django.core.mail import send_mail


def send_emails(email):
    letter_subject = 'Email confirm'
    letter_body = 'Please confirm your email'
    sender_email = 'kochinashviliilya@gmail.com'
    recipient_email = f'{email}'
    return send_mail(letter_subject, letter_body, sender_email, [recipient_email])
