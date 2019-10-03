import argparse
import csv
import os
from jinja2 import Environment, FileSystemLoader


def render_html(teams):
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'template')
    env = Environment(loader = FileSystemLoader(templates_dir))
    template = env.get_template('index.html')
    filename = os.path.join(root, 'html', 'index.html')
    with open(filename, 'w') as fh:
        fh.write(template.render(teams=teams))


def print_scoreboard(scoreboard):
    print('\nThe incredible FTWK scoreboard:\n')
    for score in scoreboard:
        print('{:3}. Platz, {:3} Punkte: {}'.format(score[0], score[1], score[2]))


def sort_places(teams):
    #Sort scores in descending order
    sorted_teams = sorted(teams, reverse=True, key=lambda x: x[1])

    place = 1
    scoreboard = []
    for i in range(len(sorted_teams)):
        score = []
        # Increase number of place only when has fewer points than the last one (same points share the same place)
        if i >= 1 and sorted_teams[i][1] < sorted_teams[i-1][1]:
            place = i + 1
        score.append(place)
        score.append(sorted_teams[i][0])
        score.append(sorted_teams[i][1])
        scoreboard.append(score)
    return scoreboard

def main():
    # Get filename from command line
    parser = argparse.ArgumentParser(description='Read Quiz Scores from csv and make scoreboard')
    parser.add_argument('file', type=argparse.FileType('r'), help='The CSV file containing the scores')
    args = parser.parse_args()

    # Open file
    scorereader = csv.reader(args.file, delimiter=',')
    teams = []

    # Cumulate score for each team
    for team in scorereader:
        # Skip if we don't have at least one round
        if len(team) < 2:
            continue
        # Accumulate all round scores for each team
        score = sum(map(lambda x: float(x), team[1:]))
        teams.append((team[0], score))

    scoreboard = sort_places(teams)
    print_scoreboard(scoreboard)
    render_html(scoreboard)

if __name__ == "__main__":
    main()
