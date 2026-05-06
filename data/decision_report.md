# Decision Report

- generated_at: 2026-05-06T20:52:38.769256+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3499**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3499, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/13 | 30.8% | +1.90% | **+0.59%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.98% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.04% | **+0.03%** |
| ASK | 20/20 | 100.0% | +0.01% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +7.41% | **+3.18%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.93% | **+0.88%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.00% | **+0.85%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.36% | **+0.82%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.48% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 51件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T20:52:35.313132+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=81280.1
- Funnel: target 765 → liquid 196 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.7 >= 65=1, 4h RSI 84.3 >= 65=1, 4h RSI 67.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +50.29% | $11,505,679.23 |
| ZEREBRO/USDT:USDT | +11.05% | $1,170,274.09 |
| ARMSTOCK/USDT:USDT | +8.16% | $7,008,639.69 |
| DOGS/USDT:USDT | +8.13% | $6,680,315.10 |
| SMCISTOCK/USDT:USDT | +7.89% | $9,767,276.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOGS/USDT:USDT | below_1h_threshold | +2.98% | +3.15% |
| UB/USDT:USDT | below_1h_threshold | +2.86% | +3.02% |
| BILL/USDT:USDT | below_1h_threshold | +1.66% | +1.82% |
| PANWSTOCK/USDT:USDT | below_1h_threshold | +1.50% | +1.67% |
| RIVER/USDT:USDT | below_1h_threshold | +1.39% | +1.55% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
