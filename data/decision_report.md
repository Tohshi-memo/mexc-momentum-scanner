# Decision Report

- generated_at: 2026-09-01T02:21:20.792673+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13217**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.68% / filled 20/20。**
- 全期間 MARKET基準: n=13217, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.68% | **+1.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.14% | **+2.03%** |
| MARKET | 20/20 | 100.0% | +1.68% | **+1.68%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.64% | **+1.31%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.39% | **+0.63%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.96% | **+1.33%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.19% | **+0.59%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.60% | **+0.39%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.18% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 195件 (TP 73 / SL 117 / EXP 5)
- 最新: ARB/USDT:USDT SL_HIT PnL -2.46% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.74** / 初期 $100.00 (+692.74%)
- 確定: 4878件 (Win 1485 / Loss 1609 / Flat 1784) / skip 4900件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $792.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.13** / 初期 $100.00 (+74.13%)
- 確定: 2199件 (Win 609 / Loss 529 / Flat 1061) / skip 4429件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0344 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $174.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.69** / 初期 $100.00 (+15.69%)
- 確定: 2085件 (Win 610 / Loss 813 / Flat 662) / pending 0件 / skip 2608件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000194 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.69

## 6. Latest Market Context

- 更新: 2026-09-01T02:21:09.000717+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=78227.0
- Funnel: target 1031 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +28.10% | $6,689,637.08 |
| ARB/USDT:USDT | +27.34% | $49,569,172.12 |
| USELESS/USDT:USDT | +23.96% | $17,901,214.80 |
| 0G/USDT:USDT | +19.98% | $23,796,595.27 |
| CRV/USDT:USDT | +11.03% | $4,200,069.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHEINSTOCK/USDT:USDT | below_1h_threshold | +1.46% | +1.65% |
| COLLECT/USDT:USDT | below_1h_threshold | +1.06% | +1.25% |
| BEAT/USDT:USDT | below_1h_threshold | +0.89% | +1.08% |
| JASMY/USDT:USDT | below_1h_threshold | +0.66% | +0.85% |
| STX/USDT:USDT | below_1h_threshold | +0.55% | +0.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
