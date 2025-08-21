from pathlib import Path
import shutil

# INIT_CONF_DIR = Path(__file__).resolve().parent.parent.parent / "config"
INIT_CONF_DIR = Path(__file__).resolve().parent.parent / "config"

def get_usr_conf_dir():
    USR_CONF_DIR = Path.home() / "qChronolyze"
    USR_CONF_DIR.mkdir(parents=True, exist_ok=True)
    return USR_CONF_DIR


def get_usr_conf_file():
    USR_CONF_DIR = get_usr_conf_dir()
    USR_CONF_FILE = USR_CONF_DIR / "cnf.json"

    if not USR_CONF_FILE.is_file():
        # from ..constants import INIT_SORTER_PATH
        INIT_CONF_FILE = INIT_CONF_DIR / "cnf.json"
        shutil.copy2(INIT_CONF_FILE, USR_CONF_FILE)

    return USR_CONF_FILE
    

def get_usr_sorter_path():
    USR_CONF_DIR = get_usr_conf_dir()
    USR_SORTER_PATH = USR_CONF_DIR / "sorter.json"

    if not USR_SORTER_PATH.is_file():
        # from ..constants import INIT_SORTER_PATH
        INIT_SORTER_PATH = INIT_CONF_DIR / "sorter.json"
        shutil.copy2(INIT_SORTER_PATH, USR_SORTER_PATH)

    return USR_SORTER_PATH




def get_usr_surord_path():
    USR_CONF_DIR = get_usr_conf_dir()
    USR_SURORD_PATH = USR_CONF_DIR / "surOrd.tsv"

    if not USR_SURORD_PATH.is_file():
        INIT_SURORD_PATH = INIT_CONF_DIR / "surOrd.tsv"
        # from ..constants import INIT_SURORD_PATH
        shutil.copy2(INIT_SURORD_PATH, USR_SURORD_PATH)
    
    return USR_SURORD_PATH

    
def get_usr_posser_path():
    USR_CONF_DIR = get_usr_conf_dir()
    USR_POSSER_PATH = USR_CONF_DIR / 'posSerDict.json'

    if not USR_POSSER_PATH.is_file():
        INIT_POSSER_PATH = INIT_CONF_DIR / 'posSerDict.json'
        # from ..constants import INIT_POSSER_PATH
        shutil.copy2(INIT_POSSER_PATH, USR_POSSER_PATH)
    
    return USR_POSSER_PATH