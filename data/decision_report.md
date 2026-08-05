# Decision Report

- generated_at: 2026-08-05T11:01:21.113143+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10397**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.29% / filled 20/20。**
- 全期間 MARKET基準: n=10397, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.29% | **+1.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +2.03% | **+1.32%** |
| MARKET | 20/20 | 100.0% | +1.29% | **+1.29%** |
| LIMIT_BB3S | 5/19 | 26.3% | +2.94% | **+0.77%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.76% | **+0.55%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.43% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.24% | **+0.17%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.49% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3769件 (Win 1195 / Loss 1236 / Flat 1338) / skip 3189件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.35** / 初期 $100.00 (+43.35%)
- 確定: 1316件 (Win 372 / Loss 310 / Flat 634) / skip 2492件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0366 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $143.35

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.95** / 初期 $100.00 (+17.95%)
- 確定: 1137件 (Win 364 / Loss 441 / Flat 332) / pending 5件 / skip 730件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000103 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.95

## 6. Latest Market Context

- 更新: 2026-08-05T11:01:11.592985+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64042.2
- Funnel: target 945 → liquid 178 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +88.35% | $21,517,007.70 |
| BLESS/USDT:USDT | +86.97% | $39,962,964.16 |
| HFT/USDT:USDT | +70.72% | $3,436,088.40 |
| GRVT/USDT:USDT | +29.05% | $7,008,473.00 |
| BICO/USDT:USDT | +28.61% | $16,514,153.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +4.11% | +4.09% |
| LLYSTOCK/USDT:USDT | below_1h_threshold | +3.52% | +3.51% |
| SHOPSTOCK/USDT:USDT | below_1h_threshold | +2.50% | +2.49% |
| PLTRSTOCK/USDT:USDT | below_1h_threshold | +1.00% | +0.98% |
| METASTOCK/USDT:USDT | below_1h_threshold | +0.87% | +0.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
