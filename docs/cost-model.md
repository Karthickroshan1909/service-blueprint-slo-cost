## Baseline Cost Estimate

### Current Hosting Configuration

The application is deployed using Azure App Service on the Free F1 plan.

| Component | Current choice | Estimated monthly cost |
|---|---|---:|
| Web hosting | Azure App Service F1 | ₹0 |
| Database | SQLite in the application | ₹0 additional service charge |
| Custom domain | Not included | ₹0 |
| Azure SQL Database | Not provisioned | ₹0 |
| Azure Monitor / Log Analytics | No paid configuration confirmed | Not estimated |
| Backup service | Not configured | Not estimated |

**Estimated baseline: ₹0/month for the listed current components**, assuming the app remains on F1 and no separately chargeable services are added. This is not a complete Azure invoice estimate.

### Important F1 Limitations

The F1 tier is intended for development, learning, and experimentation. It provides shared compute, a daily CPU quota, and no App Service SLA. It is not recommended for production workloads.

SQLite does not have a separate Azure database charge in this prototype, but its persistence and recovery on App Service have not been validated. A production design should use a suitable persistent database and configure backups.

### Traffic Scenarios

| Scenario | Requests per day | Hosting assumption | Cost approach |
|---|---:|---|---|
| Low | 1,000 | F1 for demonstration, if within its limits | ₹0 for F1 hosting |
| Medium | 10,000 | Reassess CPU quota, latency, and storage | Recalculate if upgrading |
| High | 100,000 | F1 should not be assumed sufficient | Estimate a suitable paid plan and database |

These traffic levels are planning scenarios, not measured load-test results. Request count alone does not determine the required plan; execution time, concurrency, and resource usage also matter.

### Cost Optimization

- Start with F1 while developing and demonstrating the prototype.
- Check Azure Cost Management for actual charges.
- Avoid provisioning paid databases, monitoring workspaces, or other services unless required.
- Before production use, estimate the required hosting and database tiers using the Azure Pricing Calculator.
- Revisit this estimate whenever the architecture or traffic assumptions change.

### Estimate Status

The F1 hosting baseline is identified. Paid-tier estimates remain pending because a production hosting plan, database, region-specific prices, and measured workload have not been selected.
