import os

from dotenv import load_dotenv
from dynaconf import Dynaconf, Validator
import logging

load_dotenv(".env")
logger = logging.getLogger(__name__)

DEFAULT_ENVIRONMENT = "default"
REQUIRED_CONFIG = [
    "db_host",
    "db_port",
    "db_name",
    "db_user",
    "db_pool_recycle",
]

config_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../config"))

# If not running in GKE, use `local.env` to override certain settings
running_in_gke = os.environ.get("KUBERNETES_SERVICE_HOST") is not None
if not running_in_gke:
    local_env_file = os.path.join(config_directory, "local.env")
    logger.info(f"Running outside of GKE so applying settings in {local_env_file}")
    load_dotenv(local_env_file)

config = Dynaconf(
    settings_files=[config_directory + "/ignite_data_assessment.yaml"],
    load_dotenv=True,
    envvar_prefix=False,
    environments=True,
    env_switcher="ENVIRONMENT",
    env=DEFAULT_ENVIRONMENT,
    validators=[Validator(*REQUIRED_CONFIG, must_exist=True)],
    apply_default_on_none=True,
)

config.validators.validate_all()
