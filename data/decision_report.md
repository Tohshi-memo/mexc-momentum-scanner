# Decision Report

- generated_at: 2026-09-26T23:11:52.511435+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15625**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.62% / filled 20/20。**
- 全期間 MARKET基準: n=15625, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 12/20 | 60.0% | +1.27% | **+0.76%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.77% | **+0.73%** |
| LIMIT_BB3S | 2/13 | 15.4% | +4.64% | **+0.71%** |
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +1.25% | **+0.37%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.16% | **+0.32%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.43% | **+0.26%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.43% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,239.61** / 初期 $100.00 (+1139.61%)
- 確定: 5978件 (Win 1766 / Loss 1923 / Flat 2289) / skip 6208件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,239.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3533件 (Win 974 / Loss 812 / Flat 1747) / skip 5503件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0275 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RARE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.44** / 初期 $100.00 (+19.44%)
- 確定: 3208件 (Win 945 / Loss 1272 / Flat 991) / pending 4件 / skip 3885件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000188 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KMNO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.06% 残高後 $119.44

## 6. Latest Market Context

- 更新: 2026-09-26T23:11:41.497536+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=84285.8
- Funnel: target 1070 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| QNT/USDT:USDT | +25.56% | $28,139,645.26 |
| GRASS/USDT:USDT | +12.58% | $4,791,160.32 |
| MARSCOIN/USDT:USDT | +9.26% | $1,914,233.48 |
| ZEC/USDT:USDT | +6.68% | $789,655,473.60 |
| GRAM/USDT:USDT | +5.58% | $5,090,530.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PAID/USDT:USDT | below_1h_threshold | +4.03% | +3.99% |
| QNT/USDT:USDT | below_1h_threshold | +2.04% | +2.00% |
| KMNO/USDT:USDT | below_1h_threshold | +1.82% | +1.78% |
| JTO/USDT:USDT | below_1h_threshold | +1.10% | +1.06% |
| TLM/USDT:USDT | below_1h_threshold | +0.95% | +0.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
