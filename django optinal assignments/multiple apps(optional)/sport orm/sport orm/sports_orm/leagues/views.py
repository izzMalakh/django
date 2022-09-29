from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		#1.all baseball leagues
		"baseball": League.objects.filter(sport="Baseball"),
		#2...all womens' leagues
		"womens_league": League.objects.filter(name__contains="Womens"),
		#3...all leagues where sport is any type of hockey
		"hockey_legue": League.objects.filter(sport__contains="Hockey"),
		#4...all leagues where sport is something OTHER THAN football
		"exclude_football": League.objects.exclude(sport__contains="Football"),
		#5...all leagues that call themselves "conferences"
		"conferences_league": League.objects.filter(name__contains="conferences"),
		#6...all leagues in the Atlantic region
		# "atlantic_league": Team.objects.filter(name__contains="Atlantic"),
		#7...all teams based in Dallas
		"Dallas_teams": Team.objects.filter(location__contains="Dallas"),
		#8...all teams named the Raptors
		"raptors_teams": Team.objects.filter(team_name__contains="Raptors"),
		#9...all teams whose location includes "City"
		"City_teams": Team.objects.filter(location__contains="City"),
		#10...all teams whose names begin with "T"
		"t_teams": Team.objects.filter(team_name__startswith="T"),
		# #11...all teams, ordered alphabetically by location
		"alphabetically_team_location": Team.objects.all().order_by("location"),
		# #12...all teams, ordered by team name in reverse alphabetical order
		"reverse_team": Team.objects.all().order_by("-team_name"),
		# #13...every player with last name "Cooper"
		"coper_name":Player.objects.filter(last_name="Cooper"),
		# #14 the same with previouse
		# #15...every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
		"cooper_name_without_jushua":Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		# #...all players with first name "Alexander" OR first name "Wyatt"
		"Alexander_or_Wyatt_names":Player.objects.filter(first_name="Alexander") ,
		"var":Player.objects.filter(first_name="Wyatt") 
		


	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")