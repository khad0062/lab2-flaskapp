# CST8919 Lab 2: Building a Web App with Threat Detection using Azure Monitor and KQL

## Overview

This lab demonstrates how to deploy a simple Flask login application to Azure Web App, enable diagnostic logging to Azure Log Analytics, detect brute-force login attempts using KQL (Kusto Query Language), and configure automated alerts in Azure Monitor.

---

## What I Learned

During this lab, I learned how to:
- Deploy a Python Flask application to Azure Web App.
- Enable and route diagnostic logs (AppServiceConsoleLogs, HTTP logs) to Azure Log Analytics.
- Query logs in Azure Monitor using KQL to detect failed login attempts.
- Configure Azure Monitor alerts to detect brute-force behavior and trigger email notifications.

---

## Challenges Faced

- **Log Collection Consistency:** Ensuring that log messages from Flask (using Python logging) were actually captured in the correct Azure tables. Sometimes, logs appear in `AppServiceAppLogs` instead of `AppServiceConsoleLogs`.
- **KQL Query Tuning:** Adjusting the KQL query to match the exact message format and table in which the logs were stored.
- **Alert Thresholds:** Deciding on realistic thresholds (number of failed attempts and time window) to avoid false positives.

---

## Improvements for Real-World Detection

- **Track by IP/User:** Enhance detection logic to count failed attempts per user or per IP address, not just global count.
- **Rate Limiting:** Implement app-level lockouts or CAPTCHA after several failed attempts.
- **Geolocation:** Alert on failed attempts from unusual locations.
- **Log Enrichment:** Include user agent, device, and session info in logs for more context.
- **Correlation:** Correlate failed logins with other suspicious activities, like password resets.

---

## KQL Query & Explanation

```kql
AppServiceConsoleLogs
| where TimeGenerated > ago(5m)
| where ResultDescription has "FAILED LOGIN"
| project TimeGenerated, Level, ResultDescription
| order by TimeGenerated desc

```
Explanation:

AppServiceConsoleLogs:
This is the Azure Log Analytics table that stores your web app’s console logs, including custom log messages from your Flask app.

| where TimeGenerated > ago(5m):
Limits the results to logs generated in the last 5 minutes, making the query suitable for real-time brute-force detection.

| where ResultDescription has "FAILED LOGIN":
Filters to only those log entries that contain your custom "FAILED LOGIN" string, which is written by your Flask app on each failed login attempt.

| project TimeGenerated, Level, ResultDescription:
Selects and displays only the timestamp, log level, and log message content for easy analysis.

| order by TimeGenerated desc:
Sorts results from newest to oldest, so the latest failed attempts are shown first


## Youtube Video demo
[Youtube Video Link](https://youtu.be/trzotZzdjeA)
