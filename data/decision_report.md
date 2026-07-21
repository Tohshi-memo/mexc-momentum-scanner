# Decision Report

- generated_at: 2026-07-21T05:01:16.298090+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9153**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.31% / filled 20/20。**
- 全期間 MARKET基準: n=9153, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.31% | **+1.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.97% | **+0.59%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.97% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.30% | **+1.17%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.52% | **+0.75%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.85% | **+0.68%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.91% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$108.05** / 初期 $100.00 (+8.05%)
- 確定トレード: 125件 (TP 44 / SL 76 / EXP 5)
- 最新: KIOXIASTOCK/USDT:USDT SL_HIT PnL -3.51% 残高後 $108.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$416.22** / 初期 $100.00 (+316.22%)
- 確定: 3215件 (Win 1008 / Loss 1024 / Flat 1183) / skip 2499件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ERA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $416.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.21** / 初期 $100.00 (+30.21%)
- 確定: 1114件 (Win 294 / Loss 232 / Flat 588) / skip 1450件
- 成長率目線: 平均log +0.000237 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0896 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ERA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $130.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.08** / 初期 $100.00 (+1.08%)
- 確定: 340件 (Win 120 / Loss 151 / Flat 69) / pending 1件 / skip 284件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000188 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KIOXIASTOCK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $101.08

## 6. Latest Market Context

- 更新: 2026-07-21T05:01:11.574369+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=65482.0
- Funnel: target 885 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +78.42% | $3,022,545.23 |
| ERA/USDT:USDT | +65.53% | $4,230,575.55 |
| ZHIPUSTOCK/USDT:USDT | +24.30% | $1,638,330.46 |
| ESPORTS/USDT:USDT | +13.58% | $5,303,634.72 |
| LDO/USDT:USDT | +11.39% | $8,113,151.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JIMOTHY/USDT:USDT | below_1h_threshold | +1.10% | +1.12% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.86% | +0.88% |
| ERA/USDT:USDT | below_1h_threshold | +0.56% | +0.58% |
| AKE/USDT:USDT | below_1h_threshold | +0.55% | +0.57% |
| APT/USDT:USDT | below_1h_threshold | +0.43% | +0.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
