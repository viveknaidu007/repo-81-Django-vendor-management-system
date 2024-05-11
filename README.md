# here install environemnt
- conda activate urenv

# install python package
- pip install djangorestframework

# setup ur django project and app
- django-admin startproject vendor
- cd vendor
- django-admin startapp vendor_app

# datbase migartions
- python manage.py makemigrations
- python manage.py migarte

# create admin,superuser
- python manage.py createsuperuser

# and now generate the token:
* using curl bash terminal:
- note: you have to run the project "python manage.py runserver" and similarly open a new bash terminal and run this below , u will get a token
- curl -X POST -d "username=your_superuser_username&password=your_superuser_password" http://localhost:8000/api-token-auth/

## or 

* using postman api app in ur pc , u can generate token:
- o create a token using the /api-token-auth/ endpoint in Django REST Framework, you typically send a POST request with the username and password of the user you want to authenticate. Here's how you can do it in Postman:

    Open Postman: Launch Postman on your computer.

    Create a New Request: Click on the "New" button in the top-left corner of the Postman window to create a new request.

    Set Request Method: In the request tab, select "POST" as the request method.

    Enter Request URL: Enter the URL http://localhost:8000/api-token-auth/ in the address bar.

    Set Request Body: In the request body, select "x-www-form-urlencoded" as the format. Then, add two key-value pairs:
        Key: username, Value: <YourUsername>
        Key: password, Value: <YourPassword>

    Replace <YourUsername> and <YourPassword> with the actual username and password you want to authenticate.

    Send Request: Click the "Send" button to send the POST request.

    Retrieve Token: If the request is successful, you should receive a response containing the authentication token. This token is typically returned in JSON format.

* it will disp;ay like this , if it was runnning sucessfull
{
    "token": "8ed09d5f6d957b1f37699ce976ae17a861cd53a4"
}


# using or tesing the API's endpoint:
- we can use any of this : curl or http commands

# *************************************************************************************

# using API endpoints by CURL:

## Create a Vendor

- curl -H "Authorization: Token your_obtained_token" -X POST http://127.0.0.1:8000/api/vendors/ -d "vendor_code=01&name=Vendor+1&contact_details=Contact+1&address=Address+1"

## List all Vendor Details
- curl -H "Authorization: Token your_obtained_token" http://127.0.0.1:8000/api/vendors/

## Retrieve a Specific Vendor's Details:
- curl -H "Authorization: Token your_obtained_token" http://127.0.0.1:8000/api/vendors/{vendor_id}/


# Update a Vendor's Details

## PUT Method
- curl -H "Authorization: Token your_obtained_token" -X PUT http://127.0.0.1:8000/api/vendors/{vendor_id}/ -d "vendor_code=updated code&name=Updated Vendor Name&contact_details=Updated Contact Details&address=Updated Address"

## PATCH Method
- curl -H "Authorization: Token your_obtained_token" -X PATCH http://127.0.0.1:8000/api/vendors/{vendor_id}/ -d "name=Updated Vendor Name"


# Delete a Vendor
- curl -H "Authorization: Token your_obtained_token" -X DELETE http://127.0.0.1:8000/api/vendors/{vendor_id}/

# Create a Purchase Order
- curl -H "Authorization: Token your_obtained_token" -X POST http://127.0.0.1:8000/api/purchase_orders/ -d "po_number=01&vendor=01&order_date=2023-01-01T12:00:00&delivery_date=2023-01-10T12:00:00&items=[{\"item_name\":\"Item 1\",\"quantity\": 10 },{\"item_name\": 10 }]&quality_rating=4.5&issue_date=2023-01-01T12:00:00&status=updated&acknowledgment_date=2023-01-02T12:00:00"

# List all Purchase Orders
- curl -H "Authorization: Token your_obtained_token" http://127.0.0.1:8000/api/purchase_orders/

# Retrieve a Specific Purchase Order's Details
- curl -H "Authorization: Token your_obtained_token" http://127.0.0.1:8000/api/purchase_orders/{po_id}/

# Update a Purchase Order's Details

## PUT Method
- curl -H "Authorization: Token your_obtained_token" -X PUT http://127.0.0.1:8000/api/purchase_orders/{po_id}/ -d "po_number=updatedno&vendor=updatedvno&order_date=2023-01-02T12:00:00&delivery_date=2023-01-15T12:00:00&items=[{\"item_name\": 10 },{\"item_name\":10}]&quality_rating=5&issue_date=2023-01-01T12:00:00&status=updated&acknowledgment_date=2023-01-01T12:00:00"

## PATCH Method
- curl -H "Authorization: Token your_obtained_token" -X PATCH http://127.0.0.1:8000/api/purchase_orders/{po_id}/ -d "vendor=updatedvno&quality_rating=5"

# Delete a Purchase Order
- curl -H "Authorization: Token your_obtained_token" -X DELETE http://127.0.0.1:8000/api/purchase_orders/{po_id}/

# Retrieve a Vendor's Performance Metrics
- curl -H "Authorization: Token your_obtained_token" http://127.0.0.1:8000/api/vendors/1/performance/

# Update acknowledgment_data and trigger the recalculation of average_response_time
- curl -H "Authorization: Token your_obtained_token" -X PATCH http://127.0.0.1:8000/api/purchase_orders/{po_id}/acknowledge/ --data "acknowledgment_date=2023-12-30T12:00:00Z"





# API endpints:
- 
    API Endpoints
    Vendor Management
    List/Create Vendors:

    Endpoint: /api/vendors/
    Method: GET (List all vendors) / POST (Create a new vendor)
    Retrieve/Update/Delete Vendor:

    Endpoint: /api/vendors/{vendor_id}/
    Method: GET (Retrieve) / PUT (Update) / DELETE (Delete)
    Vendor Performance Metrics:

    Endpoint: /api/vendors/{vendor_id}/performance/
    Method: GET
    Purchase Order Tracking
    List/Create Purchase Orders:

    Endpoint: /api/purchase_orders/
    Method: GET (List all purchase orders) / POST (Create a new purchase order)
    Retrieve/Update/Delete Purchase Order:

    Endpoint: /api/purchase_orders/{po_id}/
    Method: GET (Retrieve) / PUT (Update) / DELETE (Delete)
    Acknowledge Purchase Order:

    Endpoint: /api/purchase_orders/{po_id}/acknowledge/
    Method: POST


## API 

    http://127.0.0.1:8000/admin/
    http://127.0.0.1:8000/api/vendors/ 
    http://127.0.0.1:8000/api/vendors/<int:pk>/ 
    http://127.0.0.1:8000/api/purchase_orders/
    http://127.0.0.1:8000/api/purchase_orders/<int:pk>/ 
    http://127.0.0.1:8000/api/historical_performance/ 
    http://127.0.0.1:8000/api/vendors/<int:vendor_id>/performance/ 
    http://127.0.0.1:8000/api/purchase_orders/<int:pk>/acknowledge/ 


5.  ## API Documentation
    Detailed API documentation is available in the [API Documentation](api_documentation.md) file. Please refer to this documentation for detailed information about each API endpoint, including input parameters, authentication requirements, and response formats.






