'''There are 2 types of enemies:
    1) Which Oscillate
    2) Which Do not oscillate
Case2)Ones that do not oscillate
    They start from right most corner, oges to the left most corner. If player gets into the same block as enemy through 'a' or 'd' then it dies. However if it gets into the same block becaues of gravity the enemy dies.
Case1)Ones that oscillate
    They have a starting point, goes to the leftmmost possible position, now on checking we realize that it oscillates, so we change the direction of motion and thus this thing continues

For all enemies:
    if the player is M and enemy hits it then the enemy dies and player converts to m
    however if the player is m and then the enemey hits it then the player dies
'''
import random, os, time, datetime,sys,select,tty,termios
from person import *
from board import *

os.system('aplay stage_clear.wav&')
time.sleep(.01)
os.system('clear')
print("\t\t\t      WELCOME TO MARIO")
print("\t\t\t\t\tDeveloped by Himanshu Maheshwari")
print("Controls:\n1. Use 'a' key to move towards left\n2. Use 'd' key to move towards right\n3. Use 'w' key to jump\n")
name=input("What is your name? ")
life=3
score=(-100)
if name=='':
    name='Guest'
os.system('clear')

board=Board()
board.Print(name,life,score)

def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [],
            [])

old_settings = termios.tcgetattr(sys.stdin)

ot=0
rising=False
rise=4
isGameOver=False
gameWon=False
isSpawned=True
ote=0
ots=0
allEnemyGone=False
enemiesThere=False
scene=0#To be set to 0
sceneChange=True
crash=False
starCrash=False
starLoc=0
starIteration=0

def blockCreator(height,startLoc,middle='|'):
    board.matrix[height][startLoc]='\033[93m'+'|'+'\033[0m'
    board.matrix[height][startLoc+1]='\033[93m'+'|'+'\033[0m'
    board.matrix[height][startLoc+2]='\033[93m'+middle+'\033[0m'
    board.matrix[height][startLoc+3]='\033[93m'+'|'+'\033[0m'
    board.matrix[height][startLoc+4]='\033[93m'+'|'+'\033[0m'

def thornCreator(startLoc,length):
    for i in range(length):
        board.matrix[19][startLoc+i]='\033[92m'+'^'+'\033[0m'

def pipeCreator(startLoc,height):
    for i in range(height):
        board.matrix[19-i][startLoc]='\033[93m'+'|'+'\033[0m'
        board.matrix[19-i][startLoc+6]='\033[93m'+'|'+'\033[0m'
    board.matrix[20-height][startLoc+1]='\033[93m'+'|'+'\033[0m'
    board.matrix[20-height][startLoc+2]='\033[93m'+'|'+'\033[0m'
    board.matrix[20-height][startLoc+3]='\033[93m'+'|'+'\033[0m'
    board.matrix[20-height][startLoc+4]='\033[93m'+'|'+'\033[0m'
    board.matrix[20-height][startLoc+5]='\033[93m'+'|'+'\033[0m'    

def stairsCreator(startLoc,height,facing="Right"):
    adder=0
    if facing=="Right":
        last=startLoc+(height*3)
        for i in range(height):
            board.matrix[19-i][startLoc+adder]='\033[93m'+'|'+'\033[0m'
            board.matrix[19-i][startLoc+adder+1]='\033[93m'+'|'+'\033[0m'
            board.matrix[19-i][startLoc+adder+2]='\033[93m'+'|'+'\033[0m'
            adder+=3
            board.matrix[19-i][last]='\033[93m'+'|'+'\033[0m'
    else:
        adder=1
        for i in range(height-1,-1,-1):
            board.matrix[19-i][startLoc+adder]='\033[93m'+'|'+'\033[0m'
            board.matrix[19-i][startLoc+adder+1]='\033[93m'+'|'+'\033[0m'
            board.matrix[19-i][startLoc+adder+2]='\033[93m'+'|'+'\033[0m'
            adder+=3
            board.matrix[19-i][startLoc]='\033[93m'+'|'+'\033[0m'

