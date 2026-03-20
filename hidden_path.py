import sys
import funcs as fc
import search


def main(strategy, filename):
    
    start, grid, goal, teleports = fc.parse_input(filename)

    
    return

if __name__ == '__main__':   
    if len(sys.argv) < 3:
        # You can modify these values to test your code
        strategy = 'B'
        filename = 'example2.txt'
    else:
        strategy = sys.argv[1]
        filename = sys.argv[2]
    main(strategy, filename)
