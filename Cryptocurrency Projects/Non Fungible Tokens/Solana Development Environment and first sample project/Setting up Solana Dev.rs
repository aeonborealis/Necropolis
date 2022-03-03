// Setting up Solana Development Environment 

// We are going to use Anchor, a framework for Solana which is in active development
// The main purpose of Anchor is to provide convenient tools for developers o write Solana Programs
// Instead of spending time working on the tedious part pf Raw Solana Programs 

// *Important Note: Anchor only runs on x86_64 Linux environments, and will not run in 32 bit Mode. 

// Setting up WSL

// Open the Terminal and install WSL:
// wsl --install

// Once the installation is complete restard your computer

// Once you have a virtualization of Ubuntu on your computer

// 1. Install curl type the following into your terminal:
// sudo apt-get install curl 

// 2. Install nvm 
// curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash

// To verify your nvm installation run the following command in your terminal after restarting your computer
// command -v nvm

// The previous command will return the Version of nvm installed on your machine
// Now install Node using nvm 

// nvm install --lts 

// Installing Rust

// Install Rust via terminal with the following code: 
// curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

// Verify that Rust was correctly installed as well as the rust compiler 
// rustup --version
// rustc --version

// That should have also installed Cargo, a rust package manager 
// To verify the Cargo installation run the following command: 

// cargo --version 

// Installing Solana 
// run the following command in your terminal 
// sh -c "$(curl -sSfL https://release.solana.com/stable/install)"

// once the installation is complete verify it was succesfully installed: 
// solana --version

// Installing Anchor
// sudo apt-get update && sudo apt-get upgrade && sudo apt-get install -y pkg-config build-essential libudev-dev

// Once the dependencies are installed, use Cargo to install Anchor’s CLI.
// cargo install --git https://github.com/project-serum/anchor --tag v0.20.1 anchor-cli --locked

// Finally, verify Anchors CLI is installed correctly: 
// anchor --version

// Generate Paper Wallet 
// For us to test our Solana program, we need to have a crypto wallet.
// A crypto wallet stores collections of keys used to send and receive cryptocurrencies.

// To generate a paper wallet, we will use solana-keygen , which should have been installed when we installed solana. 
// To verify run the following command:
// solana-keygen --version

// If you see the version of solana-keygen, that means we can start using it.
// Run the following command to generate a keypair.
// solana-keygen new

// This will generate a random seed phrase and prompt you to add an optional passphrase.

// Running the localnet Cluster
// To run our Solana Program we need to be in a cluster. 
// According to the Solana documentation, 
// a Solana cluster is a set of validators working together to serve client transactions and maintain the integrity of the ledger.

// currently Solana has the followng Clusters: 
// devnet
// testnet
// mainnet 

// It is possible to connect to localnet, which is the cluster run in our local machine in localhost. To connect to localnet, we will use Solana CLI.
// solana config set --url localhost

// Now Verify your connection: 
// solana config get

// The terminal should display the RPC URL, the Websocket URL and the keypair path. 
// by default it will connect to port 8899 for RPC and port 8900 for Websocket

// Starting a Project with Anchor Framework 

// Use Anchor's CLI to start a new project. The following command is the syntax to initialize a new project. 
// anchor init <new-project-name>

// We are going to give the name of "mySolanaProgram"
// anchor init mySolanaProgram 

// This will create a new folder with the name of the project. 
// This will create a directory propopulated with several working directories for your project
// this is extremely helpful because it is a great way to get up and running with Solana super quick. 

// Working on the Solana Program
// Notice there is a lib.rs file that lives in the programs/mySolanaProgram/src folder.
// In there, it lives the Solana program, or smart contract. Notice the file extension finishes in rs which means it is a Rust file.

// Open the lib.rs file 
// You should see code similar to the following: 

