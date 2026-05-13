# Decision Report

- generated_at: 2026-05-13T08:48:10.707414+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4202**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=4202, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.38% | **+0.96%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.89% | **+0.62%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.91% | **+0.50%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.19% | **+0.17%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.12% | **+0.06%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.05% | **+0.04%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.06% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.64** / 初期 $100.00 (+20.64%)
- 確定: 338件 (Win 94 / Loss 121 / Flat 123) / skip 425件
- 成長率目線: 平均log +0.000555 / 幾何平均 +0.056% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.07% 残高後 $120.64

## 4. Latest Market Context

- 更新: 2026-05-13T08:48:04.448820+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=81123.6
- Funnel: target 764 → liquid 189 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.8 >= 65=1, 4h RSI 78.8 >= 65=1, 4h RSI 69.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COS/USDT:USDT | +47.14% | $1,497,761.91 |
| IRYS/USDT:USDT | +25.35% | $6,647,394.71 |
| UB/USDT:USDT | +22.41% | $4,771,768.90 |
| SATO/USDT:USDT | +21.06% | $1,306,979.86 |
| LAB/USDT:USDT | +20.08% | $106,288,083.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COS/USDT:USDT | below_1h_threshold | +4.69% | +4.52% |
| JTO/USDT:USDT | below_1h_threshold | +2.83% | +2.65% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +2.75% | +2.58% |
| BASED/USDT:USDT | below_1h_threshold | +2.72% | +2.55% |
| KITE/USDT:USDT | below_1h_threshold | +2.38% | +2.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
