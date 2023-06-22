import logging
import azure.functions as func

def process_payment(order_id):
    logging.info(f"Simulating payment processing for order {order_id}.")
    return True

def main(req: func.HttpRequest, message: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    order_id = req.params.get('order_id')
    if not order_id:
        return func.HttpResponse(
             "Please pass an order_id on the query string",
             status_code=400
        )

    try:
        payment_result = process_payment(order_id)
        if payment_result:
            message.set(f'Payment processed for order {order_id}')
            return func.HttpResponse(f"Payment processed for order {order_id}")
        else:
            message.set(f'Payment failed for order {order_id}')
            return func.HttpResponse(f"Payment failed for order {order_id}", status_code=500)

    except Exception as e:
        logging.error(f"Error processing payment for order {order_id}: {str(e)}")
        return func.HttpResponse(f"Error processing payment for order {order_id}", status_code=500)
