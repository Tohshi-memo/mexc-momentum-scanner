# Decision Report

- generated_at: 2026-09-21T09:06:16.616058+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15243**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.94% / filled 20/20。**
- 全期間 MARKET基準: n=15243, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.73% | **+0.62%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.38% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.31% | **+0.15%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | -0.11% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,172.15** / 初期 $100.00 (+1072.15%)
- 確定: 5734件 (Win 1708 / Loss 1846 / Flat 2180) / skip 6070件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LDO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,172.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.16** / 初期 $100.00 (+147.16%)
- 確定: 3305件 (Win 913 / Loss 765 / Flat 1627) / skip 5349件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0175 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $247.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.65** / 初期 $100.00 (+22.65%)
- 確定: 3021件 (Win 891 / Loss 1186 / Flat 944) / pending 2件 / skip 3689件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000160 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LDO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $122.65

## 6. Latest Market Context

- 更新: 2026-09-21T09:06:05.691193+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=83909.8
- Funnel: target 1050 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZETA/USDT:USDT | +82.96% | $4,974,668.10 |
| NIL/USDT:USDT | +34.36% | $7,020,468.11 |
| PTB/USDT:USDT | +27.21% | $1,098,393.80 |
| KMNO/USDT:USDT | +20.24% | $1,244,751.31 |
| UAI/USDT:USDT | +19.92% | $1,354,515.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +2.61% | +2.39% |
| SOXL/USDT:USDT | below_1h_threshold | +1.89% | +1.67% |
| UAI/USDT:USDT | below_1h_threshold | +1.78% | +1.56% |
| PTB/USDT:USDT | below_1h_threshold | +1.71% | +1.49% |
| NIL/USDT:USDT | below_1h_threshold | +1.39% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
