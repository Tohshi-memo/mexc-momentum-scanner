# Decision Report

- generated_at: 2026-09-27T22:51:33.659751+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15670**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15670, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.93% | **-1.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.48% | **+0.66%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.47% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +6.81% | **+4.54%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.95% | **+1.92%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.64% | **+1.82%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.21% | **+1.77%** |
| MARKET_LONG | 20/20 | 100.0% | +1.75% | **+1.75%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,239.61** / 初期 $100.00 (+1139.61%)
- 確定: 5981件 (Win 1766 / Loss 1923 / Flat 2292) / skip 6250件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,239.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5547件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.76** / 初期 $100.00 (+18.76%)
- 確定: 3243件 (Win 946 / Loss 1277 / Flat 1020) / pending 3件 / skip 3897件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000151 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $118.76

## 6. Latest Market Context

- 更新: 2026-09-27T22:51:19.599624+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.55% price=84173.7
- Funnel: target 1069 → liquid 137 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.3 >= 65=1, 4h RSI 73.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| QNT/USDT:USDT | +57.71% | $237,635,147.22 |
| BATON/USDT:USDT | +51.85% | $1,177,215.45 |
| GRT/USDT:USDT | +22.56% | $6,662,585.48 |
| ONE/USDT:USDT | +13.87% | $3,396,453.54 |
| RARE/USDT:USDT | +13.22% | $1,636,484.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RARE/USDT:USDT | below_1h_threshold | +2.87% | +3.42% |
| SKY/USDT:USDT | below_1h_threshold | +1.55% | +2.10% |
| JUP/USDT:USDT | below_1h_threshold | +1.44% | +1.99% |
| SEI/USDT:USDT | below_1h_threshold | +0.52% | +1.07% |
| SOXS/USDT:USDT | below_1h_threshold | +0.50% | +1.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
