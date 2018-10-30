"""
Central location for all hard coded data needed for tests.
"""

DOWNLOAD_OPTIONS_FROM_ALL_SERVICES = {
    # 'svc://nasa:srtm-3-arc-second': {},
    # 'svc://nasa:srtm-30-arc-second': {},
    'svc://noaa-ncdc:ghcn-daily': {
        'properties': [{
            'default': None,
            'description': 'parameter',
            'name': 'parameter',
            'range': [
                ['air_temperature:daily:mean', 'air_temperature:daily:mean'],
                ['air_temperature:daily:minimum', 'air_temperature:daily:minimum'],
                ['air_temperature:daily:total', 'air_temperature:daily:total'],
                ['rainfall:daily:total', 'rainfall:daily:total'],
                ['snow_depth:daily:total', 'snow_depth:daily:total'],
                ['snowfall:daily:total', 'snowfall:daily:total']],
            'type': 'ObjectSelector'},
            {'bounds': None,
             'default': None,
             'description': 'start date',
             'name': 'start',
             'type': 'Date'},
            {'bounds': None,
             'default': None,
             'description': 'end date',
             'name': 'end',
             'type': 'Date'}],
        'title': 'NCDC GHCN Daily Download Options'},
    'svc://noaa-ncdc:gsod': {
        'properties': [
            {'default': None,
             'description': 'parameter',
             'name': 'parameter',
             'range': [
                 ['air_temperature:daily:max', 'air_temperature:daily:max'],
                 ['air_temperature:daily:min', 'air_temperature:daily:min'],
                 ['rainfall:daily:total', 'rainfall:daily:total'],
                 ['snow_depth:daily:total', 'snow_depth:daily:total']],
             'type': 'ObjectSelector'},
            {'bounds': None,
             'default': None,
             'description': 'start date',
             'name': 'start',
             'type': 'Date'},
            {'bounds': None,
             'default': None,
             'description': 'end date',
             'name': 'end',
             'type': 'Date'}],
        'title': 'NCDC GSOD Download Options'},
    'svc://noaa-coast:coops-meteorological':
        {'properties': [
            {'default': None,
             'description': 'parameter',
             'name': 'parameter',
             'range': [
                 ['air_temperature', 'air_temperature'],
                 ['barometric_pressure', 'barometric_pressure'],
                 ['collective_rainfall', 'collective_rainfall'],
                 ['direction_of_sea_water_velocity', 'direction_of_sea_water_velocity'],
                 ['relative_humidity', 'relative_humidity'],
                 ['sea_water_electric_conductivity', 'sea_water_electric_conductivity'],
                 ['sea_water_speed', 'sea_water_speed'],
                 ['sea_water_temperature', 'sea_water_temperature'],
                 ['visibility_in_air', 'visibility_in_air'],
                 ['wind_from_direction', 'wind_from_direction'],
                 ['wind_speed', 'wind_speed'],
                 ['wind_speed_from_gust', 'wind_speed_from_gust']],
             'type': 'ObjectSelector'},
            {'bounds': None,
             'default': None,
             'description': 'start date',
             'name': 'start',
             'type': 'Date'},
            {'bounds': None,
             'default': None,
             'description': 'end date',
             'name': 'end',
             'type': 'Date'}
        ],
            'title': 'NOAA COOPS Met Download Options'},
    'svc://noaa-coast:coops-water':
        {'properties': [
            {'default': None,
             'description': 'parameter',
             'name': 'parameter',
             'range': [
                 ['predicted_waterLevel', 'predicted_waterLevel'],
                 ['sea_surface_height_amplitude', 'sea_surface_height_amplitude']
             ],
             'type': 'ObjectSelector'},
            {'bounds': None,
             'default': None,
             'description': 'start date',
             'name': 'start',
             'type': 'Date'},
            {'bounds': None,
             'default': None,
             'description': 'end date',
             'name': 'end',
             'type': 'Date'},
            {'default': 'R',
             'description': 'quality',
             'name': 'quality',
             'range': [
                 ['Preliminary', 'Preliminary'],
                 ['R', 'R'],
                 ['Verified', 'Verified']],
             'type': 'ObjectSelector'},
            {'default': '6',
             'description': 'time interval',
             'name': 'interval',
             'range': [['6', '6'], ['60', '60']],
             'type': 'ObjectSelector'},
            {'default': 'Mean Lower_Low Water',
             'description': 'datum',
             'name': 'datum',
             'range': [
                 ['Great Diurnal Range', 'Great Diurnal Range'],
                 ['Greenwich High Water Interval( in Hours)', 'Greenwich High Water Interval( in Hours)'],
                 ['Greenwich Low Water Interval( in Hours)', 'Greenwich Low Water Interval( in Hours)'],
                 ['Mean Diurnal High Water Inequality', 'Mean Diurnal High Water Inequality'],
                 ['Mean Diurnal Low Water Inequality', 'Mean Diurnal Low Water Inequality'],
                 ['Mean Diurnal Tide L0evel', 'Mean Diurnal Tide L0evel'],
                 ['Mean High Water', 'Mean High Water'],
                 ['Mean Higher - High Water', 'Mean Higher - High Water'],
                 ['Mean Low Water', 'Mean Low Water'],
                 ['Mean Lower_Low Water', 'Mean Lower_Low Water'],
                 ['Mean Range of Tide', 'Mean Range of Tide'],
                 ['Mean Sea Level', 'Mean Sea Level'],
                 ['Mean Tide Level', 'Mean Tide Level'],
                 ['North American Vertical Datum', 'North American Vertical Datum'],
                 ['Station Datum', 'Station Datum']],
             'type': 'ObjectSelector'}],
            'title': 'NOAA COOPS Water Download Options'},
    'svc://noaa-coast:ndbc':
        {'properties': [
            {'default': None,
             'description': 'parameter',
             'name': 'parameter',
             'range': [
                 ['air_pressure', 'air_pressure'],
                 ['air_temperature', 'air_temperature'],
                 ['eastward_wind', 'eastward_wind'],
                 ['northward_wind', 'northward_wind'],
                 ['sea_surface_temperature', 'sea_surface_temperature'],
                 ['water_level', 'water_level'],
                 ['wave_height', 'wave_height'],
                 ['wind_direction', 'wind_direction'],
                 ['wind_from_direction', 'wind_from_direction'],
                 ['wind_speed_of_gust', 'wind_speed_of_gust']],
             'type': 'ObjectSelector'},
            {'bounds': None,
             'default': None,
             'description': 'start date',
             'name': 'start',
             'type': 'Date'},
            {'bounds': None,
             'default': None,
             'description': 'end date',
             'name': 'end',
             'type': 'Date'}
        ],
            'title': 'NOAA National Data Buoy Center Download Options'},
    'svc://usgs-ned:1-arc-second': {},
    'svc://usgs-ned:13-arc-second': {},
    'svc://usgs-ned:19-arc-second': {},
    'svc://usgs-ned:alaska-2-arc-second': {},
    'svc://usgs-nlcd:2001': {},
    'svc://usgs-nlcd:2006': {},
    'svc://usgs-nlcd:2011': {},
    'svc://usgs-nwis:dv':
        {'properties': [
            {'default': None,
             'description': 'parameter',
             'name': 'parameter',
             'range': [
                 ['streamflow:mean:daily', 'streamflow:mean:daily'],
                 ['water_temperature:daily:max', 'water_temperature:daily:max'],
                 ['water_temperature:daily:mean', 'water_temperature:daily:mean'],
                 ['water_temperature:daily:min', 'water_temperature:daily:min']],
             'type': 'ObjectSelector'},
            {'bounds': None,
             'default': None,
             'description': 'start date',
             'name': 'start',
             'type': 'Date'},
            {'bounds': None,
             'default': None,
             'description': 'end date',
             'name': 'end',
             'type': 'Date'},
            {'default': 'P365D',
             'description': 'time period (e.g. P365D = 365 days or P4W = 4 weeks)',
             'name': 'period',
             'type': 'String'}],
            'title': 'NWIS Daily Values Service Download Options'},
    'svc://usgs-nwis:iv':
        {'properties': [
            {'default': None,
             'description': 'parameter',
             'name': 'parameter',
             'range': [
                 ['gage_height', 'gage_height'],
                 ['streamflow', 'streamflow'],
                 ['water_temperature', 'water_temperature']
             ],
             'type': 'ObjectSelector'},
            {'bounds': None,
             'default': None,
             'description': 'start date',
             'name': 'start',
             'type': 'Date'},
            {'bounds': None,
             'default': None,
             'description': 'end date',
             'name': 'end',
             'type': 'Date'},
            {'default': 'P365D',
             'description': 'time period (e.g. P365D = 365 days or P4W = 4 weeks)',
             'name': 'period',
             'type': 'String'}
        ],
            'title': 'NWIS Instantaneous Values Service Download Options'},
    'svc://quest:quest': {},
    'svc://cuahsi-hydroshare:hs_geo': {},
    'svc://cuahsi-hydroshare:hs_norm': {},
    'svc://wmts:seamless_imagery':
        {'title': 'Web Mercator Tile Service Download Options',
         'properties': [
             {'name': 'url',
              'type': 'ObjectSelector',
              'description': '',
              'default': 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/'
                         '{Z}/{Y}/{X}',
              'range': [
                  ['http://c.tile.openstreetmap.org/{Z}/{X}/{Y}.png',
                   'http://c.tile.openstreetmap.org/{Z}/{X}/{Y}.png'],
                  ['http://tile.stamen.com/terrain/{Z}/{X}/{Y}.png',
                   'http://tile.stamen.com/terrain/{Z}/{X}/{Y}.png'],
                  ['https://s.basemaps.cartocdn.com/light_all/{Z}/{X}/{Y}.png',
                   'https://s.basemaps.cartocdn.com/light_all/{Z}/{X}/{Y}.png'],
                  ['https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{Z}/{Y}/{X}',
                   'https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{Z}/{Y}/{X}'],
                  ['https://server.arcgisonline.com/ArcGIS/rest/services/Ocean_Basemap/MapServer/tile/{Z}/{Y}/{X}',
                   'https://server.arcgisonline.com/ArcGIS/rest/services/Ocean_Basemap/MapServer/tile/{Z}/{Y}/{X}'],
                  ['https://server.arcgisonline.com/ArcGIS/rest/services/USA_Topo_Maps/MapServer/tile/{Z}/{Y}/{X}',
                   'https://server.arcgisonline.com/ArcGIS/rest/services/USA_Topo_Maps/MapServer/tile/{Z}/{Y}/{X}'],
                  ['https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{Z}/{Y}/{X}',
                   'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{Z}/{Y}/{X}'],
                  ['https://server.arcgisonline.com/ArcGIS/rest/services/World_Physical_Map/MapServer/tile/'
                   '{Z}/{Y}/{X}',
                   'https://server.arcgisonline.com/ArcGIS/rest/services/World_Physical_Map/MapServer/tile/'
                   '{Z}/{Y}/{X}'],
                  ['https://server.arcgisonline.com/ArcGIS/rest/services/World_Shaded_Relief/MapServer/tile/'
                   '{Z}/{Y}/{X}',
                   'https://server.arcgisonline.com/ArcGIS/rest/services/World_Shaded_Relief/MapServer/tile/'
                   '{Z}/{Y}/{X}'],
                  ['https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{Z}/{Y}/{X}',
                   'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{Z}/{Y}/{X}'],
                  ['https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/'
                   '{Z}/{Y}/{X}',
                   'https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{'
                   'Z}/{Y}/{X}'],
                  ['https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{Z}/{Y}/{X}',
                   'https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{Z}/{Y}/{X}']
              ]},
             {'name': 'zoom_level',
              'type': 'Integer',
              'description': '',
              'default': 8,
              'bounds': None},
             {'name': 'bbox',
              'type': 'List',
              'description': '[x-min, y-max, x-max, y-min]',
              'default': [-180, 90, 180, -90]},
             {'name': 'crop_to_bbox',
              'type': 'Boolean',
              'description': None,
              'default': True},
             {'name': 'max_tiles',
              'type': 'Number',
              'description': 'Maximum number of tiles to allow (a number between 1 and `zoom_level`^4)',
              'default': 1000,
              'bounds': None}]}
}


