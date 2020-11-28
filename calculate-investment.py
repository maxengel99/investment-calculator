import plotly.graph_objects as go

header = dict(
    values=['ANWPX Percentage', 'ABALX Percentage',
            'Bonds Goal', 'Bonds Amount', 'Bonds Difference',
            'Domestic Goal', 'Domestic Amount', 'Domestic Difference',
            'Foreign Goal', 'Foreign Amount', 'Foreign Difference',
            'Total Deviation'],
    line_color='darkslategray',
    fill_color='lightskyblue',
    align='left')

bonds_goal = .4
domestic_goal = .32
foreign_goal = .18
percentage_goal = 90

bonds_goal_col = [bonds_goal] * percentage_goal
domestic_goal_col = [domestic_goal] * percentage_goal
foreign_goal_col = [foreign_goal] * percentage_goal

an_percent_col = []
ab_percent_col = []
bonds_amount_col = []
bonds_diff_col = []
domestic_amount_col = []
domestic_diff_col = []
foreign_amount_col = []
foreign_diff_col = []
total_deviation_col = []

for an_percent in range(0, percentage_goal + 1):
    ab_percent = percentage_goal - an_percent
    an_percent_col.append(an_percent)
    ab_percent_col.append(ab_percent)

    cur_bonds = round((.4 * ab_percent) / 100, 2)
    cur_domestic = round(((.54 * an_percent) + (.6 * ab_percent)) / 100, 2)
    cur_foreign = round((.42 * an_percent) / 100, 2)

    bonds_amount_col.append(cur_bonds)
    domestic_amount_col.append(cur_domestic)
    foreign_amount_col.append(cur_foreign)

    bonds_diff_col.append(round(cur_bonds - bonds_goal, 2))
    domestic_diff_col.append(round(cur_domestic - domestic_goal, 2))
    foreign_diff_col.append(round(cur_foreign - foreign_goal, 2))

    total_deviation_col.append(round(abs(cur_bonds - bonds_goal)
                                     + abs(cur_domestic - domestic_goal)
                                     + abs(cur_foreign - foreign_goal), 2))

fill_colors = []
fill_colors.append(['#e6f2fd'] * 90)
fill_colors.append(['#e6f2fd'] * 90)
fill_colors.append(['#e6f2fd'] * 90)
fill_colors.append(['#e6f2fd'] * 90)

bonds_colors = []
for value in bonds_diff_col:
    if value < 0:
        bonds_colors.append('red')
    elif value == 0:
        bonds_colors.append('green')
    else:
        bonds_colors.append('blue')

fill_colors.append(bonds_colors)
fill_colors.append(['#e6f2fd'] * 90)
fill_colors.append(['#e6f2fd'] * 90)

domestic_colors = []
for value in domestic_diff_col:
    if value < 0:
        domestic_colors.append('red')
    elif value == 0:
        domestic_colors.append('green')
    else:
        domestic_colors.append('blue')

fill_colors.append(domestic_colors)
fill_colors.append(['#e6f2fd'] * 90)
fill_colors.append(['#e6f2fd'] * 90)

foreign_colors = []
for value in foreign_diff_col:
    if value < 0:
        foreign_colors.append('red')
    elif value == 0:
        foreign_colors.append('green')
    else:
        foreign_colors.append('blue')

fill_colors.append(foreign_colors)
fill_colors.append(['#e6f2fd'] * 90)


fig = go.Figure(data=[go.Table(
    header=header,
    cells=dict(
        values=[an_percent_col, ab_percent_col,
                bonds_goal_col, bonds_amount_col, bonds_diff_col,
                domestic_goal_col, domestic_amount_col, domestic_diff_col,
                foreign_goal_col, foreign_amount_col, foreign_diff_col,
                total_deviation_col],
        line_color='darkslategray',
        fill_color=fill_colors,
        align='left'))
])

fig.update_layout(width=900, height=1000, font=dict(size=10))
fig.show()
