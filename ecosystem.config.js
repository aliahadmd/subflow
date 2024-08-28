// edit based on your project path
module.exports = {
    apps: [{
      name: "subflow",
      script: "/home/p/production/subflow/venv/bin/gunicorn",
      args: "--config gunicorn_config.py core.wsgi:application",
      cwd: "/home/p/production/subflow",
      interpreter: "/home/p/production/subflow/venv/bin/python",
    }]
  }