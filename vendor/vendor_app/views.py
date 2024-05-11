from django.shortcuts import get_object_or_404
from .models import Vendor, PurchaseOrder
from .models import Vendor
from .models import PurchaseOrder
from .serializers import VendorSerializer,PerfomanceSerializer,PurchaseOrderSerializer
from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .serializers import AcknowledgeSerializer


# Vendor

# List all vendors  

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def vendor_list(request):
    vendors = Vendor.objects.all()
    serializer = VendorSerializer(vendors, many=True)

    if not vendors.exists():
        return Response({"message": "No vendors found"}, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)

# Create a new vendor 

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def vendor_create(request):
    serializer = VendorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Retrive a specific vendor

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def vendor_retrive(request,vendor_code):
    try:
        vendors = Vendor.objects.get(vendor_code=vendor_code)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = VendorSerializer(vendors)
    return Response(serializer.data)


# Update a specific vendor    

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def vendor_update(request, vendor_id):
    try:
        vendor = Vendor.objects.get(id=vendor_id)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = VendorSerializer(vendor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete a specific vendor    

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def vendor_destroy(request, vendor_id):
    try:
        vendor = Vendor.objects.get(id=vendor_id)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    vendor.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Purchase Order

# List all purchase orders with an option to filter by vendor id

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def purchase_order_list(request,vendor_id):
    vendor_id = request.query_params.get('vendor')
    if vendor_id:
        purchase_orders = PurchaseOrder.objects.filter(vendor_id=vendor_id)
    else:
        purchase_orders = PurchaseOrder.objects.all()
    serializer = PurchaseOrderSerializer(purchase_orders, many=True)
    return Response(serializer.data)

#Create a purchase order

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def purchase_order_create(request):
    serializer = PurchaseOrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve details of a specific purchase order
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def purchase_order_retrieve(request, po_number):
    try:
        purchase_order = PurchaseOrder.objects.get(po_number=po_number)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PurchaseOrderSerializer(purchase_order)
    return Response(serializer.data)


# Update details of a specific purchase order

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def purchase_order_update(request, po_number):
    try:
        purchase_order = PurchaseOrder.objects.get(po_number=po_number)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete a specific purchase order

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def purchase_order_destroy(request, po_number):
    try:
        purchase_order = PurchaseOrder.objects.get(po_number=po_number)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    purchase_order.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Updates a purchase order with the given ID and sets the acknowledgment date.

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def acknowledge_update(request, pk):
    purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
    serializer = AcknowledgeSerializer(purchase_order, data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save(acknowledgment_date=timezone.now())
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Retrieves the performance data for all vendors.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def vendor_performance(request): 
    vendors = Vendor.objects.all()
    serializer = PerfomanceSerializer(vendors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)    