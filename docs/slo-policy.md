
# SLO Policy — Task Tracker

## 1. Purpose

This document defines the reliability targets, measurements,
error budget, and alert thresholds for the Task Tracker application.

The application uses Python Flask hosted on Azure App Service
and a database for storing tasks.

These are proposed targets for the project. They must be
validated using monitoring data after deployment.

## 2. Service Level Indicators (SLIs)

SLIs are measurements used to understand the performance
and reliability of the application.

### SLI 1: Availability

Measurement:
Percentage of valid application requests that complete
successfully without a server-side error.

Formula:

Availability (%) =
Successful requests / Total valid requests × 100

Example:
If 995 out of 1,000 requests succeed, availability is 99.5%.

### SLI 2: Response Latency

Measurement:
The time taken by the application to respond to a request.

Metric:
95th percentile response time (p95).

Example:
If p95 is 500 milliseconds, 95% of measured requests
complete within 500 milliseconds.

### SLI 3: Application Errors

Measurement:
The percentage of requests that return server-side errors,
such as HTTP 5xx responses.

Formula:

Error rate (%) =
HTTP 5xx responses / Total valid requests × 100

### SLI 4: Database Connectivity

Measurement:
Whether the application can successfully read and write
task data in the database.

Evidence may include successful database operations,
connection failures, and application logs.

## 3. Service Level Objectives (SLOs)

An SLO is the target reliability or performance level
that the service aims to achieve.

### Availability Target

Target:
99.5% monthly availability.

Measurement window:
A rolling 30-day period.

### Latency Target

Target:
95% of application requests should complete within
500 milliseconds under normal expected traffic.

Measurement window:
A rolling 30-day period.

### Application Error Target

Target:
Fewer than 1% of valid requests should return HTTP 5xx
server-side errors over a rolling 30-day period.

### Database Target

Target:
Database-dependent operations should succeed in at
least 99.5% of attempts over a rolling 30-day period.

This target depends on selecting and monitoring a
suitable persistent database.

## 4. Error Budget

The error budget is the amount of unreliability allowed
by the availability SLO.

Availability SLO = 99.5%

Error budget = 100% - 99.5% = 0.5%

For a 30-day month:

Total time = 30 × 24 = 720 hours

Allowed unavailable time =
720 × 0.005 = 3.6 hours

Therefore, the approximate monthly error budget is
3 hours and 36 minutes.

The time-based calculation is an illustration.
The actual request-based error budget should be calculated
from the measured availability SLI.

## 5. Alert Thresholds

### Critical Alert: Application Unavailable

Trigger:
Three consecutive failed health checks.

Action:
Investigate App Service health, application startup,
deployment status, and logs.

### Critical Alert: High Error Rate

Trigger:
HTTP 5xx error rate exceeds 5% for 5 consecutive minutes,
with enough requests to make the measurement meaningful.

Action:
Check application exceptions, recent deployments,
resource limits, and database connectivity.

### Warning Alert: High Latency

Trigger:
p95 response time exceeds 1 second for 10 consecutive minutes.

Action:
Review request latency, CPU and memory usage,
database query time, and traffic levels.

### Warning Alert: Database Failures

Trigger:
Three or more database connection failures within 5 minutes.

Action:
Check database availability, connection settings,
network restrictions, and credentials.

These thresholds are proposed operational rules.
They are not active Azure alerts until configured.

## 6. Error Budget Policy

When less than 50% of the error budget remains:

- Review recent failures.
- Investigate recurring errors.
- Prioritize reliability improvements.

When the error budget is exhausted:

- Prioritize fixing reliability problems.
- Delay non-essential risky changes until reliability improves.
- Review the causes of failure before further releases.

## 7. Monitoring Requirements

The service should collect:

- Request count and response status codes.
- Response latency.
- Application exceptions.
- Health-check results.
- Database connection failures.
- CPU and memory usage where available.
- Deployment success and failure information.

Azure Application Insights or another suitable monitoring
solution can be used to collect and analyze these measurements.

## 8. Measurement Limitations

The targets in this document are design goals, not measured results.

Availability and latency must be measured using actual
monitoring data. Health checks alone do not prove that
all application features work correctly.

Database reliability depends on the final database design.
The current local SQLite setup must not be assumed to provide
production-grade persistence in the Azure deployment.

## 9. Review

Review these targets after collecting real traffic and
performance data. Adjust them according to user needs,
operational evidence, and the available cloud budget.
