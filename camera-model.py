from matplotlib import pyplot as plt
import numpy as np


def objective_one(teapot) -> None:

    '''Objective One: Place the camera at location [0, 0, 10] and perform the
    projection. Please explain why the entire object is not visible? Note that,
    only the pixels with positive coordinates are visible.'''

    # K is known as the Intrinsics Matrix
    k = np.array([[1000, 0, 0, 0], [0, 1000, 0, 0], [0, 0, 1, 0]])

    # R|t is known as the Extrinsics Matrix
    rt = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 10], [0, 0, 0, 1]])

    # M is known as the Projection Matrix
    m = k.dot(rt)

    # insert ones at index position 3
    teapot = np.insert(teapot, 3, 1, axis=1)

    # transpose teapot
    teapot = np.transpose(teapot)

    # given the matrix M, we can map from a 3D point P to a 2D point P' on the image plane
    result = m.dot(teapot)

    # transpose teapot again
    result = np.transpose(result)

    # compute: x / z
    x = np.divide(result[: , 0], result[: , 2])

    # compute: y / z
    y = np.divide(result[: , 1], result[: , 2])

    ax = plt.axes()
    plot(ax, x, y)


# Objective Two
def objective_two(teapot) -> None:

    '''Objective Two: Modify the intrinsics matrix in order to capture an
    image with the resolution 1920 x 1080 pixels. Change the camera position
    and visually inspect the differences. Note that, c = [cx, cy] is where
    the optical axis intersects the image plane. This is usually in the center
    of the image plane and digital image coordinates are measured from the
    lower-left corner, these values are often well approximated with half the
    width and height of the image.'''

    # K is known as the Intrinsics Matrix
    k = np.array([[1600, 0, 960, 0], [0, 1800, 540, 0], [0, 0, 1, 0]])

    # R|t is known as the Extrinsics Matrix
    rt = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 10], [0, 0, 0, 1]])

    # M is known as the Projection Matrix
    m = k.dot(rt)

    # insert ones at index position 3
    teapot = np.insert(teapot, 3, 1, axis=1)

    # transpose teapot
    teapot = np.transpose(teapot)

    # given the matrix M, we can map from a 3D point P to a 2D point P' on the image plane
    result = m.dot(teapot)

    # transpose teapot again
    result = np.transpose(result)

    # compute: x / z
    x = np.divide(result[: , 0], result[: , 2])

    # compute: y / z
    y = np.divide(result[: , 1], result[: , 2])

    ax = plt.axes()
    plot(ax, x, y, (0, 1920), (0, 1080))


def plot(ax, x, y, xlim=0, ylim=0, margin=0, marker=10) -> None:

    '''This function plots the 2D projection on the image plane,
    given x and y coordinates, x limit (default=0), y limit
    (default=0), margin (deault=0) and marker size (default=0).'''

    ax.margins(margin)

    # plot x and y, in red
    ax.plot(x, y, 'r.', markersize=marker)

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    plt.show()


def main():
    t = np.load('./numpy/teapot.npy')
    objective_one(t)
    objective_two(t)


if __name__ == '__main__':
    main()