%global fontname madan
%global fontconf 65-0-%{fontname}.conf

Name: %{fontname}-fonts
Version: 2.000
Release: 3%{?dist}
Summary: Font for Nepali language
Group: User Interface/X
License: GPL+
URL: http://madanpuraskar.org/
#Note if downloading this URL using wget,move this file to madan.zip
#Source0: http://madanpuraskar.org/index.php?option=com_docman&task=doc_download&gid=8&Itemid=63
Source0: madan.zip
Source1: %{fontconf}
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
This package provides the Madan font for Nepali made by the
Madan Puraskar Pustakalaya project.

%prep
%setup -c -q
for file in madan/license.txt; do
 sed "s|\r||g" $file > $file.new && \
 touch -r $file $file.new && \
 mv $file.new $file
done


%build
echo "Nothing to do in Build."

%install
rm -rf %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{fontname}/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%clean
rm -rf %{buildroot}

%_font_pkg -f %{fontconf} *.ttf
%doc %{fontname}/license.txt


%changelog
* Tue May 18 2010 Parag <pnemade AT redhat.com> - 2.000-3
- Resolves: rh#586899 - Rename 65-madan.conf to 65-0-madan.conf 

* Tue May 18 2010 Parag <pnemade AT redhat.com> - 2.000-2
- Resolves: rh#586870  - lang-specific overrides rule doesn't work as expected

* Tue Feb 23 2010 Parag <pnemade AT redhat.com> - 2.000-1
- Update to next upstream release
- Resolves: rh#567560-[ne_NP] Need fontconfig rules for Madan font

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0-11.1
- Rebuilt for RHEL 6

* Tue Aug 11 2009 Parag <pnemade@redhat.com> - 1.0-11
- Fix source audit 2009-08-10

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 08 2009 Pravin Satpute <psatpute@redhat.com> - 1.0-9
- updated spec as per new packaging guideline

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-7
- fix license tag

* Mon Oct 15 2007 Rahul Bhalerao <rbhalera@redhat.com> - 1.0-6.fc8
- Spec update as per review

* Thu Oct 11 2007 Rahul Bhalerao <rbhalera@redhat.com> - 1.0-5.fc8
- Spec update as per reveiw

* Wed Sep 26 2007 Rahul Bhalerao <rbhalera@redhat.com> - 1.0-4.fc8
- Spec update as per review

* Fri Sep 21 2007 Rahul Bhalerao <rbahlera@redhat.com> - 1.0-3.fc8
- Added LICENSE as Source1

* Thu Sep 20 2007 Rahul Bhalerao <rbhalera@redhat.com> - 1.0-2.fc8
- Removed use of tarball and ghost files

* Thu Sep 13 2007 Rahul Bhalerao <rbhalera@redhat.com> - 1.0-1.fc8
- Initial packaging
