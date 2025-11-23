from aiogram import Dispatcher

from handlers.start import router as start_router
from handlers.info import router as info_router
from handlers.catalog_OGE import router as OGE_router
from handlers.catalog_EGE import router as EGE_router


def register_routes(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(info_router)
    dp.include_router(OGE_router)
    dp.include_router(EGE_router)