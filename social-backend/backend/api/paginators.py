from rest_framework.pagination import PageNumberPagination


class DefaultPaginator(PageNumberPagination):
    page_size = 20
    max_page_size = 100


class ExtendedPaginator(PageNumberPagination):
    page_size = 100
    max_page_size = 500
