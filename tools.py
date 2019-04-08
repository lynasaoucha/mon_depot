# coding: utf-8
from soccersimulator import Vector2D, MobileMixin , SoccerAction
from soccersimulator.settings import *

class SuperState():
    def __init__(self,state,id_team,id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
        
    def __getattr__ (self , attr):
        return getattr (self.state , attr)
   
    #positon de la balle     
    @property
    def ball(self):
        return self.state.ball.position

	#position du joueur
    @property
    def player(self):
        return self.state.player_state(self.id_team,self.id_player).position
 
	#position du goal
    @property
    def goal(self):
        if (self.id_team==1):
            return Vector2D(GAME_WIDTH,GAME_HEIGHT /2)
        else :
            return Vector2D(0, GAME_HEIGHT/2)

    
    #aller à un point donné
    def go_to_position(self, x, y):
        pos = Vector2D(x,y)
        return SoccerAction(pos-self.player)
   
        
    #aller vers la balle
    @property
    def go (self):
        return SoccerAction((self.ball-self.player)*maxPlayerAcceleration)   
    
    #retourne vrai si le joueur peut shoot, faux sinon
    @property
    def can_shoot(self):
        return self.ball.distance(self.player) < PLAYER_RADIUS+BALL_RADIUS
    
    #shooter dans la baller
    @property
    def shoot(self):
        return SoccerAction(shoot=((self.goal-self.player)/20)*maxPlayerShoot)


	#shooter dans la balle ou aller vers la balle
    @property    
    def shoot_or_go(self):
        if (self.can_shoot):
            return self.shoot
        else:
            return self.go
    
    #shooter dans la baller
    @property
    def petit_shoot(self):
        return SoccerAction(shoot=0.2*((self.goal-self.player)/20))
    
      #shooter dans la balle ou aller vers la balle
    @property    
    def petit_shoot_or_go(self):
        if (self.can_shoot):
            return self.petit_shoot
        else:
            return self.go 
    
