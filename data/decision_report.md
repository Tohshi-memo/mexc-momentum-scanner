# Decision Report

- generated_at: 2026-06-14T22:50:05.606893+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6708**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6708, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.01% | **-0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +0.80% | **+0.64%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.82% | **+0.57%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.88% | **+0.56%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.37% | **+1.35%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.75% | **+0.79%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.83% | **+0.50%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$172.74** / 初期 $100.00 (+72.74%)
- 確定: 1581件 (Win 420 / Loss 498 / Flat 663) / skip 1688件
- 成長率目線: 平均log +0.000346 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FARTCOIN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $172.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.70** / 初期 $100.00 (-1.30%)
- 確定: 78件 (Win 20 / Loss 15 / Flat 43) / skip 41件
- 成長率目線: 平均log -0.000168 / 幾何平均 -0.017% per trade / maxDD +2.07%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0481 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FARTCOIN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $98.70

## 5. Latest Market Context

- 更新: 2026-06-14T22:49:58.235407+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=65393.2
- Funnel: target 770 → liquid 137 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPG/USDT:USDT | +43.29% | $4,423,442.24 |
| BABY/USDT:USDT | +15.36% | $2,102,753.72 |
| EDEN/USDT:USDT | +13.18% | $1,287,394.15 |
| BP/USDT:USDT | +12.90% | $1,092,115.40 |
| LAB/USDT:USDT | +11.53% | $9,734,236.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BABY/USDT:USDT | below_1h_threshold | +3.79% | +3.63% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +2.55% | +2.38% |
| ZEC/USDT:USDT | below_1h_threshold | +2.42% | +2.26% |
| DASH/USDT:USDT | below_1h_threshold | +2.29% | +2.12% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.07% | +1.91% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
