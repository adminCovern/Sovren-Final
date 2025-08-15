# Hardware Configuration Report

## Table of Contents
1. [System Overview](#system-overview)
2. [Processor Configuration](#processor-configuration)
3. [Memory Configuration](#memory-configuration)
4. [GPU Configuration](#gpu-configuration)
5. [Storage Configuration](#storage-configuration)
6. [Network Configuration](#network-configuration)
7. [PCIe Subsystem](#pcie-subsystem)
8. [Power Supply Configuration](#power-supply-configuration)
9. [Additional Components](#additional-components)

## System Overview

### Server Specifications
- **Model**: Supermicro SYS-A22GA-NBRT
- **Motherboard**: X14DBG-DAP
- **Serial Number**: S946907X5417211
- **BIOS Version**: 1.2 (American Megatrends International, LLC)
- **BIOS Date**: 03/07/2025
- **Architecture**: 64-bit x86
- **Form Factor**: Dual Socket Enterprise Server

### System Capabilities
- **SMP Support**: Yes
- **UEFI Support**: Yes
- **Virtualization**: Full hardware virtualization support
- **ECC Memory**: Enabled

## Processor Configuration

### CPU 1 - Primary Processor
- **Model**: Intel(R) Xeon(R) 6960P
- **Socket**: CPU1
- **Cores**: 72 physical cores
- **Threads**: 144 threads (with HyperThreading)
- **Base Clock**: 2.7 GHz
- **Max Clock**: 3.9 GHz
- **Microcode Version**: 16778146
- **Architecture**: Intel Ice Lake (6.173.1)

### CPU 2 - Secondary Processor
- **Model**: Intel(R) Xeon(R) 6960P
- **Socket**: CPU2
- **Cores**: 72 physical cores
- **Threads**: 144 threads (with HyperThreading)
- **Base Clock**: 2.7 GHz
- **Max Clock**: 3.9 GHz
- **Microcode Version**: 16778146
- **Architecture**: Intel Ice Lake (6.173.1)

### Cache Hierarchy
- **L1 Cache**: 8064 KiB per processor
- **L2 Cache**: 144 MiB per processor
- **L3 Cache**: 432 MiB per processor

### CPU Features
Advanced instruction sets and capabilities including:
- AVX-512 (F, DQ, CD, BW, VL, IFMA, VBMI, VBMI2, VNNI, BITALG, VPOPCNTDQ, BF16, FP16)
- Intel AMX (BF16, TILE, INT8)
- Security: IBRS, IBPB, STIBP, TME, User SHSTK
- Virtualization: VMX, EPT, VPID

## Memory Configuration

### System Memory Overview
- **Total Capacity**: 2304 GiB (2.25 TiB)
- **Maximum Capacity**: 12 TiB
- **Memory Type**: DDR5 ECC Registered
- **Memory Speed**: 6400 MHz
- **Error Correction**: ECC Enabled

### Memory Module Distribution

#### CPU 1 Memory Banks (Slots P1)
- **DIMMA1-DIMML1**: 12x 96GiB Samsung M321RYGA0PB2-CCPKC modules
- **Speed**: 2105 MHz actual (6400 MHz rated)
- **Total**: 1152 GiB

#### CPU 2 Memory Banks (Slots P2)
- **DIMMA1-DIMML1**: 12x 96GiB Samsung M321RYGA0PB2-CCPKC modules
- **Speed**: 2105 MHz actual (6400 MHz rated)
- **Total**: 1152 GiB

## GPU Configuration

### NVIDIA Graphics Accelerators
The system contains **8x NVIDIA 3D Controllers** (likely H100 or similar datacenter GPUs) distributed across multiple PCIe switches:

#### GPU Distribution
- **GPU 1**: Bus 0000:17:00.0 - PCIe Gen5 x16
- **GPU 2**: Bus 0000:3d:00.0 - PCIe Gen5 x16
- **GPU 3**: Bus 0000:5f:00.0 - PCIe Gen5 x16
- **GPU 4**: Bus 0000:70:00.0 - PCIe Gen5 x16
- **GPU 5**: Bus 0000:97:00.0 - PCIe Gen5 x16
- **GPU 6**: Bus 0000:ba:00.0 - PCIe Gen5 x16
- **GPU 7**: Bus 0000:dc:00.0 - PCIe Gen5 x16
- **GPU 8**: Bus 0000:ed:00.0 - PCIe Gen5 x16

### GPU Specifications
- **Driver**: NVIDIA proprietary driver
- **Bus Width**: 64-bit
- **PCIe Generation**: Gen 5
- **Capabilities**: MSI-X, Power Management, Bus Master

## Storage Configuration

### NVMe Storage Devices

#### Primary Storage Array
Four Samsung PM9A3 Enterprise NVMe SSDs configured as follows:

##### Drive 1 - /dev/nvme0
- **Model**: SAMSUNG MZQL27T6HBLA-00A07
- **Serial**: S6CKNN0XA19189
- **Capacity**: 7153 GiB (7.68 TB)
- **Firmware**: GDC5A02Q
- **Partitions**:
  - EFI Boot: 1074 MiB (FAT32)
  - System: 499 GiB
  - Data: 6652 GiB (EXT4)

##### Drive 2 - /dev/nvme1
- **Model**: SAMSUNG MZQL27T6HBLA-00A07
- **Serial**: S6CKNN0XA19194
- **Capacity**: 7153 GiB (7.68 TB)
- **Firmware**: GDC5A02Q
- **Partitions**:
  - System: 499 GiB
  - Data: 6653 GiB (EXT4)

##### Drive 3 - /dev/nvme2
- **Model**: SAMSUNG MZQL27T6HBLA-00A07
- **Serial**: S6CKNN0XA19454
- **Capacity**: 7153 GiB (7.68 TB)
- **Firmware**: GDC5A02Q
- **Partitions**:
  - System: 499 GiB
  - Data: 6653 GiB (EXT4)

##### Drive 4 - /dev/nvme3
- **Model**: SAMSUNG MZQL27T6HBLA-00A07
- **Serial**: S6CKNN0XA19060
- **Capacity**: 7153 GiB (7.68 TB)
- **Firmware**: GDC5A02Q
- **Partitions**:
  - EFI Boot: 1074 MiB (FAT32)
  - System: 499 GiB
  - Data: 6652 GiB (EXT4)

### RAID Controller
- **Model**: Broadcom MegaRAID 12GSAS/PCIe Secure SAS38xx
- **Driver**: megaraid_sas
- **Bus**: PCIe Gen5

## Network Configuration

### High-Speed InfiniBand Interfaces
The system includes multiple Mellanox ConnectX-7 InfiniBand adapters:

#### InfiniBand Adapters
- **8x MT2910 Family [ConnectX-7]** interfaces
  - Driver: mlx5_core with ib_ipoib
  - Firmware: 28.41.1000 / 28.42.1280
  - Interface names: ibs112-ibs119
  - Status: Currently disabled

#### Multi-port InfiniBand Controller
- **MT2910 ConnectX-7 Quad Port** (Bus 0000:ab:00.0-3)
  - 4 ports (ibs100f0-ibs100f3)
  - Firmware: 28.42.1280
  - Status: Currently disabled

### Ethernet Interfaces

#### 10 Gigabit Ethernet
- **Intel X710 Dual Port 10GBASE-T**
  - Port 1: ens110f0np0 (90:5a:08:9a:47:9a)
  - Port 2: ens110f1np1 (90:5a:08:9a:47:9b)
  - Driver: i40e
  - Firmware: 9.40
  - Speed: 10 Gbit/s capability

#### 40 Gigabit Ethernet
- **Mellanox ConnectX-6 Dx Dual Port**
  - Port 1: ens121f0np0
  - Port 2: ens121f1np1
  - Driver: mlx5_core
  - Firmware: 22.41.1000
  - Speed: 40 Gbit/s capability
  - Media: Fiber

## PCIe Subsystem

### PCIe Architecture
- **Generation**: PCIe Gen 5 throughout
- **Switch Technology**: Broadcom PEX890xx PCIe Gen 5 Switches
- **Switch Configuration**: Multiple hierarchical switches for GPU and NVMe distribution

### Intel Accelerators

#### Intel Data Streaming Accelerators (DSA)
- **16x Intel DSA devices** (idxd driver)
- Distributed across NUMA nodes
- Used for high-speed memory operations

#### Intel QuickAssist Technology (QAT)
- **16x Intel 4xxx Series QAT accelerators**
- Hardware acceleration for cryptography and compression
- PCIe Gen5 connectivity

#### Intel AI Accelerators
- **16x Intel Co-processor devices** (unclaimed)
- Likely Intel Gaudi or similar AI accelerators
- PCIe Gen5 x16 interfaces

## Power Supply Configuration

### Redundant Power Supply System
The system features a 6+0 redundant power supply configuration:

- **Model**: Supermicro PWS-5K26G-2R1
- **Capacity**: 5250W per unit
- **Total Capacity**: 31,500W (6x 5250W)
- **Redundancy**: N+0 configuration
- **Efficiency**: 80+ Titanium certified

### Power Supply Units
1. **PSU 1**: Serial P5K27CO48BB0062
2. **PSU 2**: Serial P5K27CO48BB0058
3. **PSU 3**: Serial P5K27CO48BB0040
4. **PSU 4**: Serial P5K27CO48BB0078
5. **PSU 5**: Serial P5K27CO48BB0056
6. **PSU 6**: Serial P5K27CO48BB0060

## Additional Components

### Management and Support Systems

#### BMC/IPMI
- **Graphics**: ASPEED AST1150 BMC Graphics
- **Resolution**: 1920x1200
- **Driver**: ast
- **Purpose**: Remote management interface

#### USB Controllers
- **Renesas uPD720201 USB 3.0 Host Controller**
- **ASPEED USB Virtual Hub** (BMC integrated)
- **Ports**: 4x USB 3.0, multiple USB 2.0

#### Serial Attached SCSI
- **Multiple Broadcom SAS controllers**
- **PCIe Switch management endpoints**
- **Support for SAS enclosures**

### System Monitoring
- **Hardware monitoring**: Multiple hwmon interfaces
- **Temperature sensors**: CPU, GPU, and system thermal monitoring
- **Power monitoring**: Per-PSU power consumption tracking

This hardware configuration represents a high-performance computing system optimized for AI/ML workloads with substantial GPU acceleration, massive memory capacity, and enterprise-grade storage and networking capabilities.