def flagCreator(startLoc):
    for i in range(7):
        board.matrix[19][startLoc+i]='\033[93m'+'|'+'\033[0m'
    for i in range(3):
        board.matrix[18][startLoc+i+2]='\033[93m'+'|'+'\033[0m'
    for i in range(7,18):
        board.matrix[i][startLoc+3]='\033[93m'+'|'+'\033[0m'    
    board.matrix[7][startLoc+2]='\033[93m'+'/'+'\033[0m'
    board.matrix[8][startLoc+1]='\033[93m'+'/'+'\033[0m'
    board.matrix[9][startLoc+1]='\033[93m'+'\\'+'\033[0m'
    board.matrix[10][startLoc+2]='\033[93m'+'\\'+'\033[0m'    
def sceneCreator(scene):
    if scene==1:
        blockCreator(15,12,'*')
        blockCreator(15,30)
        blockCreator(15,35,'*')
        blockCreator(15,40)
        blockCreator(15,45,'*')
        blockCreator(15,50)
        blockCreator(10,40,'?')
        
    elif scene==2:
        pipeCreator(10,2)
        pipeCreator(30,4)
        pipeCreator(58,6)
    elif scene==3:
        thornCreator(7,3)
        blockCreator(15,25)
        blockCreator(15,30,'?')
        blockCreator(15,35)
        thornCreator(48,3)
        thornCreator(53,3)
        thornCreator(58,3)
        thornCreator(63,3)
    elif scene==4:
        blockCreator(15,20,'*')
        blockCreator(10,20,'?')
        blockCreator(10,15,'*')
        blockCreator(10,25,'*')
        blockCreator(15,45)
        blockCreator(15,50,'*')
        blockCreator(15,55)
    elif scene==5:
        blockCreator(15,25,'*')
        blockCreator(15,15,'*')
        blockCreator(15,35,'?')
        blockCreator(10,35,'?')
        blockCreator(15,45,'*')
        blockCreator(15,55,'*')
    elif scene==6:
        blockCreator(15,40)
        blockCreator(15,45)
        blockCreator(10,40,'*')        
        blockCreator(10,45,'*')
        blockCreator(10,50,'*')
        blockCreator(10,35,'*')
    elif scene==7:
        stairsCreator(5,5)
        thornCreator(21,4)
        stairsCreator(25,5,"Left")
        pipeCreator(55,4)
        board.matrix[19][54]='\033[92m'+'^'+'\033[0m'
        board.matrix[19][62]='\033[92m'+'^'+'\033[0m'
    elif scene==8:
        stairsCreator(5,10)
        thornCreator(36,7)
        flagCreator(60)    
