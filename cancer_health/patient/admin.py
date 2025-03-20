from django.contrib import admin
from .models import PatHealthRec, ApplyScan, CounsellingBook, RegFreevig, Comments

admin.site.register(PatHealthRec)
admin.site.register(ApplyScan)
admin.site.register(CounsellingBook)
admin.site.register(RegFreevig)
admin.site.register(Comments)