#!/usr/bin/env python

import numpy as np
import psrchive

"""A list of useful psrchive dependent functions to use in python"""
"""Just getting started - hoping to add to this. Please feel free to add your own functions too. 
and thanks for get_archive_info that was supplied by Maciej Serylak."""


def get_archive_info(archive):
   """Query archive attributes.
   Input:
       archive: loaded PSRCHIVE archive object.
   Output:
       Print attributes of the archive.
   """
   filename = archive.get_filename()
   nbin = archive.get_nbin()
   nchan = archive.get_nchan()
   npol = archive.get_npol()
   nsubint = archive.get_nsubint()
   obs_type = archive.get_type()
   telescope_name = archive.get_telescope()
   source_name = archive.get_source()
   ra = archive.get_coordinates().ra()
   dec = archive.get_coordinates().dec()
   centre_frequency = archive.get_centre_frequency()
   bandwidth = archive.get_bandwidth()
   DM = archive.get_dispersion_measure()
   RM = archive.get_rotation_measure()
   is_dedispersed = archive.get_dedispersed()
   is_faraday_rotated = archive.get_faraday_corrected()
   is_pol_calib = archive.get_poln_calibrated()
   data_units = archive.get_scale()
   data_state = archive.get_state()
   obs_duration = archive.integration_length()
   obs_start = archive.start_time().fracday() + archive.start_time().intday()
   obs_end = archive.end_time().fracday() + archive.end_time().intday()
   receiver_name = archive.get_receiver_name()
   receptor_basis = archive.get_basis()
   backend_name = archive.get_backend_name()
   backend_delay = archive.get_backend_delay()
   # low_freq = archive.get_centre_frequency() - archive.get_bandwidth() / 2.0
   # high_freq = archive.get_centre_frequency() + archive.get_bandwidth() / 2.0
   print 'file             Name of the file                           %s' % filename
   print 'nbin             Number of pulse phase bins                 %s' % nbin
   print 'nchan            Number of frequency channels               %s' % nchan
   print 'npol             Number of polarizations                    %s' % npol
   print 'nsubint          Number of sub-integrations                 %s' % nsubint
   print 'type             Observation type                           %s' % obs_type
   print 'site             Telescope name                             %s' % telescope_name
   print 'name             Source name                                %s' % source_name
   print 'coord            Source coordinates                         %s%s' % (ra.getHMS(), dec.getDMS())
   print 'freq             Centre frequency (MHz)                     %s' % centre_frequency
   print 'bw               Bandwidth (MHz)                            %s' % bandwidth
   print 'dm               Dispersion measure (pc/cm^3)               %s' % DM
   print 'rm               Rotation measure (rad/m^2)                 %s' % RM
   print 'dmc              Dispersion corrected                       %s' % is_dedispersed
   print 'rmc              Faraday Rotation corrected                 %s' % is_faraday_rotated
   print 'polc             Polarization calibrated                    %s' % is_pol_calib
   print 'scale            Data units                                 %s' % data_units
   print 'state            Data state                                 %s' % data_state
   print 'length           Observation duration (s)                   %s' % obs_duration
   print 'start            Observation start (MJD)                    %.10f' % obs_start
   print 'end              Observation end (MJD)                      %.10f' % obs_end
   print 'rcvr:name        Receiver name                              %s' % receiver_name
   print 'rcvr:basis       Basis of receptors                         %s' % receptor_basis
   print 'be:name          Name of the backend instrument             %s' % backend_name
   print 'be:delay         Backend propn delay from digi. input.      %s\n' % backend_delay
    
   
 
def get_lower_and_upper_freq(archive):
    lower_freq = archive.get_centre_frequency() - archive.get_bandwidth()/2.0
    high_freq = archive.get_centre_frequency() + archive.get_bandwidth()/2.0
    return lower_freq, high_freq


def get_pulseperiod(archive):
    ephem = archive.get_ephemeris()
    rot_freq = ephem.get_value('F0')
    pulseperiod = 1.0/float(rot_freq)
    return pulseperiod
    