SERVICES_CATALOG_COUNT = [
    # ('svc://nasa:srtm-3-arc-second', 14297, 1000),
    # ('svc://nasa:srtm-30-arc-second', 27, 10),
    ('svc://noaa-ncdc:ghcn-daily', 104126, 5000),
    ('svc://noaa-ncdc:gsod', 28754, 1500),
    ('svc://noaa-coast:coops-meteorological', 375, 50),
    ('svc://noaa-coast:coops-water', 234, 50),
    ('svc://noaa-coast:ndbc', 1136, 100),
    ('svc://usgs-ned:1-arc-second', 3644, 100),
    ('svc://usgs-ned:13-arc-second', 1245, 100),
    # ('svc://usgs-ned:19-arc-second', 8358, 100),  #  As of Sept 2018 this service is no longer consistent
    ('svc://usgs-ned:alaska-2-arc-second', 503, 50),
    ('svc://usgs-nlcd:2001', 147, 100),
    ('svc://usgs-nlcd:2006', 131, 100),
    ('svc://usgs-nlcd:2011', 203, 100),
    ('svc://usgs-nwis:dv', 36368, 1000),
    ('svc://usgs-nwis:iv', 20412, 1000),
    ('svc://wmts:seamless_imagery', 1, 1),
    ('svc://cuahsi-hydroshare:hs_geo', 1090, 1000),
    ('svc://cuahsi-hydroshare:hs_norm', 2331, 1000),
]


