from playwright.sync_api import Playwright, sync_playwright
import pathlib
import logging
import typer
import time
import calendar
import pandas as pd
import zipfile

BTS_URL = "https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr"

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

app = typer.Typer()

@app.command()
def download(start_date: str, end_date: str, download_folder: str = 'bts-data', headless: bool = True):
    """
    Download Airline On-Time Performance data from the Bureau of Transportation Statistics
    (https://www.transtats.bts.gov/) between START_DATE and END_DATE. Use YYYY-MM as date format.
    Choose --headless to run browser in headless mode.

    """
    dates = [(d.year, d.month) for d in pd.date_range(start_date, end_date, freq='MS')]

    path = pathlib.Path(download_folder)
    path.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        get_data(playwright, path, dates, headless)


def get_data(playwright: Playwright, path: pathlib.Path, dates: list, headless: bool) -> None:
 
    # launch browser context
    logging.info(f'Launching browser context with headless={headless}')
    browser = playwright.chromium.launch(headless=headless, downloads_path=str(path))
    context = browser.new_context()
    page = context.new_page()
    page.goto(BTS_URL)

    # check all the boxes desired (a few fields are prechecked so they did not show up in the recording)
    page.get_by_label("Year").check()
    page.get_by_label("Quarter").check()
    page.get_by_label("Month", exact=True).check()
    page.get_by_label("DayofMonth").check()
    page.get_by_label("DayOfWeek").check()
    page.get_by_label("FlightDate").check()
    page.get_by_label("Reporting_Airline", exact=True).check()
    page.get_by_label("DOT_ID_Reporting_Airline").check()
    page.get_by_label("IATA_CODE_Reporting_Airline").check()
    page.get_by_label("Tail_Number").check()
    page.get_by_label("Flight_Number_Reporting_Airline").check()
    page.get_by_label("Origin", exact=True).check()
    page.get_by_label("OriginCityName").check()
    page.get_by_label("OriginState", exact=True).check()
    page.get_by_label("OriginStateFips").check()
    page.get_by_label("OriginStateName").check()
    page.get_by_label("OriginWac").check()
    page.get_by_label("Dest", exact=True).check()
    page.get_by_label("DestCityName").check()
    page.get_by_label("DestState", exact=True).check()
    page.get_by_label("DestStateFips").check()
    page.get_by_label("DestStateName").check()
    page.get_by_label("DestWac").check()
    page.get_by_label("CRSDepTime").check()
    page.get_by_label("DepTime", exact=True).check()
    page.get_by_label("DepDelay", exact=True).check()
    page.get_by_label("DepDelayMinutes").check()
    page.get_by_label("DepDel15").check()
    page.get_by_label("DepartureDelayGroups").check()
    page.get_by_label("DepTimeBlk").check()
    page.get_by_label("TaxiOut").check()
    page.get_by_label("WheelsOff", exact=True).check()
    page.get_by_label("WheelsOn", exact=True).check()
    page.get_by_label("TaxiIn").check()
    page.get_by_label("CRSArrTime").check()
    page.get_by_label("ArrTime", exact=True).check()
    page.get_by_label("ArrDelay", exact=True).check()
    page.get_by_label("ArrDelayMinutes").check()
    page.get_by_label("ArrDel15").check()
    page.get_by_label("ArrivalDelayGroups").check()
    page.get_by_label("ArrTimeBlk").check()
    page.get_by_label("Cancelled").check()
    page.get_by_label("CancellationCode").check()
    page.get_by_label("Diverted").check()
    page.get_by_label("CRSElapsedTime").check()
    page.get_by_label("ActualElapsedTime", exact=True).check()
    page.get_by_label("AirTime").check()
    page.get_by_label("Flights").check()
    page.get_by_label("Distance", exact=True).check()
    page.get_by_label("DistanceGroup").check()
    page.get_by_label("CarrierDelay").check()
    page.get_by_label("WeatherDelay").check()
    page.get_by_label("NASDelay").check()
    page.get_by_label("SecurityDelay").check()
    page.get_by_label("LateAircraftDelay").check()
    page.get_by_label("FirstDepTime").check()
    page.get_by_label("TotalAddGTime").check()
    page.get_by_label("LongestAddGTime").check()
    page.get_by_label("DivAirportLandings").check()
    page.get_by_label("DivReachedDest").check()
    page.get_by_label("DivActualElapsedTime").check()
    page.get_by_label("DivArrDelay").check()
    page.get_by_label("DivDistance").check()
    page.get_by_label("Div1Airport", exact=True).check()
    page.get_by_label("Div1AirportID").check()
    page.get_by_label("Div1AirportSeqID").check()
    page.get_by_label("Div1WheelsOn").check()
    page.get_by_label("Div1TotalGTime").check()
    page.get_by_label("Div1LongestGTime").check()
    page.get_by_label("Div1WheelsOff").check()
    page.get_by_label("Div1TailNum").check()
    page.get_by_label("Div2Airport", exact=True).check()
    page.get_by_label("Div2AirportID").check()
    page.get_by_label("Div2AirportSeqID").check()
    page.get_by_label("Div2WheelsOn").check()
    page.get_by_label("Div2TotalGTime").check()
    page.get_by_label("Div2LongestGTime").check()
    page.get_by_label("Div2WheelsOff").check()
    page.get_by_label("Div2TailNum").check()
    page.get_by_label("Div3Airport", exact=True).check()
    page.get_by_label("Div3AirportID").check()
    page.get_by_label("Div3AirportSeqID").check()
    page.get_by_label("Div3WheelsOn").check()
    page.get_by_label("Div3TotalGTime").check()
    page.get_by_label("Div3LongestGTime").check()
    page.get_by_label("Div3WheelsOff").check()
    page.get_by_label("Div3TailNum").check()
    page.get_by_label("Div4Airport", exact=True).check()
    page.get_by_label("Div4AirportID").check()
    page.get_by_label("Div4AirportSeqID").check()
    page.get_by_label("Div4WheelsOn").check()
    page.get_by_label("Div4TotalGTime").check()
    page.get_by_label("Div4LongestGTime").check()
    page.get_by_label("Div4WheelsOff").check()
    page.get_by_label("Div4TailNum").check()
    page.get_by_label("Div5Airport", exact=True).check()
    page.get_by_label("Div5AirportID").check()
    page.get_by_label("Div5AirportSeqID").check()
    page.get_by_label("Div5WheelsOn").check()
    page.get_by_label("Div5TotalGTime").check()
    page.get_by_label("Div5LongestGTime").check()
    page.get_by_label("Div5WheelsOff").check()
    page.get_by_label("Div5TailNum").check()

    # choose year and month and download
    for year, month in dates:
        logging.info(f'Retrieving data for {year}-{month}')
        file_name = f"bts_airline_ontime_performance_{calendar.month_name[month].lower()}_{year}.zip"
        file_path = path.joinpath(file_name)
        if file_path.exists():
            logging.info(f'... {file_name} exists, skipping download')
            continue
        
        page.locator("#cboYear").select_option(str(year))
        page.locator("#cboPeriod").select_option(str(month))

        logging.info(f'... initiating download request for {year}-{month}')
        with page.expect_download(timeout=1000*60*20) as download_info:
            page.get_by_role("button", name="Download").click(timeout=1000*60*20)

        download = download_info.value
        logging.info(f'... saving data to temporary file: {download.path()}')
        download.save_as(str(file_path))
        logging.info(f'... download complete, saved as: {file_name}')

    time.sleep(60)  # wait for download to complete before closing browser
    
    # ---------------------
    context.close()
    browser.close()
    logging.info(f'Closing browser context')


@app.command()
def extract(download_folder: str):
    """
    Extract csv's from downloaded zipped data files
    """
    logging.info(f"Extracting csv's from zip files in {download_folder}:") 
    for file_name in pathlib.Path(download_folder).glob('*.zip'):
        archive = zipfile.ZipFile(file_name, mode="r")
        csv_file = archive.infolist()[0]
        csv_file.filename = str(file_name.with_suffix('.csv'))
        archive.extract(csv_file)
        logging.info(f'... extracted {csv_file.filename}')


if __name__ == "__main__":
    app()