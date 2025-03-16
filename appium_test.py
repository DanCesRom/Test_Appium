from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración de capacidades
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"
options.app = r"C:\\Users\\danie\\OneDrive\\Desktop\\Appium\\PokeApp.apk"
options.automation_name = "UiAutomator2"

# Iniciar sesión en Appium
try:
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    print("Driver conectado con éxito")

    # Esperar que cargue la pantalla de login
    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='password']"))
    )
    time.sleep(2)  # Sleep for 3 seconds to let the page settle

    # Ingresar contraseña y enviar formulario
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='password']")))
    password_input = driver.find_element(By.XPATH, "//android.widget.EditText[@resource-id='password']")
    password_input.send_keys("CsF2ty9vjx@VHpbZq7")
    submit_button = driver.find_element(By.XPATH, "//android.widget.Button[@text='Submit']")  # Update the locator if needed
    submit_button.click()                           
    time.sleep(2)
    # Esperar redirección a la página de búsqueda
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//android.view.View[@resource-id='set_name']"))
    )

    # Seleccionar "Prismatic" en el dropdown del set
    set_dropdown = driver.find_element(By.XPATH, "//android.view.View[@resource-id='set_name']")
    set_dropdown.click()
    prismatic_option = driver.find_element(By.XPATH, "//android.widget.CheckedTextView[@resource-id='android:id/text1' and @text='Prismatic Evolutions']")
    prismatic_option.click()
    time.sleep(1)

    # Seleccionar "FullArt" en el dropdown de rareza
    rarity_dropdown = driver.find_element(By.XPATH, "//android.view.View[@resource-id='rarity']")
    rarity_dropdown.click()
    fullart_option = driver.find_element(By.XPATH, "//android.widget.CheckedTextView[@resource-id='android:id/text1' and @text='Full Art']")
    fullart_option.click()
    time.sleep(2)
    driver.find_element(By.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollForward()')


    # Captura de pantalla para verificar selección
    driver.save_screenshot("appium_test_screenshot.png")

    # Cerrar la sesión
    driver.quit()

except Exception as e:
    print("Error al ejecutar Appium:", e)
    if 'driver' in locals():
        driver.quit()