use anchor_lang::prelude::*;

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program]
pub mod my_solana_program {
    use super::*;
    pub fn initialize(ctx: Context<Initialize>) -> ProgramResult {
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize {}

// If you don’t have previous knowledge of Rust, this won’t make sense at all. 
// The first line of code is a way to import dependencies or libraries in Rust. In this case, it is importing the anchor library.

// use anchor_lang::prelude::*;

// The declareId is where Solana stores the address or program id of your program. By default, Anchor generates a program id for us.

// declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

// Then, you will see a #[program] section. This is the program module and is where the logic of the program lives.

// #[program]
// pub mod my_solana_program {
//    use super::*;
//    pub fn initialize(ctx: Context<Initialize>) -> ProgramResult {
//        Ok(())
//    }
// }

// Finally, there is a #[derive(Acccounts)] section. This is where the Accounts struct lives which is where accounts are validated.

// #[derive(Accounts)]
// pub struct Initialize {}

// You might be wondering what a struct is. A struct defines a group of properties.
// In other words, structs define the structure of the data.

// It’s like defining an interface in TypeScript if you have a background in TypeScript.
// interface Initialize {
// }

// While it is tempting to relate structs as classes or objects, these concepts do not exist in Rust. 
// For example, it is not possible to define methods in structs like you would using another programming language.
// However, it is possible to define functions to access structs.

// You will see the methods manipulating the data are available in the module pub mod my_solana_program. 
// This means, our program will have to pass data by reference from the outside in order to modify it.

// This is one of the main differences between Solana and Ethereum
// Solana’s goal is to separate code and data.
// This means the logic could be applied to other pieces of data. That’s why Solana programs are considered stateless contracts.

// Updating the Solana Program

// Update the logic of the program using the following code. I recommend giving it a look and trying to understand what is going on

#[program]
pub mod my_solana_program {
    use super::*;
    pub fn setup_platform(ctx: Context<TweetPlatform>) -> ProgramResult {
        let tweet = &mut ctx.accounts.tweet;
        tweet.likes = 0;
        tweet.message = ("").to_string();
        Ok(())
    }

    pub fn write_tweet(
        ctx: Context<WriteTweet>,
        message: String,
        user_public_key: Pubkey
    ) -> ProgramResult {
        let tweet = &mut ctx.accounts.tweet;

        if !tweet.message.trim().is_empty() {
            return Err(Errors::CannotUpdateTweet.into());
        }

        if message.trim().is_empty() {
            return Err(Errors::EmtpyMessage.into());
        }

        tweet.message = message;
        tweet.likes = 0;
        tweet.creator = user_public_key;

        Ok(())
    }

    pub fn like_tweet(ctx: Context<LikeTweet>, user_liking_tweet: Pubkey) -> ProgramResult {
        let tweet = &mut ctx.accounts.tweet;

        if tweet.message.trim().is_empty() {
            return Err(Errors::NotValidTweet.into());
        }

        if tweet.likes == 5 {
            return Err(Errors::ReachedMaxLikes.into());
        }

        let mut iter = tweet.people_who_liked.iter();
        if iter.any(|&v| v == user_liking_tweet) {
            return Err(Errors::UserLikedTweet.into());
        }

        tweet.likes += 1;
        tweet.people_who_liked.push(user_liking_tweet);

        Ok(())
    }
}

#[derive(Accounts)]
pub struct TweetPlatform<'info> {
    #[account(init, payer = user, space = 9000 )]
    pub tweet: Account<'info, Tweet>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct WriteTweet<'info> {
    #[account(mut)]
    pub tweet: Account<'info, Tweet>,
}

#[derive(Accounts)]
pub struct LikeTweet<'info> {
    #[account(mut)]
    pub tweet: Account<'info, Tweet>
}

#[account] //An attribute for a data structure representing a Solana account.
#[derive(Default)]
pub struct Tweet {
    message: String,
    likes: u8,
    creator: Pubkey,
    people_who_liked: Vec<Pubkey>, // with  #[derive(Default)] we can assign default values
}


#[error]
pub enum Errors {
    #[msg("Tweet message cannot be updated")]
    CannotUpdateTweet,

    #[msg("Message cannot be empty")]
    EmtpyMessage,

    #[msg("Cannot receive more than 5 likes")]
    ReachedMaxLikes,

    #[msg("Cannot like a tweet without a valid message")]
    NotValidTweet,

    #[msg("User has already liked the tweet")]
    UserLikedTweet,
}

// Understanding the Logic 
// What does the program do?

// The main purpose of this Solana program is for a user to write a tweet. The requirements for this program are:
// Only one person can write a tweet
// The tweet's message cannot be empty
// a user cannot like a tweet more than once. 

// Break down the logical rules above: they can be reworked as a simple way to write and fetch data from an API, and can be used to script
// Functionality of an API as a Solana component.

// Defining the Program Errors
// Let’s start with the bottom of the code. It is an enum of Errors, and it is used to define each of the errors.

#[error]
pub enum Errors {
    #[msg("Tweet message cannot be updated")]
    CannotUpdateTweet,

