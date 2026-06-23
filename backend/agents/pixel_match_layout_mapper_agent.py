from dataclasses import dataclass
from typing import List


@dataclass
class LayoutBlock:
    block_name: str
    x: int
    y: int
    width: int
    height: int
    border_radius: int
    shadow: str
    background: str


@dataclass
class LayoutMapRequest:
    page_name: str
    reference_image: str
    canvas_width: int = 1366
    canvas_height: int = 640


@dataclass
class LayoutMapResult:
    page_name: str
    layout_blocks: List[LayoutBlock]
    generated_html: List[str]
    notes: List[str]


class PixelMatchLayoutMapperAgent:

    def map_layout(self, request: LayoutMapRequest):

        blocks = [

            LayoutBlock(
                block_name="sidebar",
                x=0,
                y=0,
                width=260,
                height=640,
                border_radius=0,
                shadow="none",
                background="#ffffff"
            ),

            LayoutBlock(
                block_name="header",
                x=260,
                y=0,
                width=1106,
                height=98,
                border_radius=0,
                shadow="0 1px 4px rgba(0,0,0,.08)",
                background="#ffffff"
            ),

            LayoutBlock(
                block_name="stats_row",
                x=280,
                y=115,
                width=1050,
                height=120,
                border_radius=18,
                shadow="0 4px 12px rgba(0,0,0,.08)",
                background="#ffffff"
            ),

            LayoutBlock(
                block_name="farms_card",
                x=280,
                y=255,
                width=500,
                height=375,
                border_radius=18,
                shadow="0 4px 12px rgba(0,0,0,.08)",
                background="#ffffff"
            ),

            LayoutBlock(
                block_name="crop_snapshot",
                x=800,
                y=255,
                width=500,
                height=375,
                border_radius=18,
                shadow="0 4px 12px rgba(0,0,0,.08)",
                background="#ffffff"
            )

        ]

        html = []

        for block in blocks:

            html.append(
                f'''
<div style="
position:absolute;
left:{block.x}px;
top:{block.y}px;
width:{block.width}px;
height:{block.height}px;
background:{block.background};
border-radius:{block.border_radius}px;
box-shadow:{block.shadow};
">
</div>
'''.strip()
            )

        return LayoutMapResult(
            page_name=request.page_name,
            layout_blocks=blocks,
            generated_html=html,
            notes=[
                "Layout mapper active.",
                "Current version uses manual layout definitions.",
                "Future version will detect containers automatically.",
                "Future version will detect buttons and cards from screenshots."
            ]
        )


if __name__ == "__main__":

    agent = PixelMatchLayoutMapperAgent()

    result = agent.map_layout(
        LayoutMapRequest(
            page_name="farmer-dashboard",
            reference_image="frontend/assets/farmer-dashboard-reference-1366x640.png"
        )
    )

    print(result)