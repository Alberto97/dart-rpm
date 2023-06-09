Name:           dart
Version:        3.0.4
Release:        1%{?dist}
Summary:        Dart SDK

License:        BSD
URL:            https://dart.dev/

Source0:        https://storage.googleapis.com/dart-archive/channels/stable/release/%{version}/sdk/dartsdk-linux-x64-release.zip
Source1:        https://storage.googleapis.com/dart-archive/channels/stable/release/%{version}/sdk/dartsdk-linux-ia32-release.zip
Source2:        https://storage.googleapis.com/dart-archive/channels/stable/release/%{version}/sdk/dartsdk-linux-arm64-release.zip
Source3:        https://storage.googleapis.com/dart-archive/channels/stable/release/%{version}/sdk/dartsdk-linux-arm-release.zip

%description
The Dart SDK has the libraries and command-line tools that you need to develop Dart web, command-line, and server apps.

%prep

%ifarch x86_64
%autosetup -T -b 0 -n dart-sdk
%elifarch %{ix86}
%autosetup -T -b 1 -n dart-sdk
%elifarch aarch64
%autosetup -T -b 2 -n dart-sdk
%elifarch %{arm}
%autosetup -T -b 3 -n dart-sdk
%endif

%install
install -dp %{buildroot}%{_bindir}
install -dp %{buildroot}%{_libdir}/dart
cp -pr . %{buildroot}%{_libdir}/dart
%{__ln_s} -f ../%{_lib}/dart/bin/dart %{buildroot}%{_bindir}/dart


%files
%license LICENSE
%{_bindir}/dart
%{_libdir}/dart/*

%changelog
* Fri Jun 09 2023 Github Actions <github-actions@users.noreply.github.com> - 3.0.4-1
- Update Dart SDK

* Fri Jun 02 2023 Github Actions <github-actions@users.noreply.github.com> - 3.0.3-1
- Update Dart SDK

* Thu May 25 2023 Github Actions <github-actions@users.noreply.github.com> - 3.0.2-1
- Update Dart SDK

* Thu May 18 2023 Github Actions <github-actions@users.noreply.github.com> - 3.0.1-1
- Update Dart SDK

* Wed May 10 2023 Github Actions <github-actions@users.noreply.github.com> - 3.0.0-1
- Update Dart SDK

* Thu Mar 30 2023 Github Actions <github-actions@users.noreply.github.com> - 2.19.6-1
- Update Dart SDK

* Thu Mar 23 2023 Github Actions <github-actions@users.noreply.github.com> - 2.19.5-1
- Update Dart SDK

* Thu Mar 09 2023 Github Actions <github-actions@users.noreply.github.com> - 2.19.4-1
- Update Dart SDK

* Thu Mar 02 2023 Github Actions <github-actions@users.noreply.github.com> - 2.19.3-1
- Update Dart SDK

* Thu Feb 09 2023 Github Actions <github-actions@users.noreply.github.com> - 2.19.2-1
- Update Dart SDK

* Thu Feb 02 2023 Github Actions <github-actions@users.noreply.github.com> - 2.19.1-1
- Update Dart SDK

* Wed Jan 25 2023 Github Actions <github-actions@users.noreply.github.com> - 2.19.0-1
- Update Dart SDK

* Fri Jan 13 2023 Github Actions <github-actions@users.noreply.github.com> - 2.18.7-1
- Update Dart SDK

* Thu Dec 15 2022 Github Actions <github-actions@users.noreply.github.com> - 2.18.6-1
- Update Dart SDK

* Sun Nov 27 2022 Alberto Pedron <albertop2197@gmail.com> - 2.18.5-1
- Initial release
