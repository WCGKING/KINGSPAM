import asyncio
import os
import sys
import git
from telethon import events
from .. import UstaD, UstaD2, UstaD3, UstaD4, UstaD5, UstaD6, UstaD7, UstaD8, UstaD9, UstaD10, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

# -- Constants -- #
IS_SELECTED_DIFFERENT_BRANCH = (
    "looks like a custom branch {branch_name} "
    "is being used:\n"
    "in this case, Updater is unable to identify the branch to be updated."
    "please check out to an official branch, and re-start the updater."
)
OFFICIAL_UPSTREAM_REPO = "https://github.com/dangerousjatt/SpamBot-2.0"
BOT_IS_UP_TO_DATE = "**The 𝐒𝐏𝐀𝐌𝐁𝐎𝐓** is up-to-date sur."
NEW_BOT_UP_DATE_FOUND = (
    "new update found for {branch_name}\n"
    "changelog: \n\n{changelog}\n"
    "updating your 𝐒𝐏𝐀𝐌𝐁𝐎𝐓 ..."
)
NEW_UP_DATE_FOUND = "New update found for {branch_name}\n" "`updating your 𝐒𝐏𝐀𝐌𝐁𝐎𝐓...`"
REPO_REMOTE_NAME = "temponame"
IFFUCI_ACTIVE_BRANCH_NAME = "master"
DIFF_MARKER = "HEAD..{remote_name}/{branch_name}"
NO_HEROKU_APP_CFGD = "no heroku application found, but a key given? 😕 "
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/master"
RESTARTING_APP = "re-starting heroku application"
# -- Constants End -- #

@UstaD.on(
    events.NewMessage(pattern="^/update", func=lambda e: e.sender_id in SMEX_USERS)
)
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = " 🔰𝐔𝐏𝐃𝐀𝐓𝐈𝐍𝐆 𝐘𝐎𝐔𝐑 𝐒𝐏𝐀𝐌𝐁𝐎𝐓🔰....\n𝐓𝐘𝐏𝐄 /𝐩𝐢𝐧𝐠 𝐀𝐅𝐓𝐄𝐑 𝟓 𝐌𝐈𝐍𝐒 𝐓𝐎 𝐂𝐇𝐄𝐂𝐊 𝐈𝐅 𝐈'𝐌 𝐎𝐍"
        await e.reply(text, parse_mode=None, link_preview=None)


@UstaD.on(
    events.NewMessage(pattern="^/update", func=lambda e: e.sender_id in SMEX_USERS)
)
async def updater(message):
    try:
        repo = git.Repo()
    except git.exc.InvalidGitRepositoryError as e:
        repo = git.Repo.init()
        origin = repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
        origin.fetch()
        repo.create_head(IFFUCI_ACTIVE_BRANCH_NAME, origin.refs.master)
        repo.heads.master.checkout(True)

    active_branch_name = repo.active_branch.name
    if active_branch_name != IFFUCI_ACTIVE_BRANCH_NAME:
        await message.edit(
            IS_SELECTED_DIFFERENT_BRANCH.format(branch_name=active_branch_name)
        )
        return False

    try:
        repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
    except Exception as e:
        print(e)

    temp_upstream_remote = repo.remote(REPO_REMOTE_NAME)
    temp_upstream_remote.fetch(active_branch_name)

    changelog = generate_change_log(
        repo,
        DIFF_MARKER.format(
            remote_name=REPO_REMOTE_NAME, branch_name=active_branch_name
        ),
    )

    if not changelog:
        await message.edit("`Updation in Progress......`")
        await asyncio.sleep(5)

    message_one = NEW_BOT_UP_DATE_FOUND.format(
        branch_name=active_branch_name, changelog=changelog
    )
    message_two = NEW_UP_DATE_FOUND.format(branch_name=active_branch_name)

    if len(message_one) > 4095:
        with open("change.log", "w+", encoding="utf8") as out_file:
            out_file.write(str(message_one))
        await UstaD.send_message(
            message.chat_id, document="change.log", caption=message_two
        )
        os.remove("change.log")
    else:
        await message.edit(message_one)

    temp_upstream_remote.fetch(active_branch_name)
    repo.git.reset("--hard", "FETCH_HEAD")

    if HEROKU_API_KEY is not None:
        import heroku3

        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_applications = heroku.apps()
        if len(heroku_applications) >= 1:
            if HEROKU_APP_NAME is not None:
                heroku_app = None
                for i in heroku_applications:
                    if i.name == HEROKU_APP_NAME:
                        heroku_app = i
                if heroku_app is None:
                    await message.edit(
                        "Invalid APP Name. Please set the name of your bot in heroku in the var `HEROKU_APP_NAME.`"
                    )
                    return
                heroku_git_url = heroku_app.git_url.replace(
                    "https://", "https://api:" + HEROKU_API_KEY + "@"
                )
                if "heroku" in repo.remotes:
                    remote = repo.remote("heroku")
                    remote.set_url(heroku_git_url)
                else:
                    remote = repo.create_remote("heroku", heroku_git_url)
                asyncio.get_event_loop().create_task(
                    deploy_start(UstaD, message, HEROKU_GIT_REF_SPEC, remote)
                )

            else:
                await message.edit(
                    "Please create the var `HEROKU_APP_NAME` as the key and the name of your bot in heroku as your value."
                )
                return
        else:
            await message.edit(NO_HEROKU_APP_CFGD)
    else:
        await message.edit("No heroku api key found in `HEROKU_API_KEY` var")


def generate_change_log(git_repo, diff_marker):
    out_put_str = ""
    d_form = "%d/%m/%y"
    for repo_change in git_repo.iter_commits(diff_marker):
        out_put_str += f"•[{repo_change.committed_datetime.strftime(d_form)}]: {repo_change.summary} <{repo_change.author}>\n"
    return out_put_str


async def deploy_start(UstaD, message, refspec, remote):
    await message.edit(RESTARTING_APP)
    await message.edit(
        "Updated your 𝐒𝐏𝐀𝐌𝐁𝐎𝐓 successfully sur!!!\nNow type `/ping` after 5 mins to check if I'm on🚶😏"
    )
    await remote.push(refspec=refspec)
    await UstaD.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
