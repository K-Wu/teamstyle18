__author__ = 'Administrator'
from gamemain import GameMain
from communication import MainServer
from time import sleep
import unit
import threading
import asyncore

comm_server=MainServer(('127.0.0.1',18223))
game=GameMain()
server_thread=threading.Thread(target=asyncore.loop)
server_thread.start()
while not comm_server.gamestart:
    sleep(1)
print ('start')
while True:
    game.next_tick()
    #print (game.resource,game.buff,game.units.values())
    comm_server.send_to_player(game.resource)
    #comm_server.send_to_player(game.buff)
    comm_server.send_to_player(list(game.units.values()))
    print (len(game.units.values()))
    game.produce_instr_0=comm_server.conn_list[0].produce_instr
    sleep(0.5)