from django.contrib.admin import SimpleListFilter


class HighOrderFilter(SimpleListFilter):
    title = "Order range"
    parameter_name = "order_params"

    def lookups(self, request, model_admin):
        return [
            ('ho', 'High Order'),
            ('lo', 'Low Order')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'ho':
            qs = queryset.filter(order__gte=5)
        elif self.value() == 'lo':
            qs = queryset.filter(order__lt=5)
        else:
            qs = queryset
        return qs


class SaveCountFilter(SimpleListFilter):
    title = "Number of saves"
    parameter_name = "save_count"

    def lookups(self, request, model_admin):
        return [
            ('most', 'Most Popular'),
            ('least', 'Least Popular')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'most':
            qs = queryset.filter(save_count__gt=1).order_by("-save_count")
        elif self.value() == 'least':
            qs = queryset.filter(save_count=1)
        else:
            qs = queryset
        return qs
