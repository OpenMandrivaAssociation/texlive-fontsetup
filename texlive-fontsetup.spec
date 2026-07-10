%global tl_name fontsetup
%global tl_revision 79284

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.6.0
Release:	%{tl_revision}.1
Summary:	A front-end to fontspec, for selected fonts with math support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/fontsetup
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontsetup.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontsetup.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package facilitates the use of fontspec for users who do not wish
to bother with details, with a special focus on quality fonts supporting
Mathematics.

