from vv_trigo import Vector2d


class Boid:

    pos = Vector2d(0, 0)

    def __init__(self, x, y, size, mass):
        # vectors
        self.pos = Vector2d(x, y)
        self.previous_pos = Vector2d(x, y)
        self.vel = Vector2d(0, 0)
        self.acc = Vector2d(0, 0)

        # floats
        self.max_speed = 10
        self.max_steer = 0.8
        self.size = size
        self.mass = mass

    def wrap_edges(self, width, height):
        if self.pos.x > width:
            self.pos.x = 0
        elif self.pos.x < 0:
            self.pos.x = width
        if self.pos.y > height:
            self.pos.y = 0
        elif self.pos.y < 0:
            self.pos.y = height

    # PHYSICS
    def update(self):
        # store previous position
        self.previous_pos.x = self.pos.x
        self.previous_pos.y = self.pos.y
        # vel gets incremented by acceleration
        self.vel.add(self.acc)
        # print(self.vel)
        # limit vel
        if self.vel.get_mag() > self.max_speed:
            self.vel.normalize()
            self.vel.mult(self.max_speed)
        # position gets incremented by velocity
        self.pos.add(self.vel)
        # reset acceleration
        self.acc.mult(0)

    # used to apply forces to boids
    def apply_force(self, force):
        # print("------------------------")
        #print("apply_force(), force class: " + force.__class__.__name__)
        # since f = ma, a = f/m, in this case we're multiplying for the inverse
        tmp_force = Vector2d(force.x, force.y)
        tmp_force.mult(1 / self.mass)
        #tmp_force = force / self.mass
        self.acc.add(force)

    # steering behaviours
    def arrive(self, target):
        # print("------------------------")
        #print("arrive(), target class: " + target.__class__.__name__)
        #print("arrive(), self.pos class: " + self.pos.__class__.__name__)
        #print("self pos: {0}, {1}".format(self.pos.x, self.pos.y))

        desired = Vector2d.subtract(vec1=target, vec2=self.pos)

        #print("desired class: " + desired.__class__.__name__)
        # print(desired)
        distance = desired.get_mag()
        # smooth arrive at the target
        # If the boid is within a certain distance form the target,
        # set the magnitude based on the distance from the target
        # If distance = 100 then mag is maxSpeed
        # If distance = 50 then mag is maxSpeed * 0.5
        # If distance = 25 then mag is maxSpeed * 0.25
        desired.normalize()
        desired.mult(self.max_speed)
        if distance < 100:
            m = map(distance, 0, 100, 0, self.max_speed)
            desired.normalize()
            desired.mult(m)
        else:
            desired.normalize()
            desired.mult(self.max_speed)

        # using Reynolds formula
        steering_force = Vector2d.subtract(vec1=desired, vec2=self.vel)
        if steering_force.get_mag() > self.max_steer:
            steering_force.normalize()
            steering_force.mult(self.max_steer)
        self.apply_force(steering_force)

    # graphics

    def render(self):
        ellipse(self.pos.x, self.pos.y, self.size, self.size)