try:
    tty.setcbreak(sys.stdin.fileno())
    while isGameOver==False:
        if crash==True:
            player.position=1
            sceneChange=True
            scene-=1
            board.matrix[19][1]=player.shape
            isSpawned=False
            os.system('clear')
            board.Print(name,life,score)
            crash=False
            score-=100

        if sceneChange==True:
            scene+=1
            score+=100
            board.factoryCondition()
            sceneCreator(scene)
            sceneChange=False
            board.matrix[19-player.height][1]=player.shape
            board.matrix[19][68]='\033[91m'+'_'+'\033[0m'
            player.position=1
            os.system('clear')
            isSpawned=False
            board.Print(name,life,score)

        if isSpawned==False:
            allEnemyGone=False
            enemiesThere=True
            os.system('clear')
            enemy=[]
            if scene==1:
                enemy.append(Enemy())
            elif scene==2:
                enemy.append(Enemy(29,17,True))
                enemy.append(Enemy(57,37,True))
                enemy.append(Enemy(53,37,True))
            elif scene==3:
                enemy.append(Enemy(45,11,True))    
            elif scene==4:
                enemy.append(Enemy())
                enemy.append(Enemy(50,0,False))
                enemy.append(Enemy(45,25,True))
                enemy.append(Enemy(55,5,True))
            elif scene==5:
                enemy.append(Enemy())
                enemy.append(Enemy(59,0,False))
                enemy.append(Enemy(49,0,False))
                enemy.append(Enemy(39,0,False))
                enemy.append(Enemy(29,0,False))
            elif scene==6: 
                enemy.append(Enemy())
                enemy.append(Enemy(37,13,True))
                enemy.append(Enemy(29,2,True))
            else:
                enemiesThere=False  
            for i in enemy:    
                board.matrix[19][i.startPosition]='\033[90m'+'0'+'\033[0m'
            board.Print(name,life,score)
            isSpawned=True
            ote=datetime.datetime.now()
            ote=(ote.hour*3600+ote.minute*60+ote.second)*1000+ote.microsecond/1000

        ct=datetime.datetime.now()
        ct=(ct.hour*3600+ct.minute*60+ct.second)*1000+ct.microsecond/1000
        if isData():
            c=sys.stdin.read(1)
            if(c=='d' or c=='D'):
                if board.matrix[19-player.height][player.position+1]=='\033[91m'+'|'+'\033[0m' or board.matrix[19-player.height][player.position+1]=='\033[93m'+'|'+'\033[0m':
                    pass
                else:
                    if player.height==0:
                        board.matrix[19][player.position]='\033[91m'+'_'+'\033[0m'
                    else:
                        board.matrix[19-player.height][player.position]=' '
                    if board.matrix[19-player.height][player.position+1] == '\033[92m'+'^'+'\033[0m' or board.matrix[19-player.height][player.position+1]=='\033[90m'+'0'+'\033[0m':
                        life-=1 
                        player.shape='m'
                        score-=100
                        crash=True
                        os.system('aplay death.wav&')
                        time.sleep(.01)
                    board.matrix[19-player.height][player.position+1]=player.shape
                    player.position+=1
                    os.system('clear')
                    board.Print(name,life,score)
                    if player.position==68:
                        sceneChange=True
                    if scene==8 and player.position>=60:
                        gameWon=True
                        isGameOver=True
            elif (c=='a' or c=='A'):
                if board.matrix[19-player.height][player.position-1]=='\033[91m'+'|'+'\033[0m' or board.matrix[19-player.height][player.position-1]=='\033[93m'+'|'+'\033[0m':
                    pass
                else:
                    if player.height==0:
                        board.matrix[19][player.position]='\033[91m'+'_'+'\033[0m'
                    else:
                        board.matrix[19-player.height][player.position]=' '
                    if board.matrix[19-player.height][player.position-1]== '\033[92m'+'^'+'\033[0m' or board.matrix[19-player.height][player.position-1]=='\033[90m'+'0'+'\033[0m':
                        life-=1
                        score-=100
                        player.shape='m'
                        crash=True
                        os.system('aplay death.wav&')
                        time.sleep(.01)
                    board.matrix[19-player.height][player.position-1]=player.shape
                    player.position-=1
                    os.system('clear')
                    board.Print(name,life,score)
            elif c=='w' or c=='W':
                if player.height==0 or board.matrix[20-player.height][player.position]=='\033[93m'+'|'+'\033[0m' or board.matrix[20-player.height][player.position]=='\033[93m'+'?'+'\033[0m' or board.matrix[20-player.height][player.position]=='\033[93m'+'*'+'\033[0m':
                    os.system('aplay jump.wav&')
                    time.sleep(.01)
                    if player.height==0:
                        board.matrix[19][player.position]='\033[91m'+'_'+'\033[0m'
                    else:
                        board.matrix[19-player.height][player.position]=' '
                    player.height+=1
                    if board.matrix[19-player.height][player.position]== '\033[92m'+'^'+'\033[0m':
                        life-=1
                        score-=100
                        player.shape='m'
                        crash=True
                        os.system('aplay death.wav&')
                        time.sleep(.01)
                    board.matrix[19-player.height][player.position]=player.shape
                    os.system('clear')
                    board.Print(name,life,score)
                    ot=0
                    rising=True
                    if player.shape=='m':
                        rise=4
                    else:
                        rise=6
            elif c=='q' or c=='Q':
                isGameOver=True
                os.system('aplay death.wav&')
                time.sleep(.01)     
                os.system('clear')
                print("\t\t\t\tYOU LOST")
                print("\t\t\t     Your Score =",score)

        if ct-ot>=80 and rising==True:
            if board.matrix[18-player.height][player.position]=='\033[93m'+'*'+'\033[0m':
                starCrash=True
                score+=100
                board.matrix[18-player.height][player.position]='\033[93m'+'|'+'\033[0m'
                starLoc=player.position
                starHeight=player.height+2
                starIteration=1
                os.system('aplay coin.wav&')
                time.sleep(.01)
                ots=datetime.datetime.now()
                ots=(ots.hour*3600+ots.minute*60+ots.second)*1000+ots.microsecond/1000
            elif board.matrix[18-player.height][player.position]=='\033[93m'+'?'+'\033[0m':
                board.matrix[18-player.height][player.position]='\033[93m'+'|'+'\033[0m'
                player.shape='M'
                score+=150
                os.system('aplay power.wav&')
                time.sleep(.01)
            if board.matrix[18-player.height][player.position]!=' ':#\033[93m'+'|'+'\033[0m':
                rising=False
            else:
                if player.height==0:
                    board.matrix[19][player.position]='\033[91m'+'_'+'\033[0m'
                else:
                    board.matrix[19-player.height][player.position]=' '
                rise-=1
                player.height+=1
                board.matrix[19-player.height][player.position]=player.shape
                ot=ct
                os.system('clear')
                board.Print(name,life,score)
                if rise==0:
                    rising=False
        elif ct-ot>=80 and rising==False and player.height!=0 and board.matrix[20-player.height][player.position]!='\033[93m'+'|'+'\033[0m' and board.matrix[20-player.height][player.position]!='\033[93m'+'?'+'\033[0m' and board.matrix[20-player.height][player.position]!='\033[93m'+'*'+'\033[0m':
            if player.height==0:
                board.matrix[19][player.position]='\033[91m'+'_'+'\033[0m'
            else:
                board.matrix[19-player.height][player.position]=' '
            player.height-=1
            if board.matrix[19-player.height][player.position]== '\033[92m'+'^'+'\033[0m':
                life-=1
                score-=100
                player.shape='m'
                crash=True
                os.system('aplay death.wav&')
                time.sleep(.01)
            elif board.matrix[19-player.height][player.position]== '\033[90m'+'0'+'\033[0m':
                for i,o in enumerate(enemy):
                    if o.position==player.position:
                        del enemy[i]
                score+=100
                if len(enemy)==0:
                    allEnemyGone=True        
            board.matrix[19-player.height][player.position]=player.shape
            ot=ct
            os.system('clear')
            board.Print(name,life,score)

        if ct-ots>=80 and starIteration<=4 and starIteration!=0:
            if starIteration==1:
                board.matrix[19-starHeight][starLoc]='\033[93m'+'*'+'\033[0m'
            elif starIteration==2:
                board.matrix[19-starHeight][starLoc]=' '
                board.matrix[18-starHeight][starLoc]='\033[93m'+'*'+'\033[0m'
            elif starIteration==3:
                board.matrix[19-starHeight][starLoc]='\033[93m'+'*'+'\033[0m'
                board.matrix[18-starHeight][starLoc]=' '
            else:
                board.matrix[19-starHeight][starLoc]=' '
            os.system('clear')
            board.Print(name,life,score)
            starIteration+=1
            ots=ct                            
        
        if ct-ote>=100:
            if allEnemyGone==True:
                pass
            elif enemiesThere==True:
                for i,o in enumerate(enemy):
                    if o.oscillate==False:
                        o.position-=1
                        if o.position==o.endPosition:
                            if len(enemy)==1:
                               allEnemyGone=True
                            board.matrix[19][o.position+1]='\033[91m'+'_'+'\033[0m'
                            del enemy[i]
                            os.system('clear')
                            board.Print(name,life,score)
                        else:
                            board.matrix[19][o.position+1]='\033[91m'+'_'+'\033[0m'
                            if board.matrix[19][o.position]==player.shape:
                                life-=1
                                score-=100
                                player.shape='m'
                                crash=True
                                os.system('aplay death.wav&')
                                time.sleep(.01)
                            board.matrix[19][o.position]='\033[90m'+'0'+'\033[0m'
                            os.system('clear')
                            board.Print(name,life,score)
                            ote=ct
                    else:
                        if o.currDirection=="RL":
                            o.position-=1
                            if o.position==o.endPosition:
                                o.currDirection="LR"
                            else:
                                board.matrix[19][o.position+1]='\033[91m'+'_'+'\033[0m'
                                if board.matrix[19][o.position]==player.shape:
                                    life-=1
                                    score-=100
                                    player.shape='m'
                                    crash=True
                                    os.system('aplay death.wav&')
                                    time.sleep(.01)
                                board.matrix[19][o.position]='\033[90m'+'0'+'\033[0m'
                                os.system('clear')
                                board.Print(name,life,score)
                                ote=ct
                        else:
                            o.position+=1
                            if o.position==o.startPosition:
                                o.currDirection="RL"
                            else:
                                board.matrix[19][o.position-1]='\033[91m'+'_'+'\033[0m'
                                if board.matrix[19][o.position]==player.shape:
                                    life-=1
                                    score-=100
                                    player.shape='m'
                                    crash=True
                                    os.system('aplay death.wav&')
                                    time.sleep(.01)
                                board.matrix[19][o.position]='\033[90m'+'0'+'\033[0m'
                                os.system('clear')
                                board.Print(name,life,score)
                                ote=ct
        if life==0:
            isGameOver=True
            os.system('aplay death.wav&')
            time.sleep(.01)     
            os.system('clear')
            print("\t\t\t\tYOU LOST")
            print("\t\t\t     Your Score =",score)           
    ot=datetime.datetime.now()
    ot=(ot.hour*3600+ot.minute*60+ot.second)*1000+ot.microsecond/1000
    flagPos=7
    if gameWon==True:
        os.system('aplay world_clear.wav&')
        time.sleep(.01)
        while True:
            ct=datetime.datetime.now()
            ct=(ct.hour*3600+ct.minute*60+ct.second)*1000+ct.microsecond/1000
            if ct-ot>=300 and flagPos<=13:
                board.matrix[flagPos][62]=' '
                board.matrix[flagPos+1][61]=' '
                board.matrix[flagPos+2][61]=' '
                board.matrix[flagPos+3][62]=' '
                flagPos+=1
                board.matrix[flagPos][62]='\033[93m'+'/'+'\033[0m'
                board.matrix[flagPos+1][61]='\033[93m'+'/'+'\033[0m'
                board.matrix[flagPos+2][61]='\033[93m'+'\\'+'\033[0m'
                board.matrix[flagPos+3][62]='\033[93m'+'\\'+'\033[0m'
                os.system('clear')
                board.Print(name,life,score)
                ot=ct
            elif flagPos>13:
                break
        ot=datetime.datetime.now()
        ot=(ot.hour*3600+ot.minute*60+ot.second)*1000+ot.microsecond/1000
        situation=1
        while True:
            ct=datetime.datetime.now()
            ct=(ct.hour*3600+ct.minute*60+ct.second)*1000+ct.microsecond/1000
            if ct-ot>=300 and situation==1:
                board.matrix[17][62]=' '
                board.matrix[16][61]=' '
                board.matrix[15][61]=' '
                board.matrix[14][62]=' '
                os.system('clear')
                board.matrix[15][62]='\033[93m'+'/'+'\033[0m'
                board.matrix[16][62]='\033[93m'+'\\'+'\033[0m'
                board.Print(name,life,score)
                ot=ct
                situation+=1
            elif ct-ot>=300 and situation==2:
                board.matrix[15][62]=' '
                board.matrix[16][62]=' '
                os.system('clear')
                board.Print(name,life,score)
                ot=ct
                situation+=1
            elif ct-ot>=300 and situation==3:
                board.matrix[7][62]='/'
                board.matrix[8][61]='/'
                board.matrix[9][61]='\\'
                board.matrix[10][62]='\\'
                board.matrix[8][62]=player.shape
                ot=ct
                os.system('clear')
                board.Print(name,life,score)
                situation+=1
            elif ct-ot>=2000 and situation==4:
                break    

        os.system('clear')
        print("\t\t\t\tCONGRATS")
        print("\t\t\t\tYOU  WON")
        print("\t\t\t     Your Score =",score)                            
finally:                
    termios.tcsetattr(sys.stdin,termios.TCSADRAIN,old_settings)