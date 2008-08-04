%define Product fckeditor-plone
%define product fckeditor
%define name    zope-%{product}
%define version 2.4.7
%define bad_version %(echo %{version} | sed -e 's/\\./-/g')
%define release %mkrel 3

%define zope_minver	2.7
%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	An alternate WYSIWUG editor for Plone
License:	GPL
Group:		System/Servers
URL:		http://plone.org/products/%{product}
Source:		http://plone.org/products/%{product}/releases/%{version}/%{Product}_%{bad_version}.tgz
Requires:	zope >= %{zope_minver}
Requires:	zope-Plone >= 2.1
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description 
FCKEditor is an alternate WYSIWYG through-the-web editor for Plone. It
is offering control over styles, paragraph formatting, fonts, colors,
borders, image flash and file browsing/uploading, with a really good
Plone integration.

%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*

