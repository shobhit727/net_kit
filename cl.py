import matplotlib

matplotlib.use("AGG")
import numpy as np
import matplotlib.pyplot as plt
import os


def apply_rules(s):
    """Hilbert Curve as a Lindenmayer system (L-system)
    https://en.wikipedia.org/wiki/Hilbert_curve#Representation_as_Lindenmayer_system"""
    s = s.replace(
        "a", "-Bf+AfA+fB-"
    )  # capital letters "A" and "B" so that the second operation
    s = s.replace("b", "+Af-BfB-fA+")  # doesn't apply to the changes already made
    return s.lower()  # make everyone lowercase


axiom = "a"
n = 2  # number of iterations
# displacements, ordered in a counter-clockwise direction
dxdy = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]])  # right  # up  # left  # down
# displacement is of size 1, so the higher n is, the greater the domain
length = 2**n - 1
margin = 0.05 * length
domain = [
    0 - margin,
    length + margin,
    0 - margin,
    length + margin,
]  # a 5% margin around the curve
s = axiom  # string to iterate upon

for i in np.arange(n):
    s = apply_rules(s)
make_movie = True
plt.ion()  # interactive mode disabled if "matplotlib.use('AGG')"
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
ax.axis("off")  # no frame
ax.axis(domain)  # domain size
ax.set_aspect("equal")  # square look
ax.set_xticks([])
ax.set_yticks([])  # no ticks
ax.set_title(r"$n = {:d}$".format(n))
plt.show()

# "a" and "b" can be erased now
s = s.replace("a", "")
s = s.replace("b", "")

frame_names = []  # these two are only relevant if make_movie==True
frame_counter = 0

p = np.array([[0.0, 0.0]])  # this is the starting point (0,0)
(p_plot,) = plt.plot(p[:, 0], p[:, 1], color="black")

# iterate on the string s
for i, c in enumerate(s):
    # uncomment to see how fast things are going
    # print("{:d}/{:d}".format(i,len(s)))

    # rotations "+" and "-" change the displacement array dxdy
    # "+" means clockwise rotation
    if c == "+":
        dxdy = np.roll(dxdy, +1, axis=0)
    # "-" means counter-clockwise rotation
    if c == "-":
        dxdy = np.roll(dxdy, -1, axis=0)
    # forward "f"
    if c == "f":
        # add one more point to array p
        p = np.vstack([p, [p[-1, 0] + dxdy[0, 0], p[-1, 1] + dxdy[0, 1]]])
        # update p_plot data, this is MUCH faster that plotting
        # several line segments separately
        p_plot.set_data(p[:, 0], p[:, 1])
        fig.canvas.draw()
        if make_movie:
            fname = "_tmp{:05d}.png".format(frame_counter)
            frame_names.append(fname)
            fig.savefig(fname, bbox_inches="tight", resolution=300)
        frame_counter += 1
if make_movie:
    frames = "_tmp%5d.png"
    # movie_command = "mencoder mf://*.png -mf fps=24:type=png --ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -oac copy -o hil{:d}.avi".format(n)

    # we might have other .png figures in the directory
    # in this case, use the code below
    f = open("png_list.txt", "w")
    for i in frame_names:
        f.write(i + "\n")
    f.close()
    movie_command = "mencoder mf://@png_list.txt -mf fps=24:type=png -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -oac copy -o hil{:d}.avi".format(
        n
    )

    err = os.system(movie_command)
    if err != 0:
        raise RuntimeError("Couldn't run mencoder.  Data in tmp*.png files")
    for fname in frame_names:
        os.remove(fname)

    # we now have one video ready.
    # if you want to join several videos, use this:
    # sudo apt-get install gpac
    # MP4Box -cat part1.avi -cat part2.avi -new joinedfile.avi
