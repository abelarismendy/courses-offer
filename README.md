# Obtain Information from University's Course Offer

This is a Python project that uses Selenium and ChromeDriver to scrape information from the Universidad de los Andes' [course offer website](https://ofertadecursos.uniandes.edu.co/).

## Dependencies

The following packages are required to run this application:

- selenium
- pyunitreport
- tkinter
- re

## Running the application

To run the application, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/abelarismendy/oferta-cursos
```

2. Navigate to the project directory:

```bash
cd oferta-cursos
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Download and install the appropriate ChromeDriver for your system from the following link: https://chromedriver.chromium.org/downloads.

5. Place the ChromeDriver executable in the drivers folder.

6. Run the tests:

```bash
python -m unittest discover
```

## Input

The application expects a text file containing a list of NRCs (course codes) in the input folder. The file should have one course code per line.


## Output
The application will generate a JSON file with the information of the courses in the output folder. The JSON file will have the following structure:

```json
{
    "course_code": {
        "course_name": "name_value",
        "creditos": "creditos_value",
        "secciones": {
             "cupo": "cupo_value",
             "seccion": "seccion_value",
             "teacher": "teacher_full_name",
             "room": "room_alue",
             "schedule": {
                    "DAY_LETTER": [
                        "hour-hour"
                    ],
                    "DAY_LETTER": [
                        "hour-hour"
                    ]
             }
    },
    ...
}
```

### Example

```json
"ISIS-2304": {
        "course_name": "SISTEMAS TRANSACCIONALES",
        "creditos": "3",
        "secciones": {
            "25588": {
                "cupo": "30",
                "seccion": "1",
                "teacher": "AVILA CIFUENTES OSCAR JAVIER",
                "room": "- -",
                "schedule": {
                    "M": [
                        "0930-1050"
                    ],
                    "J": [
                        "0930-1050"
                    ]
                }
            },
            "27390": {
                "cupo": "30",
                "seccion": "2",
                "teacher": "BRAVO CORDOBA GERMAN ENRIQUE",
                "room": "- -",
                "schedule": {
                    "M": [
                        "1100-1220"
                    ],
                    "J": [
                        "1100-1220"
                    ]
                }
            },
            ...
}
```

## Limitations

- The application is limited by the CAPTCHA that the website displays. The user must manually enter the CAPTCHA before the application can continue.
- The application only retrieves information from the first page of the search results.
- The application is also limited by the stability of the website. If the website is down or experiencing issues, the application will not be able to obtain the information.
