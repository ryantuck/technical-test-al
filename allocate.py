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
    investors = set(inv['name'] for inv in investor_amounts)

    investor_requests = {
        investor['name']: investor['requested_amount']
        for investor in investor_amounts
    }

    investor_averages = {
        investor['name']: investor['average_amount']
        for investor in investor_amounts
    }

    return allocate_recursive(
        amt=allocation_amount,
        investors=investors,
        reqs=investor_requests,
        avgs=investor_averages,
    )

    # TODO handle case where requested_amt < prorated_allocation
    return {
        investor: investor_averages[investor] / total_amt_averages * allocation_amount
        for investor, requested_amt in investor_requests.items()
    }


def _weigh_allocation(amt, avgs):
    return {investor: avg / sum(avgs.values()) * amt for investor, avg in avgs.items()}

def allocate_recursive(amt, investors, reqs, avgs):

    output = {}

    while True: # TODO avoid, should deterministically resolve

        if investors == set():
            break

        inv_reqs = {inv: req for inv, req in reqs.items() if inv in investors}

        if sum(inv_reqs.values()) < amt: # not sure if this case gets hit?
            for inv, req in inv_reqs.items():
                output[inv] = req
            break

        inv_avgs = {inv: avg for inv, avg in avgs.items() if inv in investors}

        prorated_amts = _weigh_allocation(amt, inv_avgs)
        print(f'prorated_amts: {prorated_amts}', file=sys.stderr)

        use_reqs_instead = set(inv for inv in investors if reqs[inv] < prorated_amts[inv])
        print(f'use_reqs_instead: {use_reqs_instead}', file=sys.stderr)

        # if prorated amts are good to go, update output and exit
        if use_reqs_instead == set():
            for inv in investors:
                output[inv] = prorated_amts[inv]
            break

        # update output to use reqs where appropriate
        for inv in use_reqs_instead:
            output[inv] = reqs[inv]
            investors = investors - set([inv])
            amt = amt - reqs[inv]

    return output



def read_stdin():
    """Handy one-liner for making python scripts more unix-y"""
    return '\n'.join(line for line in sys.stdin)


def main():
    input_data = json.loads(read_stdin())
    output_data = allocate(**input_data)
    print(json.dumps(output_data, sort_keys=True))


if __name__ == '__main__':
    main()