from markdownify import markdownify


def test_markdownify(file_regression):
    html = '''<h1>Test Data</h1>

    <p>Mussum Ipsum, cacilds vidis litro abertis. Diuretics paradis
    num copo e motivis de denguis. Manduma pindureta quium dia nois paga.</p>

    <a href="http://nowhere">this is a link</a>
    '''
    markdown = markdownify(html)
    file_regression.check(markdown, extension=".md")
