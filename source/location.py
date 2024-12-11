"""Choose location from input file."""

from enum import Enum, auto
from typing import Self

import pandas as pd

from source.scrape import input_location_filepath


class Location(Enum):
    ABERPORTH = auto()
    ARMAGH = auto()
    BALLYPATRICK_FOREST = auto()
    BRADFORD = auto()
    BRAEMAR_NO_2 = auto()
    CAMBORNE = auto()
    CAMBRIDGE_NIAB = auto()
    CARDIFF_BUTE_PARK = auto()
    CHIVENOR = auto()
    CWMYSTWYTH = auto()
    DUNSTAFFNAGE = auto()
    DURHAM = auto()
    EASTBOURNE = auto()
    ESKDALEMUIR = auto()
    HEATHROW = auto()
    HURN = auto()
    LERWICK = auto()
    LEUCHARS = auto()
    LOWESTOFT_MONCKTON_AVENUE = auto()
    MANSTON = auto()
    NAIRN_DRUIM = auto()
    NEWTON_RIGG = auto()
    OXFORD = auto()
    PAISLEY = auto()
    RINGWAY = auto()
    ROSS_ON_WYE = auto()
    SHAWBURY = auto()
    SHEFFIELD = auto()
    SOUTHAMPTON_MAYFLOWER_PARK = auto()
    STORNOWAY_AIRPORT = auto()
    SUTTON_BONINGTON = auto()
    TIREE = auto()
    VALLEY = auto()
    WADDINGTON = auto()
    WHITBY = auto()
    WICK_AIRPORT = auto()
    YEOVILTON = auto()

    def __init__(self: Self):
        """Populate enum variable with correct web links."""

        # find df
        df = pd.read_csv(input_location_filepath)

        # populate all locations with web links
        self.ABERPORTH = self.find_web_link(df, "ABERPORTH")
        self.ARMAGH = self.find_web_link(df, "ARMAGH")
        self.BALLYPATRICK_FOREST = self.find_web_link(df, "BALLYPATRICK_FOREST")
        self.BRADFORD = self.find_web_link(df, "BRADFORD")
        self.BRAEMAR_NO_2 = self.find_web_link(df, "BRAEMAR_NO_2")
        self.CAMBORNE = self.find_web_link(df, "CAMBORNE")
        self.CAMBRIDGE_NIAB = self.find_web_link(df, "CAMBRIDGE_NIAB")
        self.CARDIFF_BUTE_PARK = self.find_web_link(df, "CARDIFF_BUTE_PARK")
        self.CHIVENOR = self.find_web_link(df, "CHIVENOR")
        self.CWMYSTWYTH = self.find_web_link(df, "CWMYSTWYTH")
        self.DUNSTAFFNAGE = self.find_web_link(df, "DUNSTAFFNAGE")
        self.DURHAM = self.find_web_link(df, "DURHAM")
        self.EASTBOURNE = self.find_web_link(df, "EASTBOURNE")
        self.ESKDALEMUIR = self.find_web_link(df, "ESKDALEMUIR")
        self.HEATHROW = self.find_web_link(df, "HEATHROW")
        self.HURN = self.find_web_link(df, "HURN")
        self.LERWICK = self.find_web_link(df, "LERWICK")
        self.LEUCHARS = self.find_web_link(df, "LEUCHARS")
        self.LOWESTOFT_MONCKTON_AVENUE = self.find_web_link(
            df, "LOWESTOFT_MONCKTON_AVENUE"
        )
        self.MANSTON = self.find_web_link(df, "MANSTON")
        self.NAIRN_DRUIM = self.find_web_link(df, "NAIRN_DRUIM")
        self.NEWTON_RIGG = self.find_web_link(df, "NEWTON_RIGG")
        self.OXFORD = self.find_web_link(df, "OXFORD")
        self.PAISLEY = self.find_web_link(df, "PAISLEY")
        self.RINGWAY = self.find_web_link(df, "RINGWAY")
        self.ROSS_ON_WYE = self.find_web_link(df, "ROSS_ON_WYE")
        self.SHAWBURY = self.find_web_link(df, "SHAWBURY")
        self.SHEFFIELD = self.find_web_link(df, "SHEFFIELD")
        self.SOUTHAMPTON_MAYFLOWER_PARK = self.find_web_link(
            df, "SOUTHAMPTON_MAYFLOWER_PARK"
        )
        self.STORNOWAY_AIRPORT = self.find_web_link(df, "STORNOWAY_AIRPORT")
        self.SUTTON_BONINGTON = self.find_web_link(df, "SUTTON_BONINGTON")
        self.TIREE = self.find_web_link(df, "TIREE")
        self.VALLEY = self.find_web_link(df, "VALLEY")
        self.WADDINGTON = self.find_web_link(df, "WADDINGTON")
        self.WHITBY = self.find_web_link(df, "WHITBY")
        self.WICK_AIRPORT = self.find_web_link(df, "WICK_AIRPORT")
        self.YEOVILTON = self.find_web_link(df, "YEOVILTON")

    def find_web_link(self: Self, df: pd.DataFrame, name: str) -> str:
        """Find web link from name."""
        web_link = df.loc[
            df["Name"]
            .str.upper()
            .str.replace("-", "_")
            .str.replace("\s", "_", regex=True)
            == name,
            "Data",
        ].iloc[0]

        return web_link
