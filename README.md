# Command engine (I didn't come up with a better name lol)

First of all, this project is made for my intertainment. I'm not planning to make it like a serios thing, it's just an experiment slash training or whatever you call it, I do it just for fun and to see what I can make and train a bit for my future studies/work.

Then, after I pointed out this one little thing, I thing I can finally start talking about functionality and possibilities!

## Basis

This little console program is made in Python 3.10.5. I got inspired by Linux with its commands and remembered my idea to make a small "engine" where you could create commands and execute them pretty much how you do in Linux or cmd in Windows. It was more practical idea as a helping package / little library. In each assignment we were given a number of tasks that you write as a sepirate def function, and since I LOVE overcomplicating things, each time I made it so you type a number of task you want to execute, and the programs executes it. Then we had final project for which I wanted to go a bit against the rules and make a library for python, and I wanted to add this engine there. But I woke up too late and I had roughly 2 days to complite my project so I gave up this idea.

And now after a half of a trimester studying Operating Systems (Linux) subject I remembered it a decided to finally make it. By the way, looking back I think it was a right decision to not make this "engine" then, because now when I finally started it, I understamd that it is far more complex than I thought back then. But I'm glad I'm making it because it is SOOO much fun!

Alright, after this long prelude I can finally start talking about things.

# Commands

## Briefly about how it works

First, I want to say how it works. Each command is a sepirate Python file. Like in Linux, commands have options and can take arguments. It works the same as in Linux:

> command -(options) [arguments followed by single space]

For example let's see on 'yell' command.

input:
> yell Hello, World!

output:
> Hello, World!

You see, it's that simple. And now about one function with options.

input:
> var -l a

output:
> a: 1

I'll explain each function so don't bother trying to figure out what's happening now.

## List of commands

### yell

I already showed you how it works but let me show again.

> input:
```command-engine
yell Hello, World!
```

> output:
```command-engine
Hello, World!
```

---

**Options**

It doesn't have options yet.

**Arguments**

As an argument, it takes text. You don't need to write it inside of quotes or something like that because now it can't output variables' names or anything. And I don't really know whether I will add it into THIS command or make a new one for this particular thing.

### var

This command creates variables. Keep in mind that each engine has it's own space and they don't share them. So if you create two different engine objects, let's say engine1 and engine2, and create a variable 'a' in engine1, it won't be available for engine2. Let's go on.

**options**

- var (no options) [name] [value] : creates a variable and assigns it a value (if you don't write a value, it will be set to None by default)

> input:
```command-engine
var a 1
```

> output:
```command-engine
Variable 'a' set to '1'.
```

- var -l [no argumens] : will list all the existing variables

> input:
```command-engine
var -l
```

> output:

```command-engine
Current variables:
a: 1
b: 2
c: 3
```

- var -l [name] : will show the variable and it's value

> input:
```command-engine
var -l a
```

> output:

```command-engine
a: 1
```

- var -d [name] : deletes a variable

> input:
```command-engine
var -d a
```

> output:

```command-engine
Variable 'a' deleted.
```

- var -c : deletes all the variables

> input:
```command-engine
var -c
```

> output:

```command-engine
All variables cleared.
```

### version

This command is pretty simple. It doesn't have any options and doesn't take arguments. All it does is outputs the version of this project

> input:
```command-engine
version
```

> output:

```command-engine
Alpha 1
```

### ghost

This one is funny because it is a crutch. It literally does nothing. It even doesn't output anything.

> input:
```command-engine
ghost
```

> output:

```command-engine

```

It was made made to create comments. Talking about comments...

### comments

Everything that even looks like programming language or command engine should have a possibility to write comments. As in many languages, comments start with the '#' sign. EVERYTHING that goes after it will be ignored by the console. You can write them individually like this.

> input:
```command-engine
# This is a comment!
```

> output:

```command-engine

```

Or you can write them after commands like this.

> input:
```command-engine
yell Hello, World! # Goodbye, World!
```

> output:

```command-engine
Hello, World!
```

Remember, everything that goes after the '#' sign will be interpretated as a comment. So this thing:

> input:
```command-engine
var #comment a 1
```

> output:

```command-engine
Error: Variable name is required.
```

### sign

This one is small too. It's just an analog of VAR1 command from Linux. Let's see.

> input:
```command-engine
sign ->
```

> output:

`-> `

By default it looks like this

`>> yell Hi!`

And after we executed "sign ->" it turned into this:

`-> yell Hi!`

If you want to turn it back to the default sign, you can use the '--d' option.

> input:
`-> sign --d`

> output:
`>> `

Note that if you use this options, everything you type after it (that would be considered as arguments) will be ignored.

> input:
`-> sign --d some nonesense`

> output:
`>> `

This command is quite unique because it pecieves everything you write differntly that other commands. You can (almost) freely use the '-' character and it won't be considered as an option. The only thing that is considered as an option is "--d". You can even do something like this.

> input:
```command-engine
sign Hello, World!~
```

> output:
`Hello, World!~ `

### run

This is my personal favourite one! This command can use .txt files as scripts. Let's say I have a hello.txt file.

```txt
yell Hello, Wordl! # print the message
var x 1
var -l x
yell Goodbye, World!

# this is a comment
yell I'm back >:)
```

And it has this path:
> command-engine\src\scripts\hello.txt

So let's try to execute it. The command only takes one argument, which is a path to your script, and has no options.

> input
```command-engine
run command-engine\src\scripts\hello.txt
```

> output:
```command-engine
Hello, Wordl!
Variable 'x' set to '1'.
x: 1
Goodbye, World!
I'm back >:)
```

See? Isn't that cool?! Also look at hello.txt again. There you can the use of comments and even an empty line. Naturally, the engine doesn't allow any empty lines and will throw an error. But if you have an empty line in your script, it will simply be ignored.

### exit

This command just stops the engine.

> input
```command-engine
exit
```

> output:
```command-engine
Exiting the engine...
```

And then it will return back to your program.

### pipe

> Currently in development

### history

> I decided to rework it so I turned it off for a while