    #[msg("Message cannot be empty")]
    EmtpyMessage,

    #[msg("Cannot receive more than 5 likes")]
    ReachedMaxLikes,

    #[msg("Cannot like a tweet without a valid message")]
    NotValidTweet,

    #[msg("User has already liked the tweet")]
    UserLikedTweet,
}


// Notice the attribute #[error] above the enum Errors. This attribute is provided by anchor_lang library,
// which is imported at the top of the file.

#[error]
pub enum Errors {
    #[msg("Tweet message cannot be updated")]
    CannotUpdateTweet
}

// Notice how there is a #[msg()] attribute right above each enum error. This allows us to define a user-friendly error message.

// In the following snippet of code, we show you how to throw one of the enum Errors by using the Err 
// which represents a result type containing a value, value we provide using into(). For instance, we return the error CannotUpdateTweet
// using the following syntax Err(Errors::CannotUpdateTweet.into()) if the message of the tweet is not empty.

pub fn write_tweet(
    ctx: Context<WriteTweet>,
    message: String,
    user_public_key: Pubkey
) -> ProgramResult {
    // some logic

    if !tweet.message.trim().is_empty() {
        return Err(Errors::CannotUpdateTweet.into());
    }

    // more logic
}

// Defining the Structures
// Let’s move on to defining the structs, or the structures of data.

#[derive(Accounts)]
pub struct TweetPlatform<'info> {
    #[account(init, payer = user, space = 9000 )]
    pub tweet: Account<'info, Tweet>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct WriteTweet<'info> {
    #[account(mut)]
    pub tweet: Account<'info, Tweet>,
}

#[derive(Accounts)]
pub struct LikeTweet<'info> {
    #[account(mut)]
    pub tweet: Account<'info, Tweet>
}

#[account]
#[derive(Default)]
pub struct Tweet {
    message: String,
    likes: u8,
    creator: Pubkey,
    people_who_liked: Vec<Pubkey>
}

// Let’s start with the struct where the main logic of the program is based on, the Tweet struct.

#[account]
#[derive(Default)]
pub struct Tweet {
    message: String,
    likes: u8,
    creator: Pubkey,
    people_who_liked: Vec<Pubkey>
}

// It is incorrect to call message, likes, creator, and people_who_liked “properties”. 
// However, you can think of them in that way to relate if you are coming from object-oriented programming.

// The String type is itself a string, but the other types you might not be familiar with.
// u8 is an unsigned integer type.
// Pubkey is a public key type of a solana account.
// Vec<> is a growable array type. Hence, Vec<Pubkey> is a growable array type of public key types.

// There is the #[account] attribute and it defines the data structure of a Solana account. 
// One of the main characteristics of this attribute is to generate implementations to serialize and deserialize an account
// According to the docs, when implementing account serialization traits the first 8 bytes are reserved for a unique account discriminator, 
// self-described by the first 8 bytes of the SHA256 of the account’s Rust ident.AccountSerialize.

// Finally, there is #[derive(Default)], and it allows defining default values for the pieces of data whenever the struc is generated.
// Currently, we are not setting default data.

// Let’s move on to the TweetPlatform structure, which contains the tweet, user and system_program pieces of data.

#[derive(Accounts)]
pub struct TweetPlatform<'info> {
    #[account(init, payer = user, space = 9000 )]
    pub tweet: Account<'info, Tweet>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Pay attention to the use of the derive attribute #[derive(Accounts)]. This allows deserializing the Solana accounts 
// so they can be validated and prevent account substitution attacks. 
// A derive attribute allows new items to be automatically generated for data structures

#[account(init, payer = user, space = 9000 )]
 pub tweet: Account<'info, Tweet>

// Notice the use of init attribute for the tweet field.
// In other words, this will create a new account owned by the current program.
// Using init requires someone to pay for creating the account.

#[account(init, payer = user, space = 9000 )]
 pub tweet: Account<'info, Tweet>,
 #[account(mut)]
 pub user: Signer<'info>,

// In this case, the user field is defined as the account that will provide the funds to create the tweet account.
// Finally, there is the space attribute. This defines how large the tweet account should be. For the purposes of this tutorial,
// we assigned 9000, but this should be calculated beforehand to know how much space it will occupy the program.

// When using the init attribute, we must provide the system_program . This is required by the runtime to create the account.

pub system_program: Program<'info, System>,

// Finally, we have the WriteTweet and LikeTweet structs.

