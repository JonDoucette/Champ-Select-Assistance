import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg #Install
import pygame_gui as pgui #Install
import pygame.freetype

import requests

import webbrowser
import sys
import urllib3
import json
#import pygame.gfxdraw

import lockfileLocation

# print(lockfileLocation.lockfileLocation)

####BENCH CHAMPION ID INSIDE OF SESSION
#"bans":{"myTeamBans":[],"numBans":0,"theirTeamBans":[]},"benchChampionIds":[117,68,1],"benchEnabled":true,
#EXAMPLE RESPONSE


true = True
false = False
null = None
LOCKFILE_LOCATION = lockfileLocation.lockfileLocation
#LOCKFILE_LOCATION = 'C:/Riot Games/League of Legends/lockfile'
# LOCKFILE_LOCATION = '/mnt/c/Riot Games/League of Legends/lockfile'


exampleResponse = {"actions":[],"allowBattleBoost":true,"allowDuplicatePicks":false,"allowLockedEvents":false,"allowRerolling":true,"allowSkinSelection":true,"bans":{"myTeamBans":[],"numBans":0,"theirTeamBans":[]},"benchChampionIds":[117,68,1],"benchEnabled":true,"boostableSkinCount":1,"chatDetails":{"chatRoomName":"678723d4-0cb7-4e56-b8f0-2276b7edb06f@champ-select.pvp.net","chatRoomPassword":null},"counter":15,"entitledFeatureState":{"additionalRerolls":0,"unlockedSkinIds":[]},"gameId":4083137282,"hasSimultaneousBans":true,"hasSimultaneousPicks":true,"isCustomGame":false,"isSpectating":false,"localPlayerCellId":5,"lockedEventIndex":-1,"myTeam":[{"assignedPosition":"","cellId":5,"championId":201,"championPickIntent":0,"entitledFeatureType":"NONE","selectedSkinId":201000,"spell1Id":4,"spell2Id":14,"summonerId":23154616,"team":2,"wardSkinId":1},{"assignedPosition":"","cellId":6,"championId":57,"championPickIntent":0,"entitledFeatureType":"NONE","selectedSkinId":57001,"spell1Id":4,"spell2Id":7,"summonerId":19848698,"team":2,"wardSkinId":-1},{"assignedPosition":"","cellId":7,"championId":518,"championPickIntent":0,"entitledFeatureType":"NONE","selectedSkinId":518000,"spell1Id":13,"spell2Id":4,"summonerId":65134043,"team":2,"wardSkinId":-1},{"assignedPosition":"","cellId":8,"championId":45,"championPickIntent":0,"entitledFeatureType":"NONE","selectedSkinId":45003,"spell1Id":4,"spell2Id":3,"summonerId":50402045,"team":2,"wardSkinId":-1},{"assignedPosition":"","cellId":9,"championId":120,"championPickIntent":0,"entitledFeatureType":"NONE","selectedSkinId":120006,"spell1Id":4,"spell2Id":32,"summonerId":72349956,"team":2,"wardSkinId":-1}],"recoveryCounter":0,"rerollsRemaining":1,"skipChampionSelect":false,"theirTeam":[{"assignedPosition":"","cellId":0,"championId":0,"championPickIntent":0,"entitledFeatureType":"","selectedSkinId":0,"spell1Id":0,"spell2Id":0,"summonerId":0,"team":1,"wardSkinId":-1},{"assignedPosition":"","cellId":1,"championId":0,"championPickIntent":0,"entitledFeatureType":"","selectedSkinId":0,"spell1Id":0,"spell2Id":0,"summonerId":0,"team":1,"wardSkinId":-1},{"assignedPosition":"","cellId":2,"championId":0,"championPickIntent":0,"entitledFeatureType":"","selectedSkinId":0,"spell1Id":0,"spell2Id":0,"summonerId":0,"team":1,"wardSkinId":-1},{"assignedPosition":"","cellId":3,"championId":0,"championPickIntent":0,"entitledFeatureType":"","selectedSkinId":0,"spell1Id":0,"spell2Id":0,"summonerId":0,"team":1,"wardSkinId":-1},{"assignedPosition":"","cellId":4,"championId":0,"championPickIntent":0,"entitledFeatureType":"","selectedSkinId":0,"spell1Id":0,"spell2Id":0,"summonerId":0,"team":1,"wardSkinId":-1}],"timer":{"adjustedTimeLeftInPhase":54123,"internalNowInEpochMs":1635315706208,"isInfinite":false,"phase":"FINALIZATION","totalTimeInPhase":70000},"trades":[{"cellId":7,"id":35,"state":"AVAILABLE"},{"cellId":9,"id":43,"state":"AVAILABLE"},{"cellId":8,"id":13,"state":"AVAILABLE"},{"cellId":6,"id":54,"state":"AVAILABLE"}]}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#Initialize Pygame and Pygame Freetype (for fonts)
pg.init()
pg.freetype.init()

