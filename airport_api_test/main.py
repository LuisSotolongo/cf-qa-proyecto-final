import subprocess

def run_pytest_html():
    subprocess.run(["pytest", "--html=airport_api_test/reports/html_reports/report.html"])

def run_pytest_allure():
    subprocess.run(["pytest", "--alluredir=airport_api_test/reports/html_reports/allure_results"])

if __name__ == "__main__":
    run_pytest_html()
    run_pytest_allure()