#[derive(Accounts)]
pub struct WriteTweet<'info> {
    #[account(mut)]
    pub tweet: Account<'info, Tweet>,
}

#[derive(Accounts)]
pub struct LikeTweet<'info> {
    #[account(mut)]
    pub tweet: Account<'info, Tweet>
}

// Hence, there are two flags you must take into consideration. The init and the mut flags. 
// The first is used when the account (tweet) is used for the first time and the mut is used to persist any changes, 
// for instance, writing a value to message or updating the likes field.

// Defining instructions in the module
// It’s time to talk about the methods defined in the module. 
// These are called instructions. Based on Solana documentation, an instruction specifies a single program, 
// a subset of the transaction’s accounts that should be passed to the program
// and a data byte array that is passed to the program. 
// The program interprets the data array and operates on the accounts specified by the instructions.

#[program]
pub mod my_solana_program {
    use super::*;
    pub fn setup_platform(ctx: Context<TweetPlatform>) -> ProgramResult {
        let tweet = &mut ctx.accounts.tweet;
        tweet.likes = 0;
        tweet.message = ("").to_string();
        Ok(())
    }

    pub fn write_tweet(
        ctx: Context<WriteTweet>,
        message: String,
        user_public_key: Pubkey
    ) -> ProgramResult {
        let tweet = &mut ctx.accounts.tweet;

        if !tweet.message.trim().is_empty() {
            return Err(Errors::CannotUpdateTweet.into());
        }

        if message.trim().is_empty() {
            return Err(Errors::EmtpyMessage.into());
        }

        tweet.message = message;
        tweet.likes = 0;
        tweet.creator = user_public_key;

        Ok(())
    }

    pub fn like_tweet(ctx: Context<LikeTweet>, user_liking_tweet: Pubkey) -> ProgramResult {
        let tweet = &mut ctx.accounts.tweet;

        if tweet.message.trim().is_empty() {
            return Err(Errors::NotValidTweet.into());
        }

        if tweet.likes == 5 {
            return Err(Errors::ReachedMaxLikes.into());
        }

        let mut iter = tweet.people_who_liked.iter();
        if iter.any(|&v| v == user_liking_tweet) {
            return Err(Errors::UserLikedTweet.into());
        }

        tweet.likes += 1;
        tweet.people_who_liked.push(user_liking_tweet);

        Ok(())
    }
}

// Let’s start with the setup_platform method.

pub fn setup_platform(ctx: Context<TweetPlatform>) -> ProgramResult {
    let tweet = &mut ctx.accounts.tweet;
    tweet.likes = 0;
    tweet.message = ("").to_string();
    Ok(())
}

// The first thing to notice is the usage of a ctx parameter via Context<>. The Context<> deserializes the accounts 
// found in the struct type passed, in this case, the TweetPlatform. That’s why you can access the field tweet when using ctx.accounts.

// There are other data fields you can access via ctx parameter

// program_id: The current executing program id.
// remaining_accounts: Other accounts given but not deserialized or validated.
// Which we are not using, but it is important to know about in case we need access to other data fields of a struct.

// Also, we use the keyword &mut to get the mutable reference of the tweet data field. 
// Remember, Solana programs are considered stateless contracts. This means there are no variables 
// and data must be passed from the outside if we want to modify it.

let tweet = &mut ctx.accounts.tweet;

// While the setup_platform instruction doesn’t seem to do much besides setting the likes data to 
// 0 and the message to an empty string, it is important to remember this process must happen as the 
// TweetPlatform struc uses the init attribute to create tweet account.

// Now, let’s look a the write_tweet instruction.

pub fn write_tweet(
    ctx: Context<WriteTweet>,
    message: String,
    user_public_key: Pubkey
) -> ProgramResult {
    let tweet = &mut ctx.accounts.tweet;

    if !tweet.message.trim().is_empty() {
        return Err(Errors::CannotUpdateTweet.into());
    }

    if message.trim().is_empty() {
        return Err(Errors::EmtpyMessage.into());
    }

    tweet.message = message;
    tweet.likes = 0;
    tweet.creator = user_public_key;

    Ok(())
}

// There are two new things happening in this instruction.

// One of them is for the Solana program to accept incoming data used to modify an account (tweet).
//  Besides accepting the context ctx: Context<WriteTweet>, which we used to deserialize and access tweet account,

// A user can pass a message.
// A user can pass their user_public_key to “write” a new tweet and identify the creator or owner of the tweet.

// The second new part is to apply restrictions to the tweet account.

