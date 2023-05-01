%bcond_without check

# https://github.com/prashantv/gostub
%global goipath         github.com/prashantv/gostub
%global commit          9fc4f583f114a72d2d711ec21d8963c7dfda9a8c

%gometa

%global common_description %{expand:
gostub is a library to make stubbing in unit tests easy.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        stubbing library for golang unit tests

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Sun Apr 30 11:00:00 -05 2023 CAD <fedora@autonomia.digital> - 0-0.1.20211211git9fc4f58
- Initial package
