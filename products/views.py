from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.exceptions import NotFound, ValidationError
from .models import Product
from .serializers import ProductSerializer
from .pagination import CustomPagination

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    throttle_classes = [AnonRateThrottle] 
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            if page is not None:
                return self.get_paginated_response({'products': ProductSerializer(page, many=True).data})
            
            return Response({
                'status': 'success',
                'code': 200,
                'message': 'Products retrieved successfully',
                'data': {'products': ProductSerializer(queryset, many=True).data}
            })
        except Exception as e:
            return Response({'status': 'error', 'code': 500, 'message': 'Internal Server Error', 'errors': {'details': str(e)}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            return Response({
                'product': ProductSerializer(instance).data,
                'status': 'success',
                'message': 'Product details retrieved successfully.',
                'headers': {
                    'X-RateLimit-Limit': request.headers.get('X-RateLimit-Limit', '100'),
                    'X-RateLimit-Remaining': request.headers.get('X-RateLimit-Remaining', '99'),
                    'X-RateLimit-Reset': request.headers.get('X-RateLimit-Reset', '1668144600')
                }
            })
        except Product.DoesNotExist:
            raise NotFound({'status': 'error', 'code': 404, 'message': 'Product not found', 'errors': {'details': 'No product was found with the given ID.'}})
        except Exception as e:
            return Response({'status': 'error', 'code': 500, 'message': 'Internal Server Error', 'errors': {'details': str(e)}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'status': 'error', 'code': 400, 'message': 'Invalid input', 'errors': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': 'error', 'code': 500, 'message': 'Internal Server Error', 'errors': {'details': str(e)}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Product.DoesNotExist:
            raise NotFound({'status': 'error', 'code': 404, 'message': 'Product not found', 'errors': {'details': 'No product was found with the given ID.'}})
        except Exception as e:
            return Response({'status': 'error', 'code': 500, 'message': 'Internal Server Error', 'errors': {'details': str(e)}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Product.DoesNotExist:
            raise NotFound({'status': 'error', 'code': 404, 'message': 'Product not found', 'errors': {'details': 'No product was found with the given ID.'}})
        except Exception as e:
            return Response({'status': 'error', 'code': 500, 'message': 'Internal Server Error', 'errors': {'details': str(e)}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
