# Decision Report

- generated_at: 2026-11-08T21:01:12.991959+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18486**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=18486, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.68% | **+0.51%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.48% | **+0.41%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.68% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +5.69% | **+1.42%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.80% | **+1.40%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +4.55% | **+1.36%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.43% | **+0.41%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.77% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 265件 (TP 97 / SL 160 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,642.52** / 初期 $100.00 (+1542.52%)
- 確定: 7156件 (Win 2057 / Loss 2283 / Flat 2816) / skip 7891件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,642.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4756件 (Win 1277 / Loss 1047 / Flat 2432) / skip 7141件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1432 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_10PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6644件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000432 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-08T21:01:02.152696+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=75753.6
- Funnel: target 1089 → liquid 103 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +17.35% | $48,726,223.30 |
| ICNT/USDT:USDT | +3.65% | $2,729,522.41 |
| AIOT/USDT:USDT | +3.46% | $5,713,030.07 |
| CLAUDIA/USDT:USDT | +2.85% | $13,610,833.54 |
| BTW/USDT:USDT | +2.44% | $5,695,930.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +3.84% | +3.79% |
| AKE/USDT:USDT | below_1h_threshold | +1.56% | +1.51% |
| FET/USDT:USDT | below_1h_threshold | +0.28% | +0.23% |
| USOIL/USDT:USDT | below_1h_threshold | +0.26% | +0.21% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.24% | +0.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
