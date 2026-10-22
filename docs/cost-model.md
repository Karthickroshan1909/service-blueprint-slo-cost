
# Cloud Cost Envelope — Task Tracker

## 1. Purpose

This document estimates the monthly cloud cost of running
the Task Tracker application on Microsoft Azure.

The model considers three traffic levels:
Low, Medium, and High.

The estimates are planning scenarios, not live Azure quotes.
Actual prices depend on the region, selected service tiers,
usage, discounts, and current Azure pricing.

## 2. Application Architecture

- Application hosting: Azure App Service on Linux.
- Application runtime: Python Flask.
- Database: A persistent managed database must be selected.
- Monitoring: Azure Monitor and Application Insights.
- Backup: Database backup and recovery capability.
- Network: HTTPS requests and outbound data transfer.
- Support: Azure support plan, if required.

## 3. Traffic Scenarios

### Low Traffic

Assumptions:
- 1,000 application requests per day.
- Approximately 30,000 requests per month.
- Small number of users.
- Minimal data storage and outbound transfer.

### Medium Traffic

Assumptions:
- 10,000 application requests per day.
- Approximately 300,000 requests per month.
- Regular daily usage.
- Moderate database activity and logging.

### High Traffic

Assumptions:
- 100,000 application requests per day.
- Approximately 3,000,000 requests per month.
- Larger number of concurrent users.
- Higher compute, database, monitoring, and network requirements.

These are hypothetical workload levels, not measured traffic.

## 4. Monthly Cost Categories

| Cost Category | Low Traffic | Medium Traffic | High Traffic |
|---|---|---|---|
| Compute / App Service | Verify Azure price | Verify Azure price | Verify Azure price |
| Managed database | Verify selected tier | Verify selected tier | Verify selected tier |
| Storage | Estimate from usage | Estimate from usage | Estimate from usage |
| Network transfer | Estimate outbound GB | Estimate outbound GB | Estimate outbound GB |
| Logging and monitoring | Estimate ingestion GB | Estimate ingestion GB | Estimate ingestion GB |
| Backup | Estimate database size and retention | Estimate database size and retention | Estimate database size and retention |
| Support | Confirm support plan | Confirm support plan | Confirm support plan |
| Monthly total | Calculate after pricing | Calculate after pricing | Calculate after pricing |

## 5. Cost Calculation Method

For each scenario:

Monthly total =
Compute + Database + Storage + Network transfer
+ Logging and monitoring + Backup + Support

For usage-based services:

Estimated cost =
Monthly usage quantity × Unit price

Examples:
- Compute cost = Selected plan monthly price.
- Storage cost = Stored GB × storage price per GB.
- Network cost = Billable outbound GB × applicable transfer price.
- Logging cost = Billable ingestion GB × applicable ingestion price.
- Backup cost = Billable backup storage × applicable backup price.

Free allowances and included service features must be
deducted where applicable.

## 6. Important Cost Considerations

- A Free App Service plan may have limitations and is
  intended for learning and testing, not production guarantees.
- A managed database may become a major part of the monthly cost.
- Monitoring ingestion can grow with application traffic.
- Backup costs depend on database size, retention, and service tier.
- Network transfer pricing depends on the destination and region.
- A paid Azure support plan should not be assumed unless selected.
- Azure for Students credits may offset eligible charges,
  but credits do not mean the underlying services have no cost.

## 7. Cost Optimization

- Start with the smallest service tier that meets requirements.
- Avoid unnecessary always-on resources.
- Set budgets and cost alerts.
- Review monitoring retention and ingestion volume.
- Use suitable storage tiers.
- Scale up only when measurements justify it.
- Delete unused test resources.
- Review student-credit eligibility and remaining balance.

## 8. Limitations

The numerical monthly totals are intentionally pending
until the exact Azure region, hosting tier, database product,
storage volume, outbound transfer, logging ingestion,
backup requirements, and support plan are confirmed.

No unverified pricing values should be presented as
actual Azure quotes.

## 9. Next Steps

1. Confirm the current App Service plan and region.
2. Select a persistent database service.
3. Define storage, transfer, logging, and backup assumptions.
4. Obtain current prices using the Azure Pricing Calculator.
5. Calculate the monthly total for each traffic scenario.
6. Review the cost envelope against the project budget.

