from django.views.generic import TemplateView
from pybaseball import standings, team_batting_bref, team_pitching_bref

class HomeView(TemplateView):
    """
    View that displays the statistics dashboard including the division standings
    and a SportsRadar widget.
    """
    template_name = "bjstatistics/home.html"
    extra_context = {"standings": standings(2023)[0]}

class BatterView(TemplateView):
    """
    View for 2023 recent individual batter statistics, pulled from pybaseball. Only specific 
    columns are included for display.
    """
    template_name = "bjstatistics/batters.html"
    data = team_batting_bref("TOR", start_season=2023, end_season=None)[:17]
    TOR_batting = data[["Pos", "Name", "Age", "PA", "AB", "R", "H", "2B", "3B", "HR", "RBI", "BB", "SO", "BA", "OBP", "OPS", "SLG"]]
    extra_context = {"batting": TOR_batting}

class PitcherView(TemplateView):
    """
    View for 2023 recent individual pitcher statistics, pulled from pybaseball. Only specific 
    columns are included for display.
    """
    template_name = "bjstatistics/pitchers.html"
    data = team_pitching_bref("TOR", start_season=2023, end_season=None)
    TOR_pitching = data[["Pos", "Name", "Age", "W", "L", "W-L%", "ERA", "ERA+", "WHIP", "G", "GS", "GF", "SO", "BB", "HBP"]]
    extra_context = {"pitching": TOR_pitching}
    