from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('database', 'Database'),
        ('devops', 'DevOps & Infrastructure'),
        ('tools', 'Tools & Workflow'),
        ('other', 'Other'),
    ]

    ICON_CHOICES = [
        ('bi-filetype-py', 'Python'),
        ('bi-server', 'Server/Django'),
        ('bi-lightning-charge', 'Lightning/FastAPI'),
        ('bi-database', 'Database'),
        ('bi-box', 'Box/Docker'),
        ('bi-git', 'Git'),
        ('bi-code-slash', 'Code'),
        ('bi-diagram-3', 'Diagram/Nginx'),
        ('bi-arrow-repeat', 'Repeat/Gunicorn'),
        ('bi-graph-up', 'Graph/React'),
        ('bi-ubuntu', 'Ubuntu'),
        ('bi-filetype-html', 'HTML'),
        ('bi-filetype-css', 'CSS'),
        ('bi-filetype-js', 'JavaScript'),
        ('bi-robot', 'Robot/Bot'),
        ('bi-cloud', 'Cloud'),
        ('bi-shield-check', 'Security'),
        ('bi-cpu', 'CPU/Processing'),
        ('bi-terminal', 'Terminal'),
        ('bi-braces', 'Braces/API'),
        ('bi-hdd-network', 'Network'),
        ('bi-layers', 'Layers'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='backend')
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default='bi-code-slash',
                            help_text="Bootstrap icon class")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.JSONField(default=list, help_text="List of technologies used")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    tech_used = models.JSONField(default=list)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.title} at {self.company}"

    @property
    def duration(self):
        from datetime import date
        end = self.end_date or date.today()
        months = (end.year - self.start_date.year) * 12 + (end.month - self.start_date.month)
        if months >= 12:
            years = months // 12
            rem = months % 12
            return f"{years}y {rem}m" if rem else f"{years}y"
        return f"{months}m"


class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.CharField(max_length=300, blank=True)
    icon = models.CharField(max_length=50, default='bi-patch-check-fill',
                            help_text="Bootstrap icon class for the certificate type")
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    is_verified = models.BooleanField(default=True)
    credential_url = models.URLField(blank=True, help_text="Link to verify the certificate")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-year']

    def __str__(self):
        return f"{self.title} — {self.issuer}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.subject}"
