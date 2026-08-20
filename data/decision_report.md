# Decision Report

- generated_at: 2026-08-20T06:36:16.645786+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12015**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.51% / filled 20/20。**
- 全期間 MARKET基準: n=12015, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.51% | **+0.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/13 | 23.1% | +3.20% | **+0.74%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.18% | **+0.55%** |
| MARKET | 20/20 | 100.0% | +0.51% | **+0.51%** |
| LIMIT_4PCT | 7/20 | 35.0% | +1.29% | **+0.45%** |
| LIMIT_6PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +1.27% | **+0.91%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.00% | **+0.75%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.98% | **+0.74%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.10% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.47** / 初期 $100.00 (+505.47%)
- 確定: 4241件 (Win 1302 / Loss 1388 / Flat 1551) / skip 4335件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUU/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $605.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3605件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.76** / 初期 $100.00 (+16.76%)
- 確定: 1754件 (Win 520 / Loss 670 / Flat 564) / pending 3件 / skip 1730件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000604 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MINIMAXSTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.76

## 6. Latest Market Context

- 更新: 2026-08-20T06:36:10.373357+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.45% price=69723.6
- Funnel: target 1004 → liquid 200 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +31.88% | $7,016,076.98 |
| BASECAT/USDT:USDT | +27.08% | $1,191,086.18 |
| RED/USDT:USDT | +26.66% | $1,714,988.94 |
| ON/USDT:USDT | +17.02% | $4,826,500.64 |
| HYPE/USDT:USDT | +16.73% | $525,981,455.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BOME/USDT:USDT | below_1h_threshold | +4.36% | +3.90% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.21% | +2.76% |
| BICO/USDT:USDT | below_1h_threshold | +2.95% | +2.49% |
| USELESS/USDT:USDT | below_1h_threshold | +1.60% | +1.14% |
| ORDI/USDT:USDT | below_1h_threshold | +1.44% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
