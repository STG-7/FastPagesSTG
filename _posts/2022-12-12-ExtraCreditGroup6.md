---
toc: true
layout: post
description: Extra Credit Group 6
categories: [markdown]
title: Extra Credit Group 6
---


# Vocab
- Method/Function/Procedure - A set of code that can be run as a package, that takes in parameters and returns a return value
- Example: add(1, 2), which adds two numbers
- Catch all terms for a set of code
- Parameter - Input values for procedures # Vocab Section 13
- Procedure: is a named group of programming instructions that serves a purpose
- Parameter: are input values of a procedure ^ There are two types of procedures, one that returns a value or some type of data and on that just executes a block of statements (void)
- Modularity - the practice of breaking a complex program into smaller, independent parts or modules that can be used and reused in different parts of the program

# Notes:
Make your names descriptive! 
Make your program into smaller independent modules that can be used multiple times
Utilize update functions and recursive

# Research Off Harvard

**Remote procedure call is the synchronous language-level transfer of control between programs disjoint address spaces whose primary communication medium is a narrow channel. The thesis of this dissertation is that remote procedure call (RPC) is a satisfactory and efficient programming language primitive for constructing distributed systems. A survey of existing remote procedure mechanisms shows that past RPC efforts are weak in addressing the five crucial issues: uniform call semantics, binding and configuration, strong typechecking, parameter functionality, and concurrency and exception control. The body of the dissertation elaborates these issues and defines a set of corresponding essential properties for RPC mechanisms. These properties must be satisfied by any RPC mechanism that is fully and uniformly integrated into a programming language for a homogeneous distributed system.** 

**Uniform integration is necessary to meet the dissertation's fundamental goal of syntactic and semantic transparency for local and remote procedures. Transparency is important so that programmers need not concern themselves with the physical distribution of their programs. In addition to these essential language properties, a number of pleasant properties are introduced that ease the work of distributed programming. These pleasant properties are good performance, sound remote interface design, atomic transactions, respect for autonomy, type translation, and remote debugging.**

With the essential and pleasant properties broadly explored, the detailed design of an RPC
mechanism that satisfies all of the essential properties and the performance property is presented.
Two design approaches are used: The first assumes full programming language support and involves
changes to the language's compiler and binder. The second involves no language changes, but uses
a separate translator-a source-to-source RPC compiler-to implement the same functionality.
Design decisions crucial to the efficiency of the mechanism are made using a set of RPC
perfonnance lessons. These lessons are based on the empirical performance evaluation of a
sequence of five working RPC mechanisms. each one faster than its predecessor. Some expected
results about the costs of parameter copying. process switching, and runtime type manipulation are
confinned; a surprising result about the price of protocol layering is presented as well. These
performance lessons, applied in concert, reduce the roundtrip time for a remote procedure call by a
remarkable factor of 35. For moderate speed personal computers communicating over an Ethernet,
for example, a simple remote can takes 800 microseconds; on a higher speed personal computer, the
same remote call takes 149 microseconds. In both cases the remote call takes about 20 times longer
than the same local call. This represents a substantial performance improvement over other
operational RPC mechanisms.
Key words and phrases: communication primitives, computer networks, distributed computing,
interprocess communication, message passing, naming and binding, procedure call, programming
languages, protocols, remote procedure call, software performance evaluation. 


**Remote procedure calls (RPC) appear to be a useful paradig m for providing communication across a network between programs written in a high-level language.**


# 1.1 Background 
**The idea of remote procedure calls (hereinafter called RPC) is quite simple. It is based on the observation that procedure calls are a well-known and wellunderstood mechanism for transfer of control and data within a program running on a single computer. Therefore, it is proposed that this same mechanism be extended to provide for transfer of control and data across a communication network. When a remote procedure is invoked, the calling environment is suspended, the parameters are passed across the network to the environment where the procedure is to execute (which we will refer to as the callee), and the desired procedure is executed there. When the procedure finishes and produces its results, the results are passed backed to the calling environment, where execution resumes as if returning from a simple single-machine call. While the calling environment is suspended, other processes on that machine may (possibly) still execute (depending on the details of the parallelism of that environment and the RPC implementation).**

