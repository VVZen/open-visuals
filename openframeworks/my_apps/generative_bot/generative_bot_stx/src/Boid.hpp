//
//  Boid.hpp
//  generative_bot_soh
//
//  Created by Valerio Viperino on 03/09/16.
//
//

#ifndef Boid_hpp
#define Boid_hpp

#include <stdio.h>
#include "ofMain.h" // reference to the of library

class Boid {
    public:
    
        // Constructor
        Boid();
        // Setup with pos and size
        void setup(ofVec2f pos, ofVec2f size);
        void update(bool checkEdges);
        void render(ofColor color, ofFbo * fbo);
    
        ofVec2f getPosition();
        ofVec2f getVelocity();
        ofVec2f getAcceleration();
    
        void addForce(ofVec2f force);
        void seek(ofVec2f target);
        void follow(ofVec2f target);
        void fear(ofVec2f target, float fearDistance);
    
        // Group behaviours
        ofVec2f computeAlignment(vector<Boid *> boids);
        ofVec2f computeSeparation(vector<Boid *> boids, float distanceThreshold);
        ofVec2f computeCohesion(vector<Boid *> boids);
        void flock(vector<Boid *> boids, float alignMultiplier, float sepMultiplier, float sepDistance);
    
        static float MAX_FORCE;
        static float MAX_STEER;
        static float MAX_SPEED;
    
    private:
    
        ofVec2f previousPosition;
        ofVec2f position, velocity, acceleration;
        ofVec2f size;
};

#endif /* Boid_hpp */
