# Decision Report

- generated_at: 2026-05-11T00:27:48.307670+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3999**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.03% / filled 20/20。**
- 全期間 MARKET基準: n=3999, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.03% | **+1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_BB3S | 7/14 | 50.0% | +2.04% | **+1.02%** |
| ASK | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.04% | **+0.98%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.67% | **+0.92%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.70% | **+1.44%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.77% | **+1.24%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.88% | **+0.66%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.47% | **+0.40%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.62% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$110.03** / 初期 $100.00 (+10.03%)
- 確定: 206件 (Win 52 / Loss 69 / Flat 85) / skip 354件
- 成長率目線: 平均log +0.000464 / 幾何平均 +0.046% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TROLLSOL/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $110.03

## 4. Latest Market Context

- 更新: 2026-05-11T00:27:44.857424+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.58% price=81702.1
- Funnel: target 770 → liquid 175 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.8 >= 65=1, 4h RSI 81.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +47.85% | $8,450,370.20 |
| TROLLSOL/USDT:USDT | +27.94% | $5,147,485.54 |
| ALCH/USDT:USDT | +19.60% | $3,729,230.72 |
| B/USDT:USDT | +12.63% | $2,511,110.69 |
| SAHARA/USDT:USDT | +9.59% | $2,081,295.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +4.96% | +5.54% |
| VVV/USDT:USDT | below_1h_threshold | +3.47% | +4.05% |
| ENS/USDT:USDT | below_1h_threshold | +2.47% | +3.05% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.24% | +2.82% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +2.07% | +2.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
