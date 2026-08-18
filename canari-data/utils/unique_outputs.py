from grids import temporal_domains, domain_profiles

def process_outputs(file='main_config_report 2022-10-21.txt', resolution='N216'):
    with open(file,'r') as f:
        lines = f.readlines()
    uniques = []
    streams = {}
    grids = domain_profiles(model=resolution)
    default_streams, temporals, temporal_index, n_timesteps = temporal_domains()
    proposed = {}

    for line in lines[4:]:
        columns = line[57:].split(':')
        try:
            domain, time, stream = columns[0],columns[1],columns[2]
        except:
            continue
        domain = domain.strip()
        times = time.strip()
        if domain not in grids:
            raise ValueError('Unexpected domain profile', domain)
        if times not in temporals:
            raise ValueError('Unexpected temporal sampling', times)
        domaintime = f'{domain}:{times}'
        if domaintime not in uniques:
            uniques.append(domaintime)
        volume = grids[domain]['VolumeBytes']*n_timesteps[times]
        
        # vanilla
        if stream not in streams:
            streams[stream]={'VolumeMB':0}
        streams[stream]['VolumeMB'] += volume
        if domaintime not in streams[stream]:
            streams[stream][domaintime]=1
        else:
            streams[stream][domaintime]+=1
        
        # proposed
        index = temporal_index[times]
        if index not in proposed:
            proposed[index]={'VolumeMB':volume,'Contains':default_streams[index]}
        else:
            proposed[index]['VolumeMB']+=volume

    # ok fix up the lie in the volume key
    for stream in streams:
        streams[stream]['VolumeMB'] = streams[stream]['VolumeMB']/1e6
    for index in proposed:
        proposed[index]['VolumeMB'] = proposed[index]['VolumeMB']/1e6


    print('\n\nStash analysis\n\n')
    print(f'There are {len(uniques)} CF domain combinations to be output\n')
    print(uniques,'\n')
    print(f'Which are using {len(grids)} different grids\n')
    print(f'and {len(temporals)} different temporal options\n')
    print(f'There are {len(streams)} different output streams\n')
    for stream in streams:
        print(stream,streams[stream])

    print('\n---\nAlternatively\n')
    for k,v in proposed.items():
        print(k,v)

    print('Sanity check')

    sum1 = sum([streams[stream]['VolumeMB'] for stream in streams])
    sum2 = sum([proposed[stream]['VolumeMB'] for stream in proposed])

    print(sum1)
    print(sum2)


if __name__=="__main__":
    process_outputs()