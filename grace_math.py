# Math to determine the amount length of all the lines within a grace
import math as m

# all math done in relation to the radius of the big circle

# Big circle
def calculate_big_circle_contribution(radius):
    return 2.0 * m.pi * radius


def calculate_side_of_a_square_inside_a_circle(radius):
    '''
        Uses pythagorean theorum to determine the side of the square.

        radius of big circle is the distance from a square corner to the center
        thus we can use the pythagorean theorum to calculate the square's side
    '''
    return m.sqrt(m.pow(radius, 2.0) + m.pow(radius, 2.0))


def calculate_square_contribution(radius):
    return 4.0 * calculate_side_of_a_square_inside_a_circle(radius)


def calculate_little_circle_radius(radius):
    '''half the length of a square's side is the little circle's radius'''
    square_side = calculate_side_of_a_square_inside_a_circle(radius)
    return square_side / 2.0


def calculate_little_circle_contribution(radius):
    return 2.0 * m.pi * calculate_little_circle_radius(radius)


def calculate_length_of_one_side_of_the_star(radius):
    '''
        Use pythagorean theorum again.

        angles of the star's point are 45 degrees, and are split in half
        by a radius line heading straight to the center of the circle.
        A line perpendicular to one of the stars lines going to the center of the circle
        is used to make a right triangle so the pythagorean theorum can be used.
        also, soh cah toa. sin(angle) = opposite side / hypotenous to get that perpendicular lines length.
    '''
    r = calculate_little_circle_radius(radius)
    y = r * m.sin(m.radians(22.5))
    return 2 * m.sqrt(m.pow(r, 2) - m.pow(y, 2))


def calculate_star_beam_bit_between_the_two_circles(radius):
    '''
        Use difference of the two radius' to get the bits outside the little circle and inside the big circle

        This affects all the star points since they all terminate at the boundary of the little circle.
    '''
    return (radius - calculate_little_circle_radius(radius)) * 8


def calculate_star_contribution(radius):
    length = 8 * calculate_length_of_one_side_of_the_star(radius)
    length += calculate_star_beam_bit_between_the_two_circles(radius)
    return length


def calculate_total_line_length(big_circle_radius, ray_length_outside_circle):
    length = calculate_big_circle_contribution(big_circle_radius)
    length += calculate_square_contribution(big_circle_radius)
    length += calculate_little_circle_contribution(big_circle_radius)
    length += calculate_star_contribution(big_circle_radius)
    length += ray_length_outside_circle * 8
    return length

if __name__ == "__main__":
    import sys
    R = float(sys.argv[1])
    L = float(sys.argv[2])
    print(calculate_total_line_length(R, L))

