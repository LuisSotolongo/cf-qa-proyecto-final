import os
from shophub_ui_test.utils.driver_manager import get_driver
import time
SCREENSHOT_DIRECTORY = "shophub_ui_test/reports/failed_screenshots"


def before_all(context):
    is_ci = os.environ.get("CI", "false").lower() == "true"
    context.driver = get_driver(headless=is_ci)
    if context.driver:
        print("WebDriver iniciado.")
    else:
        print("Error al iniciar WebDriver.")
    print("Configurando el entorno global de prueba...")
    if not os.path.exists(SCREENSHOT_DIRECTORY):
        os.makedirs(SCREENSHOT_DIRECTORY)
    print(f"-> Directorio de capturas de pantalla: {SCREENSHOT_DIRECTORY}")


def after_all(context):
    if context.driver:
        context.driver.quit()
        print("WebDriver cerrado.")
    print("Limpieza global finalizada.")


def before_scenario(context, scenario, ):
    print(f"\n Iniciando escenario: {scenario.name}")


def after_scenario(context, scenario):
    print(f"Finalizando escenario: {scenario.name}")
    if scenario.status == "failed":
        print("El escenario falló. Tomando captura de pantalla...")
        scenario_name = scenario.name.replace(" ", "_").replace("/", "_")
        screenshot_path = os.path.join(SCREENSHOT_DIRECTORY, f"failed_at_{scenario_name}.png")
        context.driver.save_screenshot(screenshot_path)
        print(f"Captura guardada en: {screenshot_path}")
    print("El escenario ha finalizado. Pausando para depuración...")
    time.sleep(5)
    print("Reanudando la ejecución...")