# def apply_freq_weights(archive):    
#     """This function applies weights to t-scrunched full-intensity data"""
#     nchan = archive.get_nchan()
#     nbin = archive.get_nbin()
#     nsubint = archive.get_nsubint()
#     npol = archive.get_npol()
#     print "Archive loaded to apply weights has:\n"
#     print "%d freq chan" %nchan
#     print "%d subints" %nsubint
#     print "%d phase bins" %nbin
#     print "%d polarisations" %npol
#     print "This function applies weights to t-scrunched, p-scrunched data - for now"
    
#     if int(nchan) == 1:
#         print "Applying weights doesn't make sense, data has already been f-scrunched"
#     if int(npol) > 1:
#         print "Scrunching in polarisation before continuing"
#         archive.pscrunch()
#     weights = archive.get_weights().reshape(nchan)
#     freq_data = archive.get_data()
#     spec_data = freq_data.reshape(nchan,nbin)
       
#     data_weighted = np.ones((nchan, nbin))
#     for n in range(nchan):
#         data_weighted[n] =  weights[n]*spec_data[n,:]
#     return data_weighted



def apply_freq_weights1(archive,verbose=True):    
    """This function applies weights to t-scrunched full-intensity data"""
    nchan = archive.get_nchan()
    nbin = archive.get_nbin()
    nsubint = archive.get_nsubint()
    npol = archive.get_npol()
    if verbose == True:
        print "Archive loaded to apply weights has:\n"
        print "%d freq chan" %nchan
        print "%d subints" %nsubint
        print "%d phase bins" %nbin
        print "%d polarisations" %npol
        print "This function applies weights to t-scrunched, p-scrunched data - for now"
    
    if int(nchan) == 1:
        print "Applying weights doesn't make sense, data has already been f-scrunched"
    if int(npol) > 1:
        print "Scrunching in polarisation before continuing"
        archive.pscrunch()
    weights = archive.get_weights().reshape(nchan)   
    weights[np.where(weights!=0)] = 1
    print "Setting non-zero weights to 1"
    
    freq_data = archive.get_data()
    spec_data = freq_data.reshape(nchan,nbin)
       
    data_weighted = np.ones((nchan, nbin))
    
    for n in range(nchan):
        data_weighted[n] =  weights[n]*spec_data[n,:]
    return data_weighted


def apply_freq_weights(archive,verbose=True):    
    """This function applies weights to t-scrunched full-intensity data"""
    nchan = archive.get_nchan()
    nbin = archive.get_nbin()
    nsubint = archive.get_nsubint()
    npol = archive.get_npol()
    if verbose == True:
        print "Archive loaded to apply weights has:\n"
        print "%d freq chan" %nchan
        print "%d subints" %nsubint
        print "%d phase bins" %nbin
        print "%d polarisations" %npol
        print "This function applies weights to t-scrunched, p-scrunched data - for now"
    
    if int(nchan) == 1:
        print "Applying weights doesn't make sense, data has already been f-scrunched"
    if int(npol) > 1:
        print "Scrunching in polarisation before continuing"
        archive.pscrunch()
    weights = archive.get_weights().reshape(nchan)
    
    freq_data = archive.get_data()
    spec_data = freq_data.reshape(nchan,nbin)
       
    data_weighted = np.ones((nchan, nbin))
    for n in range(nchan):
        data_weighted[n] =  weights[n]*spec_data[n,:]
    return data_weighted



"""Below follows a set of functions required to do flux calibration via radiometer equation estimates"""

def find_rms(data,windowsize):
    nbins = len(data) 
    windows = int(nbins/windowsize)
    rms_loc = np.zeros(windows)
    for i in range(windows):
        start = i*windowsize
        end = start + windowsize
        rms_loc[i] = np.std(data[start:end])
    return np.min(rms_loc)

def smooth(y, boxsize):
    gauss = np.ones(boxsize)
#    box = np.ones(box_pts)/box_pts
    sigma = (1./10.)*boxsize
    mean = boxsize/2.
    for i in range(boxsize):
        gauss[i] = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-(i-mean)**2/(2*sigma**2))
    y_smooth = np.convolve(y, gauss, mode='same')
    return y_smooth



