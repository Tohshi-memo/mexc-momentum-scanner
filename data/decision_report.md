# Decision Report

- generated_at: 2026-08-13T14:36:47.921553+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11447**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=11447, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.66% | **+1.58%** |
| LIMIT_3PCT | 16/20 | 80.0% | +1.78% | **+1.43%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.57% | **+1.33%** |
| LIMIT_BB3S | 4/13 | 30.8% | +3.31% | **+1.02%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.33% | **+1.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.61% | **+0.73%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.83% | **+0.37%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.41% | **+0.35%** |
| MARKET_LONG | 20/20 | 100.0% | +0.28% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.13** / 初期 $100.00 (+516.13%)
- 確定: 3965件 (Win 1238 / Loss 1296 / Flat 1431) / skip 4043件
- 成長率目線: 平均log +0.000459 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUU/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $616.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$151.19** / 初期 $100.00 (+51.19%)
- 確定: 1635件 (Win 467 / Loss 389 / Flat 779) / skip 3223件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1199 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MUU/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $151.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.39** / 初期 $100.00 (+16.39%)
- 確定: 1452件 (Win 427 / Loss 546 / Flat 479) / pending 6件 / skip 1467件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000233 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $116.39

## 6. Latest Market Context

- 更新: 2026-08-13T14:36:34.964455+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.39% price=63947.2
- Funnel: target 978 → liquid 178 → pre 50 → checked 50 → surge 7 → strict 0
- Surge前reject: below_1h_threshold=41, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.2 >= 65=1, 4h RSI 80.1 >= 65=1, 4h RSI 83.9 >= 65=1, 4h RSI 79.4 >= 65=1, 4h RSI 83.6 >= 65=1, 4h RSI 74.3 >= 65=1, 4h RSI 71.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +50.90% | $23,364,472.98 |
| ACU/USDT:USDT | +34.73% | $7,634,949.02 |
| COTI/USDT:USDT | +25.56% | $11,627,945.14 |
| AVNT/USDT:USDT | +24.44% | $2,030,178.97 |
| BTW/USDT:USDT | +20.75% | $24,469,151.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVNT/USDT:USDT | below_relative_strength | +5.29% | +4.90% |
| SOXL/USDT:USDT | below_relative_strength | +5.10% | +4.71% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +4.95% | +4.56% |
| SMCISTOCK/USDT:USDT | below_1h_threshold | +4.69% | +4.30% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +4.58% | +4.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
