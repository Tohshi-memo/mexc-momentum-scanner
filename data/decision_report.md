# Decision Report

- generated_at: 2026-09-18T14:01:23.844581+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14900**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.94% / filled 20/20。**
- 全期間 MARKET基準: n=14900, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/10 | 40.0% | +2.56% | **+1.02%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.84% | **+0.96%** |
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.27% | **+1.15%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.05% | **+0.79%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.69% | **+0.52%** |
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +0.65% | **+0.39%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.40% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,153.97** / 初期 $100.00 (+1053.97%)
- 確定: 5605件 (Win 1679 / Loss 1815 / Flat 2111) / skip 5856件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: G/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,153.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$241.67** / 初期 $100.00 (+141.67%)
- 確定: 3173件 (Win 878 / Loss 757 / Flat 1538) / skip 5138件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0893 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $241.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.32** / 初期 $100.00 (+23.32%)
- 確定: 2960件 (Win 878 / Loss 1166 / Flat 916) / pending 0件 / skip 3416件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000189 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.32

## 6. Latest Market Context

- 更新: 2026-09-18T14:01:14.688213+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=80287.9
- Funnel: target 1050 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.6 >= 65=1, 4h RSI 77.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| G/USDT:USDT | +89.15% | $23,942,200.74 |
| MYX/USDT:USDT | +79.15% | $4,995,124.14 |
| CNPY/USDT:USDT | +37.49% | $4,348,199.12 |
| ONE/USDT:USDT | +31.51% | $53,811,554.66 |
| BR/USDT:USDT | +28.41% | $17,954,894.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COINBASE/USDT:USDT | below_relative_strength | +5.07% | +4.77% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +4.39% | +4.09% |
| NEAR/USDT:USDT | below_1h_threshold | +0.78% | +0.48% |
| ETHFI/USDT:USDT | below_1h_threshold | +0.72% | +0.42% |
| ENA/USDT:USDT | below_1h_threshold | +0.67% | +0.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