text = "Test Button"

WIDTH, HEIGHT = 800, 600

global test_entry, textbox, image

winrateText = '0'


# r = requests.get(f'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-icons/78.png')
# open('champImage.png', 'wb').write(r.content)
# del r

#Set the active window to win
win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Sweaty Champ Select')
icon =  pygame.image.load('sweat.ico')
pygame.display.set_icon(icon)

#Saving background color
BACKGROUNDCOLOR = pg.Color("#322f3d")

#Set UI Manager
ui_manager = pgui.UIManager((WIDTH, HEIGHT))

#Generate all Buttons
def generate_ui():
    ui_manager.clear_and_reset()

    global test_entry, textbox


    UggButton = pgui.elements.UIButton(relative_rect=pg.Rect(WIDTH - 300 - 200, HEIGHT - 100, 200, 50),
                                               text="U.GG", manager=ui_manager, object_id="ugg")
    lolAlyticsButton = pgui.elements.UIButton(relative_rect=pg.Rect(40, HEIGHT - 100, 200, 50),
                                               text="Lolalytics", manager=ui_manager, object_id="lolalytics")
    leagueOfGraphsButton = pgui.elements.UIButton(relative_rect=pg.Rect(WIDTH - 240, HEIGHT - 100, 200, 50),
                                               text="League of Graphs", manager=ui_manager, object_id="graphs")



#Draw all Text Items
def drawText(champImage, champDict, champId, gameMode):
    global image, winrateText

    currentText = ''

    champImage = pygame.image.load(champImage)
    image = pygame.transform.scale(champImage, (75,75))
    win.blit(image, (190+90, 225))

    if winrateText == '0' or winrateText == '':
        currentText = ' '
    else:
        currentText = f"Winrate: {winrateText}%"

    if gameMode == 0:
        pygame.freetype.SysFont("freesansbold.ttf", 30).render_to(win,(190+50,(190)), 'Waiting on Champ Select', (255,255,255))
    elif gameMode == "Summoner's Rift":
        pygame.freetype.SysFont("freesansbold.ttf", 30).render_to(win,(190+60,(190)), "Summoner's Rift", (255,255,255))
    elif gameMode == "ARAM":
        pygame.freetype.SysFont("freesansbold.ttf", 30).render_to(win,(190+135,(190)), "ARAM", (255,255,255))



    #Using System font called Freesans bold draw text to 50,50
    pygame.freetype.SysFont("freesansbold.ttf", 16).render_to(win,(WIDTH-175, HEIGHT - 35), "Sweaty Champ Select", (255,255,255))
    pygame.freetype.SysFont("freesansbold.ttf", 12).render_to(win,(WIDTH-105, HEIGHT - 20), "By Jon Doucette", (255,255,255))
    pygame.freetype.SysFont("freesansbold.ttf", 30).render_to(win,(190+180,(230+75/2)), currentText, (255,255,255))

    if champId != 0:
        try:
            champName = champDict[champId][0]
        except:
            champName = ''

        pygame.freetype.SysFont("freesansbold.ttf", 30).render_to(win,(190+180,(230+15/2)), champName, (255,255,255))




def drawTeam(activeChampions, champDict):
    yValue = 85
    fakeChampions = 5 - len(activeChampions)



    for i in activeChampions:

        try:
            champName = champDict[i][0]
            winrate = champDict[i][1]
        except:
            champName = ''
            winrate = '0'

        if i == 0:
            champImage = 'champImages/-1.png'
        else:
            champImage = f'champImages/{i}.png'
            pygame.freetype.SysFont("freesansbold.ttf", 16).render_to(win,(105,yValue+15), f"{champName}", (255,255,255))
            pygame.freetype.SysFont("freesansbold.ttf", 16).render_to(win,(105,yValue+35), f"{winrate}%", (255,255,255))

        champImage = pygame.image.load(champImage)
        image = pygame.transform.scale(champImage, (60,60))
        win.blit(image, (42.5, yValue))



        yValue += 80

    for i in range(fakeChampions):
        champImage = 'champImages/-1.png'
        champImage = pygame.image.load(champImage)

        image = pygame.transform.scale(champImage, (60,60))
        win.blit(image, (42.5, yValue))
        yValue += 80


