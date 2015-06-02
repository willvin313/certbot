"""Let's Encrypt constants."""
import logging

from acme import challenges


SETUPTOOLS_PLUGINS_ENTRY_POINT = "letsencrypt.plugins"
"""Setuptools entry point group name for plugins."""

CLI_DEFAULTS = dict(
    config_files=["/etc/letsencrypt/cli.ini"],
    verbose_count=-(logging.WARNING / 10),
    server="https://www.letsencrypt-demo.org/acme/new-reg",
    rsa_key_size=2048,
    rollback_checkpoints=0,
    config_dir="/etc/letsencrypt",
    work_dir="/var/lib/letsencrypt",
    no_verify_ssl=False,
    dvsni_port=challenges.DVSNI.PORT,
)
"""Defaults for CLI flags and `.IConfig` attributes."""


RENEWER_DEFAULTS = dict(
    renewer_config_file="/etc/letsencrypt/renewer.conf",
    renewal_configs_dir="/etc/letsencrypt/configs",
    archive_dir="/etc/letsencrypt/archive",
    live_dir="/etc/letsencrypt/live",
    renewer_enabled="yes",
    renew_before_expiry="30 days",
    deploy_before_expiry="20 days",
)
"""Defaults for renewer script."""


EXCLUSIVE_CHALLENGES = frozenset([frozenset([
    challenges.DVSNI, challenges.SimpleHTTPS])])
"""Mutually exclusive challenges."""


ENHANCEMENTS = ["redirect", "http-header", "ocsp-stapling", "spdy"]
"""List of possible :class:`letsencrypt.interfaces.IInstaller`
enhancements.

List of expected options parameters:
- redirect: None
- http-header: TODO
- ocsp-stapling: TODO
- spdy: TODO

"""


CONFIG_DIRS_MODE = 0o755
"""Directory mode for ``.IConfig.config_dir`` et al."""

ACCOUNTS_DIR = "accounts"
"""Directory where all accounts are saved."""

ACCOUNT_KEYS_DIR = "keys"
"""Directory where account keys are saved. Relative to `ACCOUNTS_DIR`."""

BACKUP_DIR = "backups"
"""Directory (relative to `IConfig.work_dir`) where backups are kept."""

CERT_KEY_BACKUP_DIR = "keys-certs"
"""Directory where all certificates and keys are stored (relative to
`IConfig.work_dir`). Used for easy revocation."""

CERT_DIR = "certs"
"""Directory (relative to `IConfig.config_dir`) where CSRs are saved."""

IN_PROGRESS_DIR = "IN_PROGRESS"
"""Directory used before a permanent checkpoint is finalized (relative to
`IConfig.work_dir`)."""

KEY_DIR = "keys"
"""Directory (relative to `IConfig.config_dir`) where keys are saved."""

TEMP_CHECKPOINT_DIR = "temp_checkpoint"
"""Temporary checkpoint directory (relative to `IConfig.work_dir`)."""

REC_TOKEN_DIR = "recovery_tokens"
"""Directory where all recovery tokens are saved (relative to
`IConfig.work_dir`)."""


RENEWER_CONFIG_FILENAME = "renewer.conf"
"""Renewer config file name (relative to `IConfig.config_dir`)."""


NETSTAT = "/bin/netstat"
"""Location of netstat binary for checking whether a listener is already
running on the specified port (Linux-specific)."""
