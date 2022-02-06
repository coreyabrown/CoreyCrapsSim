import crapssim as craps
import customstrat
import csv

n_sim = 10000
bankroll = 200
strategies = {
    "corey": customstrat.corey,
    "coreynofield": customstrat.coreynofield,
    "hammerlock": craps.strategy.hammerlock,
    "knockout": craps.strategy.knockout,
    "pass2come": craps.strategy.pass2come
}

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ["Sim Number", "Strategy", "End Bankroll", "Start Bankroll", "Dice Rolls"]
    writer.writerow(header)
    for i in range(n_sim):
        table = craps.Table()
        for s in strategies:
            table.add_player(craps.Player(bankroll, strategies[s], s))

        table.run(max_rolls=float("inf"), max_shooter=10, verbose=False)
        for s in strategies:
            row = [i, s, table._get_player(s).bankroll, bankroll, table.dice.n_rolls]
            print(f"{i}, {s}, {table._get_player(s).bankroll}, {bankroll}, {table.dice.n_rolls}")

            writer.writerow(row)