There are many attractive aspects to this idea. One is clean and simple
semantics: these should make it easier to build distributed computations, and to
get them right. Another is efficiency: procedure calls seem simple enough for the
communication to be quite rapid. A third is generality: in singie-machine computations, procedures are often the most important mechanism for communication between parts of the algorithm.
The idea of RPC has been around for many years. It has been discussed in the
public literature many times since at least as far back as 1976 [15]. Nelson's
doctoral dissertation [13] is an extensive examination of the design possibilities
for an RPC system and has references to much of the previous work on RPC.
However, full-scale implementations of RPC have been rarer than paper designs.
Notable recent efforts include Courier in the Xerox NS family of protocols [4],
and current work at MIT [10].
This paper results from the construction of an RPC facility for the Cedar
project. We felt, because of earlier work (particularly Nelson's thesis and associated experiments), that we understood the choices the designer of an RPC
facility must make. Our task was to make the choices in light of our particular
aims and environment. In practice, we found that several areas were inadequately
understood, and we produced a system whose design has several novel aspects.
Major issues facing the designer of an RPC facility include: the precise semantics
of a call in the presence of machine and communication failures; the semantics
of address-containing arguments in the (possible) absence of a shared address
space; integration of remote calls into existing (or future) programming systems;
binding (how a caller determines the location and identity of the callee); suitable
protocols for transfer of data and control between caller and callee; and how to
provide data integrity and security (if desired) in an open communication
network. In building our RPC package we addressed each of these issues, but it
not possible to describe all of them in suitable depth in a single paper. This paper
includes a discussion of the issues and our major decisions about them, and
describes the overall structure of our solution. We also describe in some detail
our binding mechanism and our transport level communication protocol. We
plan to produce subsequent papers describing our facilities for encryption-based
security, and providing more information about the manufacture of the stub
modules (which are responsible for the interpretation of arguments and results
of RPC calls) and our experiences with practical use of this facility.

# 1.2 Environment

The remote-procedure-call package we have built was developed primarily for
use within the Cedar programming environment, communicating across the
Xerox research internetwork. In building such a package, some characteristics of
the environment inevitably have an impact on the design, so the environment is
summarized here.
Cedar [6] is a large project concerned with developing a programming environment that is powerful and convenient for the building of experimental programs
and systems. There is an emphasis on uniform, highly interactive user interfaces,
and ease of construction and debugging of programs. Cedar is designed to be used on single-user workstations, although it is also used for the construction of
servers (shared computers providing common services, accessible through the
communication network).
Most of the computers used for Cedar are Dorados [8]. The Dorado is a very
powerful machine (e.g., a simple Algol-style call and return takes less than 10
microseconds). It is equipped with a 24-bit virtual address space (of 16-bit words)
and an 80-megabyte disk. Think of a Dorado as having the power of an IBM
370/168 processor, dedicated to a single user.
Communication between these computers is typically by means of a 3-megabitper-second Ethernet [11]. {Some computers are on a 10-megabit-per-second
Ethernet [7].) Most of the computers running Cedar are on the same Ethernet,
but some are on different Ethernets elsewhere in our research internetwork. The
internetwork consists of a large number of 3-megabyte and 10-megabyte Ethernets (presently about 160) connected by leased telephone and satellite links (at
data rates of between 4800 and 56000 bps). We envisage that our RPC communication will follow the pattern we have experienced with other protocols: most
communication is on the local Ethernet (so the much lower data rates of the
internet links are not an inconvenience to our users), and the Ethernets are not
overloaded (we very rarely see offered loads above 40 percent of the capacity of
an Ethernet, and 10 percent is typical).
The PUP family of protocols [3] provides uniform access to any computer on
this internetwork. Previous PUP protocols include simple unreliable (but highprobability) datagram service, and reliable flow-controlled byte streams. Between
two computers on the same Ethernet, the lower level raw Ethernet packet format
is available.
Essentially all programming is in high-level languages. The dominant language
is Mesa [12] (as modified for the purposes of Cedar), although Smalltalk and
InterLisp are also used. There is no assembly language for Dorados. 

