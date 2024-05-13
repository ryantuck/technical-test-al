import json
import sys


def allocate(allocation_amount, investor_amounts):
    """
    EXAMPLE
    Available allocation: $100
    Investor A requested to invest $150
    Investor B requested to invest $50

    Investor A has a historical average investment size of $100
    Investor B has a historical average investment size of $25

    After proration:
    Investor A will invest $100 * (100 / (100 + 25)) = $80
    Investor B will invest $100 * (25 / (100 + 25)) = $20
    """
    investor_requests = {
        investor['name']: investor['requested_amount']
        for investor in investor_amounts
    }

    total_amts_requested = sum(investor_requests.values())

    if total_amts_requested <= allocation_amount:
        return investor_requests

    investor_averages = {
        investor['name']: investor['average_amount']
        for investor in investor_amounts
    }

    total_amt_averages = sum(investor_averages.values())

    # TODO handle case where requested_amt < prorated_allocation
    return {
        investor: investor_averages[investor] / total_amt_averages * allocation_amount
        for investor, requested_amt in investor_requests.items()
    }


def read_stdin():
    """Handy one-liner for making python scripts more unix-y"""
    return '\n'.join(line for line in sys.stdin)


def main():
    input_data = json.loads(read_stdin())
    output_data = allocate(**input_data)
    print(json.dumps(output_data))


if __name__ == '__main__':
    main()