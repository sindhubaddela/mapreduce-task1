## Task 1: Store Profit and Loss

### Story Background:
You are given data from a retail chain in India that sells a wide range of products, including groceries, home appliances, beauty items, apparel, and many more goods in multiple cities across the country. 
However, not all stores in the chain sell every product category. Each store has its own top-selling categories based on consumer demand.
Only these top-selling categories will determine the profit gained or the loss incurred by a store.

### Objective:
Given the input, the task is to determine:
- The number of stores that are profitable for each city.
- The number of stores operating at a loss for each city.

### Points to Consider:
- Sales data (Revenue and COGS) for a product category (top-selling or not) may or may not be recorded.
- Net results (Profit or Loss) for each store is only calculated if there exists Sales data (Revenue and COGS) for at least some top-selling category.
- If Net results > 0, it is a profitable store, otherwise, it’s incurring a loss.
