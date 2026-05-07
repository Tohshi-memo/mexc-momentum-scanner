# Decision Report

- generated_at: 2026-05-07T16:53:19.461887+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3666**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3666, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 12/20 | 60.0% | +2.13% | **+1.28%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_2PCT | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.34% | **+1.52%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.63% | **+1.45%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +3.78% | **+0.95%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$111.18** / 初期 $100.00 (+11.18%)
- 確定: 160件 (Win 46 / Loss 55 / Flat 59) / skip 67件
- 成長率目線: 平均log +0.000663 / 幾何平均 +0.066% per trade / maxDD +2.62%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JTO/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account +0.00% 残高後 $111.18

## 4. Latest Market Context

- 更新: 2026-05-07T16:53:05.512441+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=79837.1
- Funnel: target 771 → liquid 181 → pre 50 → checked 50 → surge 10 → strict 7
- Surge前reject: below_1h_threshold=40, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.3 >= 65=1, 4h RSI 73.9 >= 65=1, 4h RSI 77.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +22.14% | $4,841,600.00 |
| JTO/USDT:USDT | +15.87% | $6,943,740.57 |
| B/USDT:USDT | +8.57% | $4,229,595.48 |
| LAB/USDT:USDT | +7.81% | $271,120,419.19 |
| HIGH/USDT:USDT | +7.06% | $1,356,795.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| M/USDT:USDT | below_1h_threshold | +3.96% | +3.99% |
| AVNT/USDT:USDT | below_1h_threshold | +3.83% | +3.86% |
| PLAY/USDT:USDT | below_1h_threshold | +3.16% | +3.19% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.75% | +2.78% |
| PENGUIN/USDT:USDT | below_1h_threshold | +2.67% | +2.71% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
