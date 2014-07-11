# revision 33023
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/estonian
# catalog-date 2014-02-21 00:49:56 +0100
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-babel-estonian
Epoch:		1
Version:	1.1
Release:	3
Summary:	Babel support for Estonian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/estonian
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-estonian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-estonian.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-estonian.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the language definition file for support
of Estonian in babel. Some shortcuts are defined, as well as
translations to Estonian of standard "LaTeX names".

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-estonian/estonian.ldf
%doc %{_texmfdistdir}/doc/generic/babel-estonian/estonian.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-estonian/estonian.dtx
%doc %{_texmfdistdir}/source/generic/babel-estonian/estonian.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
