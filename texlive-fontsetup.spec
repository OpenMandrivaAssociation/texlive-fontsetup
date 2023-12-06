Name:		texlive-fontsetup
Version:	68602
Release:	1
Summary:	A front-end to fontspec, for selected fonts with math support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fontsetup
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontsetup.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontsetup.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package facilitates the use of fontspec for users who do
not wish to bother with details, with a special focus on
quality fonts supporting Mathematics.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/fontsetup
%doc %{_texmfdistdir}/doc/latex/fontsetup

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
