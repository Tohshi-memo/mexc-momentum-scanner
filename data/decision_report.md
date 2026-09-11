# Decision Report

- generated_at: 2026-09-11T16:56:25.982000+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14238**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.84% / filled 20/20。**
- 全期間 MARKET基準: n=14238, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.44% | **+0.35%** |
| LIMIT_BB3S | 3/16 | 18.8% | +1.66% | **+0.31%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.85% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.34% | **+1.75%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.84% | **+0.42%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.53% | **+0.35%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.14% | **+0.11%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 210件 (TP 78 / SL 127 / EXP 5)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,076.28** / 初期 $100.00 (+976.28%)
- 確定: 5396件 (Win 1625 / Loss 1747 / Flat 2024) / skip 5403件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.32% 残高後 $1,076.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$207.05** / 初期 $100.00 (+107.05%)
- 確定: 2814件 (Win 772 / Loss 655 / Flat 1387) / skip 4835件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0588 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $207.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.06** / 初期 $100.00 (+23.06%)
- 確定: 2731件 (Win 807 / Loss 1047 / Flat 877) / pending 6件 / skip 2976件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000184 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.06

## 6. Latest Market Context

- 更新: 2026-09-11T16:56:15.616379+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=77882.6
- Funnel: target 1067 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIVER/USDT:USDT | +6.18% | $2,594,468.97 |
| LAB/USDT:USDT | +5.12% | $3,903,771.23 |
| STORJ/USDT:USDT | +4.92% | $5,945,622.90 |
| MET/USDT:USDT | +4.19% | $1,694,522.16 |
| STRK/USDT:USDT | +2.79% | $1,185,940.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_relative_strength | +5.12% | +4.88% |
| STORJ/USDT:USDT | below_relative_strength | +5.06% | +4.81% |
| MET/USDT:USDT | below_1h_threshold | +4.23% | +3.98% |
| STRK/USDT:USDT | below_1h_threshold | +2.76% | +2.51% |
| MINA/USDT:USDT | below_1h_threshold | +2.57% | +2.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
