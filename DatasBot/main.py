from aiogram import Bot, Dispatcher, executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
token = '5918763059:AAEQaetx5xoz1v5jHmLPU8ms6aq4jtxziao'
storage = MemoryStorage()
bot = Bot(token = token)
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    data_str = State()
@dp.message_handler(commands=['start'])
async def Start(message:types.Message):
    await bot.send_message(chat_id = message.from_user.id,
                           text = 'Наш бот приветствует вас')
    await bot.send_message(chat_id = message.from_user.id,
                           text = 'Введите дату, чтобы узнать праздник. Пример ввода(01.01)')
    await UserState.data_str.set()
@dp.message_handler(state = UserState.data_str)
async def get_datas(message:types.Message, state: FSMContext):
    await state.update_data(data_str = message.text)
    data_result = await state.get_data()
    res = data_result["data_str"]
    await state.finish()
    with open('./Burthdays/datas.txt', 'r') as f:
        isline = False
        for line in f:
            if res in line:
                await bot.send_message(chat_id = message.from_user.id,
                                       text = line)
                isline = True
        if isline == False:
            await bot.send_message(chat_id = message.from_user.id,
                                       text = 'В этот день нету праздника')
            
                
                

if __name__ == '__main__':
    executor.start_polling(dp)