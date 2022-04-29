from matplotlib import pyplot as plt
import numpy as np

def main() -> None:

    '''A point cloud model of a teapot is attached in a numpy (.npy) format.
    You can use the following code snippet to visualize the model.'''

    teapot = np.load('./numpy/teapot.npy')
    ax = plt.axes(projection='3d')

    ax.plot3D(teapot[:, 0], teapot[:, 1], teapot[:, 2], 'r.')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

if __name__ == "__main__":
    main()