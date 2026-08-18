
def domain_profiles(source="domain-profiles.txt", model='N216'):
    """ 
    Get details of spatial domains
    """
    with open(source,'r') as f:
        lines = f.readlines()
    domains = {}
    size = get_model_size(model)
    for line in lines[3:-1]:
        columns = line.split(':')
        print(columns)
        domain, nzs = [x.strip() for x in columns[0].split()]
        description = columns[1].strip()
        if description.startswith('Pressure levels') or description.startswith('Model rho levelsList') or description.startswith('Model theta levelsList'):
            area = columns[3].strip()
        else:
            area = columns[2].strip()
        #FIXME: we need to do better with the exceptions:
        if area == 'Global' or domain in ['DTROP', 'DUKSHELF','DUKSHELFGL']:
            domains[domain] = {'NZ':int(nzs), 'NXY': size, 'Description': description, 'VolumeBytes':int(nzs)*size*4,'CompressedBytes':None}
        else:
            raise ValueError('Dont yet understand ',domain, area)
    return domains


def get_model_size(name='N216'):
    """ 
    Return xygrid_size for a given model 
    """
    ns = int(name[1:])
    return 2 * ns * (3 * (ns+1)/2)


def temporal_domains():
    """ 
    Return default intepretation of temporal domains
    """
    streams = {
        '1hr':['T1HRMN',],'1hrPt':[ 'T1HR'],
        '3hr':['T3HRMN'],'3hrPt':['T3HR'],
        '6hr':['T6HRMAX','T6HRMN'],'6hrPt':['T6HR'],
        'day':['TDAYMIN','TDAYMAX','TDAYMN'],'dayPt':['T24H0Z'],
        'mon':['TMONMN','T6HMONM'],'monPt':['T30DAY'],
        'mond00Z':['TMONMN00'],
        'mond03Z':['TMONMN03'],
        'mond06Z':['TMONMN06'],
        'mond09Z':['TMONMN09'],
        'mond12Z':['TMONMN12'],
        'mond15Z':['TMONMN15'],
        'mond18Z':['TMONMN18'],
        'mond21Z':['TMONMN21'],
    }
    n_timesteps = {}
    all_temporal_options = []
    temporal_index = {}
    av_days_per_mon = 365/12.
    for x, y in streams.items():
        for z in y:
            all_temporal_options.append(z)
            temporal_index[z]=x
            n_timesteps[z] = {'1hr':24*av_days_per_mon,'3hr':8*av_days_per_mon,'6hr':4*av_days_per_mon, 
                'day':av_days_per_mon, 'mon':1}[x[0:3]]

    return streams, all_temporal_options, temporal_index, n_timesteps