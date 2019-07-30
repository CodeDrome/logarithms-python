import math


def main():

    """
    Run the calculateamounts and timetoamount function.
    """

    print("-----------------")
    print("| codedrome.com |")
    print("| Logarithms    |")
    print("-----------------\n")

    calculateamounts(1000, 1.1, 12)

    print("")

    timetoamount(1000, 1.1, 3138.43)


def calculateamounts(startamount, interest, years):

    """
    Calculate totals including compound interest from arguments,
    as a final total and then including intermediate yearly totals.
    """

    # Calculate and show final amount
    currentamount = startamount
    # Due to operator precedence ** is evaluated before *
    endamount = startamount * interest ** years

    print("startamount {:.2f}".format(startamount))
    print("years       {:d}".format(years))
    print("interest    {:.2f}%".format((interest - 1) * 100))
    print("endamount   {:.2f}\n".format(endamount))

    # Calculate all yearly amounts.
    for y in range(1, years + 1):

        currentamount*= interest

        print("Year {:2d}: {:.2f}".format(y, currentamount))


def timetoamount(startamount, interest, requiredamount):

    """
    Calculate and print the number of years required to reach
    requiredamount from startamount at given rate of interest.
    """

    yearstorequiredamount = math.log(requiredamount / startamount) / math.log(interest)

    print("startamount           {:.2f}".format(startamount))
    print("interest              {:.2f}%".format((interest - 1) * 100))
    print("requiredamount        {:.2f}".format(requiredamount))
    print("yearstorequiredamount {:.2f}".format(yearstorequiredamount))


main()
