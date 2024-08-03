import os
import django
from django.db.models import Q, Count, F, Sum, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Astronaut, Mission, Spacecraft


# Create queries within functions

def get_astronauts(search_string=None):
    if search_string is None: return ""
    astronauts = Astronaut.objects.filter(Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)).order_by('name')
    return '\n'.join(f"Astronaut: {a.name}, phone number: {a.phone_number}, status: {'Active' if a.is_active else 'Inactive'}" for a in astronauts) if astronauts else ""


def get_top_astronaut():
    astronaut = Astronaut.objects.get_astronauts_by_missions_count().first()
    return f"Top Astronaut: {astronaut.name} with {astronaut.missions_count} missions." if astronaut and astronaut.missions_count else "No data."


def get_top_commander():
    best_commander = Astronaut.objects.annotate(commanded_missions=Count('commander')).filter(commanded_missions__gt=0).order_by('-commanded_missions', 'phone_number').first()
    return f"Top Commander: {best_commander.name} with {best_commander.commanded_missions} commanded missions." if best_commander else "No data."


def get_last_completed_mission():
    mission = Mission.objects.prefetch_related('commander','astronauts','spacecraft').annotate(total_spacewalks=Sum('astronauts__spacewalks')).filter(status='Completed').order_by('-launch_date').first()
    return f"The last completed mission is: {mission.name}. Commander: {mission.commander.name if mission.commander else 'TBA'}. Astronauts: {', '.join(a.name for a in mission.astronauts.all().order_by('name'))}. Spacecraft: {mission.spacecraft.name}. Total spacewalks: {mission.total_spacewalks}." if mission and mission.astronauts.count() else "No data."


def get_most_used_spacecraft():
    spacecraft  = Spacecraft.objects.prefetch_related('mission_set').annotate(missions_count=Count('mission__spacecraft')).all().order_by('-missions_count', 'name').first()
    return f"The most used spacecraft is: {spacecraft.name}, manufactured by {spacecraft.manufacturer}, used in {spacecraft.missions_count} missions, astronauts on missions: {Astronaut.objects.filter(mission__spacecraft=spacecraft).distinct().count()}." if Mission.objects.count() else  "No data."


def decrease_spacecrafts_weight():
    updated = Spacecraft.objects.prefetch_related("mission_set").filter(mission__status='Planned', weight__gte=200.0).update(weight=F('weight') - 200.0)
    avg_weight = Spacecraft.objects.aggregate(avg_weight=Avg('weight'))
    return f"The weight of {updated} spacecrafts has been decreased. The new average weight of all spacecrafts is {avg_weight['avg_weight']:.1f}kg" if updated else "No changes in weight."




if __name__ == '__main__':
    pass
    # print(Astronaut.objects.get_astronauts_by_missions_count())
    # print(get_astronauts('1'))
    # print(get_top_astronaut())
    # print(get_top_commander())
    print(get_last_completed_mission()) #not finished
    # print(get_most_used_spacecraft()) #not finished
    # print(decrease_spacecrafts_weight())