import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='Personal Finance Dashboard')
    parser.add_argument('command', nargs='?', choices=['run'], help='Use "run" to start the dashboard.')
    parser.add_argument('--port', type=int, default=8501, help='Port to run Streamlit on')
    args = parser.parse_args()

    if args.command == 'run':
        from dashboard import run_dashboard
        run_dashboard(port=args.port)
    else:
        print("Error: Missing command. To run the dashboard, use: python main.py run", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
