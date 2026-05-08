from datetime import date
from collections import OrderedDict

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Project, Experience, ContactMessage, Skill, Certificate


def index(request):
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    certificates = Certificate.objects.all()
    skills = Skill.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Please fill in all fields.'})
            messages.error(request, 'Please fill in all required fields.')

    # Get unique tech stacks for filter
    all_tech = set()
    for p in projects:
        if p.tech_stack:
            for t in p.tech_stack:
                all_tech.add(t)

    # Category icons mapping
    category_icons = {
        'backend': 'bi-server',
        'frontend': 'bi-palette',
        'database': 'bi-database',
        'devops': 'bi-gear',
        'tools': 'bi-tools',
        'other': 'bi-grid',
    }

    # Group skills by category as list of dicts for easy template use
    category_labels = dict(Skill.CATEGORY_CHOICES)
    category_order = ['backend', 'frontend', 'database', 'devops', 'tools', 'other']
    skills_grouped = []
    for cat_key in category_order:
        cat_skills = [s for s in skills if s.category == cat_key]
        if cat_skills:
            skills_grouped.append({
                'name': category_labels[cat_key],
                'icon': category_icons.get(cat_key, 'bi-grid'),
                'skills': cat_skills,
                'count': len(cat_skills),
            })

    # Dynamic hero stats
    years_exp = 0
    if experiences.exists():
        earliest = experiences.order_by('start_date').first()
        if earliest:
            months = (date.today().year - earliest.start_date.year) * 12 + (
                date.today().month - earliest.start_date.month
            )
            years_exp = max(1, months // 12)

    project_count = projects.count()
    tech_count = skills.count()

    context = {
        'projects': projects,
        'experiences': experiences,
        'certificates': certificates,
        'skills_grouped': skills_grouped,
        'all_tech': sorted(all_tech),
        'years_exp': years_exp,
        'project_count': project_count,
        'tech_count': tech_count,
    }
    return render(request, 'portfolio/index.html', context)
