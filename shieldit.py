import pydantic

SHIELD_DEFAULT_COLORS = [
    "red",
    "blue",
    "brightgreen",
    "green",
    "yellow",
    "greenyellow",
    "orange",
    "red",
    "blue",
    "lightgrey",
]

CSS_DEFAULT_COLORS = list(
    map(
        str.title,
        [
            "black",
            "silver",
            "gray",
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "green",
            "lime",
            "olive",
            "yellow",
            "navy",
            "blue",
            "teal",
            "aqua",
        ],
    )
)


class ShieldBadge:
    def __init__(
        self,
        label: str,
        message: str,
        color: str,
        logo: str = None,
        style: str = None,
        label_color: str = None,
    ):
        self.label: str = label
        self.message = message
        self.color = color
        self.logo = logo
        self.style = style
        self.label_color = label_color
        self.link: str = self._create_link()

    @staticmethod
    def _encode_string(string: str):
        return string.replace("-", "--").replace("_", "__").replace(" ", "_")

    def _create_link(self) -> str:
        encoded_label = self._encode_string(self.label)
        encoded_message = self._encode_string(self.message)
        encoded_color = (
            self.color
            if self.color in SHIELD_DEFAULT_COLORS
            else pydantic.color.Color(self.color).as_hex().replace("#", "")
        )
        return (
            f"https://img.shields.io/badge/"
            + "-".join((encoded_label, encoded_message, encoded_color))
            # + "?"
            # + f"&style={self.style}"
            # if self.style not in (None, "")
            # else "" + f"&logo={self.logo}"
            # if self.logo not in (None, "")
            # else ""
        )

    def get_link(self) -> str:
        return self.link
