# Decision Report

- generated_at: 2026-05-13T07:38:03.024857+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4196**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.19% / filled 20/20。**
- 全期間 MARKET基準: n=4196, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.78% | **+1.69%** |
| LIMIT_ATR | 14/20 | 70.0% | +2.05% | **+1.44%** |
| ASK | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.93% | **+1.35%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.73% | **+1.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.38% | **+0.90%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.91% | **+0.46%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.94% | **+0.42%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.59% | **+0.41%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.16% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.72** / 初期 $100.00 (+20.72%)
- 確定: 332件 (Win 93 / Loss 118 / Flat 121) / skip 425件
- 成長率目線: 平均log +0.000567 / 幾何平均 +0.057% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.03% 残高後 $120.72

## 4. Latest Market Context

- 更新: 2026-05-13T07:37:58.730464+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=80897.3
- Funnel: target 765 → liquid 191 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.0 >= 65=1, 4h RSI 88.3 >= 65=1, 4h RSI 91.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COS/USDT:USDT | +45.19% | $1,138,860.75 |
| IRYS/USDT:USDT | +21.13% | $5,880,487.58 |
| LAB/USDT:USDT | +19.18% | $105,949,587.44 |
| GUA/USDT:USDT | +17.15% | $4,499,190.49 |
| SATO/USDT:USDT | +16.30% | $1,272,489.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROSE/USDT:USDT | below_1h_threshold | +3.84% | +3.90% |
| RIVER/USDT:USDT | below_1h_threshold | +2.54% | +2.60% |
| INJ/USDT:USDT | below_1h_threshold | +1.91% | +1.97% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.64% | +1.70% |
| STX/USDT:USDT | below_1h_threshold | +1.64% | +1.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
