import subprocess

def run_pytest_html():
    subprocess.run(["pytest", "--html=reports/html_reports/report.html"])

if __name__ == "__main__":
    run_pytest_html()