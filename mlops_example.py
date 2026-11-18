"""Run a supplied Bash deployment script and propagate its exit status."""
import argparse
from pathlib import Path
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('script', type=Path, help='Bash deployment script to run')
    args = parser.parse_args()
    script = args.script.expanduser().resolve()
    if not script.is_file():
        parser.error(f'Deployment script does not exist: {script}')
    try:
        result = subprocess.run(['bash', str(script)], cwd=script.parent, check=False)
    except FileNotFoundError:
        parser.exit(1, 'Bash is required to run the deployment script.\n')
    raise SystemExit(result.returncode if result.returncode >= 0 else 1)


if __name__ == '__main__':
    main()
