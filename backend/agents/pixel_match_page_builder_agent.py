from dataclasses import dataclass
from typing import List


@dataclass
class PixelMatchPageRequest:
    page_name: str
    reference_image: str
    output_path: str
    width: int = 1366
    height: int = 640
    keep_fixed_header: bool = True


@dataclass
class PixelMatchPageResult:
    page_name: str
    output_path: str
    rules: List[str]
    required_assets: List[str]
    next_steps: List[str]


class PixelMatchPageBuilderAgent:

    def build_plan(self, request: PixelMatchPageRequest) -> PixelMatchPageResult:
        return PixelMatchPageResult(
            page_name=request.page_name,
            output_path=request.output_path,
            rules=[
                "Use reference image as source of truth.",
                "Do not redesign.",
                "Keep page size exact.",
                "Convert all readable text into HTML text.",
                "Use images only for logo, icons, thumbnails and backgrounds.",
                "Use fixed CSS positions for pixel match.",
                "Keep KisanMitraAI logo unchanged.",
                "Keep fixed header/menu unless user says otherwise.",
                "Use placeholder asset paths where real assets are missing.",
                "Final output must be full replacement HTML.",
            ],
            required_assets=[
                "Official KisanMitraAI logo",
                "Reference screenshot",
                "Farm thumbnails",
                "Crop thumbnails",
                "Icons or icon font",
            ],
            next_steps=[
                "Place reference image in frontend/assets.",
                "Create HTML at requested output path.",
                "Use 1366x640 fixed canvas.",
                "Compare browser screenshot with reference.",
                "Adjust spacing until pixel matched.",
            ],
        )


if __name__ == "__main__":
    agent = PixelMatchPageBuilderAgent()
    result = agent.build_plan(
        PixelMatchPageRequest(
            page_name="farmer-dashboard",
            reference_image="frontend/assets/farmer-dashboard-reference-1366x640.png",
            output_path="frontend/kisanmitra-web-ui/farmer-dashboard.html",
        )
    )
    print(result)