// Cannot overwrite a tweet.message if the tweet.message has already data.
// Cannot write an empty tweet.message if the message provided by the external user is empty.

// This allows us to use our custom program errors in case any of these fails.

// If you paid close attention, we used the WriteTweet struct which uses the mut attribute on the tweet account. Remember, 
// this attribute marks the account as mutable and persists changes. That’s why, if we access the tweet account in a 
// different instruction such as like_tweet, we can add additional check to verify the tweet.message is not empty,
//  which infers the tweet.message should have been previously updated in the write_tweet instruction.

// Finally, we have the like_tweet instruction.

pub fn like_tweet(ctx: Context<LikeTweet>, user_liking_tweet: Pubkey) -> ProgramResult {
    let tweet = &mut ctx.accounts.tweet;

    if tweet.message.trim().is_empty() {
        return Err(Errors::NotValidTweet.into());
    }

    if tweet.likes == 5 {
        return Err(Errors::ReachedMaxLikes.into());
    }

    let mut iter = tweet.people_who_liked.iter();
    if iter.any(|&v| v == user_liking_tweet) {
        return Err(Errors::UserLikedTweet.into());
    }

    tweet.likes += 1;
    tweet.people_who_liked.push(user_liking_tweet);

    Ok(())
}


// Probably, the only part it might be new for those without much
// Rust experience is the way we are checking if a new user has liked a tweet before or not.

let mut iter = tweet.people_who_liked.iter();
if iter.any(|&v| v == user_liking_tweet) {
    return Err(Errors::UserLikedTweet.into());
}


tweet.people_who_liked.push(user_liking_tweet);

// Build the program
// After you added all the program logic in the lib.rs file, go ahead and build the program using the following command.

// anchor build

//Testing the program
// If you haven’t written many programmatic tests in the past, you will find writing tests more often than what you have
// ever done in your career when working in web3.

// When we created this project using the Anchor framework, it generated a tests/mySolanaProgram.ts file.
// Update the mySolanaProgram.ts file with the following tests.

import * as anchor from '@project-serum/anchor';
import { Program } from '@project-serum/anchor';
import { MySolanaProgram } from '../target/types/my_solana_program';
import { expect, assert } from 'chai';

