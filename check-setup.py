import napari

with napari.gui_qt():
    viewer = napari.Viewer()
    _ = viewer.open('lessons/data/nuclei.tif')
    viewer.dims.set_point(0, 29)
