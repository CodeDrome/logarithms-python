import math


def main():

    print("-------------------------------")
    print("| codedrome.com               |")
    print("| Logarithms: a Practical Use |")
    print("-------------------------------\n")

    calculateamounts(1000.0, 1.1, 12)

    print()

    timetoamount(1000.0, 1.1, 3138.43)


def calculateamounts(startamount: float, interest: float, years: int) -> None:

    """
    Calculate totals including compound interest from arguments,
    as a final total and then including intermediate yearly totals.
    """

    # Calculate and show final amount
    currentamount = startamount
    # Due to operator precedence ** is evaluated before *
    endamount = startamount * interest ** years

    print(f"startamount {startamount:.2f}")
    print(f"years       {years:d}")
    print(f"interest    {(interest - 1) * 100:.2f}%")
    print(f"endamount   {endamount:.2f}\n")

    # Calculate all yearly amounts.
    for y in range(1, years + 1):

        currentamount*= interest

        print(f"Year {y:2d}: {currentamount:.2f}")


def timetoamount(startamount: float, interest: float, requiredamount: float) -> None:

    """
    Calculate and print the number of years required to reach
    requiredamount from startamount at given rate of interest.
    """

    yearstorequiredamount = math.log(requiredamount / startamount) / math.log(interest)

    print(f"startamount           {startamount:.2f}")
    print(f"interest              {(interest - 1) * 100:.2f}%")
    print(f"requiredamount        {requiredamount:.2f}")
    print(f"yearstorequiredamount {yearstorequiredamount:.2f}")


if __name__ == "__main__":

    main()