# Copyright (C) 2009-2011 Anders Logg
#
# This file is part of DOLFIN.
#
# DOLFIN is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DOLFIN is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with DOLFIN. If not, see <http://www.gnu.org/licenses/>.
#
# Modified by Garth N. Wells, 2012
#
# First added:  2008-10-22
# Last changed: 2012-08-18

__all__ = ["AutoSubDomain", "DirichletBC", "PeriodicBC", "homogenize"]

import types

import dolfin.cpp as cpp
from dolfin.functions.constant import Constant
from dolfin.compilemodules.subdomains import compile_subdomains
import ufl
from dolfin.fem.projection import project

class AutoSubDomain(cpp.SubDomain):
    "Wrapper class for creating a SubDomain from an inside() function."

    def __init__(self, inside_function):
        "Create SubDomain subclass for given inside() function"

        # Check that we get a function
        if not isinstance(inside_function, types.FunctionType):
            cpp.dolfin_error("bcs.py",
                             "auto-create subdomain",
                             "Expecting a function (not %s)" % \
                                 str(type(inside_function)))
        self.inside_function = inside_function

        # Check the number of arguments
        if not inside_function.func_code.co_argcount in (1, 2):
            cpp.dolfin_error("bcs.py",
                             "auto-create subdomain",
                             "Expecting a function of the form inside(x) or inside(x, on_boundary)")
        self.num_args = inside_function.func_code.co_argcount

        cpp.SubDomain.__init__(self)

    def inside(self, x, on_boundary):
        "Return true for points inside the subdomain"

        if self.num_args == 1:
            return self.inside_function(x)
        else:
            return self.inside_function(x, on_boundary)

class DirichletBC(cpp.DirichletBC):

    # Reuse doc-string from cpp.DirichletBC
    __doc__ = cpp.DirichletBC.__doc__

    def __init__(self, *args, **kwargs):
        "Create Dirichlet boundary condition"

        # Copy constructor
        if len(args) == 1:
            if not isinstance(args[0], cpp.DirichletBC):
                cpp.dolfin_error("bcs.py",
                                 "create DirichletBC",
                                 "Expecting a DirichleBC as only argument"\
                                 " for copy constructor")

            # Initialize base class
            cpp.DirichletBC.__init__(self, args[0])
            return

        # Special case for value specified as float, tuple or similar
        if len(args) >= 2 and not isinstance(args[1], cpp.GenericFunction):
            if isinstance(args[1], ufl.classes.Expr):
                expr = project(args[1], args[0])
            else:
                expr = Constant(args[1]) # let Constant handle all problems
            args = args[:1] + (expr,) + args[2:]

        # Special case for sub domain specified as a function
        if len(args) >= 3 and isinstance(args[2], types.FunctionType):
            sub_domain = AutoSubDomain(args[2])
            args = args[:2] + (sub_domain,) + args[3:]

        # Special case for sub domain specified as a string
        if len(args) >= 3 and isinstance(args[2], str):
            sub_domain = compile_subdomains(args[2])
            args = args[:2] + (sub_domain,) + args[3:]

        # Store Expression to avoid scoping issue with SWIG directors
        if isinstance(args[1], cpp.Expression):
            self.function_arg = args[1]

        # Store SubDomain to avoid scoping issue with SWIG directors
        self.domain_args = args[2:]

        # Add method argument if it's given
        if "method" in kwargs:
            args = tuple(list(args) + [kwargs["method"]])

        # Initialize base class
        cpp.DirichletBC.__init__(self, *args)

    # Set doc string
    __init__.__doc__ = cpp.DirichletBC.__init__.__doc__

# Creattion of Python class to avoid issue of SWIG directors going out
# of scope
class PeriodicBC(cpp.PeriodicBC):

    # Reuse doc-string from cpp.PeriodicBC
    __doc__ = cpp.PeriodicBC.__doc__

    def __init__(self, *args, **kwargs):
        "Create Periodic boundary condition"

        # Copy constructor
        if len(args) == 1:
            if not isinstance(args[0], cpp.PeriodicBC):
                cpp.dolfin_error("bcs.py",
                                 "create PeriodicBC",
                                 "Expecting a DirichleBC as only argument"\
                                 " for copy constructor")

            # Initialize base class
            cpp.PeriodicBC.__init__(self, args[0])

        elif len(args) == 2:
            if not isinstance(args[0], cpp.FunctionSpace):
                cpp.dolfin_error("bcs.py",
                                 "create PeriodicBC",
                                 "Expecting a FunctionSpace as first"\
                                 " constructor argument")

            if not isinstance(args[1], cpp.SubDomain):
                cpp.dolfin_error("bcs.py",
                                 "create PeriodicBC",
                                 "Expecting a SubDomain as second"\
                                 " constructor argument")

            # Store SubDomain to avoid scoping issue with SWIG directors
            self.domain_args = args[1:]

            # Initialize base class
            cpp.PeriodicBC.__init__(self, *args)

        else:
            cpp.dolfin_error("bcs.py",
                             "create PeriodicBC",
                             "Too many arguments passed to constructor")

    # Set doc string
    __init__.__doc__ = cpp.PeriodicBC.__init__.__doc__


def homogenize(bc):
    """
    Return a homogeneous version of the given boundary condition.

    *Arguments*
        bc
            a :py:class:`DirichletBC <dolfin.fem.bcs.DirichletBC>` instance,
            or a list/tuple of
            :py:class:`DirichletBC <dolfin.fem.bcs.DirichletBC>` instances.

    Other types of boundary conditions, like periodic, are ignored.

    If the given boundary condition is a list of boundary conditions,
    then a list of homogeneous boundary conditions is returned.

    """

    # Handle case when boundary condition is a list
    if isinstance(bc, (list, tuple)):
        bcs = bc
        return [homogenize(bc) for bc in bcs]

    # Only consider Dirichlet boundary conditions
    if not isinstance(bc, cpp.DirichletBC):
        return bc

    # Create zero function
    V = bc.function_space()
    if V.element().value_rank() == 0:
        zero = Constant(0)
    elif V.element().value_rank() == 1:
        zero = Constant([0]*V.element().value_dimension(0))
    else:
        cpp.dolfin_error("bcs.py",
                         "homogenize boundary condition",
                         "Unhandled value rank %d for homogenization of boundary conditions" % \
                             V.element().value_rank())

    # Create homogeneous boundary condition
    if len(bc.domain_args) == 1:
        new_bc = cpp.DirichletBC(V, zero, bc.domain_args[0])
    elif len(bc.domain_args) == 2:
        new_bc = cpp.DirichletBC(V, zero, bc.domain_args[0], bc.domain_args[1])
    else:
        cpp.dolfin_error("bcs.py",
                         "homogenize boundary condition",
                         "Unknown type of boundary specification")
    new_bc.domain_args = bc.domain_args

    return new_bc
