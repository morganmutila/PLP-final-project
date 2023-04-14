from application.models import Setting as School, Program, StudyCategory



def popular_programs(request):
    return {
        'popular_programs' : Program.objects.all()[:5]
    }

def school_settings(request):
    return {
        'school_settings': School.objects.first()
    }    