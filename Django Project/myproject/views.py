from django.shortcuts import render
from supply_chain.models import Council, Project, Department


def home(request):
    return render(request, 'supply_chain/index.html')


def search(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        councils = Council.objects.filter(name__icontains=query)
        projects = Project.objects.filter(title__icontains=query)
        departments = Department.objects.filter(name__icontains=query)
    else:
        councils = Council.objects.none()
        projects = Project.objects.none()
        departments = Department.objects.none()

    context = {
        'query': query,
        'councils': councils,
        'projects': projects,
        'departments': departments,
    }
    return render(request, 'supply_chain/search_results.html', context)
