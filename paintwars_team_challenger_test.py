# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: _________
#  Prénom Nom: _________

def get_team_name():
    return "[ team with no name ]" # à compléter (comme vous voulez)

def step(robotId, sensors):

    translation = 1 # vitesse de translation (entre -1 et +1)
    rotation = 0 # vitesse de rotation (entre -1 et +1)

    #if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
    #    rotation = 0.5  # rotation vers la droite
    #elif sensors["sensor_front_right"]["distance"] < 1:
    #    rotation = -0.5  # rotation vers la gauche

################### pour les alliés #############################

    if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == True :
         # exemple de détection d'un robot de l'équipe adversaire (ne sert à rien)
        translation = -1
        rotation = 0
        
    elif sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == True :
        translation = 1
        rotation = 1

    elif sensors["sensor_front_right"]["isSameTeam"] == True :
        translation = 1
        rotation = -1


################### pour les énemies #############################
    elif sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
        enemy_detected_by_front_sensor = True # exemple de détection d'un robot de l'équipe adversaire (ne sert à rien)
        translation = 1
        rotation = 0
        
    elif sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
        enemy_detected_by_front_sensor = True 
        translation = 1
        rotation = -1

    elif sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
        enemy_detected_by_front_sensor = True 
        translation = 1
        rotation = 1



################### pour les murs #############################

    elif sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
        translation = 1
        rotation = 0.5  # rotation vers la droite

    elif sensors["sensor_front_right"]["distance"] < 1:
        translation = 1
        rotation = -0.5  # rotation vers la gauche


    else:
        translation = 1
        rotation    = 0
    #éviter les murs hateWalls
    


    return translation, rotation
