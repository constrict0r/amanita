import sys
import logging


def main(args=None):

    logging.basicConfig(filename='amanita.log', level=logging.DEBUG)
    logging.debug(sys.argv)

    # if args is None:
    #     if len(sys.argv) > 1:
    #         args = sys.argv[1]

    print("This is the main routine.")


if __name__ == "__main__":
    sys.exit(main())
