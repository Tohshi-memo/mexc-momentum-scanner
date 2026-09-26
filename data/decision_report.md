# Decision Report

- generated_at: 2026-09-26T15:21:23.302405+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15603**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.52% / filled 20/20。**
- 全期間 MARKET基準: n=15603, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.60% | **+0.45%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.00% | **+0.35%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.35% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.82% | **+1.41%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.22% | **+1.11%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.52% | **+0.91%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.30% | **+0.91%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.28% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,250.03** / 初期 $100.00 (+1150.03%)
- 確定: 5964件 (Win 1762 / Loss 1916 / Flat 2286) / skip 6200件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RARE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,250.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3533件 (Win 974 / Loss 812 / Flat 1747) / skip 5481件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0721 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RARE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.00** / 初期 $100.00 (+19.00%)
- 確定: 3188件 (Win 937 / Loss 1264 / Flat 987) / pending 5件 / skip 3882件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000293 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RARE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.00

## 6. Latest Market Context

- 更新: 2026-09-26T15:21:12.047341+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=83995.7
- Funnel: target 1070 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PAID/USDT:USDT | +285.70% | $3,011,823.95 |
| RARE/USDT:USDT | +43.83% | $8,081,989.60 |
| BATON/USDT:USDT | +38.82% | $1,132,083.38 |
| BR/USDT:USDT | +32.67% | $11,082,534.89 |
| 2Z/USDT:USDT | +26.26% | $3,784,051.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +3.97% | +3.95% |
| RARE/USDT:USDT | below_1h_threshold | +3.73% | +3.71% |
| BEAT/USDT:USDT | below_1h_threshold | +2.91% | +2.89% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.52% | +2.50% |
| FET/USDT:USDT | below_1h_threshold | +2.51% | +2.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
