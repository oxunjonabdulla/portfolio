from django.core.management.base import BaseCommand
from portfolio.models import Skill, Certificate


class Command(BaseCommand):
    help = 'Seed initial skills and certificates data'

    def handle(self, *args, **options):
        # Clear existing
        Skill.objects.all().delete()
        Certificate.objects.all().delete()

        skills_data = [
            # Backend
            {'name': 'Python', 'category': 'backend', 'icon': 'bi-filetype-py', 'order': 1},
            {'name': 'Django', 'category': 'backend', 'icon': 'bi-server', 'order': 2},
            {'name': 'Django REST Framework', 'category': 'backend', 'icon': 'bi-braces', 'order': 3},
            {'name': 'FastAPI', 'category': 'backend', 'icon': 'bi-lightning-charge', 'order': 4},
            {'name': 'Celery', 'category': 'backend', 'icon': 'bi-arrow-repeat', 'order': 5},
            {'name': 'Aiogram', 'category': 'backend', 'icon': 'bi-robot', 'order': 6},
            # Frontend
            {'name': 'HTML', 'category': 'frontend', 'icon': 'bi-filetype-html', 'order': 1},
            {'name': 'CSS', 'category': 'frontend', 'icon': 'bi-filetype-css', 'order': 2},
            {'name': 'JavaScript', 'category': 'frontend', 'icon': 'bi-filetype-js', 'order': 3},
            {'name': 'React', 'category': 'frontend', 'icon': 'bi-graph-up', 'order': 4},
            # Database
            {'name': 'PostgreSQL', 'category': 'database', 'icon': 'bi-database', 'order': 1},
            {'name': 'Redis', 'category': 'database', 'icon': 'bi-hdd-network', 'order': 2},
            {'name': 'SQLite', 'category': 'database', 'icon': 'bi-database', 'order': 3},
            # DevOps
            {'name': 'Docker', 'category': 'devops', 'icon': 'bi-box', 'order': 1},
            {'name': 'Nginx', 'category': 'devops', 'icon': 'bi-diagram-3', 'order': 2},
            {'name': 'Gunicorn', 'category': 'devops', 'icon': 'bi-arrow-repeat', 'order': 3},
            {'name': 'Ubuntu', 'category': 'devops', 'icon': 'bi-ubuntu', 'order': 4},
            {'name': 'CI/CD', 'category': 'devops', 'icon': 'bi-gear', 'order': 5},
            # Tools
            {'name': 'Git', 'category': 'tools', 'icon': 'bi-git', 'order': 1},
            {'name': 'REST APIs', 'category': 'tools', 'icon': 'bi-braces', 'order': 2},
            {'name': 'Linux', 'category': 'tools', 'icon': 'bi-terminal', 'order': 3},
        ]

        for s in skills_data:
            Skill.objects.create(**s)

        certs_data = [
            {
                'title': 'IELTS Academic — Band 7',
                'issuer': 'IDP',
                'year': 2026,
                'icon': 'bi-translate',
                'is_verified': True,
                'order': 1,
            },
            {
                'title': 'Python Backend Developer',
                'issuer': 'IT City Academy',
                'year': 2023,
                'icon': 'bi-code-slash',
                'is_verified': True,
                'order': 2,
            },
        ]

        for c in certs_data:
            Certificate.objects.create(**c)

        self.stdout.write(self.style.SUCCESS(
            f'Created {Skill.objects.count()} skills and {Certificate.objects.count()} certificates'
        ))
