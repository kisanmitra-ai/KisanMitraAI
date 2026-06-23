from dataclasses import dataclass
from typing import List


@dataclass
class TextLayer:
    text: str
    x: int
    y: int
    font_size: int
    font_weight: str
    color: str
    width: int
    height: int
    alignment: str


@dataclass
class PixelMatchTextMapRequest:
    page_name: str
    reference_image: str
    canvas_width: int = 1366
    canvas_height: int = 640


@dataclass
class PixelMatchTextMapResult:
    page_name: str
    detected_layers: List[TextLayer]
    generated_html: List[str]
    notes: List[str]


class PixelMatchTextMapperAgent:

    def map_text(self, request: PixelMatchTextMapRequest) -> PixelMatchTextMapResult:

        sample_layers = [

            TextLayer(
                text="Welcome Back, Ranjan!",
                x=357,
                y=28,
                font_size=22,
                font_weight="700",
                color="#1B1B1B",
                width=280,
                height=28,
                alignment="left"
            ),

            TextLayer(
                text="Village: Basbona, Nadia, West Bengal",
                x=360,
                y=68,
                font_size=14,
                font_weight="400",
                color="#555555",
                width=260,
                height=18,
                alignment="left"
            ),

            TextLayer(
                text="My Farms",
                x=324,
                y=275,
                font_size=16,
                font_weight="600",
                color="#1B1B1B",
                width=100,
                height=20,
                alignment="left"
            ),

            TextLayer(
                text="Crop Health Snapshot",
                x=852,
                y=275,
                font_size=16,
                font_weight="600",
                color="#1B1B1B",
                width=180,
                height=20,
                alignment="left"
            )

        ]

        html_blocks = []

        for layer in sample_layers:

            html_blocks.append(
                f'''
<div style="
position:absolute;
left:{layer.x}px;
top:{layer.y}px;
width:{layer.width}px;
height:{layer.height}px;
font-size:{layer.font_size}px;
font-weight:{layer.font_weight};
color:{layer.color};
text-align:{layer.alignment};
">
{layer.text}
</div>
'''.strip()
            )

        return PixelMatchTextMapResult(
            page_name=request.page_name,
            detected_layers=sample_layers,
            generated_html=html_blocks,
            notes=[
                "Current version uses manual layer mapping.",
                "Future version will read OCR output automatically.",
                "Future version will estimate exact font sizes.",
                "Future version will generate complete HTML overlays."
            ]
        )


if __name__ == "__main__":

    agent = PixelMatchTextMapperAgent()

    result = agent.map_text(
        PixelMatchTextMapRequest(
            page_name="farmer-dashboard",
            reference_image="frontend/assets/farmer-dashboard-reference-1366x640.png"
        )
    )

    print(result)