from rest_framework.exceptions import APIException

class ProductNotFound(APIException):
    status_code = 404
    default_detail = "The requested product does not exist"
class NotYourProduct(APIException):
    status_code = 403
    default_detail = "You don't have the permissions to edit this product"   
