from django.contrib import admin
from .models import Room, Puzzle, UserProgress, UserStatistics


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['order', 'title', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']


@admin.register(Puzzle)
class PuzzleAdmin(admin.ModelAdmin):
    list_display = ['title', 'room', 'puzzle_type', 'points', 'order']
    list_filter = ['puzzle_type', 'room']
    search_fields = ['title', 'question']
    ordering = ['room', 'order']


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'puzzle', 'is_completed', 'score', 'time_taken', 'attempts']
    list_filter = ['is_completed', 'puzzle__room']
    search_fields = ['user__username', 'puzzle__title']
    readonly_fields = ['started_at', 'completed_at']


@admin.register(UserStatistics)
class UserStatisticsAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_score', 'rooms_completed', 'puzzles_completed', 'current_room']
    search_fields = ['user__username']
    readonly_fields = ['updated_at']


