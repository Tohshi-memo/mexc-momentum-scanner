# Decision Report

- generated_at: 2026-09-01T03:26:38.040389+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13220**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.81% / filled 20/20。**
- 全期間 MARKET基準: n=13220, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.81% | **+1.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.38% | **+2.27%** |
| LIMIT_2PCT | 17/20 | 85.0% | +2.14% | **+1.82%** |
| MARKET | 20/20 | 100.0% | +1.81% | **+1.81%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.15% | **+0.80%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.47% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.55% | **+1.28%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.78% | **+0.80%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.91% | **+0.46%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.50% | **+0.35%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.53% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 195件 (TP 73 / SL 117 / EXP 5)
- 最新: ARB/USDT:USDT SL_HIT PnL -2.46% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.74** / 初期 $100.00 (+692.74%)
- 確定: 4878件 (Win 1485 / Loss 1609 / Flat 1784) / skip 4903件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $792.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.26** / 初期 $100.00 (+74.26%)
- 確定: 2201件 (Win 610 / Loss 530 / Flat 1061) / skip 4430件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0431 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $174.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.69** / 初期 $100.00 (+15.69%)
- 確定: 2085件 (Win 610 / Loss 813 / Flat 662) / pending 1件 / skip 2610件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000145 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.69

## 6. Latest Market Context

- 更新: 2026-09-01T03:26:20.297063+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=78368.5
- Funnel: target 1031 → liquid 150 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +45.76% | $7,426,257.76 |
| ARB/USDT:USDT | +30.64% | $56,696,924.37 |
| USELESS/USDT:USDT | +26.72% | $18,705,276.70 |
| 0G/USDT:USDT | +14.18% | $26,950,714.93 |
| CRV/USDT:USDT | +13.56% | $4,608,578.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +4.54% | +4.61% |
| NOT/USDT:USDT | below_1h_threshold | +3.39% | +3.46% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.05% | +3.11% |
| USELESS/USDT:USDT | below_1h_threshold | +2.14% | +2.21% |
| JASMY/USDT:USDT | below_1h_threshold | +1.78% | +1.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
