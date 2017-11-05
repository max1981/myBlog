from django import template

register = template.Library()

@register.assignment_tag
def pagination(current_page,paginator,num_of_displaypage=10,num_of_backpage=4):
    num_of_frontpage = num_of_displaypage-num_of_backpage-3
    html = ''

    if paginator.num_pages <= num_of_displaypage:
        for i in range(1,paginator.num_pages+1):
            html += '<li><a href="?page=%s">%s</a></li>'%(i,i)
        return html
    elif current_page.number <= num_of_displaypage-num_of_backpage:
        for i in range(1,num_of_displaypage+1):
            html += '<li><a href="?page=%s">%s</a></li>' % (i, i)
        return html
    elif num_of_displaypage-num_of_frontpage <= current_page.number <= paginator.num_pages-num_of_backpage :
        html = '''
            <li><a href="?page=1">1</a></la>
            <li class="disabled"><a href="?page=1">...</a></la>

        '''
        for i in range(current_page.number-num_of_frontpage,current_page.number+num_of_backpage+1):
            html+='<li><a href="?page=%s">%s</a></la>'%(i,i)
        return html
    else:
        html = '''
                <li><a href="?page=1">1</a></la>
                <li class="disabled"><a href="?page=1">...</a></la>

            '''
        for i in range(paginator.num_pages - num_of_backpage - num_of_frontpage, paginator.num_pages + 1):
            html += '<li><a href="?page=%s">%s</a></la>' % (i, i)
        return html
