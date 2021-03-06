#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alex
#
# Created:     23/10/2014
# Copyright:   (c) Alex 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
import random

# The gravitational constant G
G = 6.67428e-11

# Assumed scale: 100 pixels = 1AU.
AU = (149.6e6 * 1000)     # 149.6 million km, in meters.
SCALE = 18 / AU
ASTEROIDCOUNT = 1000

class Body():
    """Subclass of Turtle representing a gravitationally-acting body.

    Extra attributes:
    mass : mass in kg
    vx, vy: x, y velocities in m/s
    px, py: x, y positions in m
    """

    name = 'Body'
    mass = None
    vx = vy = 0.0
    px = py = 0.0

    def attraction(self, other):
        """(Body): (fx, fy)

        Returns the force exerted upon this body by the other body.
        """
        # Report an error if the other object is the same as this one.
        if self is other:
            raise ValueError("Attraction of object %r to itself requested"
                             % self.name)

        # Compute the distance of the other body.
        sx, sy = self.px, self.py
        ox, oy = other.px, other.py
        dx = (ox - sx)
        dy = (oy - sy)
        d = math.sqrt(dx**2 + dy**2)

        # Report an error if the distance is zero; otherwise we'll
        # get a ZeroDivisionError exception further down.
        if d == 0:
            raise ValueError("Collision between objects %r and %r"
                             % (self.name, other.name))

        # Compute the force of attraction
        f = G * self.mass * other.mass / (d**2)

        # Compute the direction of the force.
        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        return fx, fy


def update_info(step, bodies):
    """(int, [Body])

    Displays information about the status of the simulation.
    """
    print('Step #{}'.format(step))
    for body in bodies:
        s = '{:<8}  Pos.={:>6.2f} {:>6.2f} Vel.={:>10.3f} {:>10.3f}'.format(
            body.name, body.px/AU, body.py/AU, body.vx, body.vy)
        print(s)
    print()


def equilikely(a, b):
    return (int)(a + ((b - a + 1) * random.random()))


def loop(bodies):
    """([Body])

    Never returns; loops through the simulation, updating the
    positions of all the provided bodies.
    """
    timestep = 24 * 3600  # One day

    step = 1
    while True:
        update_info(step, bodies)
        step += 1

        force = {}
        for body in bodies:
            # Add up all of the forces exerted on 'body'.
            total_fx = total_fy = 0.0
            for other in bodies:
                # Don't calculate the body's attraction to itself
                if body is other:
                    continue
                fx, fy = body.attraction(other)
                total_fx += fx
                total_fy += fy

            # Record the total force exerted.
            force[body] = (total_fx, total_fy)

        # Update velocities based upon on the force.
        for body in bodies:
            fx, fy = force[body]
            body.vx += fx / body.mass * timestep
            body.vy += fy / body.mass * timestep

            # Update positions
            body.px += body.vx * timestep
            body.py += body.vy * timestep
            #body.goto(body.px*SCALE, body.py*SCALE)


def main():
    sun = Body()
    sun.name = 'Sun'
    sun.mass = 1.98892 * 10**30

    mercury = Body()
    mercury.name = 'Mercury'
    mercury.mass = 3.285 * 10**23
    mercury.px = 0.39 * AU
    mercury.vy = -47.36 * 1000   #update

    venus = Body()
    venus.name = 'Venus'
    venus.mass = 4.8685 * 10**24
    venus.px = 0.723 * AU
    venus.vy = 35.02 * 1000

    earth = Body()
    earth.name = 'Earth'
    earth.mass = 5.9742 * 10**24
    earth.px = -1*AU
    earth.vy = 29.783 * 1000            # 29.783 km/sec

    mars = Body()
    mars.name = 'Mars'
    mars.mass = 6.39 * 10**23
    mars.px = 1.52 * AU
    mars.vy = -24.07 * 1000

    jupiter = Body()
    jupiter.name = 'Jupiter'
    jupiter.mass = 1.898 * 10**27
    jupiter.px = 5.2 * AU
    jupiter.vy = -13.07  * 1000

    saturn = Body()
    saturn.name = 'Saturn'
    saturn.mass = 5.683 * 10**26
    saturn.px = 10.1 * AU
    saturn.vy = -9.68  * 1000

    uranus = Body()
    uranus.name = 'Uranus'
    uranus.mass = 8.681 * 10**25
    uranus.px = 19.2 * AU
    uranus.vy = 6.8  * 1000

    neptune = Body()
    neptune.name = 'Neptune'
    neptune.mass = 1.024 * 10**26
    neptune.px = 30.1 * AU
    neptune.vy = -5.43  * 1000

    objectList = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    i = 0
    for obj in range(0, ASTEROIDCOUNT):
        obj = Body()
        obj.mass = random.uniform(.001, 500.0) * 10**15
        obj.name = 'asteroid' + str(i)
        obj.px = random.uniform(2.0, 4.6) * AU
        obj.vy = random.uniform(-20.0, -15.0) * 1000

        i += 1

        objectList.append(obj)

    loop(objectList)

if __name__ == '__main__':
    main()