def drawBench(benchChampions, benchDict):
    xValue = 165

    for i in benchChampions:
        champImage = f'champImages/{i}.png'
        champImage = pygame.image.load(champImage)
        image = pygame.transform.scale(champImage, (50,50))
        win.blit(image, (xValue, 35))
        pygame.freetype.SysFont("freesansbold.ttf", 14).render_to(win,(xValue+5,25), f"{benchDict[i][1]}%", (255,255,255))
        xValue += 60



def openURL(OPURL):
    webbrowser.open(OPURL, new=0)
    return('Test')



#Gets the current active game mode
def getGameMode(url, password):
    r = requests.get(url + '/lol-gameflow/v1/session', verify=False, auth=('riot', password))
    if r.status_code == 404:
        #print('Please go to Champion Select')
        return 0
    data = r.json()
    gameMode = data['map']['gameModeShortName']
    return gameMode



def getChampName(champId):
    championUrl = 'http://ddragon.leagueoflegends.com/cdn/11.21.1/data/en_US/champion.json'
    r = requests.get(championUrl)
    data = r.json()['data']

    for champion in data:
        if int(data[champion]['key']) == champId:
            if data[champion]['id'] == 'MonkeyKing':
                return 'Wukong'
            return data[champion]['id']


def getChampImage(champId):
    r = requests.get(f'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-icons/{champId}.png')
    imageURL = f'champImage-{champId}.png'
    open(imageURL, 'wb').write(r.content)
    del r
    return imageURL


def getWinRate(champName, champId, gameMode):

        champName = (champName).lower()

        if gameMode == 'ARAM':
            URL = f'https://lolalytics.com/lol/{champName}/aram/build/'
            # URL = f'https://u.gg/lol/champions/aram/{champName}-aram'
            # fileURL = f'https://stats2.u.gg/lol/1.1/overview/11_21/normal_aram/{champId}/1.5.0.json'
            # ranking = 'world_overall_none'
        else:
            URL = f'https://lolalytics.com/lol/{champName}/build/'
            # URL = f'https://u.gg/lol/champions/{champName}/build?role={role}'
            # fileURL = f'https://stats2.u.gg/lol/1.1/rankings/11_21/ranked_solo_5x5/{champId}/1.5.0.json'
            # ranking = f'world_gold_{role}'

        try:
            r = requests.get(URL)
            text = r.text
            winrate = (text.split('"wr":')[1]).split(',')[0]
            return winrate
        except:
            # print('Failed winrate')
            return 0


#Returns Team Champion List and Player Champion
def getTeamChampions(URL, password, summonerId):
    r = requests.get(URL + '/lol-champ-select/v1/session', verify=False, auth=('riot', password))
    data = r.json()

    if r.status_code == 404:
        return False, [], 0

    teamMateList = []
    cellIdList = []

    #Loops through teammates and stores all champions
    for teammate in data['myTeam']:
        champId = teammate['championId']
        cellId = teammate['cellId']
        teamMateList.append(champId)
        cellIdList.append(cellId)

        if summonerId == int(teammate['summonerId']):
            playerChamp = champId

    return True, teamMateList, playerChamp



def getBenchedChampions(URL, password):
    r = requests.get(URL + '/lol-champ-select/v1/session', verify=False, auth=('riot', password))
    data = r.json()
    if r.status_code == 404:
        return

    benchChampIds = data['benchChampionIds']
    return benchChampIds



