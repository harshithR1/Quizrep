from django.contrib import admin
from quiz_app.models import QuestionModel, Leaderboard, QuizName
from import_export.admin import ImportExportModelAdmin


# Register your models here.
#admin.site.register(QuestionModel)
admin.site.register(Leaderboard)
admin.site.register(QuizName)
@admin.register(QuestionModel)
class ViewAdmin(ImportExportModelAdmin):
    pass
