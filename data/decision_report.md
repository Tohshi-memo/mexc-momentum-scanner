# Decision Report

- generated_at: 2026-09-01T05:21:24.130330+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13231**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.51% / filled 20/20。**
- 全期間 MARKET基準: n=13231, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.51% | **+0.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +1.37% | **+1.03%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.17% | **+1.00%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.68% | **+0.80%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.97% | **+0.73%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.60% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.09% | **+0.71%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.51% | **+0.34%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.17% | **+0.14%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.05% | **+0.03%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.09% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.74** / 初期 $100.00 (+692.74%)
- 確定: 4878件 (Win 1485 / Loss 1609 / Flat 1784) / skip 4914件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $792.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.05** / 初期 $100.00 (+74.05%)
- 確定: 2210件 (Win 613 / Loss 534 / Flat 1063) / skip 4432件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0111 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $174.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.28** / 初期 $100.00 (+15.28%)
- 確定: 2087件 (Win 610 / Loss 815 / Flat 662) / pending 0件 / skip 2617件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000264 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.28

## 6. Latest Market Context

- 更新: 2026-09-01T05:21:13.625836+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=78788.1
- Funnel: target 1034 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +86.73% | $10,030,862.45 |
| ARB/USDT:USDT | +27.03% | $62,762,645.69 |
| USELESS/USDT:USDT | +24.21% | $19,827,630.31 |
| PONS/USDT:USDT | +16.25% | $3,945,326.65 |
| CRV/USDT:USDT | +15.32% | $5,590,502.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOMI/USDT:USDT | below_1h_threshold | +3.09% | +2.97% |
| 1000BONK/USDT:USDT | below_1h_threshold | +1.23% | +1.11% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.85% | +0.73% |
| CRV/USDT:USDT | below_1h_threshold | +0.78% | +0.67% |
| AKE/USDT:USDT | below_1h_threshold | +0.76% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
