from bezier import quadratic_bezier


def test_bezier_regression(num_regression):
    x, y = quadratic_bezier((1, 1), (0, 0), (1, 0))
    num_regression.check({'x': x, 'y': y})
