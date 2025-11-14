from django.contrib import admin
from .models import Room, Puzzle, UserProgress, UserStatistics


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['order', 'title', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title', 'description']


@admin.register(Puzzle)
class PuzzleAdmin(admin.ModelAdmin):
    list_display = ['title', 'room', 'puzzle_type', 'points', 'order']
    list_filter = ['puzzle_type', 'room']
    search_fields = ['title', 'question']
    ordering = ['room', 'order']


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'puzzle', 'room', 'is_completed', 'score', 'time_taken', 'attempts']
    list_filter = ['is_completed', 'room']
    search_fields = ['user__username', 'puzzle__title']
    readonly_fields = ['started_at', 'completed_at']
    raw_id_fields = ['user', 'puzzle', 'room']


@admin.register(UserStatistics)
class UserStatisticsAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_score', 'rooms_completed', 'puzzles_completed', 'current_room']
    list_filter = ['rooms_completed']
    search_fields = ['user__username']
    readonly_fields = ['updated_at', 'total_score', 'rooms_completed', 'puzzles_completed', 'total_time']
    raw_id_fields = ['user', 'current_room']


