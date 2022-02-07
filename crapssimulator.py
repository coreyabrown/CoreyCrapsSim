import crapssim as craps
import customstrat
import csv

n_sim = 10000
bankroll = 200
strategies = {
    "nofield": customstrat.nofield,
    "hedged2come": customstrat.hedged2come,
    "knockout": craps.strategy.knockout,
    "pass2come": craps.strategy.pass2come,
    "risk12": craps.strategy.risk12
}

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ["Sim Number", "Strategy", "End Bankroll", "Start Bankroll", "Dice Rolls", "Difference", "Dollar/Roll"]
    writer.writerow(header)
    for i in range(n_sim):
        table = craps.Table()
        for s in strategies:
            table.add_player(craps.Player(bankroll, strategies[s], s))

        table.run(max_rolls=float("inf"), max_shooter=10, verbose=False)
        for s in strategies:
            row = [i, s, table._get_player(s).bankroll, bankroll, table.dice.n_rolls, table._get_player(s).bankroll-bankroll, (table._get_player(s).bankroll-bankroll)/table.dice.n_rolls]
            print(row)

            writer.writerow(row)