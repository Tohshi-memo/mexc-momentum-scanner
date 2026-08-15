# Decision Report

- generated_at: 2026-08-15T12:56:26.222042+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11664**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.80% / filled 20/20。**
- 全期間 MARKET基準: n=11664, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.80% | **+3.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.80% | **+3.80%** |
| LIMIT_2PCT | 12/20 | 60.0% | +3.02% | **+1.81%** |
| LIMIT_1PCT | 13/20 | 65.0% | +1.93% | **+1.26%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.72% | **+0.86%** |
| LIMIT_4PCT | 7/20 | 35.0% | +1.14% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +3.11% | **+0.93%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +1.55% | **+0.62%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.56% | **-0.14%** |
| LIMIT_7PCT_LONG | 14/20 | 70.0% | -0.82% | **-0.58%** |
| LIMIT_8PCT_LONG | 13/20 | 65.0% | -0.92% | **-0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$641.37** / 初期 $100.00 (+541.37%)
- 確定: 4132件 (Win 1290 / Loss 1355 / Flat 1487) / skip 4093件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $641.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.13** / 初期 $100.00 (+55.13%)
- 確定: 1727件 (Win 491 / Loss 413 / Flat 823) / skip 3348件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1080 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.08% 残高後 $155.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.57** / 初期 $100.00 (+19.57%)
- 確定: 1606件 (Win 490 / Loss 606 / Flat 510) / pending 6件 / skip 1525件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000624 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.04% 残高後 $119.57

## 6. Latest Market Context

- 更新: 2026-08-15T12:56:17.532902+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=62944.8
- Funnel: target 985 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COW/USDT:USDT | +57.00% | $6,926,252.39 |
| WAL/USDT:USDT | +32.23% | $1,292,327.01 |
| VELVET/USDT:USDT | +24.41% | $33,111,128.49 |
| ANSEM/USDT:USDT | +22.40% | $1,662,659.99 |
| US/USDT:USDT | +18.94% | $6,175,131.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WAL/USDT:USDT | below_1h_threshold | +4.85% | +4.92% |
| PRL/USDT:USDT | below_1h_threshold | +4.43% | +4.51% |
| MOVR/USDT:USDT | below_1h_threshold | +3.83% | +3.91% |
| LINK/USDT:USDT | below_1h_threshold | +1.56% | +1.63% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +1.50% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
