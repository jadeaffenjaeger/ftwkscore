# FTWK Score Board

Tool to add up pub quiz scores, generate ranking and write the output to an HTML page for display.

## Usage
Store team names followed by the scores for each round in a CSV file. Dots need to be used for decimals. Run script via: `python ftwkscore.py <path to csv>`. For an example, type:
```
python ftwkscore.py data/demo.csv
```
The scoreboard website will be generated in the `/html` directory from the template found in the `/template` directory.
