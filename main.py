import pickle
from player import Player
import pickle

def save_state(player):
    outfile = open("savedata", "wb")
    pickle.dump(player, outfile)
    outfile.close()

def load_state():
    infile = open("savedata", "rb")
    player = pickle.load(infile)
    infile.close()
    return player

if __name__ == "__main__":
    p = load_state()
    #p = Player(10000)
    p.market.displayAll()
    p.act()
    p.update()
    save_state(p)