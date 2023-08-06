import logging
import os
import pandas as pd
import time
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variable to keep track of the progress
progress = 0


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Send an Excel file to process.')


def process_excel(update: Update, context: CallbackContext) -> None:
    # Get the file sent by the user
    file = update.message.document.get_file()

    # Make sure only one Excel file is processed at a time
    if context.chat_data.get('processing', False):
        update.message.reply_text('Processing is already in progress. Please wait for the current process to finish.')
        return

    # Mark the start of processing
    context.chat_data['processing'] = True

    # Download the file to local storage
    file_path = os.path.join('downloads', file.file_path.split('/')[-1])
    file.download(file_path)

    try:
        # Call the function to elaborate the Excel file
        process_progress(update, context, file_path)
    except Exception as e:
        update.message.reply_text(f'An error occurred: {str(e)}')

    # Mark the end of processing
    context.chat_data['processing'] = False


def process_progress(update: Update, context: CallbackContext, file_path: str) -> None:
    global progress
    progress = 0

    # Read the Excel file
    df = pd.read_excel(file_path)

    # Get the total number of rows
    total_rows = len(df)

    # Process the data (Example: Updating the 'progress' column with a percentage)
    for i in range(total_rows):
        df.at[i, 'progress'] = (i + 1) / total_rows * 100
        progress = int((i + 1) / total_rows * 100)

        # Simulate some processing time (you can replace this with your actual processing logic)
        time.sleep(0.1)

        # Display different options at different progress intervals
        if progress % 10 == 0:  # Display options every 10% progress
            message = f"Solved: {progress}\nRate: 2.3739750366694534\nCrashes: 0\nTimedOUT Captcha reuests: 117\nWrong Captchas: 137\nMain request timeouts: 67\nAlive threads: 37"
            update.message.reply_text(message)

    # Save the elaborated file
    processed_file_path = file_path.replace('.xlsx', '_processed.xlsx')
    df.to_excel(processed_file_path, index=False)

    # Send the elaborated file
    with open(processed_file_path, 'rb') as f:
        update.message.reply_document(f, caption='Here is the elaborated Excel file.')

    # Delete the temporary files
    os.remove(file_path)
    os.remove(processed_file_path)


def progress_update(update: Update, context: CallbackContext) -> None:
    global progress
    update.message.reply_text(f'Progress: {progress}%')


def main() -> None:
    # Set up the Telegram bot
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")
    dispatcher = updater.dispatcher

    # Register the handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(
        MessageHandler(Filters.document.mime_type("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"),
                       process_excel))
    dispatcher.add_handler(CommandHandler("progress", progress_update))

    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
