import json
import sys


def allocate(amt, investors, reqs, avgs):
    """
    Allocates an amt among a pool of investors given their requested
    and historical average amounts.

    Allocates requested amount to investor if less than prorated amt.

    Recursively calculates prorated amounts for remaining pool.

    Returns: dict of allocated amts {investor: allocated_amount}

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
    assert investors == set(reqs.keys()) == set(avgs.keys())

    output = {}

    if investors == set():
        return {}

    # simple case - return requests if total requests less than allocation amount
    if sum(reqs.values()) < amt:
        for inv, req in reqs.items():
            output[inv] = req
        return output

    # prorate amounts based on historical avgs and available allocation
    prorated_amts = {investor: avg / sum(avgs.values()) * amt for investor, avg in avgs.items()}

    # identify investors with lower requests than their prorated amt
    invs_req_lt_avg = set(inv for inv in investors if reqs[inv] < prorated_amts[inv])

    # return prorated amts if no low requests
    if invs_req_lt_avg == set():
        output.update(prorated_amts)
        return output

    # update variables given updated investor pool
    for inv in invs_req_lt_avg:

        # assign to output
        output[inv] = reqs[inv]

        # remove inv, subtract amt from vars
        investors = investors - set([inv])    
        amt = amt - reqs[inv]
        reqs.pop(inv)
        avgs.pop(inv)

    # recursively update allocation as needed with new values
    remaining_vals = allocate(amt, investors, reqs, avgs)
    output.update(remaining_vals)

    return output


def read_stdin():
    """Handy one-liner for making python scripts more unix-y"""
    return '\n'.join(line for line in sys.stdin)


def parse_input(input_data):
    """
    Return tuple of formatted data for recursive allocation.
    """
    allocation_amount = input_data['allocation_amount']
    investor_amounts = input_data['investor_amounts']

    investors = set(inv['name'] for inv in investor_amounts)
    reqs = {inv['name']: inv['requested_amount'] for inv in investor_amounts}
    avgs = {inv['name']: inv['average_amount'] for inv in investor_amounts}

    return allocation_amount, investors, reqs, avgs


def main():
    """
    Read stdin, parse, allocate, dump results to stdout
    """
    input_data = json.loads(read_stdin())
    amt, investors, reqs, avgs = parse_input(input_data)
    output_data = allocate(amt, investors, reqs, avgs)
    print(json.dumps(output_data, sort_keys=True))


if __name__ == '__main__':
    main()