CACHED_SERVICES = [s[0] for s in SERVICES_CATALOG_COUNT]

ALL_SERVICES = sorted(DOWNLOAD_OPTIONS_FROM_ALL_SERVICES.keys())

SERVICE = 'svc://usgs-nwis:iv'
CATALOG_ENTRY = 'svc://usgs-nwis:iv/01516350'
DATASET = 'd56fa10348894ba594dfc43f238d3b6d'

DATASET_METADATA = {
    'download_status': 'downloaded',
    'download_message': 'success',
    'name': DATASET,
    'file_format': 'timeseries-hdf5',
    'datatype': 'timeseries',
    'catalog_entry': 'svc://usgs-nwis:iv/01516350',
    'collection': 'test_data',
    'download_options': '{"parameter": "streamflow"}',
    'dataset_type': 'download',
    'timezone': 'utc',
    'unit': 'ft3/s',
    'display_name': DATASET,
    'parameter': 'streamflow',
    'metadata': {}
}

SERVICE_DOWNLOAD_OPTIONS = [
    # ('svc://nasa:srtm-3-arc-second/G1034711987-LPDAAC_ECS' , None),
    # ('svc://nasa:srtm-30-arc-second/G1005651728-LPDAAC_ECS', None),
    ('svc://noaa-ncdc:ghcn-daily/ACW00011604', {'parameter': 'air_temperature:daily:total', 'start': '1949-01-01', 'end': '1949-01-02'}),
    ('svc://noaa-ncdc:gsod/717580-99999', {'parameter': 'air_temperature:daily:max', 'start': '2016-01-01', 'end': '2016-01-02'}),
    ('svc://noaa-coast:coops-meteorological/1611400', {'parameter': 'air_temperature', 'start': '2015-05-23', 'end': '2015-05-24'}),
    ('svc://noaa-coast:coops-water/1611400', {'parameter': 'predicted_waterLevel', 'start': '2015-05-23', 'end': '2015-05-24'}),
    ('svc://noaa-coast:ndbc/0Y2W3', {'parameter': 'air_pressure', 'start': '2015-05-23', 'end': '2015-05-24'}),
    ('svc://usgs-ned:1-arc-second/581d2134e4b08da350d52cb0', None),
    ('svc://usgs-ned:13-arc-second/581d2134e4b08da350d52caf', None),
    ('svc://usgs-ned:19-arc-second/581d2561e4b08da350d5a3b2', None),
    ('svc://usgs-ned:alaska-2-arc-second/581d276ee4b08da350d5decb', None),
    ('svc://usgs-nlcd:2001/5a1c65a5e4b09fc93dd648f1', None),
    ('svc://usgs-nlcd:2006/5a1c35b6e4b09fc93dd64011', None),
    ('svc://usgs-nlcd:2011/5a1c31abe4b09fc93dd6381c', None),
    ('svc://usgs-nwis:dv/01010000', {'parameter': 'streamflow:mean:daily', 'start': '2016-01-01', 'end': '2016-01-02'}),
    ('svc://usgs-nwis:iv/01010000', {'parameter': 'gage_height', 'start': '2016-01-01', 'end': '2016-01-02'}),
]
