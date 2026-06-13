# Decision Report

- generated_at: 2026-06-13T13:45:12.940062+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6581**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6581, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.07% | **-1.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.24% | **+0.18%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.01% | **+0.01%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.27% | **-0.11%** |
| LIMIT_ATR | 17/20 | 85.0% | -0.15% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.23% | **+0.67%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.17% | **+0.64%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.26% | **+0.51%** |
| ASK_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.48** / 初期 $100.00 (+64.48%)
- 確定: 1454件 (Win 389 / Loss 464 / Flat 601) / skip 1688件
- 成長率目線: 平均log +0.000342 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $164.48

## 4. Latest Market Context

- 更新: 2026-06-13T13:45:09.249501+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=64151.5
- Funnel: target 770 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +47.91% | $8,929,528.19 |
| COAI/USDT:USDT | +36.64% | $5,561,599.17 |
| RIF/USDT:USDT | +26.83% | $4,546,553.45 |
| TAO/USDT:USDT | +18.84% | $167,230,809.15 |
| EDGE/USDT:USDT | +18.44% | $3,336,108.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDGE/USDT:USDT | below_1h_threshold | +2.86% | +2.79% |
| H/USDT:USDT | below_1h_threshold | +2.78% | +2.71% |
| SQD/USDT:USDT | below_1h_threshold | +2.18% | +2.10% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.16% | +2.09% |
| TAO/USDT:USDT | below_1h_threshold | +1.66% | +1.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
