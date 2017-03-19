import sys


def main():

    regs = {}

    try:
        file_payments = open(sys.argv[1], 'r')
    except IOError:
        print("Sorry, could not open %s for read" % sys.argv[1])
        sys.exit()

    try:
        file_youth = open(sys.argv[2], 'r')
    except IOError:
        print("Sorry, could not open %s for read" % sys.argv[2])
        sys.exit()

    try:
        file_out = open(sys.argv[3], 'w')
    except IOError:
        print("Sorry, could not open %s for write" % sys.argv[3])
        sys.exit()

    payments = file_payments.readlines()

    for payment in payments:
        # print(payment.split())
        row = payment.split()
        # print(row[0], row[1], row[2])
        regs[row[0]] = row[1]

    youth = file_youth.readlines()

    for youth_record in youth:
        reg = youth_record.split()[0]
        print("%s\t%s" % (youth_record[:-1], regs[reg]))
        file_out.write(youth_record[:-1] + "\t" + regs[reg] + "\n")

    file_payments.close()
    file_youth.close()
    file_out.close()

if __name__ == "__main__":
    main()
