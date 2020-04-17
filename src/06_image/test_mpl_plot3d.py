from mpl_plot3d import generate_3d_plot
from io import BytesIO


def test_generate_3d_plot(image_regression):
    buffer = BytesIO()
    generate_3d_plot(buffer)
    image_regression.check(buffer.getvalue())
