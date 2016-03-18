Command to spawn the socket file for nginx:

uwsgi -s /tmp/uwsgi.sock -w app:app --chmod=666 --route-run="fixpathinfo:"

--route-run="fixpathinfo:" is included to make sure the base part of the request
is removed from the path so that "/" actually serves /bikeshare/
