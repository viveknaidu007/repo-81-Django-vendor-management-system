# repo-81-Django-vendor-management-system
Develop a Vendor Management System using Django and Django REST Framework

# step1:
django-admin startproject vendor_management_system

# step2:
cd vendor_management_system
python manage.py startapp vendor_management

# Vendor Management System API

## Setup Instructions
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Apply migrations using `python manage.py migrate`.
4. Run the development server using `python manage.py runserver`.

## API Endpoints
### Vendors
- `GET /api/vendors/`: List all vendors.
- `POST /api/vendors/`: Create a new vendor.
- `GET /api/vendors/{vendor_id}/`: Retrieve details of a specific vendor.
- `PUT /api/vendors/{vendor_id}/`: Update details of a specific vendor.
- `DELETE /api/vendors/{vendor_id}/`: Delete a specific vendor.

### Purchase Orders
- `GET /api/purchase_orders/`: List all purchase orders.
- `POST /api/purchase_orders/`: Create a new purchase order.
- `GET /api/purchase_orders/{po_id}/`: Retrieve details of a specific purchase order.
- `PUT /api/purchase_orders/{po_id}/`: Update details of a specific purchase order.
- `DELETE /api/purchase_orders/{po_id}/`: Delete a specific purchase order.

### Vendor Performance Metrics
- `GET /api/vendors/{vendor_id}/performance/`: Retrieve performance metrics of a specific vendor.


# Run Migrations: Apply database migrations to create or update your database schema based on your models.
python manage.py makemigrations
python manage.py migrate
