# Decision Report

- generated_at: 2026-07-27T05:01:14.161431+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9594**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.10% / filled 20/20。**
- 全期間 MARKET基準: n=9594, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +1.57% | **+1.26%** |
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.20% | **+1.08%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.37% | **+0.28%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | -0.23% | **-0.15%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.31% | **-0.22%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | -0.94% | **-0.24%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.28% | **-0.27%** |

## 2. $100 Live Portfolio

- 残高: **$107.46** / 初期 $100.00 (+7.46%)
- 確定トレード: 144件 (TP 50 / SL 89 / EXP 5)
- 最新: NIGHT/USDT:USDT TP_HIT PnL +4.75% 残高後 $107.46
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$450.30** / 初期 $100.00 (+350.30%)
- 確定: 3400件 (Win 1078 / Loss 1107 / Flat 1215) / skip 2755件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $450.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1223件 (Win 338 / Loss 275 / Flat 610) / skip 1782件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.10** / 初期 $100.00 (+8.10%)
- 確定: 621件 (Win 209 / Loss 239 / Flat 173) / pending 6件 / skip 440件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000056 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.17% 残高後 $108.10

## 6. Latest Market Context

- 更新: 2026-07-27T05:01:07.293655+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=65261.3
- Funnel: target 898 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +22.22% | $18,368,697.00 |
| CXMTSTOCK/USDT:USDT | +21.35% | $2,343,340.75 |
| DIA/USDT:USDT | +18.51% | $7,556,903.53 |
| 4/USDT:USDT | +18.19% | $2,506,489.83 |
| ESP/USDT:USDT | +16.85% | $8,247,655.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +1.23% | +1.22% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.90% | +0.89% |
| ESP/USDT:USDT | below_1h_threshold | +0.71% | +0.70% |
| ETNSTOCK/USDT:USDT | below_1h_threshold | +0.67% | +0.67% |
| BANK/USDT:USDT | below_1h_threshold | +0.55% | +0.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
