# Decision Report

- generated_at: 2026-06-04T21:10:56.837702+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5668**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5668, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-2.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.65% | **-2.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_BB3S | 4/14 | 28.6% | +0.59% | **+0.17%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.45% | **+2.45%** |
| ASK_LONG | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +1.77% | **+1.06%** |
| LIMIT_2PCT_LONG | 8/20 | 40.0% | +2.56% | **+1.02%** |
| LIMIT_5PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.05** / 初期 $100.00 (-1.95%)
- 確定トレード: 99件 (TP 30 / SL 66 / EXP 3)
- 最新: MONAD/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1008件 (Win 239 / Loss 312 / Flat 457) / skip 1221件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T21:10:54.170699+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.33% price=63810.6
- Funnel: target 770 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +32.53% | $5,852,685.51 |
| OPN/USDT:USDT | +30.95% | $37,334,603.88 |
| AAOISTOCK/USDT:USDT | +11.70% | $1,115,029.54 |
| MEME/USDT:USDT | +9.90% | $1,793,732.69 |
| HOME/USDT:USDT | +9.16% | $5,121,810.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +2.18% | +1.85% |
| MEME/USDT:USDT | below_1h_threshold | +2.07% | +1.74% |
| XMR/USDT:USDT | below_1h_threshold | +1.43% | +1.10% |
| SIREN/USDT:USDT | below_1h_threshold | +1.15% | +0.82% |
| FILECOIN/USDT:USDT | below_1h_threshold | +1.12% | +0.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
