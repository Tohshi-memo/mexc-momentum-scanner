# Decision Report

- generated_at: 2026-10-29T07:51:15.221440+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17764**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.68% / filled 20/20。**
- 全期間 MARKET基準: n=17764, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.68% | **+2.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.68% | **+2.68%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +3.16% | **+1.10%** |
| LIMIT_1PCT | 14/20 | 70.0% | +0.98% | **+0.69%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |
| LIMIT_FIB1618_LONG | 9/20 | 45.0% | -1.04% | **-0.47%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | -0.68% | **-0.58%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.31** / 初期 $100.00 (+1431.31%)
- 確定: 6802件 (Win 1975 / Loss 2179 / Flat 2648) / skip 7523件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IDOL/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,531.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$362.59** / 初期 $100.00 (+262.59%)
- 確定: 4285件 (Win 1159 / Loss 972 / Flat 2154) / skip 6890件
- 成長率目線: 平均log +0.000301 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0103 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $362.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5923件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000406 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T07:51:06.879509+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=79836.4
- Funnel: target 1083 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +51.83% | $3,198,707.87 |
| BEAT/USDT:USDT | +10.23% | $8,447,370.82 |
| BULLA/USDT:USDT | +8.57% | $2,266,286.33 |
| ORCLSTOCK/USDT:USDT | +8.23% | $5,130,127.30 |
| LITESTOCK/USDT:USDT | +6.39% | $1,519,000.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +2.52% | +2.64% |
| BLUR/USDT:USDT | below_1h_threshold | +1.89% | +2.01% |
| SKDD/USDT:USDT | below_1h_threshold | +1.24% | +1.37% |
| BTW/USDT:USDT | below_1h_threshold | +0.78% | +0.91% |
| AKE/USDT:USDT | below_1h_threshold | +0.76% | +0.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
