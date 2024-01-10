Name:       firmware-latte
Summary:    Firmware blobs for Xiaomi Latte
Version:    1.0
Release:    1
Group:      System/Firmware
License:    Redistributable
URL:        https://github.com/sailfish-on-latte/firmware-latte
Source0:     %{name}-%{version}.tar.bz2
Source1:    brcmfmac4356-pcie.bin
Source2:    brcmfmac4356-pcie.Xiaomi_Inc-Mipad2.txt

%description
This package contains firmware for the Xiomi MiPad 2

%prep
ls -lhR .
%setup -q -n %{name}-%{version}

%build
ls -lR .

%install
pwd
ls -lR .
mkdir -p $RPM_BUILD_ROOT/lib/firmware/brcm
cp %{SOURCE1} $RPM_BUILD_ROOT/lib/firmware/brcm/
cp %{SOURCE2} "$RPM_BUILD_ROOT/lib/firmware/brcm/brcmfmac4356-pcie.Xiaomi Inc-Mipad2.txt"


%files
/lib/firmware/
