# Decision Report

- generated_at: 2026-09-15T09:51:21.928291+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14582**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.72% / filled 20/20。**
- 全期間 MARKET基準: n=14582, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.02% | **+0.61%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.76% | **+0.61%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.49% | **+1.26%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.54% | **+0.38%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.25% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 213件 (TP 79 / SL 129 / EXP 5)
- 最新: STORJ/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,077.38** / 初期 $100.00 (+977.38%)
- 確定: 5484件 (Win 1642 / Loss 1774 / Flat 2068) / skip 5659件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,077.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.55** / 初期 $100.00 (+130.55%)
- 確定: 3022件 (Win 836 / Loss 718 / Flat 1468) / skip 4971件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0491 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $230.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.11** / 初期 $100.00 (+24.11%)
- 確定: 2909件 (Win 863 / Loss 1133 / Flat 913) / pending 0件 / skip 3144件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000313 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: POWR/USDT:USDT `MARKET` EXPIRED account +0.10% 残高後 $124.11

## 6. Latest Market Context

- 更新: 2026-09-15T09:51:10.568938+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=76968.0
- Funnel: target 1060 → liquid 160 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1, 4h RSI 74.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +68.56% | $1,705,572.27 |
| AIN/USDT:USDT | +51.55% | $10,383,634.55 |
| AKE/USDT:USDT | +35.53% | $6,574,643.98 |
| POWER/USDT:USDT | +34.13% | $11,579,377.54 |
| SAGA/USDT:USDT | +17.55% | $1,111,701.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHROOM/USDT:USDT | below_1h_threshold | +4.46% | +4.46% |
| CAP/USDT:USDT | below_1h_threshold | +4.17% | +4.17% |
| NIULAI/USDT:USDT | below_1h_threshold | +3.34% | +3.33% |
| POWER/USDT:USDT | below_1h_threshold | +2.39% | +2.39% |
| XPL/USDT:USDT | below_1h_threshold | +1.47% | +1.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
