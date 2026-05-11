# Decision Report

- generated_at: 2026-05-11T06:47:54.839148+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4012**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.69% / filled 20/20。**
- 全期間 MARKET基準: n=4012, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |
| ASK | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_BB3S | 5/11 | 45.5% | +2.21% | **+1.01%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.88% | **+0.66%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.99% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.57% | **+0.11%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.03% | **+0.03%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.15% | **-0.07%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | -0.13% | **-0.08%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$99.20** / 初期 $100.00 (-0.80%)
- 確定トレード: 31件 (TP 8 / SL 20 / EXP 3)
- 最新: NAORIS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 355件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T06:47:48.579026+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=80760.5
- Funnel: target 777 → liquid 180 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.4 >= 65=1, 4h RSI 65.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +33.17% | $10,845,387.04 |
| B/USDT:USDT | +27.50% | $4,887,788.77 |
| ALCH/USDT:USDT | +17.71% | $4,516,014.31 |
| TROLLSOL/USDT:USDT | +17.52% | $5,209,206.14 |
| SAGA/USDT:USDT | +15.07% | $1,305,332.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +4.80% | +4.85% |
| OPG/USDT:USDT | below_1h_threshold | +1.03% | +1.07% |
| OG/USDT:USDT | below_1h_threshold | +0.90% | +0.95% |
| BAS/USDT:USDT | below_1h_threshold | +0.81% | +0.86% |
| US/USDT:USDT | below_1h_threshold | +0.78% | +0.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
