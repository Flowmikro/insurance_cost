from rest_framework import generics
from .serializers import DateSerializer
from .models import Date

# class DateLIst(ListCreateAPIView):
#     # В вашем представлении (view) или представлении набора (viewset)
#     dates = Date.objects.all()
#     serializer = DateSerializer(dates, many=True)
#     json_data = serializer.data


class DateList(generics.ListAPIView):
    queryset = Date.objects.all()
    serializer_class = DateSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     dates = {}
    #
    #     for date in queryset:
    #         date_str = str(date.date)
    #         if date_str not in dates:
    #             dates[date_str] = []
    #
    #         dates[date_str].append({
    #             'cargo': date.cargo,
    #             'rate': str(date.rate)
    #         })
    #
    #     return self.get_paginated_response(dates)
