
"""
**************************************************************
*  Project: user information                                 *
*  Developer: @TheEsmaeil - @ImEsmaeil1                      *
*  Version: 1.0.1                                            *
*                                                            *
*  Description:                                              *
*  This bot displays its user information                    *
*                                                            *
*  Contact:                                                  *
*  Email: info@viraigame.ir - info@codeepic.ir               *
*  Link:  viraigame.ir - codeepic.ir                         *
*                                                            *
*  Last Updated: 2024/05/15 - 10:21                          *
**************************************************************
"""

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = '' # Token Ra Vared konid

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    username = user.username
    user_id = user.id
    first_name = user.first_name

    message = f"""😐Your user information :

@{username}
Id: `{user_id}`
First: {first_name}
Lang: fa

Join : @ViraiCode"""

    await update.message.reply_text(message, parse_mode='MarkdownV2')

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == '__main__':
    main()


"""
**************************************************************
*  Project: user information                                 *
*  Developer: @TheEsmaeil - @ImEsmaeil1                      *
*  Version: 1.0.1                                            *
*                                                            *
*  Description:                                              *
*  This bot displays its user information                    *
*                                                            *
*  Contact:                                                  *
*  Email: info@viraigame.ir - info@codeepic.ir               *
*  Link:  viraigame.ir - codeepic.ir                         *
*                                                            *
*  Last Updated: 2024/05/15 - 10:21                          *
**************************************************************
"""