def counts_to_mJy(SEFD, Nants, BW, frac_used, duration, nbins, rms, data, verbose=False):  
    """SEFD: average per frequency channel per antenna per polarisation SEFD
              typically taken to be 422 Jy
              or an array of SEFDs of length nchan
       Nants: number of antennas present in array
       BW:    bandwidth in MHz
       frac_used: fraction of used bandwidth (e.g. 0.3 for 30%)
       duration: duration of observation in seconds
       nbins: number of phase bins
       rms: estimated off-pulse rms (use find_rms for that)
       data: fscrunched profile, or array of nchan x nbins, ensure that psru.applied_freq_weights1 has already been applied
    """
    
    npol=2
    BW_Hz = BW*1e6
    
    time_per_bin = float(duration)/float(nbins)
    
    SEFD_ar = np.array([SEFD/float(Nants)])
    if verbose == True:
        print "Array SEFD with %d antennas is %.2f" %(Nants,SEFD_ar)
    
    try: 
        conv_fac = SEFD_ar/np.sqrt(npol*frac_used*BW_Hz*time_per_bin)
        conv_fac_vec = conv_fac.reshape(SEFD_ar.shape[1],1)
        ## multiple each row of data by the appropriate factor
        flux_density_mJy = 1000*conv_fac_vec*data/float(rms)
        sing_conv = (1000*conv_fac/float(rms))[0]
    except:
        conv_fac = SEFD_ar/np.sqrt(npol*frac_used*BW_Hz*time_per_bin)
        conv_fac_vec = conv_fac.reshape(SEFD_ar.shape[0],1)
        ## multiple each row of data by the appropriate factor
        flux_density_mJy = (1000*conv_fac_vec*data/float(rms))[0]
        sing_conv = (1000*conv_fac/float(rms))[0]
    
    return sing_conv, flux_density_mJy




# def counts_to_mJy(SEFD, Nants, BW, frac_used, duration, nbins, rms, data, verbose=False):  
#     """SEFD: average per frequency channel per antenna per polarisation SEFD
#               typically taken to be 422 Jy
#        Nants: number of antennas present in array
#        BW:    bandwidth in MHz
#        frac_used: fraction of used bandwidth (e.g. 0.3 for 30%)
#        duration: duration of observation in seconds
#        nbins: number of phase bins
#        rms: estimated off-pulse rms (use find_rms for that)
#     """
    
#     npol=2
#     BW_Hz = BW*1e6
    
#     time_per_bin = float(duration)/float(nbins)
#     SEFD_ar = float(SEFD)/Nants
    
#     if verbose == True:
#         print "Array SEFD with %d antennas is %.2f" %(Nants,SEFD_ar)
    
#     conv_fac = SEFD_ar/np.sqrt(npol*frac_used*BW_Hz*time_per_bin)
#     flux_density_mJy = 1000*conv_fac*data/float(rms)
#     return conv_fac, flux_density_mJy




def thirddeg_poly(x,poly):
    """Third degree poly, for handling SEFD model"""
    polyfunc = poly[0]*np.power(x,0)+ poly[1]*np.power(x,1) + poly[2]*np.power(x,2) + poly[3]*np.power(x,3)
    return polyfunc

def SEFD_chan(chan_MHz):
    """Provided a frequency channel/value in MHz this function will return the polarisation averaged SEFD, based on the 3rd degree polynomial used"""
    
    """Hard-coded SEFD model at L-band"""
    polyh = [2.08778760e+02,  1.08462392e+00, -1.24639611e-03, 4.00344294e-07]
    polyv = [7.57838984e+02, -2.24205001e-01, -1.72161897e-04, 1.11118471e-07]
    
    sefd_at_chan_h = thirddeg_poly(chan_MHz,polyh)
    sefd_at_chan_v = thirddeg_poly(chan_MHz,polyv)
    
    return np.mean([sefd_at_chan_h, sefd_at_chan_v], axis=0)



def PA(U,Q):
    PA = 0.5*np.arctan(U/Q)
    return PA
    