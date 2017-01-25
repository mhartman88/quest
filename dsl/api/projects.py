"""API functions related to Projects."""
from jsonrpc import dispatcher
import os
import pandas as pd
import shutil
from ..util.log import logger
from .. import util
from .database import db_session, get_db, init_db


PROJECT_DB_FILE = 'metadata.db'
PROJECT_INDEX_FILE = 'project_index.yml'


def active_db():
    """Return path to active project database"""
    dbpath = _get_project_db(get_active_project())
    return dbpath


@dispatcher.add_method
def add_project(name, path, activate=True):
    """Add a existing DSL project to the list of available projects.

    This to add existing dsl projects to current session
    """
    name = name.lower()
    projects = _load_projects()
    if name in projects.keys():
        raise ValueError('Project %s exists, please use a unique name' % name)
    if not os.path.exists(path):
        raise ValueError('Path does not exist: %s' % path)

    try:
        folder = path
        # new_projects = dict(projects)
        projects.update({name: {'folder': folder}})
        _write_projects(projects)
        project = _load_project(name)
    except Exception as e:
        projects.pop(name)
        _write_projects(projects)
        raise ValueError('Invalid Project Folder: %s' % path)

    if activate:
        set_active_project(name)
    return project


@dispatcher.add_method
def new_project(name, display_name=None, description=None, metadata=None,
                folder=None, activate=True):
    """Create a new DSL project and add it to list of available projects."""
    name = name.lower()
    projects = _load_projects()
    if name in projects.keys():
        raise ValueError('Project %s exists, please use a unique name' % name)

    if display_name is None:
        display_name = name

    if description is None:
        description = ''

    if folder is None:
        folder = name

    if metadata is None:
        metadata = {}

    if not os.path.isabs(folder):
        path = os.path.join(util.get_projects_dir(), folder)
    else:
        path = folder

    util.mkdir_if_doesnt_exist(path)
    dbpath = os.path.join(path, PROJECT_DB_FILE)
    db = init_db(dbpath)
    with db_session:
        db.Project(display_name=display_name,
                   description=description,
                   metadata=metadata)
    db.disconnect()
    projects.update({name: {'folder': folder}})
    _write_projects(projects)

    if activate:
        set_active_project(name)
    return _load_project(name)


@dispatcher.add_method
def delete_project(name):
    """delete a project.

    Deletes a project and all data in the project folder.

    Args:
        name : str,
            The name of the collection

    Returns:
        projects : dict,
            A python dict representation of the list of available collections,
            the updated collections list is also written to a json file.
    """
    projects = _load_projects()

    if name not in list(projects.keys()):
        logger.error('Project not found')
        return projects

    folder = projects[name]['folder']
    if not os.path.isabs(folder):
        path = os.path.join(util.get_projects_dir(), folder)
    else:
        path = folder
    if os.path.exists(path):
        logger.info('deleting all data under path:', path)
        shutil.rmtree(path)

    return remove_project(name)


@dispatcher.add_method
def get_active_project():
    """Get active project name."""
    path = _get_projects_index_file()
    return util.read_yaml(path).get('active_project', 'default')


@dispatcher.add_method
def get_projects(expand=False, as_dataframe=False):
    """Get list of available projects."""
    projects = {}
    if not expand and not as_dataframe:
        return list(_load_projects().keys())

    for name, project in _load_projects().items():
        path = project['folder']
        if not os.path.isabs(path):
            path = os.path.join(util.get_projects_dir(), path)

        data = _load_project(name)
        data.update({
            'name': name,
            'folder': path,
        })

        projects[name] = data

    if as_dataframe:
        projects = pd.DataFrame.from_dict(projects, orient='index')

    return projects


@dispatcher.add_method
def remove_project(name):
    """Remove a project from the list of available projects.

    This does not delete the project folder or data, just removes it from the
    index of available projects.
    """
    projects = _load_projects()

    if name not in list(projects.keys()):
        logger.error('Project not found')
        return projects

    if name == get_active_project():
        if 'default' in projects.keys():
            active = 'default'
        else:
            active = projects.keys()[0]
        logger.info('changing active project from {} to {}'.format(name, active))
        set_active_project(active)

    logger.info('removing %s from projects' % name)

    del projects[name]
    _write_projects(projects)
    return projects


@dispatcher.add_method
def set_active_project(name):
    """Set active DSL project."""
    path = _get_projects_index_file()
    contents = util.read_yaml(path)
    if name not in contents['projects'].keys():
        raise ValueError('Project %s does not exist' % name)
    contents.update({'active_project': name})
    util.write_yaml(path, contents)
    get_db(active_db(), reconnect=True)  # change active database
    return name


def _load_project(name):
    db = init_db(_get_project_db(name))
    with db_session:
        project = db.Project.get().to_dict()

    db.disconnect()
    del project['id']
    return project


def _load_projects():
    """load list of collections."""
    path = _get_projects_index_file()
    projects = util.read_yaml(path).get('projects')
    if not projects:
        projects = {}

    return projects


def _write_projects(projects):
    """write list of collections to file."""
    path = _get_projects_index_file()
    contents = util.read_yaml(path)
    contents.update({'projects': projects})
    util.write_yaml(path, contents)


def _get_project_dir():
    return get_projects(expand=True)[get_active_project()]['folder']


def _get_project_db(name):
    projects = _load_projects()
    if name not in projects.keys():
        raise ValueError('Project %s not found' % name)

    path = projects[name]['folder']
    if not os.path.isabs(path):
        path = os.path.join(util.get_projects_dir(), path)

    util.mkdir_if_doesnt_exist(path)
    return os.path.join(path, PROJECT_DB_FILE)


def _get_projects_index_file():
    return os.path.join(util.get_projects_dir(), PROJECT_INDEX_FILE)
