# Decision Report

- generated_at: 2026-06-04T19:38:27.150612+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5662**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5662, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +4.56% | **+1.14%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.35% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.63% | **+2.54%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.59% | **+2.07%** |
| ASK_LONG | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.05** / 初期 $100.00 (-1.95%)
- 確定トレード: 99件 (TP 30 / SL 66 / EXP 3)
- 最新: MONAD/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1007件 (Win 239 / Loss 312 / Flat 456) / skip 1216件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T19:38:24.117147+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=63774.3
- Funnel: target 771 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +29.39% | $4,829,678.19 |
| HOME/USDT:USDT | +11.66% | $4,483,016.19 |
| OPN/USDT:USDT | +9.73% | $36,914,237.60 |
| PORTAL/USDT:USDT | +8.39% | $3,007,474.93 |
| MEME/USDT:USDT | +7.84% | $1,717,564.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEME/USDT:USDT | below_1h_threshold | +4.56% | +4.59% |
| OPN/USDT:USDT | below_1h_threshold | +3.79% | +3.82% |
| XPL/USDT:USDT | below_1h_threshold | +1.79% | +1.82% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +1.64% | +1.67% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.51% | +1.53% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
