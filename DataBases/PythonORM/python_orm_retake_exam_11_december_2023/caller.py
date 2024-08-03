import os
import re

import django
from django.db.models import Count, F, Value, When, Case

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import TennisPlayer, Tournament, Match


# Create queries within functions

def get_tennis_players(search_name=None, search_country=None):
    if not any((search_name, search_country)):
        return ""

    # players = (TennisPlayer.objects
    #            .filter(full_name__regex=fr'(?i).*{search_name}.*', country__regex=fr'(?i).*{search_country}.*')
    #            .order_by('ranking')
    #            )

    if search_name and search_country:
        players = (TennisPlayer.objects
                   .filter(full_name__icontains=search_name, country__icontains=search_country)
                   .order_by('ranking')
                   )
    elif search_country:
        players = (TennisPlayer.objects
                   .filter(country__icontains=search_country)
                   .order_by('ranking')
                   )
    elif search_name:
        players = (TennisPlayer.objects
                   .filter(full_name__icontains=search_name)
                   .order_by('ranking')
                   )
    else:
        return ""
    return '\n'.join(f'Tennis Player: {player.full_name}, country: {player.country}, ranking: {player.ranking}' for player in players) if len(players) else ""

def get_top_tennis_player():
    best_player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()
    return f"Top Tennis Player: {best_player.full_name} with {best_player.matches_won} wins." if best_player else ""

def get_tennis_player_by_matches_count():
    player = TennisPlayer.objects.annotate(matches_played=Count('matches__id')).filter(matches_played__gt=0).order_by('-matches_played','ranking').first()
    return f"Tennis Player: {player.full_name} with {player.matches_played} matches played." if player else ""


def get_tournaments_by_surface_type(surface=None):
    if surface is None: return ""
    tournaments = Tournament.objects.annotate(num_matches=Count('match__id')).filter(surface_type__icontains=surface).order_by('-start_date')
    return '\n'.join(f'Tournament: {tournament.name}, start date: {tournament.start_date}, matches: {tournament.num_matches}' for tournament in tournaments) if len(tournaments) else ""


def get_latest_match_info():
    last_match = Match.objects.select_related('tournament','winner').all().order_by('-date_played', '-id').first()
    if not last_match: return ""
    players = last_match.players.all().order_by('full_name')
    if not len(players) == 2: return ""
    first_player, second_player = (players[0],players[1])
    return f"Latest match played on: {last_match.date_played}, tournament: {last_match.tournament.name}, score: {last_match.score}, players: {first_player.full_name} vs {second_player.full_name}, winner: {last_match.winner.full_name if last_match.winner else 'TBA'}, summary: {last_match.summary}"


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None: return "No matches found."
    tournament = Tournament.objects.filter(name=tournament_name).first()
    if not tournament: return "No matches found."
    matches = tournament.match_set.all().order_by('-date_played')
    return '\n'.join(f'Match played on: {match.date_played}, score: {match.score}, winner: {match.winner or "TBA"}' for match in matches ) if matches else "No matches found."


if __name__ == '__main__':
    # for player in TennisPlayer.objects.get_tennis_players_by_wins_count():
    #     print(player.full_name,': ', player.matches_won)
    # print(get_tennis_players('',' '))
    # print(get_top_tennis_player())
    # print(get_tennis_player_by_matches_count())
    # print(get_tournaments_by_surface_type('ha'))
    print(get_latest_match_info())
    # print(get_matches_by_tournament(True))
    pass
