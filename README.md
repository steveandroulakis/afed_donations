Australian Federal Electoral Donations (AFED) Blank Django App
==============

Base django application pre-loaded with the Australian Electoral Commission political donation data. Ready for apps to be coded around it to highlight points of interest.

Original data: http://periodicdisclosures.aec.gov.au/Party.aspx

##Installation (linux)

```bash
# as root for ubuntu:

apt-get install python-setuptools

# as root for redhat (eg CentOS)

yum install python-setuptools

git clone https://github.com/steveandroulakis/afed_donations.git

cd afed_donations/

python bootstrap.py

bin/buildout -v

bin/django syncdb --noinput --migrate
# this step takes a couple of minutes due to the large dataset

bin/django createsuperuser

bin/django runserver # then open /admin in a browser to view donation records

# The application is also ready to directly query via the django interactive shell..

bin/django shell

```

In the interactive shell you can query the database

```python
from afed.donations.models import Donation
from django.db.models import Sum

# get top 10 donors by total overall donation
# reads: from all donors by name,
# get me a list sorted by the donor name,
# and calculate the total sum of each donor's transactions,
# sort by the highest total donors and show the top 10

top_donors = Donation.objects.values('donor_name') \
                .order_by('donor_name') \
                .annotate(total=Sum('transaction_value')) \
                .order_by('-total')[:10]

for donor in top_donors:
    print "%s: %s" % (donor['donor_name'], donor['total'])
    
# press return a couple of times and get..

```

```
Cormack Foundation Pty Ltd: 9379000
Mineralogy Pty Ltd: 3028100
Village Roadshow Limited: 2562015
Manildra Group: 2420738
Westfield Group: 2412180
Croissy Pty Ltd: 2401000
Westpac Banking Corporation: 2228255
Inghams Enterprises Pty Ltd: 2202000
Furama Pty Ltd: 2088776
Macquarie Bank: 1937840
```

```python
# show individual transactions from the top donor
# reads: find me all donations from this particular name,
# (below we display the value of the transactions and the dates)
individual_donations = Donation.objects.filter(donor_name='Cormack Foundation Pty Ltd')

for donation in individual_donations:
    print "%s: %s on %s" % (donation.donor_name,
                            donation.transaction_value,
                            donation.transaction_date)

# press return a couple of times..
```

```
Cormack Foundation Pty Ltd: 800000 on 2001-02-22
Cormack Foundation Pty Ltd: 18000 on 2000-07-27
Cormack Foundation Pty Ltd: 1000000 on 2001-08-07
Cormack Foundation Pty Ltd: 11000 on 2001-08-14
Cormack Foundation Pty Ltd: 500000 on 2001-10-31
Cormack Foundation Pty Ltd: 800000 on 2002-04-04
Cormack Foundation Pty Ltd: 750000 on 2002-05-30
Cormack Foundation Pty Ltd: 750000 on 2002-07-22
Cormack Foundation Pty Ltd: 250000 on 2002-11-21
Cormack Foundation Pty Ltd: 800000 on 2003-03-18
Cormack Foundation Pty Ltd: 800000 on 2004-02-17
Cormack Foundation Pty Ltd: 1000000 on 2004-07-02
Cormack Foundation Pty Ltd: 800000 on 2005-03-09
Cormack Foundation Pty Ltd: 100000 on 2005-04-27
Cormack Foundation Pty Ltd: 1000000 on 2006-03-23
```

## Notes:
A file called buildout-prod.cfg can be used in place of bin/buildout -v (use bin/buildout -v -c buildout-prod.cfg) to run the application on a MySQL server instead of the default SQLite which may prove slow.

Run bin/supervisord to start the server (running on nginx with uwsgi).

Requires a MySQL server installed and a settings.py created in the afed/ directory with the relevant MySQL database credentials within.

Also requires packages for python dev, mysql libraries.


