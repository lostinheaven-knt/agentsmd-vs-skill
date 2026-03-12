# Advanced VIP settings

The VIP program settings allow you to configure the fundamental rules of your customer loyalty tiers. When modified, these settings will trigger a recalculation of customer tier assignments to ensure accurate membership status.

:::tip

Ensure the VIP program is inactive before adding a new tier. Any modifications to VIP tiers will trigger an automatic recalculation of all customer tier assignments.

:::

## Program start date

Initially, the system sets the program's start date to the day the VIP program is activated. You can adjust this date forward or backward without any restrictions.

:::tip

All customer VIP tiers are recalculated from the newly set start date.

:::

## **Tier calculation rules**

Select from the following methods to calculate customer VIP tiers:

- **Points earned** (default): Points accumulated since the program's start date, covering earned points and manually adjusted points (like admin adjustments or imported points), but excluding canceled points.
- **Amount spent**: Accounts for the total amount spent post-program activation. Includes taxes, shipping, and discounts, excluding returns.
- **Number of orders placed**: Counts the number of completed orders since the start date, excluding returns.

## Reward rule for skipped tiers

Choose how to issue rewards when customers level up by skipping tiers:

- **Only issue highest-tier reward**: Customers receive only the reward for the highest tier they reach, skipping rewards for intermediate tiers. For example, jumping from Tier 1 to Tier 4, they receive only the Tier 4 reward.
- **Issue all skipped-tier rewards**:  Customers get rewards for every tier they skip. For instance, moving from Tier 1 to Tier 4, they collect rewards for Tier 2, 3, and 4.

## Allow repeat tier rewards

If customers reach the same VIP tier again, they should not repeatedly receive the initial reward. It's recommended to disable the reissuance of initial reward for repeated achievements of the same tier.

::: faq

## FAQs

### Q1. Do customers receive rewards for all skipped tiers?
> A: The rewards issued depend on the selected reward issuance method. Choosing **Issue all skipped-tier rewards** results in rewards for each skipped tier; **Only issue highest-tier reward** provides just the reward for the current tier.

### Q2. Can a customer receive the same tier of rewards more than once?
> A: By default, reissuance of the same tier rewards is not permitted. If a customer has previously received a reward at a certain tier, they will not receive the same reward again if they reach that tier in the future.

:::