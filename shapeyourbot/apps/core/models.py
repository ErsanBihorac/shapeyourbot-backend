from django.db import models

class DocumentType(models.TextChoices):
    PDF = "pdf", "PDF"
    # QUESTION = "question", "Question"
    # MANUAL = "manual", "Manual"

class Document(models.Model):
    document = models.FileField(upload_to="uploads", blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    document_type = models.CharField(choices=DocumentType.choices, max_length=20, default="pdf")
