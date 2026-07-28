# Decision Report

- generated_at: 2026-07-28T11:01:16.926889+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9691**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=9691, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.42% | **+1.42%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.48% | **+1.33%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.50% | **+1.12%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$106.38** / 初期 $100.00 (+6.38%)
- 確定トレード: 149件 (TP 51 / SL 93 / EXP 5)
- 最新: BANK/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.38
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$464.24** / 初期 $100.00 (+364.24%)
- 確定: 3461件 (Win 1091 / Loss 1123 / Flat 1247) / skip 2791件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $464.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1225件 (Win 338 / Loss 275 / Flat 612) / skip 1877件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0613 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.17** / 初期 $100.00 (+8.17%)
- 確定: 711件 (Win 230 / Loss 273 / Flat 208) / pending 5件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000230 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $108.17

## 6. Latest Market Context

- 更新: 2026-07-28T11:01:09.856434+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=63480.9
- Funnel: target 898 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +48.56% | $17,986,156.33 |
| DEXE/USDT:USDT | +23.17% | $15,913,414.30 |
| ON/USDT:USDT | +20.35% | $17,838,733.95 |
| VANRY/USDT:USDT | +15.11% | $1,298,361.68 |
| BULLA/USDT:USDT | +14.99% | $1,640,135.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COTI/USDT:USDT | below_1h_threshold | +0.86% | +0.80% |
| SOXS/USDT:USDT | below_1h_threshold | +0.36% | +0.30% |
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +0.26% | +0.20% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +0.21% | +0.15% |
| ETNSTOCK/USDT:USDT | below_1h_threshold | +0.18% | +0.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
