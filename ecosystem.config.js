// edit based on your project path
module.exports = {
    apps: [{
      name: "subflow-8010",
      script: "/home/pi/production/subflow/venv/bin/gunicorn",
      args: "--config gunicorn_config.py core.wsgi:application",
      cwd: "/home/pi/production/subflow",
      interpreter: "/home/pi/production/subflow/venv/bin/python",
    }]
  }