#Main looping function for GUI
def main():
    clock = pg.time.Clock()
    run = True
    FPS = 60
    champDict = {}
    benchDict = {}
    activeChampions = []
    benchedChampions = []


    global test_entry, textbox, winrateText

    #Get Port Number and Password for Local Host
    try:
        with open(LOCKFILE_LOCATION) as f:
            line = f.readline()
            f.close()

        port = line.split(':', 4)[2]
        password = line.split(':', 4)[3]

        # print('LCU port: ' + port)
        # print('LCU password: ' + password)
        # print()

    except Exception as e:
        # print(e)
        # print('Please open the League Client')
        pg.quit()
        sys.exit()

    URL = f'https://127.0.0.1:{port}'

    summonerId = int(requests.get(URL + '/lol-summoner/v1/current-summoner', verify=False, auth=('riot', password)).json()['summonerId'])


    # #Gets Champion Role Data
    # roleData = requests.get('https://stats2.u.gg/lol/1.1/primary_roles/11_21/1.5.0.json')
    # roleData = roleData.json()

    champId = 0
    gameMode = 1
    champId = 0
    newChampId = 0

    champImage = 'champImages/-1.png'

    #Generate the buttons once
    generate_ui()

    #While the program is set to run
    while run:
        time_delta = clock.tick(FPS)/1000.0

        #If the user clicks the Red X top right corner, stop running and quit GUI
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()


            #If the user does an action that isn't X in the top right
            if event.type == pg.USEREVENT:
                #If the action is pressing a button
                if event.user_type == pgui.UI_BUTTON_PRESSED:
                    #If the button equals object id
                    if event.ui_object_id == "ugg":
                       if gameMode == 'ARAM':
                           response = openURL(f'https://u.gg/lol/champions/aram/{(champDict[champId][0]).lower()}-aram')
                       elif gameMode == 0 or champId == 0:
                           response = openURL(f'https://u.gg')
                       else:
                           response = openURL(f'https://u.gg/lol/champions/{(champDict[champId][0]).lower()}/build')
                    if event.ui_object_id == "lolalytics":
                       if gameMode == 'ARAM':
                           response = openURL(f'https://lolalytics.com/lol/{(champDict[champId][0]).lower()}/aram/build/')
                       elif gameMode == 0 or champId == 0:
                           response = openURL(f'https://lolalytics.com')
                       else:
                           response = openURL(f'https://lolalytics.com/lol/{(champDict[champId][0]).lower()}/build')
                    if event.ui_object_id == "graphs":
                       if gameMode == 'ARAM':
                           response = openURL(f'https://www.leagueofgraphs.com/champions/builds/{(champDict[champId][0]).lower()}/aram')
                       elif gameMode == 0 or champId == 0:
                           response = openURL(f'https://www.leagueofgraphs.com/')
                       else:
                           response = openURL(f'https://www.leagueofgraphs.com/champions/builds/{(champDict[champId][0]).lower()}')





            #Lets the UI manager process all actions that have been done
            ui_manager.process_events(event)




        #Returns the current active Gamemode
        newGameMode = getGameMode(URL, password)

        #If new game mode, update game mode
        if gameMode != newGameMode:
            gameMode = newGameMode
            if gameMode == 0:
                newChampId = 0
                champDict = {}
                benchDict = {}
            #UPDATE SCREEN TO SHOW GAMEMODE

        if newChampId == 0:
            champId = newChampId

        if True:

            status, activeChampions, newChampId = getTeamChampions(URL, password, summonerId)
            # print(newChampId)









            #Loop through all champions and print winrate
            for champion in activeChampions:
                if champion == 0:
                    continue
                if champion in benchDict: #If the active champion was from benched, remove from bench add to active
                    champName = benchDict[champion][0]
                    winrate = benchDict[champion][1]
                    champDict[champion] = [champName, winrate]
                    del benchDict[champion]
                if champion not in champDict: #If the active champion is not in the dictionary, add to dictionary
                    champName = getChampName(champion)
                    winrate = getWinRate(champName, champId, gameMode)
                    champDict[champion] = [champName, winrate]

            try:
                if gameMode == 'ARAM' and status:
                    benchedChampions = getBenchedChampions(URL, password)
                    # print(benchedChampions)

                    #Check each benched champion to ensure they're still benched
                    for champion in benchedChampions:
                        if champion in champDict: #If benched is found in active, remove from active add to benched dict
                            champName = champDict[champion][0]
                            winrate = champDict[champion][1]
                            benchDict[champion] = [champName, winrate]
                            del champDict[champion]
                        elif champion not in benchDict:
                            champName = getChampName(champion)
                            winrate = getWinRate(champName, champId, gameMode)
                            benchDict[champion] = [champName, winrate]
            except Exception as e:
                # print(e)
                pass


            # for champion in champDict:
            #     if len(champDict[champion]) < 3: #If there is no image URL, then add it
            #         imageURL = getChampImage(champion)
            #         champDict[champion].append(imageURL)


            if int(champId) != int(newChampId) and newChampId != 0:
                champId = newChampId
                try:
                    champName = champDict[champId]
                    winrateText = champDict[champId][1]
                except:
                    champName = ''
                    winrateText = ''
                #UPDATE CHAMP IMAGE
                champImage = f'champImages/{champId}.png'

            elif newChampId == 0:
                champImage = 'champImages/-1.png'
                winrateText = ''


        #Update UI Manager
        ui_manager.update(time_delta)
        #Fill the background in
        win.fill(BACKGROUNDCOLOR)
        #Draws all text
        drawText(champImage, champDict, champId, gameMode)
        #Draws UI into window
        ui_manager.draw_ui(win)

        if gameMode != 0:
            drawTeam(activeChampions, champDict)
        if gameMode == 'ARAM':
            drawBench(benchedChampions, benchDict)


        # print(champDict)
        # print(benchDict)
        # print(activeChampions)
        # print(benchedChampions)

        #Updates entire window to show changes
        pg.display.update()




while True:
    main()

pg.quit()
