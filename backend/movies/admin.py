from django.contrib import admin

from .models import Actor, Movie, Review

# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)
    filter_horizontal = ("actors",)
    inlines = [ReviewInline]

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name")

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "movie", "grade")
    list_filter = ("grade",)