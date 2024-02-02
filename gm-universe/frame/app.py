from sufficient.frames import *


class App:
    name = "GM Universe"
    description = "Greetings from your first frame app using sufficient-py"
    image = "{uri}/static/home.png"
    uri = "{uri}"
    start = "PageHome"


class PageHome:
    def view(self, action: Action, result: ActionResult):
        return ImageFile("home.png")

    def btn_explore(self, action: Action):
        return "PageFeatures"


class PageFeatures:
    def view(self, action: Action, result: ActionResult):
        if "PageHome.btn_explore" == action.source:
            return ImageFile("features.png")
        elif "PageFeatures.btn_casters" == action.source:
            return SvgTemplate("features_casters.svg", result)
        elif "PageFeatures.btn_reactions" == action.source:
            return SvgTemplate("features_reactions.svg", result)
        elif "PageFeatures.btn_chain_data" == action.source:
            return SvgTemplate("features_chaindata.svg", result)
        else:
            return ImageFile("unexpected.png")

    def btn_casters(self, action: Action):
        c = FarcasterClient()
        users = c.neynar_get_users_bulk([action.actor, action.caster])
        actor_pfp = users[0]["pfp_url"]
        actor_name = users[0]["display_name"]
        caster_pfp = users[1]["pfp_url"]
        caster_name = users[1]["display_name"]
        return "PageFeatures", ActionResult(actor_name=actor_name,
                                            actor_pfp=actor_pfp,
                                            caster_name=caster_name,
                                            caster_pfp=caster_pfp)

    def btn_reactions(self, action: Action):
        c = FarcasterClient()
        cast = c.neynar_get_cast_actions(action.cast, action.actor)
        likes = cast["reactions"]["likes"]
        recasts = cast["reactions"]["recasts"]
        num_replies = cast["replies"]["count"]
        return "PageFeatures", ActionResult(num_likes=len(likes),
                                            num_recasts=len(recasts),
                                            num_replies=num_replies)

    def btn_chain_data(self, action: Action):
        c = FarcasterClient()
        users = c.neynar_get_users_bulk([action.actor, action.caster])
        actor_addresses = users[0]["verifications"]
        actor_name = users[0]["display_name"]
        caster_addresses = users[1]["verifications"]
        caster_name = users[1]["display_name"]
        return "PageFeatures", ActionResult(caster_name=caster_name,
                                            caster_addresses=caster_addresses,
                                            actor_name=actor_name,
                                            actor_addresses=actor_addresses)

    def btn_how_it_works(self, action: Action):
        return "PageHowItWorks"


class PageHowItWorks:
    def view(self, action: Action, result: ActionResult):
        if "PageFeatures.btn_how_it_works" == action.source:
            return ImageFile("howitworks.png")
        elif "PageHowItWorks.btn_programming" == action.source:
            return ImageFile("howitworks_programming.png")
        elif "PageHowItWorks.btn_deploy" == action.source:
            return ImageFile("howitworks_deploy.png")
        else:
            return ImageFile("unexpected.png")

    def btn_programming(self, action: Action):
        return "PageHowItWorks"

    def btn_deploy(self, action: Action):
        return "PageHowItWorks"

    def goto_github(self, action: Action):
        return "https://github.com/briceyan/frame-app-examples/tree/main/gm"
