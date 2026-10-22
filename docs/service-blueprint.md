
# Service Blueprint — Task Tracker

## 1. Service Overview

The Task Tracker is a web application that allows users
to add, view, and delete tasks through a browser.

The application uses Python Flask for backend processing,
HTML and CSS for the frontend, and SQLite for the current
database implementation.

The application is deployed to Azure App Service.
GitHub stores the source code, and GitHub Actions automates
the deployment process.

## 2. Architecture Components

### User and Browser

The user opens the website through a browser and submits
requests to add or delete tasks.

### Application Tier

The Flask application runs on Azure App Service.
It receives HTTPS requests, processes user input,
executes application logic, and communicates with the database.

### Data Tier

The application currently uses SQLite.

The local development database is stored in tasks.db.
The cloud deployment must use an appropriately persistent
database solution before the application is considered
production-ready.

### Source Control and Deployment

GitHub stores the application source code.
GitHub Actions runs the deployment workflow and publishes
the application to Azure App Service.

## 3. Request Flow

1. The user opens the website over HTTPS.
2. Azure App Service receives the request.
3. Flask routes the request to the correct function.
4. For the home page, the application retrieves tasks.
5. For adding a task, Flask validates the submitted task
   and writes it to the database.
6. For deleting a task, Flask identifies the task by ID
   and deletes it from the database.
7. The application redirects the user to the home page.
8. The browser displays the updated task list.

## 4. Data Flow

### Add Task

Browser form
-> Flask /add endpoint
-> Input validation
-> Database insert
-> Database commit
-> Redirect to home page

### View Tasks

Browser
-> Flask home endpoint
-> Database query
-> Task records returned
-> HTML template rendered
-> Browser displays tasks

### Delete Task

Browser delete form
-> Flask /delete/<task_id> endpoint
-> Database delete operation
-> Database commit
-> Redirect to home page

## 5. Deployment Flow

1. The developer modifies application files locally.
2. The developer commits the changes to Git.
3. The changes are pushed to the GitHub main branch.
4. GitHub Actions starts the configured workflow.
5. The workflow builds or packages the application
   and deploys it to Azure App Service.
6. The deployment result is checked in GitHub Actions.
7. The developer opens the Azure website and tests
   the application's basic functionality.

The deployment pipeline has been tested successfully
for the initial application version.

## 6. Failure Paths

### Application Startup Failure

Possible causes:
- Missing Python dependency.
- Incorrect application startup configuration.
- Invalid application code.

Response:
- Inspect deployment logs.
- Check requirements.txt and startup configuration.
- Restore a known-good release if required.

### Database Failure

Possible causes:
- Database unavailable.
- Invalid connection settings.
- Database file not present in the deployed environment.

Response:
- Inspect application logs.
- Verify database connectivity and storage configuration.
- Restore data using the chosen backup and recovery process.

### Deployment Failure

Possible causes:
- GitHub Actions workflow failure.
- Dependency installation failure.
- Incorrect deployment configuration.

Response:
- Inspect the failed workflow.
- Correct the configuration.
- Redeploy and verify the application.

### High Latency or Capacity Problems

Possible causes:
- Increased traffic.
- Slow database operations.
- Insufficient application resources.

Response:
- Review request latency and error metrics.
- Inspect resource usage.
- Optimize database operations or scale resources when justified.

### Connectivity Failure

Possible causes:
- Network restrictions.
- DNS issues.
- Incorrect database connection settings.

Response:
- Check network configuration and logs.
- Verify database access rules and credentials.

## 7. Security

- Use HTTPS for public website traffic.
- Do not commit passwords, access keys, or tokens.
- Keep secrets in supported application settings or a
  managed secret store.
- Use least-privilege permissions.
- Restrict database access.
- Avoid logging sensitive information.

## 8. Availability and Recovery

Proposed availability SLO: 99.5% over a rolling 30-day period.

The application should have monitored health checks
and documented incident-response steps.

Recovery Point Objective (RPO) and Recovery Time Objective
(RTO) must be finalized after selecting the production database
and reviewing the project's recovery requirements.

## 9. Current Limitations

- SQLite is suitable for local learning and simple testing.
- Database persistence in Azure has not yet been validated.
- Production backup and recovery are not yet configured.
- Alert thresholds are documented as proposals and must
  be configured in monitoring tools.
- Cost estimates must be calculated before selecting
  production service tiers.

## 10. Future Improvements

- Select a persistent managed database.
- Configure application monitoring and alerts.
- Add automated tests to the GitHub Actions workflow.
- Define and test backup and recovery procedures.
- Estimate monthly cloud costs at three traffic levels.
