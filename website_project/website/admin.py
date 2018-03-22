from django.contrib import admin

from .models import Post, Comment, Season, Round, Team, Match, TeamSeason, Player, PlayerStats


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Season)
admin.site.register(Round)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(TeamSeason)
admin.site.register(Player)
admin.site.register(PlayerStats)