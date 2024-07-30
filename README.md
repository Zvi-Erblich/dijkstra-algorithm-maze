# Dijkstra's Algorithm for Maze Pathfinding

This project reads an image of a maze, applies Dijkstra's algorithm to find the shortest path from a specified start point to an end point, and draws the path on the image.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Matplotlib

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/yourrepositoryname.git
    cd yourrepositoryname
    ```

2. Install the required packages:
    ```bash
    pip install opencv-python-headless numpy matplotlib
    ```

## Usage

1. Place your maze image in the project directory.
2. Edit the `file` variable in the script to point to your maze image.
3. Modify the coordinates for the start and end points in the script.
4. Run the script:
    ```bash
    python dijkstra_maze.py
    ```

### Example

```python
# file = 'maze.jpeg'
# file = 'maze5.jpeg'
file = 'maze2.png'

source = (22, 315)
end = (330, 326)
