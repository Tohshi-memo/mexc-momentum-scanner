# Decision Report

- generated_at: 2026-10-29T02:01:22.444347+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17745**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.62% / filled 20/20。**
- 全期間 MARKET基準: n=17745, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/20 | 30.0% | +4.07% | **+1.22%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.80% | **+0.76%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.42% | **+1.21%** |
| MARKET_LONG | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.32% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,545.23** / 初期 $100.00 (+1445.23%)
- 確定: 6789件 (Win 1971 / Loss 2173 / Flat 2645) / skip 7517件
- 成長率目線: 平均log +0.000403 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IDOL/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,545.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$358.73** / 初期 $100.00 (+258.73%)
- 確定: 4266件 (Win 1155 / Loss 971 / Flat 2140) / skip 6890件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0245 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IDOL/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $358.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5909件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000114 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T02:01:09.520678+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=79934.8
- Funnel: target 1083 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +63.04% | $1,872,305.67 |
| INIT/USDT:USDT | +8.67% | $2,098,667.59 |
| ORCLSTOCK/USDT:USDT | +7.08% | $5,060,392.07 |
| XPIN/USDT:USDT | +6.78% | $2,625,977.67 |
| AKE/USDT:USDT | +6.74% | $6,826,343.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKDD/USDT:USDT | below_1h_threshold | +3.01% | +3.05% |
| UNITREE/USDT:USDT | below_1h_threshold | +2.90% | +2.95% |
| SOXS/USDT:USDT | below_1h_threshold | +2.58% | +2.62% |
| SQQQ/USDT:USDT | below_1h_threshold | +1.29% | +1.33% |
| BTW/USDT:USDT | below_1h_threshold | +0.56% | +0.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
