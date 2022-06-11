
from bokeh.io import export_svgs
from bokeh.plotting import figure, show
from bokeh.models import (ColumnDataSource,HoverTool,)

def plot_loss_per_epoch(history, model_name=None, file_name=None):
    if model_name is None:
        model_name = ""
    else:
        model_name += ": "

    p = figure(
        plot_width=600,
        plot_height=400,
        title=f"{model_name}Loss per Epoch",
        x_axis_label="# Epochs",
        y_axis_label="Loss",
    )

    source = ColumnDataSource(
        data=dict(
            index=range(len(history.history["loss"])),
            loss=history.history["loss"],
            val_loss=history.history["val_loss"],
        )
    )
    _ = p.line(
        x="index",
        y="loss",
        color="black",
        line_dash="dotted",
        legend_label="Training Loss",
        source=source,
    )
    _ = p.line(
        x="index",
        y="val_loss",
        color="coral",
        line_width=1.5,
        legend_label="Validation Loss",
        source=source,
    )

    p.xgrid.grid_line_color = None
    p.legend.label_text_font_size = "8pt"
    p.legend.location = "top_right"
    p.legend.click_policy = "hide"
    p.title.align = "center"
    p.title.text_font_size = "12pt"

    p.add_tools(
        HoverTool(
            tooltips=[
                ("epoch", "@index"),
                ("training loss", "@loss"),
                ("validation loss", "@val_loss"),
            ]
        )
    )
    show(p)

    if file_name is not None:
        p.output_backend = "svg"
        _ = export_svgs(p, filename=file_name)
