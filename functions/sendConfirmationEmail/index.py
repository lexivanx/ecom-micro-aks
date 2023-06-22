import logging
import azure.functions as func

def send_email(email):
    logging.info(f"Simulating sending confirmation email to {email}.")
    return True

def main(req: func.HttpRequest, message: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    email = req.params.get('email')
    if not email:
        return func.HttpResponse(
             "Please pass an email on the query string",
             status_code=400
        )

    try:
        email_result = send_email(email)
        if email_result:
            message.set(f'Confirmation email sent to {email}')
            return func.HttpResponse(f"Confirmation email sent to {email}")
        else:
            message.set(f'Failed to send confirmation email to {email}')
            return func.HttpResponse(f"Failed to send confirmation email to {email}", status_code=500)

    except Exception as e:
        logging.error(f"Error sending confirmation email to {email}: {str(e)}")
        return func.HttpResponse(f"Error sending confirmation email to {email}", status_code=500)
