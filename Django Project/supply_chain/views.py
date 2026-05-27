from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from supply_chain.models import Council
from supply_chain.models import Project
from supply_chain.models import Department


def hello_world_index(request):
    return HttpResponse("Hello World! This is the main index of the Suppy Chain project")


def all_councils(request):
    councils = Council.objects.all()

    context = {
        'councils': councils,
    }

    return render(request, 'supply_chain/councils.html', context)

def all_projects(request):
    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'supply_chain/projects.html', context)

def all_departments(request):
    departments = Department.objects.all()

    context = {
        'departments': departments,
    }

    return render(request, 'supply_chain/departments.html', context)

def council_detail(request, slug):
    council = Council.objects.get(slug=slug)

    context = {
        'council': council,
    }

    return render(request, 'supply_chain/council_detail.html', context)

def project_detail(request, slug):
    project = Project.objects.get(slug=slug)

    context = {
        'project': project,
    }

    return render(request, 'supply_chain/project_detail.html', context)

def department_detail(request, slug):
    department = Department.objects.get(slug=slug)

    context = {
        'department': department,
    }

    return render(request, 'supply_chain/department_detail.html', context)

def search(request):
    query = request.GET.get('q', '')

    council_results = Council.objects.filter(name__icontains=query)
    project_results = Project.objects.filter(title__icontains=query)
    department_results = Department.objects.filter(name__icontains=query)

    context = {
        'query': query,
        'council_results': council_results,
        'project_results': project_results,
        'department_results': department_results,
    }




    return render(request, 'supply_chain/search_results.html', context)