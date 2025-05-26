import asyncio
import shlex
from typing import Tuple

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

import config
from ..logging import LOGGER


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())


def git():
    REPO_LINK = config.UPSTREAM_REPO
    if config.GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@{TEMP_REPO}"
    else:
        UPSTREAM_REPO = config.UPSTREAM_REPO

    try:
        repo = Repo()
        LOGGER(__name__).info("Git Client Found [VPS DEPLOYER]")
    except InvalidGitRepositoryError:
        LOGGER(__name__).info("No valid Git repo found, initializing...")
        repo = Repo.init()

        try:
            origin = repo.create_remote("origin", UPSTREAM_REPO)
        except GitCommandError:
            origin = repo.remotes.origin
            LOGGER(__name__).info("Remote 'origin' already exists.")

        try:
            origin.fetch()
        except GitCommandError as e:
            LOGGER(__name__).error(f"Failed to fetch from origin: {e}")
            return

        if config.UPSTREAM_BRANCH not in origin.refs:
            LOGGER(__name__).error(f"Branch '{config.UPSTREAM_BRANCH}' not found in remote.")
            return

        try:
            repo.create_head(config.UPSTREAM_BRANCH, origin.refs[config.UPSTREAM_BRANCH])
        except Exception:
            LOGGER(__name__).info(f"Branch '{config.UPSTREAM_BRANCH}' already exists.")

        repo.heads[config.UPSTREAM_BRANCH].set_tracking_branch(origin.refs[config.UPSTREAM_BRANCH])
        repo.heads[config.UPSTREAM_BRANCH].checkout(True)

        try:
            origin.pull(config.UPSTREAM_BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")

        LOGGER(__name__).info("Installing requirements...")
        install_req("pip3 install --no-cache-dir -r requirements.txt")

    LOGGER(__name__).info("Fetching updates from upstream repository...")
        
