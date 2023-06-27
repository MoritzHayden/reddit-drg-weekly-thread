# Reddit DRG Weekly Thread
Fetch the weekly deep dive details from the DRG API and use them to create the weekly Reddit thread via Reddit API. Executions are scheduled with cron and deployed to a GitHub Actions runner.

## Secrets

Add the following to the `.env` file in the `python` directory:

```text
REDDIT_CLIENT_ID=<VALUE>
REDDIT_CLIENT_SECRET=<VALUE>
REDDIT_USERNAME=<VALUE>
REDDIT_PASSWORD=<VALUE>
```

## Installation

```bash
mkdir .venv -p && pipenv install --dev
```

## Execution

```bash
pipenv run python main.py
```
