# Part 3 - writing

### Discovering a bug

> Suppose we discover a bug with our algorithm and investors for two deals had incorrect
> allocations. This means that some of the investors ended up investing more than they were allowed to
> while others invested less than they were allowed to. One of deals happened two years ago and the 
> other one happened two weeks ago. Please describe, in detail, how would you go about correcting this 
> issue and how would you communicate this to the affected customers.


First, address the technical issue. Identify and reproduce the bug. Reprocess all past deals to confirm overall affected scope and to verify for customers that we've confirmed the rest of their transactions weren't negatively affected. Take screenshots, log in Slack or Jira to an appropriate level of detail for a searchable technical artifact.

Next, determine the party line. Review internally with client services, account reps, and finance as needed to understand options. The previously-created technical artifacts should include a hand-off ready tl;dr of the issue and a spreadsheet containing fine-grain details of affected clients that might be asked for. Bucket the customers into two groups - lucky and unlucky - and communicate accordingly. If the losses seem really bad for any clients, probably worth it to loop in legal to review the Ts and Cs while we're at it!

If it worked out in the customer's favor, acknowledge the bug and that it's been fixed and that we've verified all the client's past transactions are valid, and point out its fortunate impact in this case.

If it didn't work out and the customer lost more than they were expecting, offer some calculated compensation based on what we are able to offer, whether that's straight cash, some prioritized spot in line for future investments, or whatever else the finance and client services teams have already thought up and blessed. 




### Squeezed down

> An angry investor sent us a note about how they keep getting squeezed down to $25K per deal even
> though their requested amount is $100K. Underneath the hood, this was because there's limited
> allocation (low supply) and a high volume of investors looking to invest (high demand). How should 
> we communicate this to an investor in a way that minimizes the damage to our relationship with 
> the investor? 
> In addition, can you think of a better way we could change the proration basis logic so that 
> this could potentially happen less often?   


Hi Investor X,

I'm Ryan Tuck, senior engineering lead responsible for maintaining the allocation engine.

I was hoping to offer a more thorough explanation in addition to the high-level "What is Allocation?" doc that ACCOUNT_REP had shared with you already.

The particular deals you've referenced - DEAL_1, DEAL_2, DEAL_3 - all attracted a lot of interest by other investors on AngelList, which often leads to adjustments. We've seen an increased demand across the board for Post-Apocalyptic EV deals ever since Elon announced the Cybertruck, all of those deals were in that space, and all of them had about 4-6x the total investor volume than the average that day. On the deals you referenced, 85% of investors, and everyone requesting above $40k, was squeezed down substantially. In your case, your existing average investment amount of $X did help your prorated rate, but it can only help so much.

AngelList is a platform for investing in deals across dozens of different industries. To improve your chances of seeing a full requested investment amount, there may be some less-buzzworthy but still-lucrative startups in boring industries that are ripe for disruption - see our "Seven Indonesian Startups Quietly Revolutionizing Fax Machines" post from earlier this month for a sample. 

I'm happy to help ACCOUNT_REP provide any more further level of technical detail about how AngelList's allocation logic operates, please reach out with followup questions. I'm sorry for your frustration to date and hope you're now armed with the information you need to make AngelList work even better for you.

We're always soliciting feedback from our customers on how to improve transparency and fairness in our allocation engine. One idea we've kicked around internally is to establish some prioritization system to give preference to high-volume investors who have gotten squeezed down on recent deals, but are still working through how to handle the unintended consequences of that complexity and how we'd roll it out thoughtfully. We'll certainly reach out directly if and when updates are made on this front.

Have a great summer!

Ryan Tuck, AngelList employee