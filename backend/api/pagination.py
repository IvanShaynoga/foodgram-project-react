from foodgram.settings import P_SIZE
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = P_SIZE
    page_size_query_param = 'limit'
