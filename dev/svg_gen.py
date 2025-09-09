'''Script that makes svg dots and arrow ends in different colors'''

color_names = ('darkolivegreen', 'cadetblue', 'chartreuse', 'cyan',
                        'coral','darkmagenta', 'mediumseagreen',
                        'purple', 'teal', 'hotpink', 'maroon',
                        'darkslateblue',
                        'darkgreen', 'mediumblue', 'darksalmon', 'springgreen',
                        'sienna', 'mediumspringgreen',
                        'gold', 'slateblue', 'deeppink', 'midnightblue', 'indianred',
                        'darkseagreen', 'blue', 'brown', 'mediumorchid',
                        'darkviolet', 'chocolate', 'navy', 'lightsalmon',
                        'darkturquoise', 'darkgoldenrod',
                        'mediumturquoise', 'limegreen', 'wheat', 'mediumpurple',
                        'lightgreen', 'green', 'olive', 'greenyellow',
                        'olivedrab', 'orange', 'forestgreen',
                        'palevioletred', 'darkorchid', 'violet', 'salmon',
                        'darkblue', 'turquoise',
                        'mediumvioletred', 'palegreen',
                        'orchid', 'burlywood', 'peru', 'seagreen',
                        'royalblue', 'mediumaquamarine', 'indigo', 'lime',
                        'cornflowerblue', 'blueviolet', 'aqua',
                        'slategray', 'saddlebrown', 'darkorange', 'moccasin',
                        'lawngreen', 'deepskyblue',
                        'dodgerblue', 'powderblue', 'darkcyan', 'steelblue',
                        'tan', 'mediumslateblue',
                        'sandybrown', 'goldenrod', 'yellowgreen')


template='''
                    <marker id='head_{color}' orient='auto' markerWidth='8' markerHeight='16' refX='0.1' refY='4'>
                        <path d='M0,0 V8 L4,4 Z' fill='{color}' />
                    </marker>
                    <marker id='dot_{color}' viewBox='0 0 10 10' refX='5' refY='5' markerWidth='5' markerHeight='5'>
                        <circle cx='5' cy='5' r='5' fill='{color}' />
                    </marker>'''

for color in  color_names:
    print(template.format(color=color))
