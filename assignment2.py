import datetime
import logging
import urllib
import urllib2
import argparse



def downloadData(url):
    """Downloads the data"""
    url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response.read()


def processData(csvdata, csv_reader, csv):
    cvs_reader = csv.reader(csvdata)
    persondata = {}
    line_count = 0
    date_format = '%d/%m/%y'
    csv_data = []
    for csv_data in csv_reader:
        id = csv_data[0]
        username = csv_data[1]
        birthday = csv_data[2]
        if id != 'id':
            id = int(id)
        line_count += 1
        try:
            birthday = datetime.datetime.strftime(csv_data[2], date_format)
        except Exception:
            logging.error('Error processing line # %s for id # %s' % (line_count, id))
        finally:
            persondata[id] = {'name': username, 'birthday': birthday}
        return persondata


def displayPerson(id, personData, name, dob):
    try:
        print(' Person # %s is %s with a birthday og %s' % (id, personData[id][name], personData[id][dob]))
    except Exception:
        logging.warning('Invalid ID')
def main():
    print(f"Running main with URL = {url}...")
    cvsdata1 = downloadData(url)
    personData = processData(cvsdata1)
    while True:
        try:
            user_input = int('Please enter the ID #  Enter 0 or a negative to exit')
        except ValueError:
            logging.info('Invalid ID')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='Please type the URL of the csv file', action='store', dest='url', type=str)
    args = parser.parse_args()
    csvdata1 = processData(args.url)



