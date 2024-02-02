from sufficient.frames import *


class App:
    name = "GM, World"
    description = "Greeting to the world of frames"
    image = "{uri}/static/home.png"
    uri = "{uri}"
    start = "PageHome"


class PageHome:
    def view(self, action: Action, result: ActionResult):
        return ImageFile("home.png")

    def btn_explore(self, action: Action):
        c = FarcasterClient()
        actor_user = c.neynar_get_user(action.actor)
        pfp_url = actor_user["pfp_url"]
        display_name = actor_user["display_name"]
        return "PageFeatures", ActionResult(pfp_url=pfp_url, display_name=display_name)


class PageFeatures:
    def view(self, action: Action, result: ActionResult):
        if "PageHome.btn_explore" == action.source:
            return SvgTemplate("features.svg", result)
        elif "PageFeatures.btn_casters" == action.source:
            return SvgTemplate("features_fc_data.svg", result)
        elif "PageFeatures.btn_chain_data" == action.source:
            return SvgTemplate("features_chain_data.svg", result)
        elif "PageFeatures.btn_reactions" == action.source:
            return SvgTemplate("features_reactions.svg", result)
        else:
            return SvgFile("unexpected.svg")

    def btn_casters(self, action: Action):
        c = FarcasterClient()
        cast_actions = c.neynar_get_cast_actions(action.cast, action.actor)
        return "PageFeatures", ActionResult(data=cast_actions)

    def btn_reactions(self, action: Action):
        return "PageFeatures"

    def btn_chain_data(self, action: Action):
        return "PageFeatures"

    def btn_usage(self, action: Action):
        return "PageUsage"


class PageUsage:
    def view(self, action: Action, result: ActionResult):
        return SvgFile("usage.svg")

    def btn_previous(self, action: Action):
        return "PageFeatures"

    def btn_next(self, action: Action):
        return "PageEnd"


class PageEnd:
    def view(self, action: Action, result: ActionResult):
        return ImageFile("end.png")

    def btn_back_home(self, action: Action):
        return "PageHome"

    def btn_github(self, action: Action):
        return "PageHome"
