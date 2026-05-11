# Decision Report

- generated_at: 2026-05-11T07:28:09.774452+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4017**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.11% / filled 20/20。**
- 全期間 MARKET基準: n=4017, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.11% | **+1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.62% | **+0.89%** |
| ASK | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 10/11 | 90.9% | +0.64% | **+0.58%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.20% | **+0.12%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.57% | **+0.11%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.02% | **-0.01%** |

## 2. $100 Live Portfolio

- 残高: **$98.70** / 初期 $100.00 (-1.30%)
- 確定トレード: 32件 (TP 8 / SL 21 / EXP 3)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 360件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T07:28:04.500179+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=80753.0
- Funnel: target 761 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +34.24% | $11,073,488.14 |
| B/USDT:USDT | +33.26% | $6,518,420.76 |
| TROLLSOL/USDT:USDT | +22.76% | $4,986,301.05 |
| SAGA/USDT:USDT | +18.89% | $1,635,804.07 |
| ALCH/USDT:USDT | +16.57% | $4,587,386.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TROLLSOL/USDT:USDT | below_1h_threshold | +3.74% | +3.79% |
| VVV/USDT:USDT | below_1h_threshold | +2.79% | +2.84% |
| ROBO/USDT:USDT | below_1h_threshold | +1.37% | +1.42% |
| TRUTH/USDT:USDT | below_1h_threshold | +1.28% | +1.32% |
| LUNC/USDT:USDT | below_1h_threshold | +1.10% | +1.15% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
