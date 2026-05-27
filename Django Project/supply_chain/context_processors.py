from supply_chain.models import Council, Project, Department


def menu_collections(request):
    return {
        "nav_councils": Council.objects.all(),
        "nav_projects": Project.objects.all(),
        "nav_departments": Department.objects.all(),
    }
