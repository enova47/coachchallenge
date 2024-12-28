import pandas as pd
import time
import tqdm


# Return all plays of 2019-20 regular season
# Code from danchyy (Daniel Bratulic): https://github.com/danchyy/Basketball_Analytics
from nba_api.stats.static.teams import find_teams_by_full_name, get_teams, find_team_name_by_id
from nba_api.stats.endpoints.playbyplayv2 import PlayByPlayV2
from nba_api.stats.endpoints.leaguegamefinder import LeagueGameFinder

teams = get_teams()

game_finder = LeagueGameFinder(league_id_nullable="00", season_type_nullable="Regular Season")

games = game_finder.get_data_frames()[0]

all_data_frames = []
for team in teams:
    cur_season_games = games.loc[(games.TEAM_ID == team['id']) & (games.SEASON_ID == "22019")]
    for game_id in tqdm.tqdm(cur_season_games.GAME_ID.unique(), desc=f"Fetching games by {team['full_name']}"):
        pbp = PlayByPlayV2(game_id=game_id)
        all_data_frames.append(pbp.get_data_frames()[0])
        time.sleep(0.5)

concated = pd.concat(all_data_frames, ignore_index=True)

len(games.loc[games.SEASON_ID == "22019"].GAME_ID.unique())

dropped_concated = concated.drop_duplicates(keep='first')

dropped_concated.to_csv('play_by_plays_all_pbps_no_dups.csv')

# Challenge reviews downloaded as PDF from NBA Official website and copied to spreadsheet
# Challenge PDF source: https://ak-static.cms.nba.com/wp-content/uploads/sites/4/2020/02/Coachs-Challenge-reviews-2.pdf

# Merge challenge review data with play-by-play data
challenge = pd.read_csv('challenge_data.csv')
pbp_data = pd.read_csv('play_by_plays_all_pbps_no_dups.csv')

challenge_pbp_merge = pd.merge(challenge,pbp_data, how='left', left_on=['Game ID', 'Period', 'Time'],
                                    right_on=['GAME_ID','PERIOD','PCTIMESTRING'])

challenge_pbp_merge.to_csv('pbp_merged.csv')

# Change data types to strings
merged_data = pd.read_csv('pbp_merged.csv',engine='python')
merged_data['SCORE'] = merged_data['SCORE'].astype('str')
merged_data['PLAYER1_NAME'] = merged_data['PLAYER1_NAME'].astype('str')
merged_data['PLAYER2_NAME'] = merged_data['PLAYER2_NAME'].astype('str')
merged_data['PLAYER1_TEAM_ABBREVIATION'] = merged_data['PLAYER1_TEAM_ABBREVIATION'].astype('str')
merged_data['PLAYER2_TEAM_ABBREVIATION'] = merged_data['PLAYER2_TEAM_ABBREVIATION'].astype('str')
merged_data['HOMEDESCRIPTION'] = merged_data['HOMEDESCRIPTION'].astype('str')
merged_data['NEUTRALDESCRIPTION'] = merged_data['NEUTRALDESCRIPTION'].astype('str')
merged_data['VISITORDESCRIPTION'] = merged_data['VISITORDESCRIPTION'].astype('str')

# Calculate home and visiting team scores
def visit_score(x):
    if x['SCORE'] is not "":
        return x['SCORE'].split(' -',1)[0]
    else:
        return ""

def home_score(x):
    if x['SCORE'] is not "":
        return x['SCORE'].split('- ',1)[-1]
    else:
        return ""

# Calculate committing and disadvantaged players and teams
def committing_player(x):
    if x['PLAYER1_NAME'] is not "":
        return x['PLAYER1_NAME']
    else:
        return ""

def disadvantaged_player(x):
    if x['PLAYER2_NAME'] is not "":
        return x['PLAYER2_NAME']
    else:
        return ""

def committing_team(x):
    if x['PLAYER1_TEAM_ABBREVIATION'] is not "":
        return x['PLAYER1_TEAM_ABBREVIATION']
    else:
        return ""

def disadvantaged_team(x):
    if x['PLAYER2_TEAM_ABBREVIATION'] is not "":
        return x['PLAYER2_TEAM_ABBREVIATION']
    else:
        return ""

# Calculate fouls for committing player if foul occurred
def foul_check(x):
    if 'foul' in x['HOMEDESCRIPTION']:
        return x['HOMEDESCRIPTION'].split('foul ',1)[1]
    elif 'FOUL' in x['HOMEDESCRIPTION']:
        return x['HOMEDESCRIPTION'].split('FOUL ',1)[1]
    elif 'Foul' in x['HOMEDESCRIPTION']:
        return x['HOMEDESCRIPTION'].split('Foul ',1)[1]
    else:
        return ""

# Concatenate play-by-play data in description
def pbp_description(x):
    if x['PLAYER1_NAME'] is not "":
        return x['HOMEDESCRIPTION'] + " " + x['NEUTRALDESCRIPTION'] + " " + x['VISITORDESCRIPTION']

# Apply functions to data
merged_data['Visiting Score'] = merged_data.apply(lambda x: visit_score(x), axis=1)
merged_data['Home Score'] = merged_data.apply(lambda x: home_score(x), axis=1)
merged_data['Committing Player'] = merged_data.apply(lambda x: committing_player(x), axis=1)
merged_data['Committing Team'] = merged_data.apply(lambda x: committing_team(x), axis=1)
merged_data['Disadvantaged Player'] = merged_data.apply(lambda x: disadvantaged_player(x), axis=1)
merged_data['Disadvantaged Team'] = merged_data.apply(lambda x: disadvantaged_team(x), axis=1)
merged_data['Play-by-Play Description'] = merged_data.apply(lambda x: pbp_description(x), axis=1)
merged_data['Committing Player Foul Count'] = merged_data.apply(lambda x: foul_check(x), axis=1)