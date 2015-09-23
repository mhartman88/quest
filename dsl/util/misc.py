import appdirs
import itertools
from .config import get_settings
import os
from stevedore import extension, driver
try:
    import simplejson as json
except ImportError:
    import json

from uuid import uuid4


def append_features(old, new):
    if not old:
        return new

    existing_features = [feature['id'] for feature in old['features']]
    for feature in new['features']:
        if feature['id'] not in existing_features:
            old['features'].append(feature)

    return old


def bbox2poly(x1, y1, x2, y2):
    xmin, xmax = sorted([float(x1), float(x2)])
    ymin, ymax = sorted([float(y1), float(y2)])
    poly = [(xmin, ymin), (xmin, ymax), (xmax, ymax), (xmax, ymin)]
    poly.append(poly[0])

    return poly


def get_cache_dir():
    settings = get_settings()
    return _abs_path(settings['CACHE_DIR'])


def get_collections_index():
    settings = get_settings()
    return _abs_path(settings['COLLECTIONS_INDEX_FILE'], mkdir=False)


def get_dsl_dir():
    settings = get_settings()
    return settings['BASE_DIR']


def get_data_dir():
    settings = get_settings()
    return _abs_path(settings['DATA_DIR'])


def mkdir_if_doesnt_exist(dir_path):
    """makes a directory if it doesn't exist"""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def parse_uri(uri):
    """parse uri and return dictionary

    webservice://<webservice>::<layer>::<feature>::<parameter>::<dataset>
    collection://<collection>::<layer>::<feature>::<parameter>::<dataset>
    """
    keys = ['name', 'layer', 'feature', 'parameter', 'dataset']
    uri_dict = {}
    uri_dict['resource'], remainder = uri.split('://')
    parts = remainder.split('::')
    uri_dict.update({k: parts[i].strip() if i < len(parts) else None for i, k in enumerate(keys)})
    return uri_dict


def listify(liststr, delimiter=','):
    """If input is a string, split on comma and convert to python list
    """
    if liststr is None:
        return None

    return isinstance(liststr, list) and liststr or [s.strip() for s in liststr.split(delimiter)] 


def list_drivers(namespace):
    namespace = 'dsl.' + namespace
    mgr = extension.ExtensionManager(
            namespace=namespace,
            invoke_on_load=False,
        )
    return [x.name for x in mgr]


def load_drivers(namespace, names=None):
    names = listify(names)
    namespace = 'dsl.' + namespace

    if names is None:
        mgr = extension.ExtensionManager(
            namespace=namespace,
            invoke_on_load=True,
        )
        return dict((x.name, x.obj) for x in mgr)

    return {name: driver.DriverManager(namespace, name, invoke_on_load='True') for name in names} 
    

def remove_key(d, key):
    r = dict(d)
    del r[key]
    return r


def jsonify(f):
    def wrapped_f(*args, **kw):
        if 'json' in list(kw.keys()):
            kw = json.loads(kw['json'])

        as_json = kw.get('as_json')
        if as_json:
            del kw['as_json']
            return json.dumps(f(*args, **kw), sort_keys=True, indent=4, separators=(',', ': '))
        else:
            return f(*args, **kw)
    return wrapped_f  # the wrapped function gets returned.


def stringify(args):
    return isinstance(args, list) and ','.join(args) or None


def uid():
    return uuid4().hex


def _abs_path(path, mkdir=True):
    if not os.path.isabs(path):
        path = os.path.join(get_dsl_dir(), path)

    if mkdir:
        mkdir_if_doesnt_exist(path)

    return path