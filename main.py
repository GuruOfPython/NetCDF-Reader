from netCDF4 import Dataset
from datetime import date, timedelta
import numpy as np

historical_data_path = r"E:\8_Project\Progress\2019-08-14 Process NetCDF data sets and do some calculations\Data\historical_data"
projected_data_path = r"E:\8_Project\Progress\2019-08-14 Process NetCDF data sets and do some calculations\Data\projected data"

file_1 = historical_data_path + '/' + 'tasmax_day_HadGEM2-ES_historical_r1i1p1_19500101-19501231.LOCA_2016-04-02.16th.CA_NV.nc'
fh = Dataset(file_1, mode='r')
ts = fh.variables['time'][:]
lons = fh.variables['lon'][:]
lats = fh.variables['lat'][:]
tmax = fh.variables['tasmax'][:]


def convert_time_to_date(times):
    since = date(1900, 1, 1)
    past_year_range = [1961, 1990]
    future_year_range = [2020, 2050]

    for t in times:
        delta = timedelta(t)
        real_t = since + delta
        start_m = date(real_t.year, 4, 1)
        end_m = date(real_t.year, 10, 31)

        if real_t >= start_m and real_t <= end_m and (
                (real_t.year >= past_year_range[0] and real_t.year <= past_year_range[1]) or (
                real_t.year >= future_year_range[0] and real_t.year <= future_year_range[1])):
            print(real_t)


convert_time_to_date(times=ts)
