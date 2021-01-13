

return render_to_string('nucleus/components/heading.html', {    
    'title': 'Title',
    'subtitle': 'Subtitle',
    'image': 'img/image.png', # Optional image
    'rounded': True, # Rounded corners, optional
    'initials': 'LV', # Optional text of the image is not available
    'background_color': 'red' # Optional background color
})


# Stat_items 
return render_to_string('nucleus/components/stat_item.html', {
    value: '5269',
    title: 'Units Sold',
    subtitle: 'Avg. 351 per week', 
    label: '-12%',
})

# Charts 
return render_to_string('nucleus/components/chart.html', {
    series: '{"labels": ["1", "2", "3"], "datasets": [{"data": [1, 2, 3]}]}', # JSON object
    height: 360,  # Optional 
})


# Singnals 
return render_to_string('nucleus/components/signed_number.html', {
    'value': 21.87,  # Value which will be compared
    'display': '$21.87 ',  # For example string with currency to display (django-money object)
})

# Progress 
return render_to_string('nucleus/components/progress.html', {
    'value': 32,  # Value in percent in this case it will be (style="width: 32%")
})


# Label 
return render_to_string('nucleus/components/progress.html', {
    'title': _('Active'),
    'class': 'success',  # Optional. Accepted values: success, info, error 
})