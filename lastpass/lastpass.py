import sys


def main():

    if len(sys.argv) < 2:
        print("Usage lastpass.py [input csv file]")
        sys.exit()

    csv = open(sys.argv[1], 'r')

    records = csv.readlines()

    for record in records:
        fields = record.split(',')
        print(record)
        #print(fields[0], fields[1], fields[2])

if __name__ == "__main__":
    main()
