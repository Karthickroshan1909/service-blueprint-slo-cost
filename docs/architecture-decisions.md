# Architecture Decision Records (ADRs)

## ADR 1: Cloud Hosting Region

**Decision:** Host the application in the Azure region where the App Service is already deployed, provided the region meets availability and cost requirements.

**Reason:** Keeping the application in its existing region avoids unnecessary migration and simplifies deployment.

**Trade-off:** Regional outages may affect the application. A secondary region would improve resilience but increase complexity and cost.

**Status:** Existing deployment region must be verified in the Azure Portal.

## ADR 2: Database Selection

**Decision:** SQLite is used for the current prototype. Azure SQL Database is a potential future choice for a production deployment.

**Reason:** SQLite is simple to configure and suitable for a small learning project. Azure SQL provides managed database capabilities for a more production-oriented design.

**Trade-off:** SQLite files stored in an App Service application directory may not provide reliable persistence across deployments or scaling. Production use requires a suitable persistent database and tested backups.

**Status:** Prototype implemented; production database migration is not completed.

## ADR 3: Recovery Objectives

**Decision:** Use provisional recovery objectives until business requirements are confirmed.

- **RTO (Recovery Time Objective):** Target recovery within 4 hours.
- **RPO (Recovery Point Objective):** Target a maximum of 24 hours of data loss.

**Reason:** These initial targets provide a starting point for planning recovery.

**Trade-off:** The targets are not guaranteed until backup, recovery, and monitoring procedures are configured and tested.

**Status:** Proposed; not yet validated.

## ADR 4: Secrets Management

**Decision:** Do not store passwords, API keys, or other secrets in source code or GitHub repositories.

**Reason:** Secrets in source control can expose the application to unauthorized access.

**Implementation:** Use Azure App Service application settings for non-secret configuration. Use Azure Key Vault for sensitive values when required, with managed identity where supported.

**Status:** Security approach documented; configuration must be verified.

## ADR 5: Least-Privilege Access

**Decision:** Give users, deployment workflows, and application components only the permissions they need.

**Reason:** Limiting permissions reduces the impact of accidental changes or compromised credentials.

**Implementation:** Review Azure role assignments, use a dedicated deployment identity where practical, and avoid unnecessary Owner permissions for routine deployment.

**Status:** Proposed; role assignments must be reviewed.

## ADR 6: Service-Level Objectives

**Decision:** Use a provisional monthly availability SLO of 99.5%, alongside latency and error-rate targets defined in `slo-policy.md`.

**Reason:** Measurable objectives help assess service reliability and guide alerts.

**Trade-off:** An SLO is a target, not proof of actual availability. Monitoring and alerting must be configured before compliance can be measured.

**Status:** Proposed; actual service performance has not yet been measured.

## Review

These decisions are initial recommendations for an internship prototype. Review them when the application's real traffic, recovery requirements, budget, and security needs are known.