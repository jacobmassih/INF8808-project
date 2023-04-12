def get_hover_template_viz1(mode):
    return "<b>%{y} </b>" + f"<span>{mode}</span>"

def get_hover_template_missed_shots_viz5():
    return "<br>".join(
      [  "<b>%{x}</b> missed shots",
        "<extra></extra>"]
    )

def get_hover_template_goals_viz5():
    return "<br>".join(
      [  "<b>%{x}</b> goals",
        "<extra></extra>"]
    )