describe('mySolanaProgram', () => {

  // Configure the client to use the local cluster.
  anchor.setProvider(anchor.Provider.env());

  const program = anchor.workspace.MySolanaProgram as Program<MySolanaProgram>;
  it('setup tweet platform!', async () => {
    const tweetKeypair = anchor.web3.Keypair.generate();
    const user = program.provider.wallet;
    await program.rpc.setupPlatform({
      accounts: {
        tweet: tweetKeypair.publicKey,
        user: user.publicKey,
        systemProgram: anchor.web3.SystemProgram.programId
      },
      signers: [tweetKeypair]
    });

    let tweet = await program.account.tweet.fetch(tweetKeypair.publicKey);
    expect(tweet.likes).to.equal(0);
    expect(tweet.message).to.equal('');
  });

  it('Write a tweet', async () => {
    const tweetKeypair = anchor.web3.Keypair.generate();
    const user = program.provider.wallet;
    await program.rpc.setupPlatform({
      accounts: {
        tweet: tweetKeypair.publicKey,
        user: user.publicKey,
        systemProgram: anchor.web3.SystemProgram.programId
      },
      signers: [tweetKeypair]
    });

    let tweet = await program.account.tweet.fetch(tweetKeypair.publicKey);
    expect(tweet.likes).to.equal(0);
    expect(tweet.message).to.equal('');

    await program.rpc.writeTweet('Hello World!', user.publicKey, {
      accounts: {
        tweet: tweetKeypair.publicKey,
      },
      signers: []
    });

    tweet = await program.account.tweet.fetch(tweetKeypair.publicKey);

    expect(tweet.likes).to.equal(0);
    expect(tweet.message).to.equal('Hello World!');
    expect(tweet.creator.toString()).to.equal(user.publicKey.toString());
  });

  it('should like tweet up no more than 5 times', async () => {
    const tweetKeypair = anchor.web3.Keypair.generate();
    const user = program.provider.wallet;
    await program.rpc.setupPlatform({
      accounts: {
        tweet: tweetKeypair.publicKey,
        user: user.publicKey,
        systemProgram: anchor.web3.SystemProgram.programId
      },
      signers: [tweetKeypair]
    });

    let tweet = await program.account.tweet.fetch(tweetKeypair.publicKey);
    expect(tweet.likes).to.equal(0);
    expect(tweet.message).to.equal('');

    await program.rpc.writeTweet('Hello World!', user.publicKey, {
      accounts: {
        tweet: tweetKeypair.publicKey,
      },
      signers: []
    });

    tweet = await program.account.tweet.fetch(tweetKeypair.publicKey);
    expect(tweet.likes).to.equal(0);
    expect(tweet.message).to.equal('Hello World!');
    expect(tweet.creator.toString()).to.equal(user.publicKey.toString());

    await program.rpc.likeTweet(user.publicKey, {
      accounts: {
        tweet: tweetKeypair.publicKey,
      },
      signers: []
    });

    tweet = await program.account.tweet.fetch(tweetKeypair.publicKey);
    expect(tweet.likes).to.equal(1);
    expect(tweet.peopleWhoLiked[0].toString()).to.equal(user.publicKey.toString());

    try {
      await program.rpc.likeTweet(user.publicKey, {
        accounts: {
          tweet: tweetKeypair.publicKey,
        },
        signers: []
      });

      assert.ok(false);
    } catch (error) {
      console.log('error ', error.toString());
      const expectedError = 'User has already liked the tweet';
      assert.equal(error.toString().toString(), expectedError);
    }


    const secondUser = anchor.web3.Keypair.generate();
    await program.rpc.likeTweet(secondUser.publicKey, {
      accounts: {
        tweet: tweetKeypair.publicKey,
      },
      signers: []
    });

    tweet = await program.account.tweet.fetch(tweetKeypair.publicKey);
    expect(tweet.likes).to.equal(2);
    expect(tweet.peopleWhoLiked[1].toString()).to.equal(secondUser.publicKey.toString());



    const thirdUser = anchor.web3.Keypair.generate();
    await program.rpc.likeTweet(thirdUser.publicKey, {
      accounts: {
        tweet: tweetKeypair.publicKey,
      },
      signers: []
    });

    tweet = await program.account.tweet.fetch(tweetKeypair.publicKey);
    expect(tweet.likes).to.equal(3);
    expect(tweet.peopleWhoLiked[2].toString()).to.equal(thirdUser.publicKey.toString());



    const fourthUser = anchor.web3.Keypair.generate();
    await program.rpc.likeTweet(fourthUser.publicKey, {
      accounts: {
        tweet: tweetKeypair.publicKey,
      },
      signers: []
    });

    tweet = await program.account.tweet.fetch(tweetKeypair.publicKey);
    expect(tweet.likes).to.equal(4);
    expect(tweet.peopleWhoLiked[3].toString()).to.equal(fourthUser.publicKey.toString());



    const fifthUser = anchor.web3.Keypair.generate();
    await program.rpc.likeTweet(fifthUser.publicKey, {
      accounts: {
        tweet: tweetKeypair.publicKey,
      },
      signers: []
    });

    tweet = await program.account.tweet.fetch(tweetKeypair.publicKey);
    expect(tweet.likes).to.equal(5);
    expect(tweet.peopleWhoLiked[4].toString()).to.equal(fifthUser.publicKey.toString());


    const sixthUser = anchor.web3.Keypair.generate();
    try {


      await program.rpc.likeTweet(sixthUser.publicKey, {
        accounts: {
          tweet: tweetKeypair.publicKey,
        },
        signers: []
      });

      assert.ok(false);
    } catch (error) {
      console.log('error ', error.toString());
      assert.equal(error.toString().toString(), 'Cannot receive more than 5 likes');
    }
  });

  it('should not allow writting an empty message', async () => {
    const tweetKeypair = anchor.web3.Keypair.generate();
    const user = program.provider.wallet;
    await program.rpc.setupPlatform({
      accounts: {
        tweet: tweetKeypair.publicKey,
        user: user.publicKey,
        systemProgram: anchor.web3.SystemProgram.programId
      },
      signers: [tweetKeypair]
    });

    let tweet = await program.account.tweet.fetch(tweetKeypair.publicKey);
    expect(tweet.likes).to.equal(0);
    expect(tweet.message).to.equal('');


    try {
      await program.rpc.writeTweet('', user.publicKey, {
        accounts: {
          tweet: tweetKeypair.publicKey,
        },
        signers: []
      });
      assert.ok(false);
    } catch (error) {
      assert.equal(error.toString().toString(), 'Message cannot be empty');
    }
  });
});

