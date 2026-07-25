# Decision Report

- generated_at: 2026-07-25T13:06:15.056521+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9514**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=9514, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/19 | 36.8% | +2.57% | **+0.95%** |
| LIMIT_5PCT | 8/20 | 40.0% | +2.31% | **+0.92%** |
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_6PCT | 5/20 | 25.0% | +2.46% | **+0.62%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.32% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.19% | **+1.01%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.33% | **+1.00%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.98% | **+0.80%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.10% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$432.47** / 初期 $100.00 (+332.47%)
- 確定: 3342件 (Win 1055 / Loss 1083 / Flat 1204) / skip 2733件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $432.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$132.39** / 初期 $100.00 (+32.39%)
- 確定: 1168件 (Win 315 / Loss 254 / Flat 599) / skip 1757件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1221 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $132.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$106.59** / 初期 $100.00 (+6.59%)
- 確定: 561件 (Win 189 / Loss 216 / Flat 156) / pending 3件 / skip 420件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000437 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $106.59

## 6. Latest Market Context

- 更新: 2026-07-25T13:06:06.978809+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64095.1
- Funnel: target 898 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +61.40% | $9,538,955.27 |
| DEXE/USDT:USDT | +43.60% | $116,668,564.86 |
| AKE/USDT:USDT | +29.68% | $46,212,115.39 |
| PROM/USDT:USDT | +21.92% | $4,729,247.74 |
| ESPORTS/USDT:USDT | +17.66% | $14,440,717.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.00% | +3.99% |
| DEXE/USDT:USDT | below_1h_threshold | +3.09% | +3.08% |
| BANK/USDT:USDT | below_1h_threshold | +1.52% | +1.51% |
| VVV/USDT:USDT | below_1h_threshold | +1.16% | +1.14% |
| BEAT/USDT:USDT | below_1h_threshold | +1.15% | +1.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
