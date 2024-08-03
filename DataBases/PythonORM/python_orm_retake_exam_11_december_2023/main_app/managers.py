from django.db import models
from django.db.models import Count


class TennisPlayerManager(models.Manager):

    def get_tennis_players_by_wins_count(self):
        return self.annotate(matches_won=Count('match__winner_id')).order_by('-matches_won', 'full_name')